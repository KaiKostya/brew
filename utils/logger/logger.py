import json
import logging
import logging.config
import os


class Logger:
    """class for logging. For logging setup we need to call Logger.create_logger()"""
    main_logger = None
    tests_logger = None
    utils_logger = None

    @staticmethod
    def create_logger():
        checkout_dir = os.environ.get("checkout_dir", "/Users/mac/projects")
        log_file = os.environ.get("LOG_FILE", f"{checkout_dir}/brew/test_log.log")
        log_config = os.environ.get("LOG_CONFIG", f'{checkout_dir}/brew/log_config.json')
        if os.path.isfile(log_file):
            os.remove(log_file)
        with open(log_config, 'r') as logging_configuration_file:
            config_dict = json.load(logging_configuration_file)
        logging.config.dictConfig(config_dict)
        logger = logging.getLogger()  # root logger
        Logger.main_logger = logging.getLogger('brew')
        Logger.tests_logger = Logger.main_logger.getChild('tests')
        Logger.utils_logger = Logger.main_logger.getChild('utils')
        Logger.main_logger.info("Tests started")
