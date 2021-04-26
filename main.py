from sys import argv
from configurator import Configurator
from connector import Connector
from resulting import Result
from test_processor import TestProcessor


def run():
    #config = Configurator(argv[1])
    config = Configurator('dev')
    database_url = config.get_database_url()
    database_folder = config.get_test_data_folder()
    # print(database_url)
    # print(database_folder)
    connector = Connector(database_url)
    logger = Result()
    test_processor = TestProcessor(config, connector, logger)
    test_processor.process()
    logger.finish_test()


if __name__ == '__main__':
    run()
