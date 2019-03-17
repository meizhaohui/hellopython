.. _control_workflow:

Python的控制流
======================

.. contents:: 目录

python中控制流语句包括if/for/while三种控制流语句。

- 使用#标记注释，从#开始到当前行结束的部分都是注释。
- 一行程序的最大长度建议为80个字符。
- 如果代码太长，可以使用连接符\连接。
- 代码块缩进时使用4个空格缩进。
- 避免使用Tab与Space混合使用的缩进风格。

if语法
-------------------

- if语句::

    语法：
    if exp1:
        cmds
    [elif:]
        cmds
    [else:]
        cmds
    elif或else从句是可选的。

- 比较操作符::

    相等    ==
    不等于  !=
    小于    <
    大于    >
    不小于  >=
    不大于  <=
    属于   in

- 真值(True)与假值(False)，下列的情况会被认为是假值False，其他情况认为是True::
    
    布尔      False
    null类型  None
    整型      0
    浮点型     0.0
    空字符串    ''
    空元组     ()
    空列表     []
    空字典     {}
    空集合     set()

    


while语法
-------------------

- while语句::

    语法：
    while exp1:
        cmds
    [else:]
        cmds
    else从句是可选的。
    
for语法
-------------------

- for语句::

    语法:
    for <variable> in <sequence>:
        <statements>
    else:
        <statements>
    else从句是可选的。
    
    
    示例:

    >>> for i in range(10):
    ...     print(i)
    ...
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>> for i in 'abcdef':
    ...     print(i)
    ... else:
    ...     print("哈哈")
    a
    b
    c
    d
    e
    f
    哈哈

break语句和continue语句
----------------------------------
    
- break语句用来终止循环
- continue语句跳转当前循环块中剩余部分，然后继续下一轮循环。
    
示例::
    
    >>> while True:
    ...     str = input('please input a string:')
    ...     if str == 'good':
    ...         print('You guess right!')
    ...         break
    ...     else:
    ...         print('You guess wrong!')
    ...         continue
    ...
    please input a string:a
    You guess wrong!
    please input a string:b
    You guess wrong!
    please input a string:c
    You guess wrong!
    please input a string:perfect
    You guess wrong!
    please input a string:good
    You guess right!

使用zip()并行迭代
----------------------------------
 
- 在使用迭代时，可以通过zip()函数对多个序列进行并行迭代   
- 使用zip()函数可以遍历多个序列，在具有相同位移的项之间创建元组
- 使用zip()配合list()和dict()函数使用::
    
    In [1]: days=['Monday','Tuesday','Wednesday']

    In [2]: chinese=['星期一','星期二','星期三']

    In [3]: for day,china in zip(days,chinese):
       ...:     print(day,'\t',china)
       ...:     
    Monday 	 星期一
    Tuesday 	 星期二
    Wednesday 	 星期三

    In [4]: list(zip(days,chinese))
    Out[4]: [('Monday', '星期一'), ('Tuesday', '星期二'), ('Wednesday', '星期三')]

    In [5]: dict(zip(days,chinese))
    Out[5]: {'Monday': '星期一', 'Tuesday': '星期二', 'Wednesday': '星期三'}

使用range()生成自然数序列
----------------------------------
 
- range()函数返回在特定区间的自然数序列。
- range(start,stop,step)，start起始值默认为0,stop是最后一个值，step步长默认值是1。
- range中返回的自然数序列中包含最小值start，不包含最大值stop。

示例::

    In [1]: range(6)
    Out[1]: range(0, 6)

    In [2]: for i in range(6):
       ...:     print(i)
       ...:     
    0
    1
    2
    3
    4
    5

    In [3]: for i in range(10,20,2):
       ...:     print(i)
       ...:     
    10
    12
    14
    16
    18


