#Filename: print_logs.py
from functools import wraps
def logit(level):
    import logging
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''decorator docs'''
            logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger = logging.getLogger(__name__)
            if level == 'warning':
                logging.warn("%s is running" % func.__name__)
            elif level == 'info':
                logging.info("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@logit(level='info') 
def print_hello(): 
    '''print_hello docs'''
    print('message:hello') 

@logit(level='warning')
def print_message(name, message=None, lang='Python'): 
    '''print_message docs'''
    print('Hi,{},you said message:{}.You are the father of {}'.format(name, message, lang)) 

print_hello()
print_message('Guido van Rossum','The Zen of Python')
print(print_hello.__name__, print_hello.__doc__)
print(print_message.__name__, print_message.__doc__)
