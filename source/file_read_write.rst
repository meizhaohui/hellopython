.. _file_read_write:

文件的读写
======================

.. contents:: 目录

文件读写内置方法open
----------------------
- 使用内置方法 ``<built-in function open>`` 对文件进行读写。

常用方法如下::

    >>> file_object=open('sys.txt','r')
    >>> file_object.
    file_object.buffer         file_object.encoding       file_object.isatty(        file_object.newlines       file_object.readlines(     file_object.truncate(
    file_object.close(         file_object.errors         file_object.line_buffering file_object.read(          file_object.seek(          file_object.writable(
    file_object.closed         file_object.fileno(        file_object.mode           file_object.readable(      file_object.seekable(      file_object.write(
    file_object.detach(        file_object.flush(         file_object.name           file_object.readline(      file_object.tell(          file_object.writelines(

    >>> file_object
    <_io.TextIOWrapper name='sys.txt' mode='r' encoding='cp936'>
    >>> file_object.buffer      # 文件缓存
    <_io.BufferedReader name='sys.txt'>
    >>> file_object.encoding    # 文件的编码
    'cp936'
    >>> file_object.errors      # 读取文件错误时的报告级别(strict严格，ignore忽略，replace替换)
    'strict'
    >>> file_object.mode        # 读取文件的模式
    'r'
    >>> file_object.name        # 文件的名称
    'sys.txt'
    >>> file_object.readable()  # 文件对象是否可读
    True 
    >>> file_object.writable()  # 文件对象是否可写
    False
    >>> file_object.seekable()  # 文件是否支持随机访问，如果为False，则seek(), tell()和truncate()会报错
    True
    >>> file_object.isatty()    # 如果文件连接(与终端设备相关联)至tty(类似的)设备
    False                        # isatty()方法返回True，否则返回False。
    >>> file_object.close()        # 关闭文件对象
    >>> file_object.closed      # 文件是否关闭
    True
    >>> file_object.fileno()    # 返回一个整型的文件描述符(file descriptor FD 整型)
    4                            # 可用于底层操作系统的 I/O 操作。
    >>> file_object=open('sys.txt','r',1)
    >>> file_object.buffer
    <_io.BufferedReader name='sys.txt'>   
    >>> file_object.line_buffering   # 文件对象是否为以单行作为缓存
    True
    >>> file_object.tell()      # 当前文件指针在文件中位置，从文件起始算起，单位为字节
    0
    >>> file_object.seek(3,1)   # 从当前位置向后偏移3个字节报错! 
                                # 原因：
                                # 在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始计算相对位置
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    io.UnsupportedOperation: can't do nonzero cur-relative seeks
    >>> del file_object            # 将file_object对象删除
    >>> file_object=open('sys.txt','rb')  # 重新打开文件，以二进制方式打开
    >>> file_object
    <_io.BufferedReader name='sys.txt'>
    >>> file_object.readline()  # 读取一行
    b'a1\r\n'
    >>> file_object.tell()        # 当前文件指针在文件中位置，从文件起始算起，单位为字节
    4
    >>> file_object.seek(2,1)   # 从当前位置向后偏移2个字节
    6
    >>> file_object.tell()        # 获取当前位置
    6
    >>> file_object.read()        # 从当前位置开始，读取文件数据，一直到文件结尾
    b'2\r\nabc3\r\nabcd4'
    >>> file_object.seek(-2,2)  # 从文件结尾向前偏移2个字节
    18
    >>> file_object.tell()      # 获取当前位置(注：windows上的换行符\r\n算做两个字节)
    18
    >>> file_object.read()      # 从当前位置开始，读取文件数据，一直到文件结尾
    b'd4'
    >>> file_object.seek(0,0)   # 从文件开头向后偏移0个字节，即返回到文件开头
    0
    >>> file_object.tell()        # 获取当前位置
    0
    >>> file_object.readlines() # 读取文件所有内容至列表中
    [b'a1\r\n', b'ab2\r\n', b'abc3\r\n', b'abcd4']
    >>> file_object.tell()      # 当前位置已经到达文件结尾
    20
    >>> file_object.seek(-19,2) # 从文件结尾向前偏移19个字节
    1
    >>> file_object.tell()        # 获取当前位置
    1
    >>> file_object.readline()    # 读取当前行中剩余字符
    b'1\r\n'
    >>> file_object.tell()        # 获取当前位置
    4
    >>> file_object.seek(0)        # 返回到文件开头
    0
    >>> file_object.read(1)     # 读取1个字节
    b'a'
    >>> file_object.read(2)        # 读取2个字节
    b'1\r'
    >>> file_object.read(3)        # 读取3个字节
    b'\nab'
    >>> file_object.seek(0)        # 返回到文件开头
    0
    >>> file_object.readline(2)    # 读取当前行当前位置后2个字节
    b'2'
    >>> file_object.seek(0)        # 返回到文件开头
    0
    >>> file_object.tell()        # 获取当前位置
    0
    >>> file_object.readlines(2)    # 读取2个字节的行的内容
    [b'a1\r\n']
    >>> file_object.tell()            # 获取当前位置
    4
    >>> file_object.seek(0)            # 返回到文件开头
    0
    >>> file_object.readlines(3)    # 读取3个字节的行的内容
    [b'a1\r\n']
    >>> file_object.seek(0)            # 返回到文件开头
    0
    >>> file_object.tell()            # 获取当前位置
    0
    >>> file_object.readlines(5)    # 读取5个字节的行的内容，也就是两行内容    
    [b'a1\r\n', b'ab2\r\n']
    >>> file_object.tell()            # 获取当前位置
    9
    >>> file_object.seek(0)            # 返回到文件开头
    0
    >>> file_object.readlines(6)    # 读取6个字节的行的内容，也就是两行内容    
    [b'a1\r\n', b'ab2\r\n']
    >>> file_object.tell()            # 获取当前位置
    9
    >>> file_object.detach()        # 将底层缓冲区与TextIOBase分离并返回
    <_io.FileIO name='sys.txt' mode='rb' closefd=True>
    >>> file_object.seek(0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: raw stream has been detached

    >>> file_object=open('sys.txt','ab+')     # 以二进制追加的形式读取文件
    >>> string1=b'\r\nabcde5'                # 创建二进制字符串string1
    >>> string1
    b'\r\nabcde5'
    >>> file_object.write(string1)            # 将二进制字符串string1写入到文件对象中
    8
    >>> file_object.flush()                    # 刷新缓存区，将数据写入到文件里
    >>> file_object.tell()                    # 获取当前位置
    28
    >>> file_object.seek(0)                    # 返回到文件开头
    0
    >>> file_object.readlines()                # 读取所有行的内容
    [b'a1\r\n', b'ab2\r\n', b'abc3\r\n', b'abcd4\r\n', b'abcde5']
    >>> list1=[b'abcdef6',b'abcdefg7']
    >>> list1
    [b'abcdef6', b'abcdefg7'] 
    >>> file_object.writelines(list1)         # 将二进制列表list1写入到文件对象中
    >>> file_object.flush()                    # 刷新缓存区，将数据写入到文件里
    >>> file_object.seek(0)                    # 返回到文件开头
    0
    >>> file_object.readlines()                # 读取所有行的内容，由于list1中未加换行符，导致都追加到最后一行了
    [b'a1\r\n', b'ab2\r\n', b'abc3\r\n', b'abcd4\r\n', b'abcde5abcdef6abcdefg7']
    >>> file_object.seek(28,0)                # 返回到追加之前的位置
    28
    >>> file_object.tell()
    28
    >>> file_object.read()                    # 查看是否到达正确的位置，后面的数据都是刚才追加的
    b'abcdef6abcdefg7'
    >>> file_object.tell()
    43
    >>> file_object.seek(0,0)                # 返回到文件开头
    0
    >>> file_object.seek(28,0)                # 返回到追加之前的位置
    28
    >>> file_object.truncate()                # 从当前位置截断文件
    28
    >>> file_object.flush()                    # 刷新缓存区，将数据写入到文件里，也就是删除了刚才追加的数据
    >>> file_object.seek(0)                    # 返回到文件开头
    0
    >>> file_object.readlines()                # 读取所有行的内容
    [b'a1\r\n', b'ab2\r\n', b'abc3\r\n', b'abcd4\r\n', b'abcde5']
    >>> list1=[b'\r\nabcdef6',b'\r\nabcdefg7']    # 重新定义列表list1，添加换行符
    >>> list1
    [b'\r\nabcdef6', b'\r\nabcdefg7']
    >>> file_object.readlines()
    []
    >>> file_object.writelines(list1)        # 将列表list1写入到文件对象中
    >>> file_object.flush()                    # 刷新缓存区，将数据写入到文件里
    >>> file_object.seek(0)                    # 返回到文件开头
    0
    >>> file_object.readlines()                # 读取所有行的内容
    [b'a1\r\n', b'ab2\r\n', b'abc3\r\n', b'abcd4\r\n', b'abcde5\r\n', b'abcdef6\r\n', b'abcdefg7']
    >>> file_object.close()                    # 关闭文件对象
    >>> file_object.closed                    # 判断文件对象是否关闭
    True

注意： ``readlines()`` 读取所有行的内容至内存中，内存占用率过高； ``readline()`` 每次读取一行，对于大文件需要综合考虑做出取舍。
    
文件的读写模式
----------------------

文件的读写模式::

    "文件的读写"中已经讲解了当文件打开后，可以对文件进行的一些读写操作。本节讲解文件的读写模式。
    使用open函数打开一个文件，并返回一个file文件对象。
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise IOError upon failure.
    [打开文件并返回一个文件对象流，失败时则会引发IOError错误]
    The available modes are:
    [有效的模式有以下几种:]
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)  
              [以只读模式打开文件，文件指针位于文件开头，为默认模式，文件不存在时，并不会新建文件，不可写]
    'w'       open for writing, truncating the file first
              [以只写模式打开文件，文件存在则清空文件内容(在打开时就被清空)，不存在则创建(慎用)，不可读]
    'x'       create a new file and open it for writing
              [x模式与w模式类似，以只写模式打开文件，只是如果文件存在时会报FileExistsError错误，不可读]
    'a'       open for writing, appending to the end of the file if it exists
              [以追加写模式打开文件，如果文件存在则在文件结尾开始追加写(不论当前指针位置在哪，都是在文件最后进行追加)，不可读]
    'b'       binary mode
              [二进制模式，返回的是二进制对象]    
    't'       text mode (default)
              [文本模式(默认以文本模式打开)，返回的是字符串对象]
    '+'       open a disk file for updating (reading and writing)
              [同时可读可写，不能单独使用，必须与rwax一起作用，文件存在与否不去考虑]
    
    不同模式打开文件的列表：
    r：以只读的方式打开文件，文件的指针将会放在文件的开头，为默认模式
    rb：以二进制格式打开一个文件用于只读，文件指针会在文件的开头
    r+：打开一个文件用于读写，文件指针将会在文件的开头(写入数据时，会将原始数据覆盖掉)
    rb+：以二进制格式打开一个文件用于读写，文件指针会放在文件的开头

    w：打开一个文件用于写入，如果该文件已存在则将会覆盖文件，如果不存在则创建新文件
    wb：以二进制打开一个文件用于写入
    w+：打开一个文件用于读写
    wb+：以二进制格式打开一个文件用于读写，如果文件存在则覆盖，如果不存在则创建新文件

    a：打开一个文件用于追加内容，如果文件已存在，文件指针会放在文件的结尾，如果不存在则创建新文件进行写入
    ab：以二进制格式打开一个文件用于追加写入
    a+：打开一个文件用于读写，如果该文件已存在，文件指针会放在结尾，文件打开时会是追加模式，该文件不存在则创建新文件(即使指针不在结尾，也会在结尾进行添加数据)
    ab+：以二进制格式打开一个文件用于追加。
    
    test1.txt文件内容如下：
    abc
    def
    ghi
    >>> file1=open('test1.txt')
    >>> file1.readlines()
    ['abc\n', 'def\n', 'ghi']
    >>> string1='jkl'
    >>> file1.write(string1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    io.UnsupportedOperation: not writable
    >>> file1.writable()
    False
    >>> file1.mode
    'r'
    >>> file1.close()
        
根据打开的模式不同，open() 返回的文件对象类型也不同::

    TextIOWrapper：文本模式，返回TextIOWrapper对象。
    BufferedReader：读二进制，即rb，返回BufferedReader对象。
    BufferedWriter：写和追加二进制，即wb、ab，返回BufferedWriter对象。
    BufferedRandom：读/写二进制模式，即含有b+的模式，返回BufferedRandom对象。
    >>> file1=open('test1.txt','r')
    >>> type(file1)
    <class '_io.TextIOWrapper'>
    >>> file2=open('test2.txt','w')
    >>> type(file2)
    <class '_io.TextIOWrapper'>
    >>> file3=open('test3.txt','a+')
    >>> type(file3)
    <class '_io.TextIOWrapper'>
    >>> file4=open('test4.txt','rb')
    >>> type(file4)
    <class '_io.BufferedReader'>
    >>> file5=open('test5.txt','wb')
    >>> type(file5)
    <class '_io.BufferedWriter'>
    >>> file6=open('test6.txt','ab')
    >>> type(file6)
    <class '_io.BufferedWriter'>
    >>> file7=open('test7.txt','ab+')
    >>> type(file7)
    <class '_io.BufferedRandom'>
    >>> file8=open('test8.txt','xb+')
    >>> type(file8)
    <class '_io.BufferedRandom'>

with上下文管理器的使用
------------------------

使用with...open方式打开文件::
    
    # 使用with...open方式打开文件，不用考虑再去关闭文件
    with open('D:\\test1.txt',mode='a+',encoding='utf-8') as file1:
        print(file1)
        print(file1.tell())
        file1.seek(0)
        for line in file1.readlines():
            print(line)
            

对于一些特殊类型的文件，可以使用相应的模块进行读取。如 ``json`` 模块可以读取json文件， ``logging`` 模块读取日志文件， ``xml.etree.ElementTree`` 读取xml文件， ``csv`` 模块读取CSV文件， ``ConfigParser`` 模块读取配置文件等。

csv模块
------------------------

csv模块的方法或属性::

    In [1]: import csv                                                              
    
    In [2]: csv. 
           Dialect              excel                list_dialects()      QUOTE_NONNUMERIC     Sniffer              writer()            
           DictReader           excel_tab            QUOTE_ALL            re                   StringIO                                 
           DictWriter           field_size_limit()   QUOTE_MINIMAL        reader()             unix_dialect                             
           Error                get_dialect()        QUOTE_NONE           register_dialect()   unregister_dialect()                        
