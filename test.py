from logger import Level, Logger
import os


LOG_FILE = './log'
DEBUG_MESSAGE = "This is a debug message"
INFO_MESSAGE = "This is an info message"
WARNING_MESSAGE = "This is a warning message"
ERROR_MESSAGE = "This is an error message"


def test_log():
    logger = Logger(LOG_FILE, buffer_size=1)
    logger.debug(DEBUG_MESSAGE)
    logger.info(INFO_MESSAGE)
    logger.warning(WARNING_MESSAGE)
    logger.error(ERROR_MESSAGE)

    with open(LOG_FILE, 'r') as log_file:
        log_entries = log_file.readlines()

        assert len(log_entries) == 4
        messages = [
            (0, Level.DEBUG, DEBUG_MESSAGE),
            (1, Level.INFO, INFO_MESSAGE),
            (2, Level.WARNING, WARNING_MESSAGE),
            (3, Level.ERROR, ERROR_MESSAGE),
        ]
        for index, level, message in messages:
            assert log_entries[index].endswith('%s: %s\n' % (level, message))

    os.remove(LOG_FILE)