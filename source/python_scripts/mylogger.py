#!/usr/bin/python3
"""
@Time    : 2019/4/1
@Author  : Mei Zhaohui
@Email   : mzh.whut@gmail.com
@Filename: mylogger.py
@Software: PyCharm
@Desc    : myself logger
"""
import logging

def mylogger(level, logfile=None):
    """myself logger"""
    logging.root.setLevel(logging.NOTSET)
    logger = logging.getLogger(__file__)
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s line:%(lineno)d %(message)s')
    console_handle = logging.StreamHandler()
    if level == 'warning':
        console_handle.setLevel(logging.WARNING)
    elif level == 'debug':
        console_handle.setLevel(logging.DEBUG)
    else:
        console_handle.setLevel(logging.INFO)

    console_handle.setFormatter(log_format)
    logger.addHandler(console_handle)

    if logfile:
        file_handle = logging.FileHandler(logfile)
        if level == 'warning':
            file_handle.setLevel(logging.WARNING)
        elif level == 'debug':
            file_handle.setLevel(logging.DEBUG)
        else:
            file_handle.setLevel(logging.INFO)
        file_handle.setFormatter(log_format)
        logger.addHandler(file_handle)
    return logger

def main():
    """main function"""
    mylog = mylogger('debug', 'info.log')
    mylog.debug('my debug log')
    mylog.info('my info log')
    mylog.warning('my warning log')


if __name__ == '__main__':
    main()
