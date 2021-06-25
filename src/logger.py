import logging
import json
class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({'msg': record.getMessage(), 'level': record.levelname})