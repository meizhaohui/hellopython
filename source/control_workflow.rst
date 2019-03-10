.. _control_workflow:

Python的控制流
======================

.. contents:: 目录

python中控制流语句包括if/for/while三种控制流语句。

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
    
    
    示例::

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
