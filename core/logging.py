import os
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logging(config):
    log_level_config = config.get("logging.level", "INFO").upper()
    log_level = getattr(logging, log_level_config, logging.INFO)

    log_format = "%(asctime)s.%(msecs)03d | %(levelname)-5s | [%(name)s:%(lineno)d] | %(message)s"
    date_format = "%Y-%m-%dT%H:%M:%S"

    formatter = logging.Formatter(log_format, datefmt=date_format)

    # <----- Root Logger ----->
    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.handlers.clear()

    # <----- Console Log ----->
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # <----- Log file Rotate ----->
    log_file = config.get("logging.file", "logs/app.log")
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    file_handler = TimedRotatingFileHandler(
        filename=log_file,
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.suffix= "%Y%m%d"

    # <----- Add Handlers ----->
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def get_logger(name: str):
    return logging.getLogger(name)