# Filename: networkerror.py
# Author: meizhaohui

class NetworkError(RuntimeError):
    def __init__(self, host):
        self._host = host

    def __str__(self):
        return 'Unknow host:{}'.format(self._host)

if __name__ == '__main__':
    try:
        raise NetworkError('python.org')
    except NetworkError as e:
        print('NetworkError: %s' % e)
