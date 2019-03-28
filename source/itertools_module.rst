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

itertools模块组合迭代器
------------------------------

待补充


参考文献

- `itertools — Functions creating iterators for efficient looping <https://docs.python.org/3.7/library/itertools.html>`_
- `Python itertools模块详解 <https://www.cnblogs.com/fengshuihuan/p/7105545.html>`_
