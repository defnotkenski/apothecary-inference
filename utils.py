import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme


def setup_logger() -> logging.Logger:
    # Set up custom logging to be used with Rich.

    rich_console = Console(stderr=True, theme=Theme({
        "log.time": "dim magenta",
        "logging.level.debug": "bold cyan1",
        "logging.level.info": "bold cyan1",
        "logging.level.warning": "bold yellow1",
        "logging.level.error": "bold yellow1",
        "logging.level.critical": "bold reverse yellow1",
        "log.message": "pink1"
    }))

    rh = RichHandler(
        show_time=True,
        omit_repeated_times=False,
        show_level=True,
        show_path=False,
        markup=False,
        rich_tracebacks=True,
        log_time_format="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
        console=rich_console,
    )

    logger = logging.getLogger("banana_bread")

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(rh)
    logger.setLevel(logging.DEBUG)

    return logger
