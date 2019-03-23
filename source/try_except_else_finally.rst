.. _try_except_else_finally:

异常
======================

.. contents:: 目录

本节介绍Python的异常。

异常的定义
-------------------

- 异常是一个事件，该事件会在程序执行时发生，影响程序的正常执行。
- 一般情况下，在Python无法正常处理程序时就会发生一个异常。
- 异常是Python对象，表示一个错误。
- 当Python脚本发生异常时，我们需要捕获处理它，否则程序会终止运行。
- 当你执行可能出错的代码时，需要适当的异常处理程序用于阻止潜在的错误发生。
- 在异常可能发生的地方添加异常处理程序，对于用户明确错误是一种好办法。


常见的异常
-------------------

- ZeroDivisionError除零异常::

   In [1]: 1/0
   ---------------------------------------------------------------------------
   ZeroDivisionError                         Traceback (most recent call last)
   <ipython-input-1-9e1622b385b6> in <module>
   ----> 1 1/0

   ZeroDivisionError: division by zero

- AttributeError属性异常::

    In [2]: import os                                                               
    
    In [3]: os.name                                                                 
    Out[3]: 'posix'
    
    In [4]: os.Name                                                                 
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-4-edb55bc87dba> in <module>
    ----> 1 os.Name
    
    AttributeError: module 'os' has no attribute 'Name'

- ImportError导入异常::

    In [5]: import maths                                                                                                                   
    ---------------------------------------------------------------------------
    ImportError                               Traceback (most recent call last)
    <ipython-input-8-6e25cba24411> in <module>
    ----> 1 import maths
    
    ImportError: No module named 'maths'
    
    In [6]: import math     

- IndexError索引异常::

    In [7]: list1=['a','b']
    
    In [8]: list1[3]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-8-831b15cbf272> in <module>
    ----> 1 list1[3]
    
    IndexError: list index out of range
   
- SyntaxError语法异常::

    In [9]: print 'hello'
      File "<ipython-input-9-5a1ef41e7057>", line 1
        print 'hello'
                    ^
    SyntaxError: Missing parentheses in call to 'print'
    
- IndentationError缩进异常::

    In [10]: a = 1                                                                                                                         
    
    In [11]: if a > 0: 
        ...:     print(a) 
        ...:   print(a + 1)                                                                                                                
      File "<tokenize>", line 3
        print(a + 1)
        ^
    IndentationError: unindent does not match any outer indentation level
    
内置异常
-------------------

Python所有的错误都是从BaseException类派生的，内置异常见如下::

    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
          |    +-- ModuleNotFoundError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning
               
异常处理语法
-------------------

异常处理语法如下::

    try:
        <statements>        #运行try语句块，并试图捕获异常
    except <ExceptionErrorName1>:
        <statements>        #如果ExceptionErrorName1异常发现，那么执行该语句块。
    except (ExceptionErrorName2,ExceptionErrorName3):
        <statements>        #如果元组内的任意异常发生，那么捕获它
    except <ExceptionErrorName4> as <variable>:
        <statements>        #如果ExceptionErrorName4异常发生，那么进入该语句块，并把异常实例命名为variable
    except:
        <statements>        #发生了以上所有列出的异常之外的异常
    else:
    <statements>            #如果没有异常发生，那么执行该语句块
    finally:
        <statement>         #无论是否有异常发生，均会执行该语句块

说明:

- else和finally是可选的，可能会有0个或多个except，但是，如果出现一个else的话，必须有至少一个except。
- 不管你如何指定异常，异常总是通过实例对象来识别，并且大多数时候在任意给定的时刻激活。一旦异常在程序中某处由一条except子句捕获，它就死掉了，除非由另一个raise语句或错误重新引发它。
- 在try中的代码如果发生异常，则会被捕获，然后执行except中的代码，否则跳过except块代码，此时执行else语句块。
- 无论异常是否发生finally语句块的代码一定会执行。
- 在对异常进行处理时，建议except后面接具体的异常名称，不要直接使用except不接任何异常名去处理异常，因为except适用于任何异常类型，你可以使用一个except去捕获所有的异常，但这样的处理方式会比较泛化。
- 可以使用as将异常名称赋值给变量，再输出存储在变量中的异常信息。
  
异常处理示例
-------------------

- 示例1

处理除零异常::

    # Filename: try_except_else_finally.py
    # Author: meizhaohui
    def expt1(a, b):
        try:
            c = a/b
            print('the value is:{}'.format(c))
        except ZeroDivisionError:
            print('程序出现异常，异常信息：被除数为0')
    
    expt1(4,0)

运行::

   meizhaohui@localhost python_scripts]$ python3 try_except_else_finally.py 
   程序出现异常，异常信息：被除数为0

以上程序，我们已经获取到了除零异常ZeroDivisionError,感觉自己处理得很完美。假如我们将expt1(4,0)改为expt1(4,''),然后再运行看看会发生什么。

运行::

    [meizhaohui@localhost python_scripts]$ python3 try_except_else_finally.py 
    Traceback (most recent call last):
      File "try_except_else_finally.py", line 10, in <module>
        expt1(4,'')
      File "try_except_else_finally.py", line 5, in expt1
        c = a/b
    TypeError: unsupported operand type(s) for /: 'int' and 'str'
    
怎么又出现了一个TypeError类型异常，但我们却没有捕获到，上面提示不能在int类型和字符串类型之间做除法运算。看来我们要补上这个异常的处理，获取到这个异常。

我们改一个这个脚本文件::


    # Filename: try_except_else_finally.py
    # Author: meizhaohui
    def expt2(a, b):
        try:
            c = a/b
            print('the value is:{}'.format(c))
        except ZeroDivisionError:
            print('程序出现异常，异常信息：被除数为0')
        except TypeError:
            print('程序出现异常，异常信息：参数a和b类型不同,仅支持float或int类型')
    
    expt2(4,'')

运行::

   [meizhaohui@localhost python_scripts]$ python3 try_except_else_finally.py
   程序出现异常，异常信息：参数a或b的类型不支持，仅支持float或int类型

我们看一下能不能捕获除零异常::


    # Filename: try_except_else_finally.py
    # Author: meizhaohui
    def expt2(a, b):
        try:
            c = a/b
            print('the value is:{}'.format(c))
        except ZeroDivisionError:
            print('程序出现异常，异常信息：被除数为0')
        except TypeError:
            print('程序出现异常，异常信息：参数a和b类型不同,仅支持float或int类型')
    
    expt2(4,0)

运行::

   [meizhaohui@localhost python_scripts]$ python3 try_except_else_finally.py
   程序出现异常，异常信息：被除数为0

可以看出除零异常和类型异常都能正常的捕获到。

参考文献:

#. `Python异常处理 <http://www.runoob.com/python/python-exceptions.html>`_
#. `Built-in Exceptions <https://docs.python.org/3.6/library/exceptions.html?highlight=exception>`_
#. `Python异常及处理方法总结 <https://blog.csdn.net/polyhedronx/article/details/81589196>`_
#. `Python中的异常处理 <https://www.cnblogs.com/jessonluo/p/4743574.html>`_
#. `Python——异常 <https://blog.csdn.net/qq_41573234/article/details/82466313>`_


