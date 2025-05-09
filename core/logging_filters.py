import logging
from logging import LogRecord


class MinLenFilter(logging.Filter):
    """
    Filter on logging system to minimum length of 20.
    """

    def filter(self, record: LogRecord) -> bool:
        """
        Overriding filter method
        :param record:
        :return: True or False
        """
        return len(record.getMessage()) > 20
