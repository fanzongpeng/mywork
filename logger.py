
import os,logging

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)  # 输出所有大于DEBUG级别的log
# 设置日志输出格式
fmt = logging.Formatter('[%(filename)-6s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')
stream_hdl = logging.StreamHandler()
stream_hdl.setFormatter(fmt)
stream_hdl.setLevel(logging.DEBUG)
logger.addHandler(stream_hdl)

# logger.info('这是info')
# logger.debug('这是debug')
# logger.error('这是error')
