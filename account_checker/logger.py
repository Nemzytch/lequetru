import logging
import sys
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

file_path = 'main.log'
file_size = 1_048_576  # 1 MB
fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
date_fmt = '%m/%d/%Y %I:%M:%S %p'

logger = logging.Logger('CLIENT')
formatter = logging.Formatter(fmt, date_fmt)
stream_handler = StreamHandler(sys.stdout)
file_handler = RotatingFileHandler(file_path, maxBytes=file_size, backupCount=1)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
# file_handler.setLevel(logging.DEBUG)
# stream_handler.setLevel(logging.INFO)
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)