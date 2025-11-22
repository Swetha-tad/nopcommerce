import logging

class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=r".\\logs\\nopcommercedemo.log",
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger



