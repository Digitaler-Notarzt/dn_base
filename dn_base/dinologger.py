import logging
from logging.handlers import RotatingFileHandler
from colorama import init, Fore, Style


# Initialize Colorama for cross-platform support
init(autoreset=True)

class ColorFormatter(logging.Formatter):
    """Custom formatter to add colors to log levels for console output."""

    COLORS = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.LIGHTRED_EX + Style.BRIGHT,
    }

    def format(self, record):
        """Override format method to add color to the log level name."""
        color = self.COLORS.get(record.levelname, "")
        record.levelname = f"{color}{record.levelname}{Style.RESET_ALL}"
        return super().format(record)


def get_logger(
    name: str,
    level: int = logging.DEBUG,
    log_file: str = "app.log",
    max_bytes: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5
) -> logging.Logger:
    """
    Creates a logger that writes to both console and a log file.

    Args:
        name (str): The name of the logger.
        level (int): The logging level (e.g., logging.DEBUG, logging.INFO).
        log_file (str): Path to the log file.
        max_bytes (int): Maximum size of the log file before rotating.
        backup_count (int): Number of backup files to keep.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger with the specified name
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Check if the logger already has handlers to avoid duplicates
    if not logger.handlers:

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # File handler
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setLevel(level)

        console_formatter = ColorFormatter('%(levelname)s: %(asctime)s - %(message)s')

        # Add a formatter to the handlers
        console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(console_formatter)

        # Add handlers to the logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
