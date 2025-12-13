from instagram.instagram_scraper import InstagramScraper
from instagram.logger import setup_logger
from pathlib import Path
import instagram

DEFAULT_DATE = "11-18-25"


def main():
    logger = setup_logger()

    BASE_DIR = Path(instagram.__file__).resolve().parent
    FOLLOWERS_DIR = BASE_DIR / "instagram_data" / "followers"
    FOLLOWING_DIR = BASE_DIR / "instagram_data" / "following"
    OUTPUT_DIR = BASE_DIR / "output" / "instagram_scraper_output"

    logger.info("Instagram scraper started.")

    date_str = input(f"Enter date (MM-DD-YY), default [{DEFAULT_DATE}]: ").strip()

    if not date_str:
        logger.info(f"No input. Using default date {DEFAULT_DATE}.")
        date_str = DEFAULT_DATE

    followers = FOLLOWERS_DIR / f"{date_str}.json"
    following = FOLLOWING_DIR / f"{date_str}.json"
    results = OUTPUT_DIR / f"{date_str}.csv"

    if not followers.exists() or not following.exists():
        logger.warning(f"Data files for {date_str} not found — falling back to {DEFAULT_DATE}.")
        date_str = DEFAULT_DATE
        followers = FOLLOWERS_DIR / f"{date_str}.json"
        following = FOLLOWING_DIR / f"{date_str}.json"
        results = OUTPUT_DIR / f"{date_str}.csv"

    logger.info(f"Using followers file: {followers}")
    logger.info(f"Using following file: {following}")
    logger.info(f"Output will be saved to: {results}")

    InstagramScraper.output_not_following_you_back(followers, following, results)

    logger.info("Scraping complete.")
    logger.info(f"Results written to {results}")


if __name__ == '__main__':
    main()
