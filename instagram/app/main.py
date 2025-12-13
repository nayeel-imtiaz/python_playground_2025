from instagram.instagram_scraper import InstagramScraper
from instagram.logger import setup_logger
from pathlib import Path
import instagram

DEFAULT_NEW_DATE = "12-12-25"
DEFAULT_REFERENCE_DATE = "11-18-25"


def resolve_data_files(base_dir: Path, date_str: str):
    followers_dir = base_dir / "instagram_data" / "followers"
    following_dir = base_dir / "instagram_data" / "following"
    return (
        followers_dir / f"{date_str}.json",
        following_dir / f"{date_str}.json",
    )


def ensure_files_exist_or_fallback(logger, base_dir: Path, date_str: str, fallback_date: str):
    followers, following = resolve_data_files(base_dir, date_str)

    if followers.exists() and following.exists():
        return date_str, followers, following

    logger.warning(f"Data files for {date_str} not found — falling back to {fallback_date}.")
    followers, following = resolve_data_files(base_dir, fallback_date)
    return fallback_date, followers, following


def main():
    logger = setup_logger()

    base_dir = Path(instagram.__file__).resolve().parent
    output_dir = base_dir / "output" / "instagram_scraper_output"
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Instagram scraper started.")

    mode = input("Choose mode: [A]ll not-following-back or [R]ecent since reference date (default A): ").strip().lower()
    if mode not in {"a", "r", ""}:
        logger.warning("Invalid mode. Defaulting to All.")
        mode = "a"
    if mode == "":
        mode = "a"

    if mode == "a":
        date_str = input(f"Enter date for snapshot (MM-DD-YY), default [{DEFAULT_NEW_DATE}]: ").strip() or DEFAULT_NEW_DATE
        date_str, followers, following = ensure_files_exist_or_fallback(logger, base_dir, date_str, DEFAULT_NEW_DATE)

        results = output_dir / f"{date_str}_not_following_back.csv"

        logger.info(f"Using followers file: {followers}")
        logger.info(f"Using following file: {following}")
        logger.info(f"Output will be saved to: {results}")

        InstagramScraper.output_not_following_you_back(followers, following, results)

    else:  # mode == "r"
        new_date = input(f"Enter NEW date (MM-DD-YY), default [{DEFAULT_NEW_DATE}]: ").strip() or DEFAULT_NEW_DATE
        ref_date = input(f"Enter REFERENCE (old) date (MM-DD-YY), default [{DEFAULT_REFERENCE_DATE}]: ").strip() or DEFAULT_REFERENCE_DATE

        new_date, followers_new, following_new = ensure_files_exist_or_fallback(logger, base_dir, new_date, DEFAULT_NEW_DATE)
        ref_date, followers_old, following_old = ensure_files_exist_or_fallback(logger, base_dir, ref_date, DEFAULT_REFERENCE_DATE)

        results = output_dir / f"{ref_date}_to_{new_date}_recent_not_following_back.csv"

        logger.info(f"Using NEW followers file: {followers_new}")
        logger.info(f"Using NEW following file: {following_new}")
        logger.info(f"Using REF followers file: {followers_old}")
        logger.info(f"Using REF following file: {following_old}")
        logger.info(f"Output will be saved to: {results}")

        InstagramScraper.output_recent_not_following_you_back(
            followers_old, following_old,
            followers_new, following_new,
            results
        )

    logger.info("Scraping complete.")
    logger.info("Done.")


if __name__ == "__main__":
    main()
