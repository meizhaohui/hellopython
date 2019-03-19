#Filename: print_message.py
def logit(func):

    def wrapper(*args, **kwargs):
        print("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logit
def print_message(name, message=None, lang='Python'): 
    print('Hi,{},you said message:{}.You are the father of {}'.format(name, message, lang)) 

print_message('Guido van Rossum','The Zen of Python')
print_message('Rob Pike','Go makes it easy to build simple, reliable, and efficient software',lang='Go')
