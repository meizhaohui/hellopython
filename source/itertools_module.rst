.. _itertools_module:

模块-itertools模块迭代器函数
==============================

.. contents:: 目录

itertools模块基本介绍
------------------------------

- Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
- itertools包含特殊用途的迭代器函数。
- 在for .. in 循环中调用迭代函数，每次返回一项，并记住当前调用的状态。


itertools的帮助信息::

    In [1]: import itertools

    In [2]: itertools?
    Type:        module
    String form: <module 'itertools' (built-in)>
    Docstring:
    Functional tools for creating and using iterators.

    Infinite iterators:   
    count(start=0, step=1) --> start, start+step, start+2*step, ...
    cycle(p) --> p0, p1, ... plast, p0, p1, ...
    repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times

    Iterators terminating on the shortest input sequence:
    accumulate(p[, func]) --> p0, p0+p1, p0+p1+p2
    chain(p, q, ...) --> p0, p1, ... plast, q0, q1, ...
    chain.from_iterable([p, q, ...]) --> p0, p1, ... plast, q0, q1, ...
    compress(data, selectors) --> (d[0] if s[0]), (d[1] if s[1]), ...
    dropwhile(pred, seq) --> seq[n], seq[n+1], starting when pred fails
    groupby(iterable[, keyfunc]) --> sub-iterators grouped by value of keyfunc(v)
    filterfalse(pred, seq) --> elements of seq where pred(elem) is False
    islice(seq, [start,] stop [, step]) --> elements from
           seq[start:stop:step]
    starmap(fun, seq) --> fun(*seq[0]), fun(*seq[1]), ...
    tee(it, n=2) --> (it1, it2 , ... itn) splits one iterator into n
    takewhile(pred, seq) --> seq[0], seq[1], until pred fails
    zip_longest(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ...

    Combinatoric generators:
    product(p, q, ... [repeat=1]) --> cartesian product
    permutations(p[, r])
    combinations(p, r)
    combinations_with_replacement(p, r)
    

itertools模块无限迭代器
------------------------------

- itertools.count(start=0, step=1) 返回从start开始，步长为step的迭代器，如果不手动终止，会无限迭代。我们可以在循环中增加判断条件或按Ctrl+C终止程序。

示例::

    In [3]: for i in itertools.count(1,2):                  
       ...:     print(i)                                    
       ...:     if i>20:                                    
       ...:         break                                   
       ...:                                                 
    1                                                       
    3                                                       
    5                                                       
    7                                                       
    9                                                       
    11                                                      
    13                                                      
    15                                                      
    17                                                      
    19                                                      
    21                                                      
    
- itertools.cycle(p) 循环可迭代对象p中的子对象。

示例::

    In [4]: count = 0                                                
                                                                     
    In [5]: for i in itertools.cycle('abcdefg'):                     
       ...:     print(i)                                             
       ...:     count += 1                                           
       ...:     if count > 20:                                       
       ...:         break                                            
       ...:                                                          
    a                                                                
    b                                                                
    c                                                                
    d                                                                
    e                                                                
    f                                                                
    g                                                                
    a                                                                
    b                                                                
    c                                                                
    d                                                                
    e                                                                
    f                                                                
    g                                                                
    a                                                                
    b                                                                
    c                                                                
    d                                                                
    e                                                                
    f                                                                
    g                                                                
    
    
    In [6]: count = 0                                                               
                                                                                     
    In [7]: for i in itertools.cycle(['one','two','three']):                        
        ...:     print(i)                                                            
        ...:     count += 1                                                          
        ...:     if count > 20:                                                      
        ...:         break                                                           
        ...:                                                                         
    one                                                                              
    two                                                                              
    three                                                                            
    one                                                                              
    two                                                                              
    three                                                                            
    one                                                                              
    two                                                                              
    three                                                                            
    one                                                                              
    two                                                                              
    three                                                                            
    one                                                                              
    two                                                                              
    three                                                                            
    one                                                                              
    two                                                                              
    three                                                                            
    one                                                                              
    two                                                                              
    three                                                                            

- itertools.repeat(elem [,n])  重复elem元素n次，如果不指定n则无限循环。

示例::

    In [8]: count = 0                                                            
                                                                                  
    In [9]: for i in itertools.repeat(['one','two','three']):                    
        ...:     print(i)                                                         
        ...:     count += 1                                                       
        ...:     if count > 20:                                                   
        ...:         break                                                        
        ...:                                                                      
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
    ['one', 'two', 'three']                                                       
                                                                                  
    In [10]: count = 0

    In [11]: for i in itertools.repeat('abcdefg'):
        ...:     print(i)
        ...:     count += 1
        ...:     if count > 20:
        ...:         break
        ...:
        ...:
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg
    abcdefg


itertools模块输入序列迭代器
------------------------------

- itertools.accumulate(p[, func]) --> p0, p0+p1, p0+p1+p2 返回序列组合后的值。
- 可以指定函数func，则按func函数进行迭代。

示例::

    In [12]: for i in itertools.accumulate(['a','b','c']):                  
        ...:     print(i)                                                   
        ...:                                                                
    a                                                                       
    ab                                                                      
    abc                                                                     

                                                                            
    In [13]: for i in itertools.accumulate('abc'):                          
        ...:     print(i)                                                   
        ...:                                                                
    a                                                                       
    ab                                                                      
    abc                                                                     
                                                                            
    In [14]: for i in itertools.accumulate(('a','b','c')):                  
        ...:     print(i)                                                   
        ...:                                                                
    a                                                                       
    ab                                                                      
    abc                                                                     

    In [15]: for i in itertools.accumulate(('a','b','c'), lambda x,y:x*2+y*3):
        ...:     print(i)
        ...:
    a
    aabbb                       # ==>   'a' * 2 + 'b' * 3
    aabbbaabbbccc               # ==>  'aabbb' * 2  + 'c' * 3

    In [16]: for i in itertools.accumulate((1,2,3,4), lambda x,y:x*2+y*2):
        ...:     print(i)
        ...:
    1
    6                           # ==>   1 * 2 + 2 * 2
    18                          # ==>   6 * 2 + 3 * 2
    44                          # ==>   18 * 2 + 4 * 2


    In [17]: import operator                                                   
                                                                               
    In [18]: for i in itertools.accumulate((1,2,3,4,5,6), operator.mul):       
        ...:     print(i)                                                      
        ...:                                                                   
    1                           # ==>    计算阶乘                              
    2                           # ==>    1 * 2                                 
    6                           # ==>    2 * 3                                 
    24                          # ==>    6 * 4                                 
    120                         # ==>    24 * 5                                
    720                         # ==>    120 * 6                               
    


- itertools.chain(p, q, ...) --> p0, p1, ... plast, q0, q1, ... 将多个迭代器作为参数，将这多个迭代器链接在一起，返回单个迭代器。

示例::

    In [19]: for i in itertools.chain('abcd',('a1','b1','c1','d1'),{'a2':1,'b2':2}):            
       ...:     print(i)                                                                       
       ...:                                                                                    
    a                                                                                          
    b                                                                                          
    c                                                                                          
    d                                                                                          
    a1                                                                                         
    b1                                                                                         
    c1                                                                                         
    d1                                                                                         
    a2                                                                                         
    b2

- itertools.chain.form_iterable([p, q, ...]) --> p0, p1, ... plast, q0, q1, ... 只接受一个参数，并将参数作为迭代器进行迭代。

示例::

    In [20]: for i in itertools.chain.from_iterable(['abc']): 
       ...:     print(i) 
       ...:                                                                         
    a
    b
    c
    
    In [21]: for i in itertools.chain.from_iterable(['abc','def']): 
       ...:     print(i) 
       ...:                                                                         
    a
    b
    c
    d
    e
    f

     In [22]: for i in itertools.chain.from_iterable(('abc','def')):
       ...:     print(i)
       ...:
    a
    b
    c
    d
    e
    f
    
    In [23]: for i in itertools.chain.from_iterable({'abc':1,'def':2}):
       ...:     print(i)
       ...:
    a
    b
    c
    d
    e
    f

- itertools.compress(data, selectors) --> (d[0] if s[0]), (d[1] if s[1]), ... compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
- 选择器，对原始数据data进行筛选，选择器selectors中元素为False时不选择，True时选择。

示例::

    In [24]: for i in itertools.compress('abcdef',[True,[],1,(),2,{'a':1}]): 
        ...:     print(i) 
        ...:                                                                        
    a
    c
    e
    f
    
    In [25]: for i in itertools.compress('ABCDEF', [1,0,1,0,1,1]): 
        ...:     print(i) 
        ...:                                                                        
    A
    C
    E
    F

     In [26]: for i in itertools.compress('ABCDEF', (1,'0',1,0,1,1)):
        ...:     print(i)
        ...:
    A
    B
    C
    E
    F

- itertools.dropwhile(pred, seq) --> seq[n], seq[n+1], starting when pred fails   dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
- 删除满足条件的元素，直到条件pred为False时，返回后续所有元素的迭代器。

示例::

    In [27]: for i in itertools.dropwhile(lambda x: x<5, [1,4,6,4,1]): 
        ...:     print(i) 
        ...:                                                                        
    6
    4
    1
    
    In [28]: def should_drop(x): 
        ...:     print('Droped: {}'.format(x)) 
        ...:     return x<5 
        ...:      
    
    In [28]: for i in itertools.dropwhile(should_drop, [1,4,6,4,1]): 
        ...:     print(i) 
        ...:     
    
    Droped: 1
    Droped: 4
    Droped: 6
    6
    4
    1

- itertools.groupby(iterable[, keyfunc]) --> sub-iterators grouped by value of keyfunc(v) 
- 返回一个按照keyfunc(v)进行分组后的值集合的子迭代器。如果iterable在多次连接迭代中产生同一项，则会定义一个组。keyfunc是计算的关键，如果未指定keyfunc则返回值与迭代元素值相同。如果定义了keyfunc，则需要对每个迭代元素执行keyfunc后的结果进行分组处理(每个分组是一个子迭代器)，最后返回的迭代器的元素是(key,group),如果要显示最后的group值，需要使用list(group)将组迭代器存储在字典中。


示例::

    In [29]: for k,v in itertools.groupby('AAABBBCCCDDEAAA'):
        ...:     print(k, '\tvalue:', v)
        ...:
    A 	value: <itertools._grouper object at 0x7feff3ab82e8>
    B 	value: <itertools._grouper object at 0x7feff3ab8ac8>
    C 	value: <itertools._grouper object at 0x7feff3ab82e8>
    D 	value: <itertools._grouper object at 0x7feff3ab8cf8>
    E 	value: <itertools._grouper object at 0x7feff3ab82e8>
    A 	value: <itertools._grouper object at 0x7feff3ab8cf8>

    # 说明：此处直接打印value，可以看出value是一个迭代器
    
    In [30]: for k,v in itertools.groupby('AAABBBCCCDDEAAA'):
        ...:     print(k, '\tvalue:', list(v))
        ...:
    A 	value: ['A', 'A', 'A']
    B 	value: ['B', 'B', 'B']
    C 	value: ['C', 'C', 'C']
    D 	value: ['D', 'D']
    E 	value: ['E']
    A 	value: ['A', 'A', 'A']

    # 说明：将value存储到list中，打印出list列表中的值

    In [31]: def keyfunc(key): 
        ...:     return key + '*' + key 
        ...:                                                                        
    
    In [32]: for k,v in itertools.groupby('AAABBBCCCDDEAAA', keyfunc): 
        ...:     print(k, '\tvalue:', list(v)) 
        ...:                                                                        
    A*A 	value: ['A', 'A', 'A']
    B*B 	value: ['B', 'B', 'B']
    C*C 	value: ['C', 'C', 'C']
    D*D 	value: ['D', 'D']
    E*E 	value: ['E']
    A*A 	value: ['A', 'A', 'A']
    
    # 说明：定义了keyfunc，重新生成的健不一样

    In [33]: for k,v in itertools.groupby(['aa','ab','abc','def','abcde'], len): 
        ...:     print(k, '\tvalue:', list(v)) 
        ...:                                                                        
    2 	value: ['aa', 'ab']
    3 	value: ['abc', 'def']
    5 	value: ['abcde']

    # 说明：使用len函数获取元素的长度值作为健

    In [34]: def keyfunc(key): 
        ...:     import random 
        ...:     return key + '*' + key + str(random.randint(0,100)) 
        ...:                                                                        
    
    In [35]: for k,v in itertools.groupby('AAABBBCCCDDEAAA', keyfunc): 
        ...:     print(k, '\tvalue:', list(v)) 
        ...:                                                                        
    A*A79 	value: ['A']
    A*A95 	value: ['A']
    A*A70 	value: ['A']
    B*B21 	value: ['B']
    B*B61 	value: ['B']
    B*B99 	value: ['B']
    C*C99 	value: ['C']
    C*C28 	value: ['C']
    C*C85 	value: ['C']
    D*D96 	value: ['D']
    D*D90 	value: ['D']
    E*E5 	value: ['E']
    A*A87 	value: ['A']
    A*A25 	value: ['A']
    A*A50 	value: ['A']

    # 说明：此处用了一个随机数放在迭代元素的后面，并没有产生相同的键，因此没有分组。返回的结果都不一样

- itertools.filterfalse(pred, seq) --> elements of seq where pred(elem) is False， filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
- 仅生成pred(elem)为False的项的迭代器

示例::

   In [36]: for i in itertools.filterfalse(lambda x: x%2, range(10)): 
        ...:     print(i) 
        ...:                                                                        
    0
    2
    4
    6
    8
    
    # 说明：返回求余值是0(即False)的数，也就是返回偶数

    In [37]: def predicate(x): 
        ...:     return len(x) > 2 
        ...:                                                                        
    
    In [38]: for i in itertools.filterfalse(predicate, ['a','ab','abc','abcd']): 
        ...:     print(i) 
        ...:                                                                        
    a
    ab

    # 说明：返回长度不大于2的元素。

- itertools.islice(seq, [start,] stop [, step]) --> elements from seq[start:stop:step]
- 返回序列seq的从start开始到stop结束的步长为step的元素的迭代器,如果不指定start和step，则第二个参数是stop。

示例::

    In [39]: for i in itertools.islice('ABCDEFG', 2):
        ...:     print(i)
        ...:
    A
    B
    
    In [40]: for i in itertools.islice('ABCDEFG', 2, 4):
        ...:     print(i)
        ...:
    C
    D
    
    In [41]: for i in itertools.islice('ABCDEFG', 2, None):
        ...:     print(i)
        ...:
    C
    D
    E
    F
    G
    
    In [42]: for i in itertools.islice('ABCDEFG', 0, None, 2):
        ...:     print(i)
        ...:
    A
    C
    E
    G

- itertools.starmap(fun, seq) --> fun(\*seq[0]), fun(\*seq[1]), itertools.starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
- 返回执行fun(elem)后的迭代器。

示例::

    In [43]: for i in itertools.starmap(pow,[(2,5),(3,2),(10,3)]):
        ...:     print(i)
        ...:
    32
    9
    1000
    
    
    In [44]: for i in itertools.starmap(lambda x:2*x, ('1','2','3','4')):
        ...:     print(i)
        ...:
    11
    22
    33
    44

- itertools.tee(it, n=2) --> (it1, it2 , ... itn) splits one iterator into n
- 返回基于原始输入的n个独立迭代器的元组。为了克隆原始迭代器，生成的项会被缓存，分割成n个独立迭代器后，原先的迭代器就不要再使用，否则缓存机制可能无法正确工作。
- 使用list()函数比tee()函数快。

示例::

    In [45]: x = itertools.tee(('a','ab','abc'), 3)
    
    In [46]: x
    Out[46]:
    (<itertools._tee at 0x7feff83a5448>,
     <itertools._tee at 0x7feff397ee08>,
     <itertools._tee at 0x7feff3ad8dc8>)
    
    In [47]: for i in x:
        ...:     print(list(i))
        ...:
    ['a', 'ab', 'abc']
    ['a', 'ab', 'abc']
    ['a', 'ab', 'abc']


- itertools.takewhile(pred, seq) --> seq[0], seq[1], until pred fails
- itertools.takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
- 保留序列元素直到条件不满足。与dropwhile相反。

示例::

    In [48]: for i in itertools.takewhile(lambda x: x<5, [1,4,6,4,1]):
        ...:     print(i)
        ...:
    1
    4



- itertools.zip_longest(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ...
- 创建一个聚合来自每个迭代的元素的迭代器。 如果迭代的长度不均匀，则使用fillvalue填充缺失值。 迭代继续，直到最长的可迭代用尽。

示例::

    In [49]: for i in itertools.zip_longest('ABCD','xy',fillvalue='-'): 
        ...:     print(i) 
        ...:                                                                        
    ('A', 'x')
    ('B', 'y')
    ('C', '-')
    ('D', '-')

    In [50]: for i in itertools.zip_longest('ABCD','xy',['a','b','c','d','e'],fillva
        ...: lue='*'*3): 
        ...:     print(i) 
        ...:                                                                        
    ('A', 'x', 'a')
    ('B', 'y', 'b')
    ('C', '***', 'c')
    ('D', '***', 'd')
    ('***', '***', 'e')
    
   # 说明：最长的元素是列表['a','b','c','d','e'],其他元素长度小于5的元素，会补充3个*星号 

itertools模块组合迭代器
------------------------------

- itertools.product(p, q, ... [repeat=1]) --> cartesian product
- 生成笛卡尔积的元组。

示例::

    In [51]: for i in itertools.product('AB','xy'): 
         ...:     print(i) 
         ...:                                                                       
    ('A', 'x')
    ('A', 'y')
    ('B', 'x')
    ('B', 'y')
    
    In [52]: for i in itertools.product('AB','xy',repeat=2): 
         ...:     print(i) 
         ...:                                                                       
    ('A', 'x', 'A', 'x')
    ('A', 'x', 'A', 'y')
    ('A', 'x', 'B', 'x')
    ('A', 'x', 'B', 'y')
    ('A', 'y', 'A', 'x')
    ('A', 'y', 'A', 'y')
    ('A', 'y', 'B', 'x')
    ('A', 'y', 'B', 'y')
    ('B', 'x', 'A', 'x')
    ('B', 'x', 'A', 'y')
    ('B', 'x', 'B', 'x')
    ('B', 'x', 'B', 'y')
    ('B', 'y', 'A', 'x')
    ('B', 'y', 'A', 'y')
    ('B', 'y', 'B', 'x')
    ('B', 'y', 'B', 'y')
    
    In [53]: for i in itertools.product('AB','xy',repeat=3): 
         ...:     print(i) 
         ...:                                                                       
    ('A', 'x', 'A', 'x', 'A', 'x')
    ('A', 'x', 'A', 'x', 'A', 'y')
    ('A', 'x', 'A', 'x', 'B', 'x')
    ('A', 'x', 'A', 'x', 'B', 'y')
    ('A', 'x', 'A', 'y', 'A', 'x')
    ('A', 'x', 'A', 'y', 'A', 'y')
    ('A', 'x', 'A', 'y', 'B', 'x')
    ('A', 'x', 'A', 'y', 'B', 'y')
    ('A', 'x', 'B', 'x', 'A', 'x')
    ('A', 'x', 'B', 'x', 'A', 'y')
    ('A', 'x', 'B', 'x', 'B', 'x')
    ('A', 'x', 'B', 'x', 'B', 'y')
    ('A', 'x', 'B', 'y', 'A', 'x')
    ('A', 'x', 'B', 'y', 'A', 'y')
    ('A', 'x', 'B', 'y', 'B', 'x')
    ('A', 'x', 'B', 'y', 'B', 'y')
    ('A', 'y', 'A', 'x', 'A', 'x')
    ('A', 'y', 'A', 'x', 'A', 'y')
    ('A', 'y', 'A', 'x', 'B', 'x')
    ('A', 'y', 'A', 'x', 'B', 'y')
    ('A', 'y', 'A', 'y', 'A', 'x')
    ('A', 'y', 'A', 'y', 'A', 'y')
    ('A', 'y', 'A', 'y', 'B', 'x')
    ('A', 'y', 'A', 'y', 'B', 'y')
    ('A', 'y', 'B', 'x', 'A', 'x')
    ('A', 'y', 'B', 'x', 'A', 'y')
    ('A', 'y', 'B', 'x', 'B', 'x')
    ('A', 'y', 'B', 'x', 'B', 'y')
    ('A', 'y', 'B', 'y', 'A', 'x')
    ('A', 'y', 'B', 'y', 'A', 'y')
    ('A', 'y', 'B', 'y', 'B', 'x')
    ('A', 'y', 'B', 'y', 'B', 'y')
    ('B', 'x', 'A', 'x', 'A', 'x')
    ('B', 'x', 'A', 'x', 'A', 'y')
    ('B', 'x', 'A', 'x', 'B', 'x')
    ('B', 'x', 'A', 'x', 'B', 'y')
    ('B', 'x', 'A', 'y', 'A', 'x')
    ('B', 'x', 'A', 'y', 'A', 'y')
    ('B', 'x', 'A', 'y', 'B', 'x')
    ('B', 'x', 'A', 'y', 'B', 'y')
    ('B', 'x', 'B', 'x', 'A', 'x')
    ('B', 'x', 'B', 'x', 'A', 'y')
    ('B', 'x', 'B', 'x', 'B', 'x')
    ('B', 'x', 'B', 'x', 'B', 'y')
    ('B', 'x', 'B', 'y', 'A', 'x')
    ('B', 'x', 'B', 'y', 'A', 'y')
    ('B', 'x', 'B', 'y', 'B', 'x')
    ('B', 'x', 'B', 'y', 'B', 'y')
    ('B', 'y', 'A', 'x', 'A', 'x')
    ('B', 'y', 'A', 'x', 'A', 'y')
    ('B', 'y', 'A', 'x', 'B', 'x')
    ('B', 'y', 'A', 'x', 'B', 'y')
    ('B', 'y', 'A', 'y', 'A', 'x')
    ('B', 'y', 'A', 'y', 'A', 'y')
    ('B', 'y', 'A', 'y', 'B', 'x')
    ('B', 'y', 'A', 'y', 'B', 'y')
    ('B', 'y', 'B', 'x', 'A', 'x')
    ('B', 'y', 'B', 'x', 'A', 'y')
    ('B', 'y', 'B', 'x', 'B', 'x')
    ('B', 'y', 'B', 'x', 'B', 'y')
    ('B', 'y', 'B', 'y', 'A', 'x')
    ('B', 'y', 'B', 'y', 'A', 'y')
    ('B', 'y', 'B', 'y', 'B', 'x')
    ('B', 'y', 'B', 'y', 'B', 'y')


- itertools.permutations(p[, r])
- 创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，那么序列的长度与iterable中的项目数量相同： 返回p中任意取r个元素做排列的元组的迭代器。

示例::

    In [54]: for i in itertools.permutations('ABCD',r=2):
         ...:     print(i)
         ...:
    ('A', 'B')
    ('A', 'C')
    ('A', 'D')
    ('B', 'A')
    ('B', 'C')
    ('B', 'D')
    ('C', 'A')
    ('C', 'B')
    ('C', 'D')
    ('D', 'A')
    ('D', 'B')
    ('D', 'C')

    In [55]: for i in itertools.permutations('ABC'):
         ...:     print(list(i))
         ...:
    ['A', 'B', 'C']
    ['A', 'C', 'B']
    ['B', 'A', 'C']
    ['B', 'C', 'A']
    ['C', 'A', 'B']
    ['C', 'B', 'A']

- itertools.combinations(p, r)
- 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 (不带重复)。

示例::

    In [56]: for i in itertools.combinations('ABC',r=2):
         ...:     print(i)
         ...:
    ('A', 'B')
    ('A', 'C')
    ('B', 'C')
    
    In [57]: for i in itertools.combinations('ABC',r=1):
         ...:     print(i)
         ...:
    ('A',)
    ('B',)
    ('C',)
    
    In [58]: for i in itertools.combinations('ABC',r=3):
         ...:     print(i)
         ...:
    ('A', 'B', 'C')

- itertools.combinations_with_replacement(p, r)
- 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 (带重复)

示例::

    In [59]: for i in itertools.combinations_with_replacement('ABC',r=3): 
         ...:     print(i) 
         ...:                                                                       
    ('A', 'A', 'A')
    ('A', 'A', 'B')
    ('A', 'A', 'C')
    ('A', 'B', 'B')
    ('A', 'B', 'C')
    ('A', 'C', 'C')
    ('B', 'B', 'B')
    ('B', 'B', 'C')
    ('B', 'C', 'C')
    ('C', 'C', 'C')
    
    In [60]: for i in itertools.combinations_with_replacement('ABC',r=2): 
         ...:     print(i) 
         ...:                                                                       
    ('A', 'A')
    ('A', 'B')
    ('A', 'C')
    ('B', 'B')
    ('B', 'C')
    ('C', 'C')
    
    In [61]: for i in itertools.combinations_with_replacement('ABC',r=1): 
         ...:     print(i) 
         ...:                                                                       
    ('A',)
    ('B',)
    ('C',)


参考文献

- `itertools — Functions creating iterators for efficient looping <https://docs.python.org/3.7/library/itertools.html>`_
- `Python itertools模块详解 <https://www.cnblogs.com/fengshuihuan/p/7105545.html>`_
