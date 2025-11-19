from instagram.instagram_scraper import InstagramScraper
from pathlib import Path
import instagram

DEFAULT_DATE = "11-18-25"


def main():
    BASE_DIR = Path(instagram.__file__).resolve().parent
    FOLLOWERS_DIR = BASE_DIR / "instagram_data" / "followers"
    FOLLOWING_DIR = BASE_DIR / "instagram_data" / "following"
    OUTPUT_DIR = BASE_DIR / "output" / "instagram_scraper_output"

    date_str = input(f"Enter date (MM-DD-YY), default [{DEFAULT_DATE}]: ").strip()

    if not date_str:
        date_str = DEFAULT_DATE

    followers = FOLLOWERS_DIR / f"{date_str}.json"
    following = FOLLOWING_DIR / f"{date_str}.json"
    results = OUTPUT_DIR / f"{date_str}.csv"

    InstagramScraper.output_not_following_you_back(followers, following, results)


if __name__ == '__main__':
    main()
