.. _decorator:

装饰器
======================

.. contents:: 目录

本节全面介绍python中的装饰器(decorator)。

装饰器的引入
------------------

- 装饰器就是拓展原来函数功能的一种函数，这个函数的返回值也是一个函数。
- 装饰器其实就是一个闭包，把一个函数当作参数然后返回一个替代版参数。
- 使用装饰器的好处是在不用更改原函数的代码前提下给函数增加新的功能。
- 装饰器可以扩展原函数的日志，性能测试，时间测试，事务处理，缓存，权限校验等等功能。


定义一个打印消息的函数::

    In [1]: def print_hello(): 
        ...:     print('message:hello') 
        ...:                                                                             

    In [2]: print_hello()                                                    
    message:hello

现在有一个新的需求，希望可以打印函数的执行日志，显示执行的是哪个函数，于是在代码中添加日志代码(假设用print代替logging.info打印日志)::

    In [1]: def print_hello(): 
        ...:     print('print_hello is running’) # 原始侵入，篡改原函数
        ...:     print('message:hello') 
        ...:                                                                             

    In [2]: print_hello()    
    print_hello is running                                                
    message:hello

如果我们还有其他的函数，如foo1(),foo2()函数也有类似的需求，再写一个print logging在foo1或foo2函数里面吗？这样就造成大量雷同的代码，为了减少重复写代码，我们可以这样做，重新定义一个新的函数：专门处理日志，日志处理完之后再执行真正的业务代码::

    In [3]: def logit(func): 
        ...:     print('{} is running'.format(func.__name__)) 
        ...:     func() 
        ...:                                                                        

    In [4]: def print_hello(): 
        ...:     print('message:hello') 
        ...:                                                                        

    In [5]: logit(print_hello)                                                     
    print_hello is running
    message:hello

这样做逻辑上是没有问题的，功能是实现了，但是我们调用的时候不再是调用真正的业务逻辑print_hello函数，而是换成了logit函数，这破坏了原的的代码结构，现在不得不每次都要把原来的print_hello函数作为参数传递给logit函数。那么有没有更好的方式呢？当然有，答案就是使用装饰器函数。

简单装饰器
------------------

定义一个logit的装饰器::

    In  [6]: def logit(func):  
        ...:     def wrapper(): 
        ...:         print('{} is running'.format(func.__name__))  
        ...:         return func()   
        ...:     return wrapper 
        ...:                                                                        

    In  [7]: def print_hello():  
        ...:     print('message:hello') 
        ...:                                                                        

    In  [8]: print_hi=logit(print_hello)  # 因为装饰器logit(print_hello)返回的是函数对象wrapper，这条语句相当于print_hi = wrapper                                         

    In  [9]: print_hi()  # 执行print_hi()就相当于执行 wrapper()                                                       
    print_hello is running
    message:hello

    In [10]: type(print_hi)                                                         
    Out[10]: function


logit是一个装饰器，它把执行真正业务逻辑的函数func包裹在其中，看起来像是print_hello被logit装饰一样，logit返回的也是一个函数，函数名称是wrapper。函数进入和退出时，被称为一个横切面，这种编程方式被称为面向切面的编程。


@语法糖
------------------

- @符号就是装饰器的语法糖，它放在函数开始定义的地方，这样就可以省略最后一步再次赋值的操作。

接上面的In  [6]定义的logit的装饰器，使用@语法糖装饰print_hello函数::

    In [11]: @logit 
        ...: def print_hello(): 
        ...:     print('message:hello') 
        ...:                                                                        

    In [12]: print_hello()                                                          
    print_hello is running
    message:hello


如上所示，有了@，我们就可以省去print_hi=logit(print_hello)这一句了，直接调用 print_hello() 即可得到想要的结果。你们看到了没有，print_hello() 函数不需要做任何修改，只需在定义的地方加上装饰器，调用的时候还是和以前一样，如果我们有其他的类似函数，我们可以继续调用装饰器来修饰函数，而不用重复修改函数或者增加新的封装。这样，我们就提高了程序的可重复利用性，并增加了程序的可读性。


\*args, \*\*kwargs的使用
-------------------------

- 在函数定义时，当参数不确定时，可以使用*args或**kwargs来接收参数组成的元组或字典；
- 使用*收集位置参数，使用**收集关键字参数；
- 元组存储在args中，字典存储在kwargs中。

如果我们业务逻辑中打印消息不固定为hello,需要传递一个参数message，并打印message的内容::

    def print_message(message): 
        print('message:{}'.format(message)) 

此时，可以在定义wrapper函数的时候指定参数::

    #Filename: print_message.py
    def logit(func):

        def wrapper(message):
            print("%s is running" % func.__name__)
            return func(message)
        return wrapper

    @logit
    def print_message(message): 
        print('message:{}'.format(message)) 

    print_message('new message1')
    print_message('new message2')

使用python3 print_message.py运行::

    [meizhaohui@localhost ~]$ python print_message.py 
    print_message is running
    message:new message1
    print_message is running
    message:new message2

这样print_message函数定义的参数，如message就可以定义在wrapper函数中。

如果print_message中定义了多个参数，并设置有关键字参数，这个时候就可以在wrapper函数中使用\*args, \*\*kwargs，这样一个新的装饰器就出现了::

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

使用python3 print_message.py运行::

    [meizhaohui@localhost ~]$ python print_message.py 
    print_message is running
    Hi,Guido van Rossum,you said message:The Zen of Python.You are the father of Python
    print_message is running
    Hi,Rob Pike,you said message:Go makes it easy to build simple, reliable, and efficient software.You are the father of Go

这样不论print_message函数有多少个参数，logit装饰器都可以使用！！！装饰器就像一个注入符号：有了它，拓展了原来函数的功能既不需要侵入函数内更改代码，也不需要重复执行原函数。


带参数的装饰器
-------------------------

装饰器还有更大的灵活性，例如带参数的装饰器，在上面的装饰器调用中，该装饰器接收唯一的参数就是执行业务的函数func。装饰器的语法允许我们在调用时，提供其它参数，比如@logit(level)。这样，就为装饰器的编写和使用提供了更大的灵活性。比如，我们可以在装饰器中指定日志的等级，因为不同业务函数可能需要的日志级别是不一样的。

我们按实际场景使用logging模块重新一个日志装饰器::


    #Filename: print_logs.py
    def logit(level):
        import logging
        def decorator(func):
            def wrapper(*args, **kwargs):
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
        print('message:hello') 

    @logit(level='warning')
    def print_message(name, message=None, lang='Python'): 
        print('Hi,{},you said message:{}.You are the father of {}'.format(name, message, lang)) 

    print_hello()
    print_message('Guido van Rossum','The Zen of Python')

使用python3 print_logs.py运行::

    [meizhaohui@localhost ~]$ python3 print_logs.py 
    2019-03-19 22:48:53,455 - root - INFO - print_hello is running
    message:hello
    2019-03-19 22:48:53,455 - root - WARNING - print_message is running
    Hi,Guido van Rossum,you said message:The Zen of Python.You are the father of Python


上面的logit是允许带参数的装饰器。它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。我们可以将它理解为一个含有参数的闭包。当我 们使用@logit(level="warning")调用的时候，Python能够发现这一层的封装，并把参数传递到装饰器的环境中。@logit(level='warning')等价于@decorator。


类装饰器
-------------------------

装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。

示例::

    #Filename: class_decorator.py
    class Foo(object):
        def __init__(self, func):
            self._func = func

        def __call__(self):
            print ('class decorator runing')
            self._func()
            print ('class decorator ending')

    @Foo
    def bar():
        print ('bar')

    bar()

使用python3 class_decorator.py运行::

    [meizhaohui@localhost ~]$ python3 class_decorator.py 
    class decorator runing
    bar
    class decorator ending

装饰器的弊端
-------------------------

使用装饰器极大地复用了代码，但是他有一个弊端就是原函数的元信息不见了，比如函数的docstring、__name__、参数列表等。

在print_logs.py文件中增加文档字符串后，最后打印函数的docstring、__name__，内容如下::

    #Filename: print_logs.py
    def logit(level):
        import logging
        def decorator(func):
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


使用python3 print_logs.py运行::

    meizhaohui@localhost ~]$ python3 print_logs.py 
    2019-03-19 23:06:29,019 - root - INFO - print_hello is running
    message:hello
    2019-03-19 23:06:29,019 - root - WARNING - print_message is running
    Hi,Guido van Rossum,you said message:The Zen of Python.You are the father of Python
    wrapper decorator docs
    wrapper decorator docs


可以发现print_hello和print_message函数都被wrapper取代了，当然它的docstring，__name__就是变成了wrapper函数的信息了。


装饰器的弊端
-------------------------

为了消除装饰器的弊端，Python的functools包中提供了一个叫wraps的装饰器来消除这样的副作用。写一个decorator装饰器的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring。

改进上面的print_logs.py，内容如下::

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

使用python3 print_logs.py运行::

    [meizhaohui@localhost ~]$ python3 print_logs.py 
    2019-03-19 23:14:45,636 - root - INFO - print_hello is running
    message:hello
    2019-03-19 23:14:45,636 - root - WARNING - print_message is running
    Hi,Guido van Rossum,you said message:The Zen of Python.You are the father of Python
    print_hello print_hello docs
    print_message print_message docs

内置装饰器
-------------------------

内置的装饰器和普通的装饰器原理是一样的，只不过返回的不是函数，而是类对象，所以更难理解一些。
如@property，@staticmethod，@classmethod，后续补充。

参考文献：

- `Python 函数装饰器 <http://www.runoob.com/w3cnote/python-func-decorators.html>`_
- `python装饰器讲解 <https://blog.csdn.net/weixin_41656968/article/details/80232507>`_
- `python装饰器详解 <https://blog.csdn.net/xiangxianghehe/article/details/77170585>`_
- `详解Python的装饰器 <https://www.cnblogs.com/cicaday/p/python-decorator.html>`_
- `python装饰器的wraps作用 <https://blog.csdn.net/hqzxsc2006/article/details/50337865>`_


