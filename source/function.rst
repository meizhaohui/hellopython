.. _function:

函数
======================

.. contents:: 目录

本节全面介绍python中函数的使用。

函数的创建
------------------

- 函数是重用的程序段。允许给一个语块一个名称，然后在别的位置调用这个函数。
- 函数通过def关键字定义。

语法如下::

    def function_name([arg1,][arg2,][arg3]):
        cmds
        
    function_name 为函数名
    arg1/arg2/arg3 为形参

    
在PyCharm中运行::

    # 函数定义
    def sayHi(name):
        print('hi! ',name,'. I am Python. How are you?')
        
    # 调用函数，并传递参数'meichaohui'
    sayHi('meichaohui')

    # 运行结果如下::
    # hi!  meichaohui . I am Python. How are you?
    
局部变量与全局变量
--------------------------

- 局部变量

当你在函数内定义变量时，它们与函数外具有相同名称的其他变量没有任何关系，即变量名称对于函数来说是局部的，这称为变量的作用域。

所有变量的作用域是它们被定义的块，从它们的名称被定义的那点开始。

- 全局变量

如果在函数中需要使用全局变量，也就是说这个变量能在函数外可以引用，需要使用global关键字进行定义，函数中的全局变量有以下限制::

    * 定义方式为global后面接全局变量名称var_name（即 global var_name   # 定义方式为global后面接全局变量名称var_name）
    * 全局变量定义时不能在后面赋值
    * 全局变量不能做为函数的传递参数，即一个变量不能即做参数也做全局变量
    
    

**如下所示的定义是正确的**::

    function Saylang(lang):
        global love_lang  # 定义全局变量love_lang
        
**如下所示的定义是错误的**::

    function Saylang(lang):
        global love_lang='python'
    
**如下所示的定义也是错误的**::

    function Saylang(love_lang):
        global love_lang

**下面是一个全局变量的示例**::

    def saylang(lang):
        global love_lang
        love_lang = "Python"
        print('I think you will more love to learn',love_lang)
    love_lang = 'Java'
    print('Before running the function,you love to learn',love_lang)
    saylang(love_lang)
    print('After running the function,you love to learn',love_lang)

    # PyCharm中运行结果如下:
    # Before running the function,you love to learn Java
    # I think you will more love to learn Python
    # After running the function,you love to learn Python

**再看另外一个例子**::

    def earnMoney():
        global Money
        Money = Money + 2000
        print('You did good job. You earned more money! now you have $%s' % Money)
    Money = 2000
    print('You have $%s' % Money,'at first.',end='\n\n')
    # print('You have ${} at first.\n'.format(Money))
    earnMoney()
    earnMoney()
    earnMoney()

    # PyCharm中运行结果如下：
    # You have $2000 at first.

    # You did good job. You earned more money! now you have $4000
    # You did good job. You earned more money! now you have $6000
    # You did good job. You earned more money! now you have $8000

    # 调用了三次earnMoney()，每次都会增加$2000，最后就变成$8000了。
    

位置参数
-----------------------

- 位置参数是指调用函数时根据函数定义的参数位置来传递参数，此时调用函数时，参数个数必须与函数定义的个数相同，否则会报错。

参见如下示例::

    def printLoveLang(name,lang):
        print('Hi,{},You love the language {}'.format(name,lang))

    printLoveLang('mei','Python')
    printLoveLang('mei')

    # PyCharm中运行结果如下：
    # Traceback (most recent call last):
    # Hi,mei,You love the language Python
    #   File "D:/data/python_scripts/test.py", line 5, in <module>
    #     printLoveLang('mei')
    # TypeError: printLoveLang() missing 1 required positional argument: 'lang'
    # 
    # 进程已结束,退出代码1
    
    
**注：示例中函数printLoveLang定义了两个参数name和lang，下面调用时printLoveLang('mei','Python')指定了两个参数，'mei'传递给参数name，'Python'传递给参数lang，可以正常打印出结果。而printLoveLang('mei')却只传递了一个参数，提示缺少一个位置参数'lang'。**

关键字参数
-----------------------

- 如果函数中有许多形式参数时，而仅想指定其中一部分时，可以通过命名来为这些参数赋值，这被称为关键参数，即使用名字(关键字)来给函数指定实参。
- 这样做有以下优点：不用担心参数的顺序；假设其他参数都有默认值，我们只用给我们关心的参数赋值。
- 函数调用时，位置参数必须在关键参数前面定义，否则会报“positional argument follows keyword argument”错误。

参见如下示例::

    def printLoveLang(name,lang,year=3):
        print('Hi,',name,'. You love the language',lang,'. You have learnt it',year,'years!')

    printLoveLang('mei','Python',2)                 # 按位置参数进行依次传值
    printLoveLang('mei','Python')                   # 按位置参数进行依次传值，未传值给year,year取默认值3
    printLoveLang(name='mei',lang='Python',year=4)  # 按关键参数进行依次传值
    printLoveLang('mei','Python',year=5)            # 按位置参数+关键参数的形式进行依次传值，位置参数必须在关键参数前面
    printLoveLang('mei',lang='Python',year=6)       # 按位置参数+关键参数的形式进行依次传值，位置参数必须在关键参数前面
    # printLoveLang(name='mei','Python',year=7)     # 此种方式是错误的，会报“positional argument follows keyword argument”错误
    printLoveLang(year=7,name='mei',lang='Python')  # 按关键参数进行依次传值,不需要按照位置参数的顺序给关键字参数传值

    # 在PyCharm中运行结果：
    # Hi, mei . You love the language Python . You have learnt it 2 years!
    # Hi, mei . You love the language Python . You have learnt it 3 years!
    # Hi, mei . You love the language Python . You have learnt it 4 years!
    # Hi, mei . You love the language Python . You have learnt it 5 years!
    # Hi, mei . You love the language Python . You have learnt it 6 years!
    # Hi, mei . You love the language Python . You have learnt it 7 years!

    # printLoveLang(name='mei','Python',year=7)       # 此种方式是错误的，位置参数必须定义在关键参数前面
    # 错误信息如下:
    #     printLoveLang(name='mei','Python',year=7)       # 此种方式是错误的，位置参数必须定义在关键参数前面。
    #                             ^
    # SyntaxError: positional argument follows keyword argument
    # 
    # 进程已结束,退出代码1

默认参数值
-----------------------

- 对于某些函数，如果不想为参数提供值的时候，函数可以自动以默认值作为参数的值。
- 声明参数时，默认参数必须放置在位置参数列表的后面，不能先声明有默认值的参数(可以理解为关键字参数)，再声明无默认值的参数(可以理解为位置参数)
- 必须先声明无默认值的参数，再声明有默认值的参数。

默认值的定义方式为parameter=default_value，参见如下示例::

    # 定义printMessage函数
    def printMessage(message,times=10):
        print(message * times)

    print('打印20个*')
    printMessage('*',20)   	# 此处给printMessage()函数正常传递两个参数
    print('打印10个#')
    printMessage('#')		# 此处给printMessage()函数仅传递了一个参数，此时函数会将取times的默认值10，进行计算。

    # 在PyCharm中运行结果：
    # D:\ProgramFiles\Python3.6.2\python.exe D:/data/python_project/python_basic/basic_learning.py
    # 打印20个*
    # ********************
    # 打印10个#
    # ##########
    
可变参数
--------------------------

- 可变参数也就是在函数中接收元组(tuple)和字典(dict)。
- 普通函数中的用法：def \_\_functionName\_\_(\*args, \*\*kwargs):
- 类函数中的用法：def \_\_functionName\_\_(self, \*args, \*\*kwargs):
- 当参数的个数不确定时，可以使用*args或**kwargs来接收参数组成的元组或字典
- 元组存储在args中，字典存储在kwargs中
- \*args是可变的positional arguments列表组成的元组
- \*\*kwargs是可变的keyword arguments列表组成的字典
- \*args必须位于\*\*kwargs之前，位置参数必须位于关键字参数前
- 参数顺序：位置参数、默认参数、\*args、\**\kwargs
- \*或\*\*后面的关键字名称随意，不必非要使用args或kwargs，如\*Name,\*\*Lang等都可以

参见如下示例::

    def printLoveLang(*args, **kwargs):
        print('args:', args, 'type(args):', type(args))
        for value in args:
            print("positional argument:", value)
        print('kwargs:', kwargs, 'type(kwargs):', type(kwargs))
        for key in kwargs:
            print("keyword argument:\t{}:{}".format(key, kwargs[key]))


    printLoveLang(1, 2, 3, name='mei', lang='Python')

    # 运行结果如下：
    # args: (1, 2, 3) type(args): < class 'tuple'>
    # positional argument: 1
    # positional argument: 2
    # positional argument: 3
    # kwargs: {'name': 'mei', 'lang': 'Python'} type(kwargs): < class 'dict'>
    # keyword argument: name:mei
    # keyword argument: lang:Python

解包裹(unpack)参数
--------------------------


- \*args和\*\*kwargs语法不仅可以在函数定义中使用，同样可以在函数调用的时候使用。
- 不同的是，如果说在函数定义的位置使用*args和**kwargs是一个将参数pack(包裹)的过程，
- 那么在函数调用的时候就是一个将参数unpack(解包裹)的过程了。
- 解包裹时，dict中定义的key值必须与函数中定义的参数值相同、且参数个数相同，key的顺序不必保持与函数定义时的一致。

下面使用一个例子来加深理解::

    def test_args(first, second, third, fourth, fifth):
        print('First argument: ', first)
        print('Second argument: ', second)
        print('Third argument: ', third)
        print('Fourth argument: ', fourth)
        print('Fifth argument: ', fifth)


    # Use *args
    args = [1, 2, 3, 4, 5]
    print('Use *args')
    test_args(*args)
    # results:
    # Use *args
    # First argument:  1
    # Second argument:  2
    # Third argument:  3
    # Fourth argument:  4
    # Fifth argument:  5

    # Use **kwargs
    kwargs = {
        'first': 1,
        'second': 2,
        'third': 3,
        'fourth': 4,
        'fifth': 5
    }
    print('Use **kwargs')
    test_args(**kwargs)
    # results:
    # Use **kwargs
    # First argument:  1
    # Second argument:  2
    # Third argument:  3
    # Fourth argument:  4
    # Fifth argument:  5

文档字符串DocStrings
-----------------------------

- 文档字符串DocStrings使用三引号包裹起来
- 文档字符串DocStrings的惯例是一个多行字符串，有以下规范::

    首行以大写字母开头，句号结尾
    第二行空行
    从第三行开始是详细的描述

- 可以使用__doc__ 调用函数的文档字符串。

如下所示::

    def printLoveLang(name, lang, year=3):
        """
        打印你学习编辑语言的年限.

        :param name: define the name
        :param lang: define the program language
        :param year: define the time you have learned the language
        :return: None
        """
        print('Hi,', name, '. You love the language', lang, '. You have learn it', year, 'years!')


    print(printLoveLang.__doc__)

    # 在PyCharm中运行结果：
    # 
    # 打印你学习编辑语言的年限.

    # :param name: define the name
    # :param lang: define the program language
    # :param year: define the time you have learned the language
    # :return: None

return语句
---------------------------

- return语句用来从一个函数返回，即跳出函数。return语句也可以返回一个值。
- 没有返回值的return语句等价于 *return None* 。
- None是python中表示没有任何东西的特殊类型。
- 如果函数结尾未提供return语句，python会给函数结尾暗含一个return None语句。

参见如下示例::

    # 指定return返回值
    def printlovelang(name, lang, year=3):
        print('Hi,', name, '. You love the language', lang, '. You have learn it', year, 'years!')
        return 'nice'


    result = printlovelang('mei', 'Python', 2)                 # 按位置参数进行依次传值
    print("return is:{}".format(result))
    
    # 运行结果如下：
    # Hi, mei . You love the language Python . You have learn it 2 years!
    # return is:nice
    
    # 不指定return返回值
    def printlovelang(name, lang, year=3):
        print('Hi,', name, '. You love the language', lang, '. You have learn it', year, 'years!')

    result = printlovelang('mei', 'Python', 2)                 # 按位置参数进行依次传值
    print("return is:{}".format(result))
    
    # 运行结果如下：
    # Hi, mei . You love the language Python . You have learn it 2 years!
    # return is:None

Python中的None
---------------------------

如果函数没有定义return返回值，则默认返回None。

- None是Python中一个特殊的值，不表示任何数据。
- None作为布尔值时与False是一样的，但其与False有很多差别。
- 0值的整型/浮点型、空符符串('')、空列表([])、空元组(())、空字典({})、空集合(set())都等价于False，但不等于None。

详细看以下示例::

    >>> def isNone(thing):
    ...     if thing is None:
    ...        print("It's None")
    ...     elif thing:
    ...        print("It's True")
    ...     else:
    ...        print("It's False")
    ...
    >>> isNone(None)
    It's None
    >>> isNone(True)
    It's True
    >>> isNone(False)
    It's False
    >>> isNone(1)
    It's True
    >>> isNone(0)
    It's False
    >>> isNone(-1)
    It's True
    >>> isNone('')
    It's False
    >>> isNone('string')
    It's True
    >>> isNone([])
    It's False
    >>> isNone(['list'])
    It's True
    >>> isNone({})
    It's False
    >>> isNone({'key':'value'})
    It's True
    >>> isNone((),)
    It's False
    >>> type((),)
    <class 'tuple'>
    >>> isNone(('tuple'))
    It's True
    >>> empty_set=set()
    >>> type(empty_set)
    <class 'set'>
    >>> isNone(empty_set)
    It's False
    >>> isNone(set('One'))
    It's True

参考文献:

【1】python的位置参数、默认参数、关键字参数、可变参数区别 https://www.cnblogs.com/bingabcd/p/6671368.html