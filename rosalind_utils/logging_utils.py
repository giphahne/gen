

import sys
from datetime import datetime
import time

TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S.%fZ'


class LogPrinter(object):
    """
    A class implementing a 'log like' interface toward 
    printing.
    """

    @classmethod
    def _format_log_message(cls, log_message):
        timestamp = datetime.strftime(datetime.now(), TIMESTAMP_FORMAT)
        return ("{timestamp}: {log_message}"
                .format(timestamp=timestamp,
                        log_message=log_message))

    @classmethod
    def _print_log_message(cls, log_message):
        print(cls._format_log_message(log_message))

    @classmethod
    def _print_err_message(cls, log_message):
        print(cls._format_log_message(log_message), file=sys.stderr)
        
    @classmethod
    def info(cls, log_message):
        cls._print_log_message(log_message)
        return log_message

    @classmethod
    def error(cls, log_message):
        cls._print_err_message(log_message)


class FlushingLogPrinter(LogPrinter):
    """
    """
    @classmethod
    def info(cls, log_message):
        cls._print_log_message(log_message)
        sys.stdout.flush()
        return log_message

    @classmethod
    def error(cls, log_message):
        cls._print_err_message(log_message)
        sys.stderr.flush()
        
lg = FlushingLogPrinter
#lg = LogPrinter
