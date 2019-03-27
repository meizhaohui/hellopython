.. _collections_module:

常用内建模块Collections模块的使用
========================================

.. contents:: 目录

Collections模块介绍
-------------------------

前面介绍了python内建数据结构包括 **列表(list)** 、**元组(tuple)** 和 **字典(dict)** 。
collections模块在这些内置数据类型的基础上，提供了几个额外的数据类型：

- namedtuple: 生成可以使用名字来访问元素内容的tuple子类
- deque: 双端队列，可以快速的从另外一侧追加和推出对象
- Counter: 计数器，主要用来计数
- OrderedDict: 有序字典
- defaultdict: 带有默认值的字典

下面主要介绍双端队列deque、命名元组namedtuple、有序字典OrderedDict。


常用内建模块之双端队列deque
-----------------------------------

- collections模块中双端队列deque结构可以看作是内置list结构的加强版，且比队列提供更强大的方法。
- deque是double-ended queue的缩写，提供在两端插入和删除的操作。
- deque([iterable[, maxlen]]) --> deque object，maxlen为双端队列的最大长度

双端队列的使用方法如下::

    >>> from collections import deque
    >>> deque=deque((),5)
    >>> deque.
    deque.append(     deque.copy(       deque.extendleft( deque.maxlen      deque.remove(
    deque.appendleft( deque.count(      deque.index(      deque.pop(        deque.reverse(
    deque.clear(      deque.extend(     deque.insert(     deque.popleft(    deque.rotate(
    >>> deque
    deque([], maxlen=5)
    deque.append(item)    # 在队列右边(末尾)添加项目[Add an element to the right side of the deque.]
    deque.appendleft(item)    # 在队列左边(开始)添加项目[Add an element to the left side of the deque.]
    deque.clear()            # 清空队列，也就是删除deque中的所有项目[Remove all elements from the deque.]
    deque.extend(iterator)  # 在deque的右边(末尾)添加iterator中的所有项目[Extend the right side of the deque with elements from the iterable]
    deque.extendleft(iterator)    # 在deque的左边(开始)添加iterator中的所有项目[Extend the left side of the deque with elements from the iterable]
    deque.copy()            # 返回deque队列的一个浅拷贝[Return a shallow copy of a deque.]
    deque.count(item)        # 返回deque队列中元素item出现的次数[return number of occurrences of value]
    deque.index(value, [start, [stop]]) # 返回value在deque队列中的索引index[integer -- return first index of value.]
    deque.index(index, object)     # 在deque队列索引号Index前插入对象object[insert object before index]
    deque.pop()                # 移除并返回队列右边(末尾)的元素[Remove and return the rightmost element.]
    deque.popleft()            # 移除并返回队列左边(开始)的元素[Remove and return the leftmost element.]
    deque.remove(value)        # 移除队列中指定的元素[remove first occurrence of value.]
    deque.reverse()            # 翻转队列，即队列前后翻转
    deque.rotate(step)        # 向右旋转step步，不设置步数是，则默认向右旋转1步，如果step小于0，则向左旋转。
    deque.maxlen            # 队列的最大长度

    >>> deque
    deque([], maxlen=5)
    >>> deque.maxlen
    5
    >>> deque.append('first')
    >>> deque
    deque(['first'], maxlen=5)
    >>> deque.append('second')
    >>> deque
    deque(['first', 'second'], maxlen=5)
    >>> deque.append('third')
    >>> deque
    deque(['first', 'second', 'third'], maxlen=5)
    >>> deque.appendleft('four')
    >>> deque
    deque(['four', 'first', 'second', 'third'], maxlen=5)
    >>> deque.extend(['four','five'])
    >>> deque
    deque(['first', 'second', 'third', 'four', 'five'], maxlen=5)
    >>> deque.extendleft(['four','five'])
    >>> deque
    deque(['five', 'four', 'first', 'second', 'third'], maxlen=5)
    >>> deque1=deque.copy()
    >>> type(deque1)
    <class 'collections.deque'>
    >>> deque1
    deque(['five', 'four', 'first', 'second', 'third'], maxlen=5)
    >>> deque.extend(('fourth','fifth'))
    >>> deque
    deque(['first', 'second', 'third', 'fourth', 'fifth'], maxlen=5)

    >>> deque.count('first')
    1
    >>> deque.count('second')
    1
    >>> deque.count('third')
    1

    >>> deque.index('first')
    0
    >>> deque.index('second')
    1
    >>> deque.index('third')
    2
    >>> deque.index('third',0,2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 'third' is not in deque
    >>> deque.index('third',0,3)
    2

    >>> deque
    deque(['first', 'second', 'third', 'fourth', 'fifth'], maxlen=5)
    >>> deque.reverse()
    >>> deque
    deque(['fifth', 'fourth', 'third', 'second', 'first'], maxlen=5)
    >>> deque.reverse()
    >>> deque
    deque(['first', 'second', 'third', 'fourth', 'fifth'], maxlen=5)

    >>> deque.rotate()
    >>> deque
    deque(['fifth', 'first', 'second', 'third', 'fourth'], maxlen=5)
    >>> deque.rotate(-1)
    >>> deque
    deque(['first', 'second', 'third', 'fourth', 'fifth'], maxlen=5)
    >>> deque.rotate(3)
    >>> deque
    deque(['third', 'fourth', 'fifth', 'first', 'second'], maxlen=5)
    >>> deque.rotate(-3)
    >>> deque
    deque(['first', 'second', 'third', 'fourth', 'fifth'], maxlen=5)

    >>> deque.pop()
    'fifth'
    >>> deque
    deque(['first', 'second', 'third', 'fourth'], maxlen=5)
    >>> deque.popleft()
    'first'
    >>> deque
    deque(['second', 'third', 'fourth'], maxlen=5)
    >>> deque.remove('fourth')
    >>> deque
    deque(['second', 'third'], maxlen=5)
    >>> len(deque)
    2
    >>> deque.maxlen
    5
    >>> deque.remove('third')
    >>> deque
    deque(['second'], maxlen=5)
    >>> len(deque)
    1
    >>> deque.maxlen
    5
     
    >>> deque.clear()
    >>> deque
    deque([], maxlen=5)

常用内建模块之命名元组namedtuple
-------------------------------------------

访问元组数据时是通过索引下标来获取相应元素的值，需要熟记每个下标对应的具体含义。

当元组元素量较大时，记住每一个下标对应的意义那是相当困难的。于是就出现了命名元组namedtuple。

命名元组的对象的定义如下::

    collections.namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
    from collections import namedtuple 导入命名元组namedtuple
    typename:此元组的名称
    field_names:字段名称，可以是whitespace或逗号分隔开的字符串或列表，如'x y z'或'x,y,z'或['x','y','z']
                保留字不要作为字段名称，数字和下划线不能作为字段开头字符。
    verbose=False:如果verbose为true，则在构建完成后打印类定义。 
                这个选项已经过时了， 相反，打印_source属性更简单。
    rename=False:是否重命名字段名称，如果rename=True，则当字段名称无效时，会被自动替换成下划线 加元素所在索引数，如_1等

命名元组namedtuple的使用方法如下::

    # 定义，导入namedtuple包
    >>> from collections import namedtuple
    
    # 下面5种方式都是定义的名称为student的命名元组，并且有三个字段名称name/年龄age/性别sex
    >>> student=namedtuple('student','name age sex')
    >>> student=namedtuple('student','name,age,sex')
    >>> student=namedtuple('student','name\tage\tsex')
    >>> student=namedtuple('student',['name','age','sex'])
    >>> student=namedtuple('student',(['name','age','sex']))
    >>> sa=student('Manu',40,'male')
    >>> sb=student(name='Danny Green',age=30,sex='male')
    >>> sc=student('Tony Parker',36,sex='male')
    >>> sa
    student(name='Manu', age=40, sex='male')
    >>> sb
    student(name='Danny Green', age=30, sex='male')
    >>> sc
    student(name='Tony Parker', age=36, sex='male')
    >>> sa.name
    'Manu'
    >>> sa.age
    40
    >>> sa.sex
    'male'

    # 定义球员的名称、国家，球衣号码组成的命名元组player
    >>> player=namedtuple('player','name country number')
    >>> player
    <class '__main__.player'>
    >>> manu=player('Manu Ginóbili','阿根廷',20)
    >>> manu.name
    'Manu Ginóbili'
    >>> manu.cou
    manu.count(  manu.country
    >>> manu.country
    '阿根廷'
    >>> manu.number
    20
    >>> Parker=player('Tony Parker','法国',9)
    >>> Parker
    player(name='Tony Parker', country='法国', number=9)
    >>> Parker.name
    'Tony Parker'
    >>> Parker.count
    Parker.count(  Parker.country
    >>> Parker.country
    '法国'
    >>> Parker.number
    9
    >>> type(Parker)
    <class '__main__.player'>

    # rename的使用
    # 默认情况下rename=False，即当字段名称无效时，不重命名字段名称
    
    # 不带rename属性时，带def和return等保留字时，定义会报错:
    >>> with_def_return=namedtuple('player','name def country return number')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "D:\ProgramFiles\Python3.6.2\lib\collections\__init__.py", line 406, in namedtuple
        'keyword: %r' % name)
    ValueError: Type names and field names cannot be a keyword: 'def'

    >>> with_two_name=namedtuple('player','name country name number')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "D:\ProgramFiles\Python3.6.2\lib\collections\__init__.py", line 413, in namedtuple
        raise ValueError('Encountered duplicate field name: %r' % name)
    ValueError: Encountered duplicate field name: 'name'
    
    # 带rename属性时，带def和return等保留字时，定义不会报错，但保留字会被替换成下划线加元素所在索引数:
    >>> with_def_return=namedtuple('player','name def country return number',rename=True)
    >>> with_def_return
    <class '__main__.player'>
    >>> with_def_return._fields
    ('name', '_1', 'country', '_3', 'number')

    >>> with_two_name=namedtuple('player','name country name number',rename=True)
    >>> with_two_name
    <class '__main__.player'>
    >>> with_two_name._fields
    ('name', 'country', '_2', 'number')

    # namedtuple命名元组的一些方法
    somenamedtuple._fields            列出字段名称的字符串元组。
    somenamedtuple._make(iterable)    从现有序列或迭代中创建新实例的类方法。
    somenamedtuple._asdict()        返回一个新的有序字典OrderedDict，它将字段名称映射到相应的值
    somenamedtuple._replace(**kwargs)    用新值替换命名元组的字段的值，并返回新命名元组
    somenamedtuple._source                python源码的字符串

    # 使用_make将列表转换成命名元组实例
    >>> list1=['Kawhi Leonard','美国',2]
    >>> kawhi=player._make(list1)
    >>> kawhi
    player(name='Kawhi Leonard', country='美国', number=2)
    >>> kawhi.name
    'Kawhi Leonard'
    >>> kawhi.country
    '美国'
    >>> kawhi.number
    2
    >>> kawhi._fields
    ('name', 'country', 'number')
    >>> kawhi._asdict()
    OrderedDict([('name', 'Kawhi Leonard'), ('country', '美国'), ('number', 2)])

    # 使用_make将元组转换成命名元组实例
    >>> tuple1=('Danny Green','美国',14)
    >>> green=player._make(tuple1)
    >>> green
    player(name='Danny Green', country='美国', number=14)
    >>> green.name
    'Danny Green'
    >>> green.country
    '美国'
    >>> green.number
    14
    >>> green._fields
    ('name', 'country', 'number')
    >>> green._asdict()
    OrderedDict([('name', 'Danny Green'), ('country', '美国'), ('number', 14)])

    # 不能使用_make将字典转换成命名元组实例，需要使用double-star-operator双*操作：
    >>> p1={'name':'Tim Duncan','country':'USA','number':11}
    >>> tim=player._make(p1)
    >>> tim   # 转换出来的结果并不是自己想要的
    player(name='name', country='country', number='number')
    >>> tim=player(**p1)
    >>> tim
    player(name='Tim Duncan', country='USA', number=11)

    # 使用_replace替换命名元组的字段的值，并返回新命名元组
    >>> green
    player(name='Danny Green', country='美国', number=14)
    >>> green._replace(number=4)
    player(name='Danny Green', country='美国', number=4)
    >>> green.number
    14
    >>> new_green=green._replace(number=4)
    >>> new_green
    player(name='Danny Green', country='美国', number=4)
    >>> new_green.number
    4
    
    # 使用_fields构建新的命名元组
    >>> location=namedtuple('location','row column')
    >>> location
    <class '__main__.location'>
    >>> location._fields
    ('row', 'column')
    >>> color=namedtuple('color','red green blue')
    >>> color._fields
    ('red', 'green', 'blue')
    >>> pixel=namedtuple('pixel',location._fields+color._fields)
    >>> pixel._fields
    ('row', 'column', 'red', 'green', 'blue')


常用内建模块之有序字典OrderedDict
----------------------------------------

python自带的字典dict是无序的，因为字典dict是按hash来存储的。

collections模块下的OrderedDict实现了对字典中元素的排序；由于有序字典会记住它的插入顺序，所以它可以与排序结合使用来创建一个已排序的字典。

有序字典OrderedDict的使用方法如下::

    >>> from collections import OrderedDict as od
    >>> od.
    od.clear(       od.fromkeys(    od.items(       od.move_to_end( od.pop(         od.setdefault(  od.values(
    od.copy(        od.get(         od.keys(        od.popitem(     od.update(

    od.fromkeys(iterator)    # 从可迭代序列中生成有序键
    od.items()                # 返回有序字典的所有元素
    od.get(key)                # 获取键key对应的value值
    od.values()                # 返回有序字典的所有的value值
    od.keys()                # 返回有序字典的所有的key值
    od.pop(key)                # 从有序字典中移除键key，并返回key对应的值value
    od.popitem(key,last=True)    # 从有序字典中移除键key，返回元组(key,value)
                                # 不指定key时，则移除最后加入的key
                                # 如果指定last=True(默认)，则LIFO(last-in,first-out后进先出)
                                # 如果指定last=False，则FIFO(first-in,first-out先进先出)
    od.copy()                # 复制有序字典
    od.setdefault(key,value)    # 获取有序字典中key对应的值
                                # 如果key不存在，则创建对应的key，并赋值为value
                                # 如果key不存在，则未指定value，则value值为None
    od.update(key_value)        # 更新有序字典中key对应的值为新value
    od.clear()                    # 清空有序字典
    od.move_to_end(key,last=True)        # 将有序字典中key对应的键值对移动到有序字典有结尾处
                                        # 如果指定last=False(默认为True)，则移动到开始处
    # 普通字典
    >>> dict1 = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    >>> dict1
    {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    # 按键排序
    >>> dict2=od(sorted(dict1.items(),key=lambda t:t[0]))
    >>> dict2
    OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
    # 按值升序排序
    >>> dict3=od(sorted(dict1.items(),key=lambda t:t[1]))
    >>> dict3
    OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
    # 按值降序排序
    >>> dict3=od(sorted(dict1.items(),key=lambda t:t[1],reverse=True))
    >>> dict3
    OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
    # 按键对应的字符串的长度升序排序
    >>> dict4=od(sorted(dict1.items(),key=lambda t:len(t[0])))
    >>> dict4
    OrderedDict([('pear', 1), ('apple', 4), ('banana', 3), ('orange', 2)])
    # 按键对应的字符串的长度降序排序
    >>> dict5=od(sorted(dict1.items(),key=lambda t:len(t[0]),reverse=True))
    >>> dict5
    OrderedDict([('banana', 3), ('orange', 2), ('apple', 4), ('pear', 1)])

    >>> od1 = od([('name','meichaohui'),('lang','python')])
    >>> od1
    OrderedDict([('name', 'meichaohui'), ('lang', 'python')])
    >>> od1['age']=28
    >>> od1
    OrderedDict([('name', 'meichaohui'), ('lang', 'python'), ('age', 28)])
    >>> od2=od.fromkeys('abcdefg')
    >>> od2
    OrderedDict([('a', None), ('b', None), ('c', None), ('d', None), ('e', None), ('f', None), ('g', None)])
    >>> od3=od.fromkeys(['a','b','c','d'])
    >>> od3
    OrderedDict([('a', None), ('b', None), ('c', None), ('d', None)])
    >>> od4=od.fromkeys({"a":1})
    >>> od4
    OrderedDict([('a', None)])

    >>> od3.items()
    odict_items([('a', None), ('b', None), ('c', None), ('d', None)])
    >>> od4.items()
    odict_items([('a', None)])

    >>> od1
    OrderedDict([('name', 'meichaohui'), ('lang', 'python'), ('age', 28)])
    >>> od1.get('name')
    'meichaohui'
    >>> od1.get('age')
    28
    >>> od1.get('lang')
    'python'

    >>> od1.values()
    odict_values(['meichaohui', 'python', 28])
    >>> od2.values()
    odict_values([None, None, None, None, None, None, None])
    >>> od2.keys()
    odict_keys(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    >>> od1.keys()
    odict_keys(['name', 'lang', 'age'])

    >>> dict1=od([('a',1),('b',2),('c',3)])
    >>> dict1
    OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    >>> dict1.pop()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Required argument 'key' (pos 1) not found
    >>> dict1.pop('b')
    2
    >>> dict1
    OrderedDict([('a', 1), ('c', 3)])
    >>> dict1.popitem()
    ('c', 3)
    >>> dict1
    OrderedDict([('a', 1)])
    >>> dict1.setdefault('b',2)
    2
    >>> dict1
    OrderedDict([('a', 1), ('b', 2)])
    >>> dict1.popitem('b')
    ('b', 2)
    >>> dict1
    OrderedDict([('a', 1)])
    >>> dict1.setdefault('b')
    >>> dict1
    OrderedDict([('a', 1), ('b', None)])
    >>> dict1.update('b')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: need more than 1 value to unpack
    >>> dict1.update('b',1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: update() takes at most 1 positional argument (2 given)
    >>> dict1.update(('b',1))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: need more than 1 value to unpack
    >>> dict1.update([('b',1)])
    >>> dict1
    OrderedDict([('a', 1), ('b', 1)])
    >>> dict1.update([('b',2)])
    >>> dict1
    OrderedDict([('a', 1), ('b', 2)])
    >>> dict1.update({'b':3})
    >>> dict1
    OrderedDict([('a', 1), ('b', 3)])
    >>> dict2=dict1.copy()
    >>> dict2
    OrderedDict([('a', 1), ('b', 3)])
    >>> dict2.clear()
    >>> dict2
    OrderedDict()

    >>> dict1
    OrderedDict([('a', 1), ('b', 3)])
    >>> dict1['c']=2
    >>> dict1
    OrderedDict([('a', 1), ('b', 3), ('c', 2)])
    >>> dict1['d']=4
    >>> dict1
    OrderedDict([('a', 1), ('b', 3), ('c', 2), ('d', 4)])
    >>> dict1.move_to_end('b')
    >>> dict1
    OrderedDict([('a', 1), ('c', 2), ('d', 4), ('b', 3)])
    >>> dict1.move_to_end('d')
    >>> dict1
    OrderedDict([('a', 1), ('c', 2), ('b', 3), ('d', 4)])


常用内建模块之defaultdict字典缺省默认值
-------------------------------------------

在Python中如果访问字典中不存在的键，则会引发KeyError异常。

示例::

    In [1]: dict1={'a':1,'b':2}                                                                   
                                                                                                  
    In [2]: dict1['a']                                                                            
    Out[2]: 1                                                                                     
                                                                                                  
    In [3]: dict1['b']                                                                            
    Out[3]: 2                                                                                     
                                                                                                  
    In [4]: dict1['c']                                                                            
    ---------------------------------------------------------------------------                   
    KeyError                                  Traceback (most recent call last)                   
    <ipython-input-4-6bf0c4d0a790> in <module>                                                    
    ----> 1 dict1['c']                                                                            
                                                                                                  
    KeyError: 'c'                                                                                 


访问dict1['c']时提示'c'键不存在。


假设我有下面这样的一段文章需要统计每个单词的数量::

    This module implements specialized container datatypes providing
    alternatives to Python's general purpose built-in containers, dict,
    list, set, and tuple.

    * namedtuple   factory function for creating tuple subclasses with named fields
    * deque        list-like container with fast appends and pops on either end
    * ChainMap     dict-like class for creating a single view of multiple mappings
    * Counter      dict subclass for counting hashable objects
    * OrderedDict  dict subclass that remembers the order entries were added
    * defaultdict  dict subclass that calls a factory function to supply missing values
    * UserDict     wrapper around dictionary objects for easier dict subclassing
    * UserList     wrapper around list objects for easier list subclassing
    * UserString   wrapper around string objects for easier string subclassing

- 不使用defaultdict，按普通的字典统计方式进行统计，在单词第一次统计的时候，在counts中相应的键存下默认值1。这需要在处理的时候添加一个判断语句。

代码如下::

    # Filename: defaultdict_count_word.py
    # Author: meizhaohui

    def count_words(article):
        # replace \n to space,then split to list
        article_list = article.replace('\n',' ').split()
        counts = {}
        for word in article_list:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
        print(counts)
        
        
    if __name__ == '__main__':
        article='''This module implements specialized container datatypes providing
    alternatives to Python's general purpose built-in containers, dict,
    list, set, and tuple.

    * namedtuple   factory function for creating tuple subclasses with named fields
    * deque        list-like container with fast appends and pops on either end
    * ChainMap     dict-like class for creating a single view of multiple mappings
    * Counter      dict subclass for counting hashable objects
    * OrderedDict  dict subclass that remembers the order entries were added
    * defaultdict  dict subclass that calls a factory function to supply missing values
    * UserDict     wrapper around dictionary objects for easier dict subclassing
    * UserList     wrapper around list objects for easier list subclassing
    * UserString   wrapper around string objects for easier string subclassing

    '''
        count_words(article)
        
运行::

    $ python defaultdict_count_word.py                                                                                      
    {'This': 1, 'module': 1, 'implements': 1, 'specialized': 1, 'container': 2, 'datatypes': 1, 'providing': 1, 'alternative
    s': 1, 'to': 2, "Python's": 1, 'general': 1, 'purpose': 1, 'built-in': 1, 'containers,': 1, 'dict,': 1, 'list,': 1, 'set
    ,': 1, 'and': 2, 'tuple.': 1, '*': 9, 'namedtuple': 1, 'factory': 2, 'function': 2, 'for': 6, 'creating': 2, 'tuple': 1,
     'subclasses': 1, 'with': 2, 'named': 1, 'fields': 1, 'deque': 1, 'list-like': 1, 'fast': 1, 'appends': 1, 'pops': 1, 'o
    n': 1, 'either': 1, 'end': 1, 'ChainMap': 1, 'dict-like': 1, 'class': 1, 'a': 2, 'single': 1, 'view': 1, 'of': 1, 'multi
    ple': 1, 'mappings': 1, 'Counter': 1, 'dict': 4, 'subclass': 3, 'counting': 1, 'hashable': 1, 'objects': 4, 'OrderedDict
    ': 1, 'that': 2, 'remembers': 1, 'the': 1, 'order': 1, 'entries': 1, 'were': 1, 'added': 1, 'defaultdict': 1, 'calls': 1
    , 'supply': 1, 'missing': 1, 'values': 1, 'UserDict': 1, 'wrapper': 3, 'around': 3, 'dictionary': 1, 'easier': 3, 'subcl
    assing': 3, 'UserList': 1, 'list': 2, 'UserString': 1, 'string': 2}                                                     
                                                                                                                        
                                                                                                                        
- 使用defaultdict，不需要对键进行判断，直接添加。

代码如下::

    # Filename: defaultdict_count_word.py
    # Author: meizhaohui

    def count_words(article):
        from collections import defaultdict as dt
        # replace \n to space,then split to list
        article_list = article.replace('\n',' ').split()
        # counts = {}
        counts = dt(int)
        for word in article_list:
            # if word not in counts:
            #     counts[word] = 1
            # else:
            #     counts[word] += 1
            counts[word] += 1
        print(counts)
        
        
    if __name__ == '__main__':
        article='''This module implements specialized container datatypes providing
    alternatives to Python's general purpose built-in containers, dict,
    list, set, and tuple.
    
    * namedtuple   factory function for creating tuple subclasses with named fields
    * deque        list-like container with fast appends and pops on either end
    * ChainMap     dict-like class for creating a single view of multiple mappings
    * Counter      dict subclass for counting hashable objects
    * OrderedDict  dict subclass that remembers the order entries were added
    * defaultdict  dict subclass that calls a factory function to supply missing values
    * UserDict     wrapper around dictionary objects for easier dict subclassing
    * UserList     wrapper around list objects for easier list subclassing
    * UserString   wrapper around string objects for easier string subclassing

    '''
        count_words(article)
        
运行::

    $ python defaultdict_count_word.py
    defaultdict(<class 'int'>, {'This': 1, 'module': 1, 'implements': 1, 'specialized': 1, 'container': 2, 'datatypes': 1, 'providing': 1, 'alternatives': 1, 'to': 2, "Python's": 1, 'general': 1, 'purpose': 1, 'built-in': 1, 'containers,': 1, 'dict,': 1, 'list,': 1, 'set,': 1, 'and': 2, 'tuple.': 1, '*': 9, 'namedtuple': 1, 'factory': 2, 'function': 2, 'for': 6, 'creating': 2, 'tuple': 1, 'subclasses': 1, 'with': 2, 'named': 1, 'fields': 1, 'deque': 1, 'list-like': 1, 'fast': 1, 'appends': 1, 'pops': 1, 'on': 1, 'either': 1, 'end': 1, 'ChainMap': 1, 'dict-like': 1, 'class': 1, 'a': 2, 'single': 1, 'view': 1, 'of': 1, 'multiple': 1, 'mappings': 1, 'Counter': 1, 'dict': 4, 'subclass': 3, 'counting': 1, 'hashable': 1, 'objects': 4, 'OrderedDict': 1, 'that': 2, 'remembers': 1, 'the': 1, 'order': 1, 'entries': 1, 'were': 1, 'added': 1, 'defaultdict': 1, 'calls': 1, 'supply': 1, 'missing': 1, 'values': 1, 'UserDict': 1, 'wrapper': 3, 'around': 3, 'dictionary': 1, 'easier': 3, 'subclassing': 3, 'UserList': 1, 'list': 2, 'UserString': 1, 'string': 2})


上面示例中defaultdict使用int给不存在的键设定默认值为int类型的默认值0，counts[word] += 1 实质上是先给counts[word]赋值0，遇到重复的单词的话就加1。使用这种方式不需要再进行判断。

注：上面的例子并没有对标点符号进行再进一步的处理，只是粗略的计算了一下单词量。

defaultdict可以使用int,list,dict等的默认值作为期字典缺省默认值。

