.. _built-in_data_structure:

内建数据结构-列表，元组，字典
=================================

.. contents:: 目录

python内建数据结构介绍
-------------------------

python内建数据结构包括 **列表(list)** 、**元组(tuple)** 和 **字典(dict)** 。

- 列表(list)由方括号[]包括起来，如::

    list1=['a','b'],
    list1=[{'name':'a','value':2},{'name':'d','value':1},{'name':'c','value':3},{'name':'b','value':4}]

- 列表是可变的( mutable ),不能作为字典的key。
- 列表是是同构数据序列( lists are homogeneous sequences )。

- 元组(tuple)由圆括号()包括起来，如::
    
    tp1=(1,2) #表示坐标轴上的点x=1,y=2
    
- 元组是不可变的( immutable ),可以作为字典的key值;
- 元组是异构数据结构--即它们的条目具有不同的含义( Tuples are heterogeneous data structures  i.e., their entries have different meanings )。

- 字典(dict)由大括号{}包括起来，如::

    >>> dict1={'name':'Mei','lang':'python'}
    >>> type(dict1)
    <class 'dict'>
- 字典由键(key)值(value)对组成，键(key)是唯一的，且不可变的；
- 键(key)和值(value)中间由冒号:连接；
- 两个键值对之间由逗号,分割；
- 字典中键值对是无序的。


列表list的使用
---------------------

列表list用于处理一组有序项目的数据结构，列表中的项目包括在方括号[]中。

常用方法及示例如下::

    list()                  # 创建空列表
                            # 如list1=list(),则list1=[]
    list.append(obj)        # 在列表list结尾新增一个对象
                            # 如list1=['a','b'],list2=['c','d']
                            # 则执行list1.append(list2)后，list1=['a', 'b', ['c', 'd']]
    list.extend(iterable)   # 通过添加元素的迭代器扩展列表
                            # 如list1=['a','b'],list2=['c','d']
                            # 则执行list1.extend(list2)后，list1=['a', 'b', 'c', 'd']
    list.clear()            # 将list列表清空，即list变成一个空列表
                            # 如list1=['a','b'],则执行list1.clear()后，list1=[]
    list.copy()             # 将list列表复制一份，浅拷贝
                            # 如list1=['a','b'],L=list1.copy(),则L=['a','b']
    list.count(value)       # 返回value在列表list中出现的次数
                            # >>> list1=['a','b','a']
                            # >>> list1.count('a')
                            # 2
                            # >>> list1.count('b')
                            # 1

    list.index(value, [start, [stop]])      # 返回value在列表list中第1次出现的索引号。
                            # 如果指定start,stop的话，则从start索引处开始查找，到stop索引处结尾(不包括stop索引处)。
                            # 如list1=['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'e']
                            #   list1.index('a')=0,list1.index('b')=1,list1.index('c')=2,list1.index('d')=3
                            #   list1.index('e')=8
                            #   list1.index('a',0,5)=0,list1.index('a',1,5)=4,
                            #   list1.index('a',2,5)=4,list1.index('a',3,5)=4,
                            #   list1.index('a',4,5)=4,
                            #   list1.index('b',5,6)=5
    list.insert(index, object)              # 在指定索引值index前插入一个对象object
                            # 如list1=['a','b'],list2=['c','d'],则执行list1.insert(1,list2)后，list1=['a',['c', 'd'],'b']
                            # 如list1=['a','b','d'],则执行list1.insert(2,'c')后，list1=['a','b','c','d']
    list.pop([index])       # 移除索引号为index的元素，如果不指定index，则默认移除最后一个元素。并返回移除元素的值。
                            # 如list1=['a','b','c','d']，执行list1.pop()后，list1=['a','b','c']
                            # 再执行list1.pop(1)后，list1=['a','c']
                            # 再执行list1.pop(0)后，list1=['c']
                            # 再执行list1.pop(-1)后，list1=[]
    list.remove(value)      # 移除list列表中第一次出现的指定元素value。 如:
                            #       >>> list1=['a','b','a','c','b','d']
                            #       >>> list1.remove('a')
                            #       >>> list1
                            #       ['b', 'a', 'c', 'b', 'd']
                            #       >>> list1.remove('b')
                            #       >>> list1
                            #       ['a', 'c', 'b', 'd']
    list.reverse()          # 将列表前后反转，如：
                            #       >>> list1
                            #       ['a', 'c', 'b', 'd']
                            #       >>> list1.reverse()
                            #       >>> list1
                            #       ['d', 'b', 'c', 'a']
    list.sort(key=None, reverse=False)  # 对list列表进行排序，可设定排序的关键字key，或指定是否需要反转reverse。
                # reverse=False 表示不需要反转，即升序排序；
                # reverse=True  表示需要反转，即降序排序。如:
                #       >>> list1=['d','b','c','a','e']
                #       >>> list1
                #       ['d', 'b', 'c', 'a', 'e']
                #       >>> list1.sort()                    # 不带参数进行排序
                #       >>> list1
                #       ['a', 'b', 'c', 'd', 'e']
                #       >>> list1=['d','b','c','a','e']
                #       >>> list1.sort(reverse=False)        # 带参数进行升序排序
                #       >>> list1
                #       ['a', 'b', 'c', 'd', 'e']
                #       >>> list1=['d','b','c','a','e']        # 带参数进行降序排序
                #       >>> list1.sort(reverse=True)
                #       >>> list1
                #       ['e', 'd', 'c', 'b', 'a']
                # 通过关键字key进行排序
                >>> list1=[{'name':'a','value':2},{'name':'d','value':1},{'name':'c','value':3},{'name':'b','value':4}]
                >>> list1
                [{'name': 'a', 'value': 2}, {'name': 'd', 'value': 1}, {'name': 'c', 'value': 3}, {'name': 'b', 'value': 4}]
                # 对第一个关键字name进行升序排序
                >>> list1.sort(key=lambda obj:obj.get('name'),reverse=False)
                >>> list1
                [{'name': 'a', 'value': 2}, {'name': 'b', 'value': 4}, {'name': 'c', 'value': 3}, {'name': 'd', 'value': 1}]
                # 对第二个关键字value进行升序排序
                >>> list1.sort(key=lambda obj:obj.get('value'),reverse=False)
                >>> list1
                [{'name': 'd', 'value': 1}, {'name': 'a', 'value': 2}, {'name': 'c', 'value': 3}, {'name': 'b', 'value': 4}]
                >>> list1.sort(key=operator.itemgetter(1),reverse=False)
                # 通过operator.itemgetter('name')获取name所在的维度，再进度升序排序
                >>> list1.sort(key=operator.itemgetter('name'))
                >>> list1
                [{'name': 'a', 'value': 2}, {'name': 'b', 'value': 4}, {'name': 'c', 'value': 3}, {'name': 'd', 'value': 1}]
                # 通过operator.itemgetter('name')获取name所在的维度，再进度降序排序
                >>> list1.sort(key=operator.itemgetter('name'),reverse=True)
                >>> list1
                [{'name': 'd', 'value': 1}, {'name': 'c', 'value': 3}, {'name': 'b', 'value': 4}, {'name': 'a', 'value': 2}]
                # 通过operator.itemgetter('value')获取value所在的维度，再进度升序排序
                >>> list1.sort(key=operator.itemgetter('value'))
                >>> list1
                [{'name': 'd', 'value': 1}, {'name': 'a', 'value': 2}, {'name': 'c', 'value': 3}, {'name': 'b', 'value': 4}]
                # 通过operator.itemgetter('value')获取value所在的维度，再进度降序排序
                >>> list1.sort(key=operator.itemgetter('value'),reverse=True)
                >>> list1
                [{'name': 'b', 'value': 4}, {'name': 'c', 'value': 3}, {'name': 'a', 'value': 2}, {'name': 'd', 'value': 1}]
    list.__len__()          # 返回list列表的长度
                            # 如：list1=['a','b']，则list1.__len__() = 2
    list.__add__(list1)     # 将两个list拼接在一起
                            # 如: list1=['a','b']，list2=['c','d']，则list1.__add__(list2)=['a', 'b', 'c', 'd']
                            # list1不变，list1=['a','b']
    list.__contains__(value)    # list列表中是否包含value值
                            # >>> list1.__contains__('c')
                            # False
                            # >>> list1.__contains__('a')
                            # True
    list.__delitem__(index) # 删除索引index处的元素，与list.pop(index)作用相同
                >>> list1=[{'name':'a','value':2},{'name':'d','value':1},{'name':'c','value':3},{'name':'b','value':4}]
                >>> list1.__delitem__(1)
                >>> list1
                [{'name': 'a', 'value': 2}, {'name': 'c', 'value': 3}, {'name': 'b', 'value': 4}]
    list.__getitem__(index) 获取索引号index对应的元素值
                            >>> list1.__getitem__(1)
                            {'name': 'c', 'value': 3}    
    list.__imul__(int_value) 将列表list重复int_value次，如果int_value=0，则清空列表
                            如：
                            >>> list1=['a','b']
                            >>> list1.__imul__(2)
                            ['a', 'b', 'a', 'b']
                            >>> list1
                            ['a', 'b', 'a', 'b']
                            >>> list1.__imul__(0)
                            []
                            >>> list1
                            []
    获取特殊的list列表:
        >>> squares = list(map(lambda x: x**2, range(10)))    
        >>> squares
        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        >>> a=[1,2,3,4]
        >>> b=[i**2 for i in a ]
        >>> b
        [1, 4, 9, 16]

    使用list()将其他数据类型转换成列表
    >>> list('cat')
    ['c', 'a', 't']
    >>> list(('ab','cd','ef'))
    ['ab', 'cd', 'ef']
    >>> 


元组(tuple)的使用
---------------------

元姐通过圆括号()中的逗号将元素分割开。如my_location = (42, 11)  # page number, line number


常用方法及示例如下::

    tuple.count(value)      返回value值在元组tuple中出现的次数
                            如：
                            >>> tu1=(1,2,3,4,5,1,2,1,2,3)
                            >>> tu1
                            (1, 2, 3, 4, 5, 1, 2, 1, 2, 3)
                            >>> tu1.count(1)
                            3
                            >>> tu1.count(2)
                            3
                            >>> tu1.count(3)
                            2
                            >>> tu1.count(4)
                            1
                            >>> tu1.count(5)
                            1
                            >>> tu1.count(0)
                            0
    tuple.index(value,[start, [stop]]) 返回value在tuple元素中第一次出现的索引号。
                            >>> tu1.index(1,0,8)
                            0
                            >>> tu1.index(1,1,8)
                            5
                            >>> tu1.index(1,5,8)
                            5
                            >>> tu1.index(1,6,8)
                            7
                            >>> tu1.index(3)
                            2
    tuple.__add__(other_tuple)    将一个元组与另外一个元组组合起来，tuple,other_tuple保持不变
                            >>> tu1
                            (1, 2, 3)
                            >>> tu1.__add__(tu1)
                            (1, 2, 3, 1, 2, 3)
                            >>> tu1
                            (1, 2, 3)
                            >>> tu2=(4,5)
                            >>> tu2
                            (4, 5)
                            >>> tu1.__add__(tu2)
                            (1, 2, 3, 4, 5)
                            >>> tu1
                            (1, 2, 3)
                            >>> tu2
                            (4, 5)
    tuple.__contains__(value)    元组tuple中是否包含值为value的元素，返回True或False
                            >>> tu1=('a','b','c')
                            >>> tu1.__contains__('a')
                            True
                            >>> tu1.__contains__('b')
                            True
                            >>> tu1.__contains__('c')
                            True
                            >>> tu1.__contains__('d')
                            False
    tuple.__eq__(other_tuple)    元组tuple与元组other_tuple是否相等，返回True或False
                            >>> tu1
                            ('a', 'b', 'c')
                            >>> tu2
                            ('a', 'b', 'c')
                            >>> tu3
                            (1, 2, 3, 4)
                            >>> tu1.__eq__(tu2)
                            True
                            >>> tu1.__eq__(tu3)
                            False
    tuple.__getitem__(index)    获取元组tuple中索引号为index的元素
                            >>> tu1
                            ('a', 'b', 'c')
                            >>> tu1.__getitem__(0)
                            'a'
                            >>> tu1.__getitem__(1)
                            'b'
                            >>> tu1.__getitem__(2)
                            'c'
                            >>> tu1.__getitem__(3)
                            Traceback (most recent call last):
                              File "<stdin>", line 1, in <module>
                            IndexError: tuple index out of range                
    tuple.__len__()         返回元组tuple的长度
                            >>> tu1
                            ('a', 'b', 'c')
                            >>> tu1.__len__()
                            3
                            >>> tu2
                            ('a', 'b', 'c')
                            >>> tu2.__len__()
                            3
                            >>> tu3
                            (1, 2, 3, 4)
                            >>> tu3.__len__()
                            4
    tuple.__mul__(n)        重复元组tuple n次
                            >>> tu1
                            ('a', 'b', 'c')
                            >>> tu1.__mul__(2)
                            ('a', 'b', 'c', 'a', 'b', 'c')
                            >>> tu1.__mul__(3)
                            ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')
                            >>> tu1
                            ('a', 'b', 'c')    
    单元素的元组tuple       如果元组tuple中仅包含一个元素，则需要在元素后面跟一个逗号,
                            >>> tu1=(1,)
                            >>> tu1
                            (1,)
                            >>> type(tu1)
                            <class 'tuple'>
                            >>> tu2=(1)
                            >>> tu2
                            1
                            >>> type(tu2)
                            <class 'int'>
    元组tuple的打印输出     通过%s和%来定制输出语句中的变量
                            如果有多个参数需要输出时，使用下面这种组合成元组的方式更加方便。
                            >>> name='mei'
                            >>> lang='python'
                            >>> print('hi,%s,you love to learn the language %s' % (name,lang))
                            hi,mei,you love to learn the language python

                            
字典(dict)的使用
---------------------

- 字典(dict)由大括号{}包括起来，如: dict1={'name':'Mei','lang':'python'}。
- 字典与列表类似，但其中元素的顺序无关紧要，因为它们不能通过像0或1的偏移量访问。每个元素拥有与之对应的互不相同的键(key),需要通过键来访问元素。
- 键通常是字符串，但它还可以是Python中其他任意的不可变类型：布尔型，整型，浮点型，元组等。



常用方法及示例如下::    

    dict.get(key)           获取字典dict中键为key的值value
                            >>> dict1
                            {'name': 'Mei', 'lang': 'python'}
                            >>> dict1.get('name')
                            'Mei'
                            >>> dict1.get('lang')
                            'python'
                            
    dict.items()            返回字典dict的(key,value)元组对的列表的对象，可供用户去迭代访问所有的key和value
                            >>> dict1.items()
                            dict_items([('name', 'Mei'), ('lang', 'python')])
                            >>> for x,y in dict1.items():
                            ...     print('key is',x,',value is',y)
                            ...
                            key is name ,value is Mei
                            key is lang ,value is python
                            
    dict.keys()             返回字典dict的key组成的列表的对象，可供用户去迭代访问所有的key
                            >>> dict1.keys()
                            dict_keys(['name', 'lang'])
                            >>> for x in dict1.keys():
                            ...     print('key is',x)
                            ...
                            key is name
                            key is lang
                            
    dict.values()           返回字典dict的键值value组成的列表的对象，可供用户去迭代访问所有的value
                            >>> dict1={'name':'Mei','lang':'python'}
                            >>> dict1.values()
                            dict_values(['Mei', 'python'])
                            
    dict.pop(key[,returnValue]) 移除字典dict中键为key的键值对，并返回键key所对应的value的值
                                如果设置了returnValue的话，则当查找不到键key时，才返回returnValue值                    
                                >>> dict1={'a':3,'b':1,'c':2}
                                >>> dict1
                                {'a': 3, 'b': 1, 'c': 2}
                                >>> dict1.pop('a')
                                3
                                >>> dict1
                                {'b': 1, 'c': 2}
                                >>> dict1.pop('b')
                                1
                                >>> dict1
                                {'c': 2}
                                >>> dict1.pop('b','b is not the key')
                                'b is not the key'
                                >>> dict1
                                {'c': 2}
                                >>> dict1.pop('c','c is not the key')
                                2    
                                >>> dict1
                                {}    
                                
    dict.popitem()              移除字典dict中最后一个键值对，并返回被移除的键值对的值；
                                当dict字典为空时，使用popitem()方法会报错
                                >>> dict1={'a':3,'b':1,'c':2,'d':5,'e':4}
                                >>> dict1
                                {'a': 3, 'b': 1, 'c': 2, 'd': 5, 'e': 4}
                                >>> dict1.popitem()
                                ('e', 4)
                                >>> dict1
                                {'a': 3, 'b': 1, 'c': 2, 'd': 5}
                                >>> dict1.popitem()
                                ('d', 5)
                                >>> dict1
                                {'a': 3, 'b': 1, 'c': 2}
                                >>> dict1.popitem()
                                ('c', 2)
                                >>> dict1
                                {'a': 3, 'b': 1}
                                >>> dict1.popitem()
                                ('b', 1)
                                >>> dict1
                                {'a': 3}
                                >>> dict1.popitem()
                                ('a', 3)
                                >>> dict1
                                {}
                                >>> dict1.popitem()
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                KeyError: 'popitem(): dictionary is empty'
                                
    dict.setdefault(key[,set_value])    获取dict字典键key对应的value字
                                当key不存在时，若未指定set_value，则添加键值对key:None
                                当key不存在时，若指定set_value，则添加键值对key:set_value，并返回set_value
                                >>> dict1={'a':1,'b':2}
                                >>> dict1
                                {'a': 1, 'b': 2}
                                >>> dict1.setdefault('a')
                                1
                                >>> dict1.setdefault('a',3)
                                1
                                >>> dict1
                                {'a': 1, 'b': 2}
                                >>> dict1.setdefault('c')
                                >>> dict1
                                {'a': 1, 'b': 2, 'c': None}
                                >>> dict1.setdefault('c')
                                >>> dict1
                                {'a': 1, 'b': 2, 'c': None}
                                >>> dict1.setdefault('d','add_by_sedefault')
                                'add_by_sedefault'
                                >>> dict1
                                {'a': 1, 'b': 2, 'c': None, 'd': 'add_by_sedefault'}
                                >>> dict1.setdefault('b','b is not the key')
                                2
                                >>> dict1
                                {'a': 1, 'b': 2, 'c': None, 'd': 'add_by_sedefault'}
                                
    dict1.update(dict2)         按dict2更新dict1
                                如果dict2中的key值在dict1中存在，则将dict2中key对应的值赋值给dict1[key]，即dict1[key]=dict2[key];
                                如果dict2中的key值在dict1中不存在，dict2[key]=value,则将dict2中key对应的键值对添加到字典dict1中，即dict1[key]=dict2[key];
                                >>> dict1={'a':1,'b':4,'c':2,'d':3,'f':5}
                                >>> dict1
                                {'a': 1, 'b': 4, 'c': 2, 'd': 3, 'f': 5}
                                >>> dict2={'a':5,'f':1}
                                >>> dict2
                                {'a': 5, 'f': 1}
                                >>> dict3={'d':2}
                                >>> dict3
                                {'d': 2}
                                >>> dict4={'b':'four','c':3}
                                >>> dict4
                                {'b': 'four', 'c': 3}
                                >>> dict1.update(dict2)
                                >>> dict1
                                {'a': 5, 'b': 4, 'c': 2, 'd': 3, 'f': 1}
                                >>> dict1.update(dict3)
                                >>> dict1
                                {'a': 5, 'b': 4, 'c': 2, 'd': 2, 'f': 1}
                                >>> dict1.update(dict3)
                                >>> dict1
                                {'a': 5, 'b': 4, 'c': 2, 'd': 2, 'f': 1}
                                >>> dict1.update(dict4)
                                >>> dict1
                                {'a': 5, 'b': 'four', 'c': 3, 'd': 2, 'f': 1}
                                >>> dict5={'g':6,'h':7}
                                >>> dict5
                                {'g': 6, 'h': 7}
                                >>> dict1.update(dict5)
                                >>> dict1
                                {'a': 5, 'b': 'four', 'c': 3, 'd': 2, 'f': 1, 'g': 6, 'h': 7}
                                >>> dict6={'b':4,'i':8}
                                >>> dict6
                                {'b': 4, 'i': 8}
                                >>> dict1
                                {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'f': 1, 'g': 6, 'h': 7, 'i': 8}
                                >>> dict1.update({'j':9})
                                >>> dict1
                                {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'f': 1, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
                                
    dict.fromkeys(iterable, value=None) 生成一个新的字典
                                可迭代对象iterable可以是字符串、元组、列表或字典，用于创建字典的键key；
                                字典所有键key对应的同一值的初始值为value，用户不输入value值时，默认以None。
                                >>> dict1={'a':1,'b':2,'c':3}
                                >>> dict1
                                {'a': 1, 'b': 2, 'c': 3}
                                >>> dict1.fromkeys('123')
                                {'1': None, '2': None, '3': None}
                                >>> dict1.fromkeys('123','string字符串')
                                {'1': 'string字符串', '2': 'string字符串', '3': 'string字符串'}
                                >>> dict1.fromkeys((1,2,3),'string字符串')
                                {1: 'string字符串', 2: 'string字符串', 3: 'string字符串'}
                                >>> dict1.fromkeys((1,2,3),'tuple元组')
                                {1: 'tuple元组', 2: 'tuple元组', 3: 'tuple元组'}
                                >>> dict1.fromkeys(('1','2','3'),'tuple元组')
                                {'1': 'tuple元组', '2': 'tuple元组', '3': 'tuple元组'}
                                >>> dict1.fromkeys(['1','2','3'],'list列表')
                                {'1': 'list列表', '2': 'list列表', '3': 'list列表'}
                                >>> dict1.fromkeys([1,2,3],'list列表')
                                {1: 'list列表', 2: 'list列表', 3: 'list列表'}
                                >>> dict1.fromkeys({1:'a',2:'b',3:'c'},'dict字典')
                                {1: 'dict字典', 2: 'dict字典', 3: 'dict字典'}
                                >>> dict1.fromkeys({'1':'a','2':'b','3':'c'},'dict字典')
                                {'1': 'dict字典', '2': 'dict字典', '3': 'dict字典'}    
                                
    dict.copy()                 字典的浅拷贝，等同于copy模块中的copy()方法，进行浅拷贝
                                字典浅拷贝：深拷贝父对象(一级目录)，子对象(二级目录)不拷贝，还是进行引用
                                copy模块中的deepcopy()方法为深拷贝，父对象和子对象同时会被拷贝。
                                >>> dict1={'a':1,'b':(1,2),'c':[3,['a','b'],5]}
                                >>> dict2=dict1                                        # 浅拷贝，仅引用对象
                                >>> dict3=dict1.copy()                                # 字典浅拷贝
                                >>> dict4=copy.copy(dict1)                            # copy模块浅拷贝
                                >>> dict5=copy.deepcopy(dict1)                        # copy模块深拷贝
                                >>> dict1
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a', 'b'], 5]}
                                >>> dict2
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a', 'b'], 5]}
                                >>> dict4
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a', 'b'], 5]}
                                >>> dict3
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a', 'b'], 5]}
                                >>> dict5
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a', 'b'], 5]}
                                >>> dict1['c']
                                [3, ['a', 'b'], 5]
                                >>> dict1['c'][1]
                                ['a', 'b']
                                >>> dict1['c'][1].remove('b')
                                >>> dict1
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a'], 5]}
                                >>> dict2
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a'], 5]}
                                >>> dict3
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a'], 5]}
                                >>> dict4
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a'], 5]}
                                >>> dict5
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a', 'b'], 5]}

                                >>> dict1.pop('c')
                                [3, ['a'], 5]
                                >>> dict1
                                {'a': 1, 'b': (1, 2)}
                                >>> dict2
                                {'a': 1, 'b': (1, 2)}
                                >>> dict3
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a'], 5]}
                                >>> dict4
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a'], 5]}
                                >>> dict5
                                {'a': 1, 'b': (1, 2), 'c': [3, ['a', 'b'], 5]}    

                                >>> adict={'姓名':'zhang','性别':['男','女']}
                                >>> adict
                                {'姓名': 'zhang', '性别': ['男', '女']}
                                >>> bdict=adict
                                >>> cdict=adict.copy()
                                >>> import copy
                                >>> ddict=copy.copy(adict)
                                >>> edict=copy.deepcopy(adict)
                                >>> adict
                                {'姓名': 'zhang', '性别': ['男', '女']}
                                >>> bdict
                                {'姓名': 'zhang', '性别': ['男', '女']}
                                >>> cdict
                                {'姓名': 'zhang', '性别': ['男', '女']}
                                >>> ddict
                                {'姓名': 'zhang', '性别': ['男', '女']}
                                >>> edict
                                {'姓名': 'zhang', '性别': ['男', '女']}
                                >>> adict['性别']
                                ['男', '女']
                                >>> adict['性别'].remove('女')
                                >>> adict
                                {'姓名': 'zhang', '性别': ['男']}
                                >>> bdict
                                {'姓名': 'zhang', '性别': ['男']}
                                >>> cdict
                                {'姓名': 'zhang', '性别': ['男']}
                                >>> edict
                                {'姓名': 'zhang', '性别': ['男', '女']}    
                                
    dict.__setitem__(key,value) 给dict字典的key赋值value，或添加新的key:value键值对
                                >>> dict1={'a':1,'b':(1,2)}
                                >>> dict1
                                {'a': 1, 'b': (1, 2)}
                                >>> dict1.__setitem__('c',3)
                                >>> dict1
                                {'a': 1, 'b': (1, 2), 'c': 3}
                                >>> dict1.__setitem__('b',None)
                                >>> dict1
                                {'a': 1, 'b': None, 'c': 3}        
    dict.clear()                清空字典
                                >>> dict1={'a':1,'b':(1,2)}
                                >>> dict1
                                {'a': 1, 'b': (1, 2)}
                                >>> dict1.clear()
                                >>> dict1
                                {}   

    dict(other)                 使用dict()将其他类型的双值子系列转换成字典

                                # 包含双值列表的列表
                                >>> list1 = [['a',1],['b',2],['c',3]]
                                >>> list1
                                [['a', 1], ['b', 2], ['c', 3]]
                                >>> dict(list1)
                                {'a': 1, 'b': 2, 'c': 3}
                                >>> 

                                # 包含双值元组的列表
                                >>> list2 = [('a','b'),('c','d'),('e','f')]
                                >>> dict(list2)
                                {'a': 'b', 'c': 'd', 'e': 'f'}
                                >>> 

                                # 包含双值列表的元组
                                >>> tuple1 = （['a','b'],['c','d'],['e','f']）
                                >>> dict(tuple1)
                                {'a': 'b', 'c': 'd', 'e': 'f'}
                                >>> 

                                # 双字符的字符串组成的列表
                                >>> list1 = ['ab','cd','ef']
                                >>> dict(list1)
                                {'a': 'b', 'c': 'd', 'e': 'f'}
                                >>> 

                                # 双字符的字符串组成的元组
                                >>> tuple1 = ('ab','cd','ef')
                                >>> dict(tuple1)
                                {'a': 'b', 'c': 'd', 'e': 'f'}
                                >>> 

                    
                            
集合(set)的使用
-------------------------

集合(set)由大括号{}包括起来，如: set1={'name','lang'}。

集合就像舍弃了值，仅剩下键的字典一样。键与键之间不允许重复。

如果仅仅想知道某一个元素是否存在而不关心其他的，使用集合是个非常好的选择。

常用方法及示例如下::

    集合的创建：
    方式1：使用set()函数创建一个集合
    方式2：使用大括号将一系列以逗号隔开的值包裹起来。
    如：
    >>> set1=set()
    >>> set1
    set()
    >>> type(set1)
    <class 'set'>
    >>> set2={'Mon','Tue','Wed','Thu','Fri','Sat','Sun'}
    >>> set2
    {'Thu', 'Sun', 'Mon', 'Tue', 'Fri', 'Wed', 'Sat'}
    >>> set('string')
    {'i', 'n', 's', 'g', 't', 'r'}
    >>> set(['One','Two','Three'])
    {'Three', 'One', 'Two'}
    >>> set(('One','Two','Three'))
    {'Three', 'One', 'Two'}
    >>> set({'name':'mei','lang':'python'})
    {'lang', 'name'}
        
    集合运算：
    交集&或intersection(),同时出现在两个集合中的元素组成的集合。
    >>> set1= set(('One','Two','Three'))
    >>> set1
    {'Three', 'One', 'Two'}
    >>> set2= set(('Two','Three','Four'))
    >>> set2
    {'Four', 'Three', 'Two'}
    >>> set1 & set2
    {'Three', 'Two'}
    >>> set1.intersection(set2)
    {'Three', 'Two'}
    
    并集|或union(),至少出现在一个集合中的元素组成的集合。
    >>> set1 | set2
    {'Three', 'One', 'Two', 'Four'}
    >>> set2 | set1
    {'Four', 'Three', 'Two', 'One'}
    >>> set1.union(set2)
    {'Three', 'One', 'Two', 'Four'}
    >>> set2.union(set1)
    {'Four', 'Three', 'Two', 'One'}
    
    差集-或difference()，出现在第一个集合但不出现在第二个集合中的元素组成的集合。
    >>> set1 - set2
    {'One'}
    >>> set1.difference(set2)
    {'One'}
    >>> set2 - set1
    {'Four'}
    >>> set2.difference(set1)
    {'Four'}
    
    异或差^或symmetric_difference()，仅在两个集合中出现一次的元素组成的集合。
    >>> set1 ^ set2
    {'Four', 'One'}
    >>> set2 ^ set1
    {'Four', 'One'}
    >>> set1.symmetric_difference(set2)
    {'Four', 'One'}
    >>> set2.symmetric_difference(set1)
    {'Four', 'One'}
    
    使用<=或issubset()判断一个集合是否是另一个集合的子集，即第一个集合中所有元素出现在第二个集合中。
    >>> set1 <= set2
    False
    >>> set3={'One','Two','Three','Four','Five'}
    >>> set1 <= set3
    True
    >>> set2 <= set3
    True
    >>> set1.issubset(set3)
    True
    >>> set2.issubset(set3)
    True
    
    使用>=或issuperset()判断一个集合是否是另一个集合的超集，即第二个集合中所有元素出现在第一个集合中。
    >>> set1 >= set3
    False
    >>> set3 >= set1
    True
    >>> set3.issuperset(set1)
    True
    >>> set3.issuperset(set2)
    True
    >>> set3.issuperset(set3)
    True
    
    真子集，第一个集合中所有元素出现在第二个集合中，且第二个集合还有其他元素。
    >>> set1 < set3
    True
    
    真超集，第二个集合中所有元素出现在第一个集合中，且第一个集合还有其他元素。
    >>> set3 > set1
    True

推导式
----------------------

列表推导式::

    列表推导能非常简洁的构造一个新列表:只用一条简洁的表达式即可对得到的元素进行转换变形
    [ expression for item in iterable ]
    [ expression for item in iterable if condition ]
    >>> [x**2 for x in range(10)]
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    >>> [x**2 for x in range(10) if x%2==0]
    [0, 4, 16, 36, 64]

    >>> [(x,y) for x in range(5) if x%2==0 for y in range(5) if y %2==1]
    [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

    >>> list1=['x','y','z']
    >>> list2=[1,2,3]
    >>> list3=[ (i,j) for i in list1 for j in list2 ]
    >>> list3
    [('x', 1), ('x', 2), ('x', 3), ('y', 1), ('y', 2), ('y', 3), ('z', 1), ('z', 2), ('z', 3)]


    >>> [[1 if i == j else 0 for i in range(5)] for j in range(5)]
    [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]


列表解析式::

    >>> func1 = [lambda x:x*i for i in range(10)]
    >>> [f1(2) for f1 in func1]
    [18, 18, 18, 18, 18, 18, 18, 18, 18, 18]

匿名函数lambda::

    lambda的一般形式是关键字lambda后面跟一个或多个参数，紧跟一个冒号，以后是一个表达式。
    lambda是一个表达式而不是一个语句。
    lambda能够出现在Python语法不允许def出现的地方。
    作为表达式，lambda返回一个值（即一个新的函数）。
    lambda用来编写简单的函数，而def用来处理更强大的任务。
    lambda首要用途是指定短小的回调函数。
    >>> add=lambda x,y:x+y
    >>> add(1,2)
    >>> f=lambda x,y,z:x+pow(y,2)+pow(z,3)
    >>> f(1,2,3)
    32
    
条件表达式::

    lambda: a if some_condition() else b
    >>> f=lambda x: 'big' if x > 100 else 'small'
    >>> f(101)
    'big'
    >>> f(100)
    'small'
    >>> f(99)
    'small'

    >>> f1=lambda x:print(x)
    >>> f1(1)
    1
    >>> f1('str')
    str


生成器解析式::

    >>> func1 = (lambda x:x*i for i in range(10))
    >>> [f1(2) for f1 in func1]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    
对于生成器, 只有你需要的时候它才会求值, 这也是和列表解析式的区别, 列表解析式只要你运行, 马上就把i变为了9, 可是生成器不会, 当你调用第一个函数的时候, 他把相应的i求出来, 然后停止, 等你下一次调用。

集合推导式::

    {expression for expression in iterable if condition}
    >>> a_set={ num for num in range(10) if num % 2 == 1 }
    >>> a_set
    {1, 3, 5, 7, 9}
    
使用zip()并行迭代::

    可以使用zip()函数对多个序列进行并行迭代。
    >>> Eng=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    >>> Eng
    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    >>> Num=[1,2,3,4,5,6,7]
    >>> Num
    [1, 2, 3, 4, 5, 6, 7]
    >>> list(zip(Eng,Num))
    [('Mon', 1), ('Tue', 2), ('Wed', 3), ('Thu', 4), ('Fri', 5), ('Sat', 6), ('Sun', 7)]
    >>> dict(zip(Eng,Num))
    {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
    >>> type(zip(Eng,Num))
    <class 'zip'>
