import json
import csv
from pathlib import Path


class InstagramScraper:
    @staticmethod
    def scrape_followers(followers_file_name: Path) -> set:
        with open(followers_file_name) as followers_json_file:
            json_followers_data = json.load(followers_json_file)
            followers_set = set()
            for json_dict in json_followers_data:
                followers_set.add((json_dict["string_list_data"][0]["value"], json_dict["string_list_data"][0]["href"]))
            return followers_set

    @staticmethod
    def scrape_following(following_file_name: Path) -> set:
        with open(following_file_name) as json_file:
            json_following_data = json.load(json_file)
            following_set = set()
            for json_dict in json_following_data["relationships_following"]:
                following_set.add((json_dict["title"], json_dict["string_list_data"][0]["href"].replace("_u/", "")))
            return following_set

    @staticmethod
    def scrape_not_following_you_back(followers_file_name: Path, following_file_name: Path) -> set:
        return (
                InstagramScraper.scrape_following(following_file_name)
                - InstagramScraper.scrape_followers(followers_file_name)
        )

    @staticmethod
    def output_not_following_you_back(
            followers_file_name: Path,
            following_file_name: Path,
            output_file_name: Path
    ) -> None:
        not_following_you_back_set = InstagramScraper.scrape_not_following_you_back(
            followers_file_name,
            following_file_name
        )
        with open(output_file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "link"])
            writer.writerows(sorted(not_following_you_back_set))