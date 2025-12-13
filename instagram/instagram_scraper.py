import json
import csv
from pathlib import Path
from typing import Iterable


class InstagramScraper:
    @staticmethod
    def _scrape_followers(followers_file_name: Path) -> set:
        with open(followers_file_name) as followers_json_file:
            json_followers_data = json.load(followers_json_file)
            followers_set = set()
            for json_dict in json_followers_data:
                followers_set.add((json_dict["string_list_data"][0]["value"], json_dict["string_list_data"][0]["href"]))
            return followers_set

    @staticmethod
    def _scrape_following(following_file_name: Path) -> set:
        with open(following_file_name) as json_file:
            json_following_data = json.load(json_file)
            following_set = set()
            for json_dict in json_following_data["relationships_following"]:
                following_set.add((json_dict["title"], json_dict["string_list_data"][0]["href"].replace("_u/", "")))
            return following_set

    @staticmethod
    def _compute_not_following_you_back(followers_file_name: Path, following_file_name: Path) -> set:
        return (
                InstagramScraper._scrape_following(following_file_name)
                - InstagramScraper._scrape_followers(followers_file_name)
        )

    @staticmethod
    def _compute_recent_not_following_you_back(
            followers_file_name_old_timestamp: Path,
            following_file_name_old_timestamp: Path,
            followers_file_name_new_timestamp: Path,
            following_file_name_new_timestamp: Path
    ):
        return (
                InstagramScraper._compute_not_following_you_back(
                    followers_file_name_new_timestamp,
                    following_file_name_new_timestamp
                ) -
                InstagramScraper._compute_not_following_you_back(
                    followers_file_name_old_timestamp,
                    following_file_name_old_timestamp
                )
        )

    @staticmethod
    def _write_rows(rows: Iterable[tuple[str, str]], output_file: Path) -> None:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "link"])
            writer.writerows(sorted(rows))

    # Public API
    @staticmethod
    def output_not_following_you_back(followers_file: Path, following_file: Path, output_file: Path) -> None:
        rows = InstagramScraper._compute_not_following_you_back(followers_file, following_file)
        InstagramScraper._write_rows(rows, output_file)

    @staticmethod
    def output_recent_not_following_you_back(
        followers_old: Path, following_old: Path,
        followers_new: Path, following_new: Path,
        output_file: Path
    ) -> None:
        rows = InstagramScraper._compute_recent_not_following_you_back(
            followers_old, following_old, followers_new, following_new
        )
        InstagramScraper._write_rows(rows, output_file)