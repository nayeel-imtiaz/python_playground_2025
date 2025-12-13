import logging
import sys


def setup_logger() -> logging.Logger:
    """
    Creates a structured logger for the whole instagram package.
    INFO and DEBUG go to stdout.
    WARNING+ go to stderr.
    """
    logger = logging.getLogger("instagram")
    logger.setLevel(logging.DEBUG)  # capture everything; handlers filter it

    # Avoid adding duplicate handlers on repeated setup calls
    if logger.handlers:
        return logger

    # --- stdout handler (INFO and below) ---
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_filter = lambda record: record.levelno <= logging.INFO
    stdout_handler.addFilter(stdout_filter)

    # --- stderr handler (WARNING and above) ---
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.WARNING)

    # --- formatter ---
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    stdout_handler.setFormatter(formatter)
    stderr_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)

    return logger
