import logging
from datetime import datetime

file_path = f'logs/app-{datetime.now().strftime("%Y-%m-%d_%H")}.log'


def configure_logger(log_file=file_path,
                     log_level=logging.DEBUG):
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename=log_file,
                        filemode='a')


def get_logger(log_file=file_path):
    configure_logger(log_file=log_file)
    return logging.getLogger(__name__)


def log_debug(message, log_file=file_path):
    logger = get_logger(log_file=log_file)
    logger.debug(message)


def log_info(message, log_file=file_path):
    logger = get_logger(log_file=log_file)
    logger.info(message)


def log_warning(message, log_file=file_path):
    logger = get_logger(log_file=log_file)
    logger.warning(message)


def log_error(message, log_file='app.log'):
    logger = get_logger(log_file=log_file)
    logger.error(message)


def log_critical(message, log_file='app.log'):
    logger = get_logger(log_file=log_file)
    logger.critical(message)
