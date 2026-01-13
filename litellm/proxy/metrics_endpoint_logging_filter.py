import logging
from typing import cast


class MetricsEndpointLoggingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if isinstance(record.args, tuple):
            method = cast(str, record.args[1])
            query_string = cast(str, record.args[2])

            return method != "GET" or not query_string.startswith("/metrics")

        return True
