''' Logger util '''

import logging
import time

from pythonjsonlogger import jsonlogger

def init_logger(name: str):
    '''
    Description: initializes custom logger

    Args:
        name (str): The name of the logger, typically __name__

    Returns: logger
    '''
    # Create logger
    logger = logging.getLogger(name)

    # only configure handlers if not already configured to avoid duplicate handlers
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        # logger.setLevel(logging.DEBUG)

        # Create console handler
        console_handler = logging.StreamHandler()

        # Create JSON formatter
        custom_format = '[%(asctime)s] [%(levelname)s] [%(pathname)s] [%(funcName)s] | %(message)s'
        formatter = jsonlogger.JsonFormatter(custom_format)

        # Use UTC time
        formatter.converter = time.gmtime

        # Add formatter to handler
        console_handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(console_handler)

    return logger
