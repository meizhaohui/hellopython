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

使用 ``with...open`` 方式打开文件::
    
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

- csv模块实现了以csv格式读取和写入表格数据的类。
- csv模块可以读取EXCEL数据和写入数据到EXCEL文件。
- csv模块 ``read`` 和 ``writer`` 对象可以写读序列。
- csv模块 ``DictReader`` 和 ``DictWriter`` 类可以读写字典形式的数据。
- csvwriter_object.writerows(rows)将rows对象的所有元素写入文件，相当于一次写入多行到文件。
- csvwriter_object.writerow(row)将row参数的元素写入文件，相当于写入一行到文件。
- csvwriter_object.writeheader()将构建方法中定义的字段名称写入到文件中作为CSV文件的表头。
- csv.reader(csvfile)读取csv文件数据。
- 使用reader()和write()的默认操作中，每一列使用逗号分开，每一行使用换行符分开。
- csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', \*args, \*\*kwds)以字典作为元素时，可以指定 ``fieldnames`` 参数，表明字典中字段的名称， ``fieldnames`` 为sequence序列，``restkey`` 参数表示当指定的字段数少于csv文件的列数时剩余的数据的列名， ``restval`` 参数表示当指定的字段数多于csv文件的列名数时，多出的字段自动插入的值。
- csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', \*args, \*\*kwds)将字典列表写入到CSV文件中，``fieldnames`` sequuence序列必须指定, ``restval`` 参数用于当指定的字段数多于字典列表的键总数时自动填充的值， ``extrasaction`` 参数用于指定当字典列表的键总数超过 ``fieldnames`` 定义的字段总数时的行为，默认引发 ``ValueError`` 异常,也可以指定为 ``extrasaction='ignore'`` 表示忽略字典中的额外值。 

csv模块的方法或属性::

    In [1]: import csv                                                              
    
    In [2]: csv. 
           Dialect              excel                list_dialects()      QUOTE_NONNUMERIC     Sniffer              writer()            
           DictReader           excel_tab            QUOTE_ALL            re                   StringIO                                 
           DictWriter           field_size_limit()   QUOTE_MINIMAL        reader()             unix_dialect                             
           Error                get_dialect()        QUOTE_NONE           register_dialect()   unregister_dialect()                        

示例1,写入列表数据到csv文件中:

.. code-block:: python
   :linenos:
   :emphasize-lines: 18,19

    In [1]: import csv
    
    In [2]: CSV_DATA = [
       ...:     ['id', 'username', 'age', 'country'],
       ...:     ['1001', 'Stephen Curry', '30', 'USA'],
       ...:     ['1002', 'Kobe Bryant', '40', 'USA'],
       ...:     ['1003', 'Manu Ginóbili', '41', 'Argentina']
       ...:     ]
    
    In [3]: CSV_DATA
    Out[3]:
    [['id', 'username', 'age', 'country'],
     ['1001', 'Stephen Curry', '30', 'USA'],
     ['1002', 'Kobe Bryant', '40', 'USA'],
     ['1003', 'Manu Ginóbili', '41', 'Argentina']]
    
    In [4]: with open('file.csv', 'wt') as fout:
       ...:     csvwriter_object = csv.writer(fout)
       ...:     csvwriter_object.writerows(CSV_DATA)
       ...:

    In [5]: csvwriter_object  
    Out[5]: <_csv.writer at 0x7fd479b0b258>

查看文件file.csv数据::

    [meizhaohui@localhost ~]$ cat file.csv
    id,username,age,country
    1001,Stephen Curry,30,USA
    1002,Kobe Bryant,40,USA
    1003,Manu Ginóbili,41,Argentina
    
示例2, 读取csv文件数据:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2

    In [6]: with open('file.csv', 'rt') as fin:
       ...:     csvreader_object = csv.reader(fin)
       ...:     data = [row for row in csvreader_object]
       ...:
    
    In [7]: csvreader_object
    Out[7]: <_csv.reader at 0x7fd479b013c8>
    
    In [8]: data
    Out[8]:
    [['id', 'username', 'age', 'country'],
     ['1001', 'Stephen Curry', '30', 'USA'],
     ['1002', 'Kobe Bryant', '40', 'USA'],
     ['1003', 'Manu Ginóbili', '41', 'Argentina']]

示例3,将csv数据读取后保存为字典为元素的列表:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2

    In [9]: with open('file.csv', 'rt') as fin:
       ...:     dictreader_object = csv.DictReader(fin)
       ...:     data_dict_list = [row for row in dictreader_object]
       ...:
    
    In [10]: dictreader_object
    Out[10]: <csv.DictReader at 0x7fd479ac7208>
    
    In [11]: data_dict_list
    Out[11]:
    [{'age': '30', 'country': 'USA', 'id': '1001', 'username': 'Stephen Curry'},
     {'age': '40', 'country': 'USA', 'id': '1002', 'username': 'Kobe Bryant'},
     {'age': '41',
      'country': 'Argentina',
      'id': '1003',
      'username': 'Manu Ginóbili'}]

说明： 此例中，因为没有在csv.DictReader(fin)中指定 ``fieldnames`` ，csv模块会自动读取第一行作为字段名称。


示例4，指定 ``fieldnames`` 字段名称:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2

    In [12]: with open('file.csv', 'rt') as fin:
        ...:     dictreader_object1 = csv.DictReader(fin, fieldnames=['first','second','third','fouth'])
        ...:     data_dict_list1 = [row for row in dictreader_object1]
        ...:
    
    In [13]: dictreader_object1
    Out[13]: <csv.DictReader at 0x7fd479c1a358>
    
    In [14]: data_dict_list1
    Out[14]:
    [{'first': 'id', 'fouth': 'country', 'second': 'username', 'third': 'age'},
     {'first': '1001', 'fouth': 'USA', 'second': 'Stephen Curry', 'third': '30'},
     {'first': '1002', 'fouth': 'USA', 'second': 'Kobe Bryant', 'third': '40'},
     {'first': '1003',
      'fouth': 'Argentina',
      'second': 'Manu Ginóbili',
      'third': '41'}]

说明：由于指定了 ``fieldnames`` 字段名称，csv文件中第一行就当做了普通的数据行，不作为表头数据。

示例5，指定 ``fieldnames`` 字段名称,但指定的字段数少于csv文件中的列数:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2

    In [15]: with open('file.csv', 'rt') as fin:
        ...:     dictreader_object2 = csv.DictReader(fin, fieldnames=['first','second'])
        ...:     data_dict_list2 = [row for row in dictreader_object2]
        ...:
    
    In [16]: dictreader_object2
    Out[16]: <csv.DictReader at 0x7fd47834ea58>
    
    In [17]: data_dict_list2
    Out[17]:
    [{None: ['age', 'country'], 'first': 'id', 'second': 'username'},
     {None: ['30', 'USA'], 'first': '1001', 'second': 'Stephen Curry'},
     {None: ['40', 'USA'], 'first': '1002', 'second': 'Kobe Bryant'},
     {None: ['41', 'Argentina'], 'first': '1003', 'second': 'Manu Ginóbili'}]

说明:此种情况会将csv多出的数据保存在列表中，并使用 ``restkey`` 指定的字段名(默认为None)进行存储，如果非空行的字段数少于字段名，则公缺少的值填入None。由于我们并未指定 ``restkey`` 值，因此除了'first'和'second'字段名外，还有一个None字段名。

示例6，指定 ``fieldnames`` 字段名称,但指定的字段数少于csv文件中的列数,但指定 ``restkey`` 值:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2
    
    In [18]: with open('file.csv', 'rt') as fin:
        ...:     dictreader_object3 = csv.DictReader(fin, fieldnames=['first','second'], restkey='other')
        ...:     data_dict_list3 = [row for row in dictreader_object3]
        ...:
    
    In [19]: dictreader_object3
    Out[19]: <csv.DictReader at 0x7fd479acae10>
    
    In [20]: data_dict_list3
    Out[20]:
    [{'first': 'id', 'other': ['age', 'country'], 'second': 'username'},
     {'first': '1001', 'other': ['30', 'USA'], 'second': 'Stephen Curry'},
     {'first': '1002', 'other': ['40', 'USA'], 'second': 'Kobe Bryant'},
     {'first': '1003', 'other': ['41', 'Argentina'], 'second': 'Manu Ginóbili'}]

说明: 此时因为指定了 ``restkey`` 参数值为'other',因此输出数据中以'first','second','other'作为字典的键。

示例7，指定 ``fieldnames`` 字段名称,但指定的字段数多于csv文件中的列数:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2

    In [21]: with open('file.csv', 'rt') as fin:
        ...:     dictreader_object4 = csv.DictReader(fin, fieldnames=['first','second','third','fouth','fifth'])
        ...:     data_dict_list4 = [row for row in dictreader_object4]
        ...:
    
    In [22]: data_dict_list4
    Out[22]:
    [{'fifth': None,
      'first': 'id',
      'fouth': 'country',
      'second': 'username',
      'third': 'age'},
     {'fifth': None,
      'first': '1001',
      'fouth': 'USA',
      'second': 'Stephen Curry',
      'third': '30'},
     {'fifth': None,
      'first': '1002',
      'fouth': 'USA',
      'second': 'Kobe Bryant',
      'third': '40'},
     {'fifth': None,
      'first': '1003',
      'fouth': 'Argentina',
      'second': 'Manu Ginóbili',
      'third': '41'}]

说明:由于指定了5个字段名，而csv文件中只的4列，因此第5个字段'fifth'会被自动指定值为None。

示例8，指定 ``fieldnames`` 字段名称,但指定的字段数多于csv文件中的列数,并指定 ``restval`` 参数:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2

    In [23]: with open('file.csv', 'rt') as fin: 
        ...:     dictreader_object5 = csv.DictReader(fin, fieldnames=['first','second','third','fouth','fifth'], restval='autoinsert') 
        ...:     data_dict_list5 = [row for row in dictreader_object5] 
        ...:
    
    In [24]: data_dict_list5                                                                                                               
    Out[24]: 
    [{'fifth': 'autoinsert',
      'first': 'id',
      'fouth': 'country',
      'second': 'username',
      'third': 'age'},
     {'fifth': 'autoinsert',
      'first': '1001',
      'fouth': 'USA',
      'second': 'Stephen Curry',
      'third': '30'},
     {'fifth': 'autoinsert',
      'first': '1002',
      'fouth': 'USA',
      'second': 'Kobe Bryant',
      'third': '40'},
     {'fifth': 'autoinsert',
      'first': '1003',
      'fouth': 'Argentina',
      'second': 'Manu Ginóbili',
      'third': '41'}]


说明:由于指定了5个字段名，并且指定了 ``restval`` 参数为'autoinsert',而csv文件中只的4列，因此第5个字段'fifth'会被自动指定值为'autoinsert'值。

示例9, 使用DictWriter()重写CSV文件:

.. code-block:: python
   :linenos:
   :emphasize-lines: 11,12

    In [25]: data_dict_list                                                                                                                
    Out[25]: 
    [{'age': '30', 'country': 'USA', 'id': '1001', 'username': 'Stephen Curry'},
     {'age': '40', 'country': 'USA', 'id': '1002', 'username': 'Kobe Bryant'},
     {'age': '41',
      'country': 'Argentina',
      'id': '1003',
      'username': 'Manu Ginóbili'}]
    
    In [26]: with open('other.csv','wt') as fout: 
        ...:     dictwriter_object = csv.DictWriter(fout, fieldnames=('id','username','age','country')) 
        ...:     dictwriter_object.writerows(data_dict_list) 
        ...:  

查看other.csv文件的内容::

    [meizhaohui@localhost ~]$ cat other.csv 
    1001,Stephen Curry,30,USA
    1002,Kobe Bryant,40,USA
    1003,Manu Ginóbili,41,Argentina

说明：发现此时只是将数据写入，但没有写入表头数据。


示例10, 使用DictWriter()重写CSV文件,并使用 ``dictwriter_object.writeheader()``  写入表头数据:

.. code-block:: python
   :linenos:
   :emphasize-lines: 11,12

    In [27]: data_dict_list
    Out[27]:
    [{'age': '30', 'country': 'USA', 'id': '1001', 'username': 'Stephen Curry'},
     {'age': '40', 'country': 'USA', 'id': '1002', 'username': 'Kobe Bryant'},
     {'age': '41',
      'country': 'Argentina',
      'id': '1003',
      'username': 'Manu Ginóbili'}]
    
    In [28]: with open('other.csv','wt') as fout:
        ...:     dictwriter_object = csv.DictWriter(fout, fieldnames=('id','username','age','country'))
        ...:     dictwriter_object.writeheader()
        ...:     dictwriter_object.writerows(data_dict_list)
        ...:


查看other.csv文件的内容::

    [meizhaohui@localhost ~]$ cat other.csv
    id,username,age,country
    1001,Stephen Curry,30,USA
    1002,Kobe Bryant,40,USA
    1003,Manu Ginóbili,41,Argentina

示例11, 使用DictWriter()重写CSV文件,并使用 ``dictwriter_object.writeheader()``  写入表头数据,但 ``fieldnames`` 仅指定'id'和'username'两个字段，此时会引发异常:

.. code-block:: python
   :linenos:
   :emphasize-lines: 17

    In [29]: data_dict_list                                                                                                                
    Out[29]: 
    [{'age': '30', 'country': 'USA', 'id': '1001', 'username': 'Stephen Curry'},
     {'age': '40', 'country': 'USA', 'id': '1002', 'username': 'Kobe Bryant'},
     {'age': '41',
      'country': 'Argentina',
      'id': '1003',
      'username': 'Manu Ginóbili'}]
    
    In [30]: with open('other.csv','wt') as fout: 
        ...:     dictwriter_object = csv.DictWriter(fout, fieldnames=('id','username')) 
        ...:     dictwriter_object.writeheader() 
        ...:     dictwriter_object.writerows(data_dict_list) 
        ...:                                                                                                                               
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    ValueError: dict contains fields not in fieldnames: 'age', 'country'
    
说明：由于没有指定 ``extrasaction`` 参数，默认 ``extrasaction='raise'``,此时data_dict_list传递给dictwriter_object对象时，找不到'age'和'country'健对应的字段名称，因此会引发 ``ValueError`` 异常。下面示例指定 ``extrasaction`` 参数。


示例12, 使用DictWriter()重写CSV文件,并使用 ``dictwriter_object.writeheader()``  写入表头数据,但 ``fieldnames`` 仅指定'id'和'username'两个字段，并指定 ``extrasaction='ignore'`` 参数:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2

    In [31]: with open('other.csv','wt') as fout: 
        ...:     dictwriter_object = csv.DictWriter(fout, fieldnames=('id','username'),extrasaction='ignore') 
        ...:     dictwriter_object.writeheader() 
        ...:     dictwriter_object.writerows(data_dict_list) 
        ...:                                                     

    In [32]: dictwriter_object
    Out[32]: <csv.DictWriter at 0x7fd4798bd668>

查看other.csv文件的内容::

    meizhaohui@localhost ~]$ cat other.csv
    id,username
    1001,Stephen Curry
    1002,Kobe Bryant
    1003,Manu Ginóbili

说明：通过指定 ``extrasaction='ignore'`` 参数，可以写入与字典列表长度不一致的字段数据到CSV文件中。

示例12, 使用DictWriter()重写CSV文件,并使用 ``dictwriter_object.writeheader()``  写入表头数据,但 ``fieldnames`` 指定的字段数超过字典列表中的字段总数:

.. code-block:: python
   :linenos:
   :emphasize-lines: 11

    In [33]: data_dict_list
    Out[33]:
    [{'age': '30', 'country': 'USA', 'id': '1001', 'username': 'Stephen Curry'},
     {'age': '40', 'country': 'USA', 'id': '1002', 'username': 'Kobe Bryant'},
     {'age': '41',
      'country': 'Argentina',
      'id': '1003',
      'username': 'Manu Ginóbili'}]
    
    In [34]: with open('other.csv','wt') as fout:
        ...:     dictwriter_object = csv.DictWriter(fout, fieldnames=('id','username','age','country','number'))
        ...:     dictwriter_object.writeheader()
        ...:     dictwriter_object.writerows(data_dict_list)
        ...:
    
    In [35]: dictwriter_object
    Out[35]: <csv.DictWriter at 0x7fd479b064a8>

查看other.csv文件的内容::

    [meizhaohui@localhost ~]$ cat other.csv 
    id,username,age,country,number
    1001,Stephen Curry,30,USA,
    1002,Kobe Bryant,40,USA,
    1003,Manu Ginóbili,41,Argentina,

说明：此时多出了'number'字段，但'number'字段没有数据。

示例13, 使用DictWriter()重写CSV文件,并使用 ``dictwriter_object.writeheader()``  写入表头数据,但 ``fieldnames`` 指定的字段数超过字典列表中的字段总数,并指定 ``restval`` 参数。

.. code-block:: python
   :linenos:
   :emphasize-lines: 11

    In [36]: data_dict_list
    Out[36]:
    [{'age': '30', 'country': 'USA', 'id': '1001', 'username': 'Stephen Curry'},
     {'age': '40', 'country': 'USA', 'id': '1002', 'username': 'Kobe Bryant'},
     {'age': '41',
      'country': 'Argentina',
      'id': '1003',
      'username': 'Manu Ginóbili'}]
    
    In [37]: with open('other.csv','wt') as fout:
        ...:     dictwriter_object = csv.DictWriter(fout, fieldnames=('id','username','age','country','number'), restval='autoinsert')
        ...:     dictwriter_object.writeheader()
        ...:     dictwriter_object.writerows(data_dict_list)
        ...:
    
    In [38]: dictwriter_object
    Out[38]: <csv.DictWriter at 0x7fd479ad9240>

查看other.csv文件的内容::

    [meizhaohui@localhost ~]$ cat other.csv
    id,username,age,country,number
    1001,Stephen Curry,30,USA,autoinsert
    1002,Kobe Bryant,40,USA,autoinsert
    1003,Manu Ginóbili,41,Argentina,autoinsert


说明：此时多出了'number'字段，且'number'字段被填充了'autoinsert'数据。


csv格式化相当麻烦，看以下示例。

示例14, 设置CSV输出格式：

.. code-block:: python
   :linenos:
   :emphasize-lines: 9

    In [39]: CSV_DATA
    Out[39]:
    [['id', 'username', 'age', 'country'],
     ['1001', 'Stephen Curry', '30', 'USA'],
     ['1002', 'Kobe Bryant', '40', 'USA'],
     ['1003', 'Manu Ginóbili', '41', 'Argentina']]
    
    In [40]: with open('format.csv', 'wt') as fout:
        ...:     writer_object = csv.writer(fout, delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        ...:     writer_object.writerows(CSV_DATA)
        ...:

查看format.csv文件内容::

    [meizhaohui@localhost ~]$ cat format.csv
    id username age country
    1001 |Stephen Curry| 30 USA
    1002 |Kobe Bryant| 40 USA
    1003 |Manu Ginóbili| 41 Argentina

示例15, 设置CSV输出格式：

.. code-block:: python
   :linenos:
   :emphasize-lines: 2

    In [41]: with open('format.csv', 'wt') as fout: 
        ...:     writer_object = csv.writer(fout, delimiter=' ',quotechar='"',quoting=csv.QUOTE_MINIMAL) 
        ...:     writer_object.writerows(CSV_DATA) 
        ...:   

查看format.csv文件内容::

    [meizhaohui@localhost ~]$ cat format.csv
    id username age country
    1001 "Stephen Curry" 30 USA
    1002 "Kobe Bryant" 40 USA
    1003 "Manu Ginóbili" 41 Argentina

为了便于指定输入和输出记录的格式，将特定格式参数组合成 ``dialect`` ,在创建 ``reader`` 和 ``writer`` 对象时，可以指定 ``dialect`` 参数，这些参数名称与下面的 ``Dialect`` 类定义的属性相同。


``Dialect`` 类支持以下属性:

- ``Dialect.delimiter`` 用于分隔字段的单字符字符串。默认为','。
- ``Dialect.lineterminator`` 用于指示 ``writer`` 生成的行的结尾符，默认是'\\r\\n'。
- ``Dialect.quotechar`` 单字符，用于表示引用包含特殊字符的字段，例如字段中包含有 ``delimiter`` 或 ``quotechar`` 或 换行符，默认是双引号'"'。
- ``Dialect.quoting`` 控制何时使用引号，可以采用 ``QUOTE_MINIMAL`` 或 ``QUOTE_NONNUMERIC`` 或 ``QUOTE_NONE`` 或 ``QUOTE_ALL``，默认是 ``QUOTE_MINIMAL`` 。

  - ``QUOTE_MINIMAL`` 表示 ``writer`` 对象仅引用包含特殊字符的字段，例如 ``delimiter`` , ``quotechar`` 或 ``lineterminator`` 中的任何字符。
  - ``QUOTE_NONNUMERIC`` 表示 ``writer`` 对象仅引用引用所有非数字字段。
  - ``QUOTE_NONE`` 表示 ``writer`` 对象永远不引用字段，当输出数据中包含 ``delimiter`` 分隔符字符时，使用 ``Dialect.escapechar`` 转义，如果未指定 ``Dialect.escapechar`` ，则在遇到需要转义的字符时，则会引起 ``Error`` 异常。 
  - ``QUOTE_ALL`` 表示 ``writer`` 对象仅引用所有的字段。

- ``Dialect.skipinitialspace`` 如果是 ``True`` ，则分隔符后面的whitespace被忽略，默认是 ``False`` 。
- ``Dialect.escapechar`` 表示 ``writer`` 对象碰到 ``delimiter`` 时的转义字符，如果 ``Dialect.quoting`` 设置为 ``QUOTE_NONE``,如果 ``doublequote`` 设置为 ``False`` ，则为 ``quotechar``。
- ``Dialect.doublequote`` 控制如何引用字段中出现的 ``quotechar`` 实例。 如果为 ``True`` ，则字符加倍。 如果为 ``False`` ，则 ``escapechar`` 将用作 ``quotechar``  的前缀。 默认为 ``True`` 。

示例16，使用|作为分隔符，且使用双引号'"'引用所有的字段:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2

    In [42]: with open('format.csv', 'wt') as fout:
        ...:     writer_object = csv.writer(fout, delimiter='|',quotechar='"',quoting=csv.QUOTE_ALL)
        ...:     writer_object.writerows(CSV_DATA)
        ...:

查看format.csv文件内容::

    [meizhaohui@localhost ~]$ cat format.csv 
    "id"|"username"|"age"|"country"
    "1001"|"Stephen Curry"|"30"|"USA"
    "1002"|"Kobe Bryant"|"40"|"USA"
    "1003"|"Manu Ginóbili"|"41"|"Argentina"

- 使用 ``writer_object.writerow(data)`` 写入单行数据到CSV文件。

示例17，使用|作为分隔符，且使用双引号'"'引用非数字的字段:

.. code-block:: python
   :linenos:
   :emphasize-lines: 6

    In [43]: first_line = ('a','b','c', 1, 2)                                                                
    
    In [44]: second_line = [',','"','|','line2']                                                             
    
    In [45]: with open('format.csv', 'wt') as fout: 
        ...:     writer_object = csv.writer(fout, delimiter='|',quotechar='"',quoting=csv.QUOTE_NONNUMERIC) 
        ...:     writer_object.writerow(first_line) 
        ...:     writer_object.writerow(second_line) 
        ...:     

查看format.csv文件内容::

    [meizhaohui@localhost ~]$ cat format.csv 
    "a"|"b"|"c"|1|2
    ","|""""|"|"|"line2"

说明：第二行中因为有字段中的字符是双引号，与quotechar字符相同，因此根据Dialect.doublequote的定义，需要两个quotechar引用“。

其他的参数选项，可以参考上面介绍的 ``Dialect`` 进行自行测试。

XML文件的读写
----------------------

- XML是一种标记(markup)格式，它使用标签(tag)分隔数据。
- XML通常用于数据传送和消息。
- XML包含的元素类型，标签<tag>。
- XML包含的元素类型，属性<tag name="attribute">。
- XML包含的元素类型，数据<tag>data</tag>。
- 在Python中解析XML最简单的方法是使用 ``xml.etree.ElementTree`` 模块。

``xml.etree.ElementTree`` 解析XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们将使用以下XML文档(country_data.xml)作为本节的示例数据:

.. code-block:: xml
   :linenos:

    <?xml version="1.0"?>
    <data>
        <country name="Liechtenstein">
            <rank>1</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor name="Austria" direction="E"/>
            <neighbor name="Switzerland" direction="W"/>
        </country>
        <country name="Singapore">
            <rank>4</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor name="Malaysia" direction="N"/>
        </country>
        <country name="Panama">
            <rank>68</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <neighbor name="Costa Rica" direction="W"/>
            <neighbor name="Colombia" direction="E"/>
        </country>
    </data>

- ElementTree将整个XML文档表示为树，Element表示此树中的单个节点。
- 从XML文件中读取XML数据，用 ``ET.parse('file.xml')`` 解析xml文件，获取xml树，用 ``tree.getroot()`` 获取根节点，根节点是一个 ``Element`` 对象。

从文件中读取XML数据::

    In [1]: import xml.etree.ElementTree as ET                                      
    
    In [2]: tree = ET.parse('country_data.xml')                                     
    
    In [3]: root = tree.getroot()                                                   
    
    In [4]: tree                                                                    
    Out[4]: <xml.etree.ElementTree.ElementTree at 0x7f932cc24d30>
    
    In [5]: root                                                                    
    Out[5]: <Element 'data' at 0x7f932e653818>

从字符串变量中读取XML数据::

    In [6]: xml_string="""<?xml version="1.0"?>
       ...: <data>test</data>
       ...: """
    
    In [7]: test_root = ET.fromstring(xml_string)
    
    In [8]: test_root
    Out[8]: <Element 'data' at 0x7f932eb034a8>

- 访问对象的标签 ``tag = element.tag``
- 访问对象的属性 ``attrib = element.attrib``
- 访问对象的值 ``value = element.text``

访问根节点标签,属性和值::

    In [9]: root.tag                                                               
    Out[9]: 'data'
    
    In [10]: root.attrib                                                            
    Out[10]: {}
    
    In [11]: root.text                                                              
    Out[11]: '\n    '

打印根节点的子节点的标签，属性::

    In [12]: for child in root:
        ...:     print(child.tag, child.attrib)
        ...:
    country {'name': 'Liechtenstein'}
    country {'name': 'Singapore'}
    country {'name': 'Panama'}

当子节点是嵌套时，我们可以通过索引方式访问子节点::

    In [13]: root[0]
    Out[13]: <Element 'country' at 0x7f932e653868>
    
    In [14]: root[0].tag
    Out[14]: 'country'
    
    In [15]: root[0].attrib
    Out[15]: {'name': 'Liechtenstein'}
    
    In [16]: root[0][1].tag
    Out[16]: 'year'
    
    In [17]: root[0][1].text
    Out[17]: '2008'

- 查找节点元素,迭代子元素， ``iter(tag=None)`` 显示tag标签及其下所有子标签。
- 查找节点元素， ``findall(match)`` 查找直接子元素中匹配match的节点。
- 查找节点元素， ``find(match)`` 查找直接子元素中第一个匹配match的节点。

迭代子元素::

    In [18]: for neighbor in root.iter('neighbor'):
        ...:     print(neighbor.attrib)
        ...:
    {'direction': 'E', 'name': 'Austria'}
    {'direction': 'W', 'name': 'Switzerland'}
    {'direction': 'N', 'name': 'Malaysia'}
    {'direction': 'W', 'name': 'Costa Rica'}
    {'direction': 'E', 'name': 'Colombia'}

findall或find查找子元素::

    In [19]: for country in root.findall('country'):
        ...:     rank = country.find('rank').text
        ...:     name = country.get('name')
        ...:     print('name:{},rank:{}'.format(name, rank))
        ...:
    name:Liechtenstein,rank:1
    name:Singapore,rank:4
    name:Panama,rank:68

    In [20]: root.findall('country')     
    Out[20]: 
    [<Element 'country' at 0x7f932e653868>,
     <Element 'country' at 0x7f932cc2bf48>,
     <Element 'country' at 0x7f932cc2b818>]
    
    In [21]: root.findall('rank')
    Out[21]: []
    
    In [22]: root.findall('neighbor')
    Out[22]: []
    
    In [23]: root[0].findall('neighbor')
    Out[23]:
    [<Element 'neighbor' at 0x7f932cc2bbd8>,
     <Element 'neighbor' at 0x7f932cc2b9f8>]
    
    In [24]: root[0].find('neighbor')
    Out[24]: <Element 'neighbor' at 0x7f932cc2bbd8>
    
    In [25]: root[0].find('neighbor').get('name')
    Out[25]: 'Austria'
    # 说明：使用find匹配只能配置到第一个'neighbor',不能匹配到名称为'Switzerland'的子节点

    In [26]: root[0].findall('neighbor')[0].get('name')
    Out[26]: 'Austria'
    
    In [27]: root[0].findall('neighbor')[1].get('name')
    Out[27]: 'Switzerland'

- ``ElementTree.write()`` 将更新后的XML数据写入到文件。
- 可以直接通过操作Element对象来修改节点元素的标签，属性等。
- ``element.text = new_value`` 给节点赋新值。
- ``element.set('attribute_name', 'attribute_value')`` 设置节点属性。
- ``element.append(subelement)`` 给节点增加子节点。

修改节点::

    In [39]: for rank in root.iter('rank'): 
        ...:     new_rank = int(rank.text) + 1 
        ...:     rank.text = str(new_rank) 
        ...:     rank.set('updated', 'yes') 
        ...:   

    In [40]: tree.write('output.xml')       

新的output.xml文件内容如下:

.. code-block:: xml
   :linenos:
   :emphasize-lines: 3,10,16

    <data>
        <country name="Liechtenstein">
            <rank updated="yes">2</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor direction="E" name="Austria" />
            <neighbor direction="W" name="Switzerland" />
        </country>
        <country name="Singapore">
            <rank updated="yes">5</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor direction="N" name="Malaysia" />
        </country>
        <country name="Panama">
            <rank updated="yes">69</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <neighbor direction="W" name="Costa Rica" />
            <neighbor direction="E" name="Colombia" />
        </country>
    </data>

可以发现第3,10,16行的rank节点已经修改成功。但输出文件中并没有 ``<?xml version="1.0"?>`` XML的版本声明。

- ``tree.write('output.xml',encoding='utf-8',xml_declaration=True)`` 声明XML的版本为1.0，并指定用XML传递数据的时候的字符编码为utf-8。

增加XML的版本声明，并设置编码格式::

   In [41]: tree.write('output.xml',encoding='utf-8',xml_declaration=True)

再查看output.xml文件的内容:

.. code-block:: xml
   :linenos:
   :emphasize-lines: 1,4,11,17

    <?xml version='1.0' encoding='utf-8'?>
    <data>
        <country name="Liechtenstein">
            <rank updated="yes">2</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor direction="E" name="Austria" />
            <neighbor direction="W" name="Switzerland" />
        </country>
        <country name="Singapore">
            <rank updated="yes">5</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor direction="N" name="Malaysia" />
        </country>
        <country name="Panama">
            <rank updated="yes">69</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <neighbor direction="W" name="Costa Rica" />
            <neighbor direction="E" name="Colombia" />
        </country>
    </data>

- 使用 ``Element.remove(subelement)`` 移除子节点。

删除rank大于50的所有国家的数据::

    In [42]: for country in root.findall('country'): 
       ...:     rank = int(country.find('rank').text) 
       ...:     print('rank:{}'.format(rank)) 
       ...:     if rank > 50: 
       ...:         root.remove(country) 
       ...:                                                                         
    rank:2
    rank:5
    rank:69
    
    In [43]: tree.write('output.xml',encoding='utf-8',xml_declaration=True)  

再查看output.xml文件的内容:

.. code-block:: xml
   :linenos:

    <?xml version='1.0' encoding='utf-8'?>
    <data>
        <country name="Liechtenstein">
            <rank updated="yes">2</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor direction="E" name="Austria" />
            <neighbor direction="W" name="Switzerland" />
        </country>
        <country name="Singapore">
            <rank updated="yes">5</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor direction="N" name="Malaysia" />
        </country>
        </data>

说明：虽然数据正常的写入到文件中，但最后的</data>标签缩进不正常，并没有与前面的<data>标签对齐。

- 使用 ``ET.SubElement((parent, tag, attrib={}, \*\*extra)`` 创建子节点Element对象。
- 使用 ``ET.dump(element)`` 将一个Element对象打印到标准输出。这个函数只用来调试（一般不把结果打印到标准输出）。

新增country子节点::

    In [44]: new_country = ET.SubElement(root, 'country', attrib={'name': 'Panama'}, other='other
        ...: _attribute')                                                                        
    
    In [45]: new_country                                                                         
    Out[45]: <Element 'country' at 0x7fecb2e51908>
    
    In [46]: ET.dump(root)                                                                       
    <data>
        <country name="Liechtenstein">
            <rank updated="yes">2</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor direction="E" name="Austria" />
            <neighbor direction="W" name="Switzerland" />
        </country>
        <country name="Singapore">
            <rank updated="yes">5</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor direction="N" name="Malaysia" />
        </country>
        <country name="Panama" other="other_attribute" /></data>

- ``element.append(subelement)`` 给节点增加子节点。

给刚才新增的country节点增加rank子节点，并指定rank节点的'updated'属性::

    In [47]: country_rank = ET.Element('rank', attrib={'updated': 'yes'})  

    In [48]: new_country.append(country_rank) 

    In [49]: ET.dump(root)

    <data>
        <country name="Liechtenstein">
            <rank updated="yes">2</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor direction="E" name="Austria" />
            <neighbor direction="W" name="Switzerland" />
        </country>
        <country name="Singapore">
            <rank updated="yes">5</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor direction="N" name="Malaysia" />
        </country>
        <country name="Panama" other="other_attribute"><rank updated="yes" /></country></data>
    
    In [50]: tree.write('output.xml',encoding='utf-8',xml_declaration=True)

再查看output.xml文件的内容:

.. code-block:: xml
   :linenos:

    <?xml version='1.0' encoding='utf-8'?>
    <data>
        <country name="Liechtenstein">
            <rank updated="yes">2</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor direction="E" name="Austria" />
            <neighbor direction="W" name="Switzerland" />
        </country>
        <country name="Singapore">
            <rank updated="yes">5</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor direction="N" name="Malaysia" />
        </country>
        <country name="Panama" other="other_attribute"><rank updated="yes" /></country></data>

- 解析带名称空间(namespace)的XML文件。

  - 名称空间是为了解决名称冲突而诞生的，将一个很长的可以保证全局唯一性的字符串与tag标签关联起来，就可以避免命名冲突。可以使用 ``统一资源标识符(Uniform Resource Identifier, URI)`` 来标识名称空间。最普通的URL是 ``统一资源定位符(Uniform Resource Locator, URL)`` ,URL用于标识网络主机的地址。
  - 用来标识名称空间的网络地址URL并不被XML解析器调用，XML解析器不需要从这个URL中查找信息，该URL的作用仅仅是给名称空间一个唯一的名字，因此这个网络地址可以是虚构的。很多公司经常把这个网络地址指向一个真实的WEB页面，这个地址包含了关于当前名称空间更详细的信息。
  - 定义一个默认的XML名称空间使得我们在子元素的开始不需要使用前缀，定义格式： ``<element xmlns="default_namespace_URI"`` 。
  - 非默认的名称空间时，需要指定名称前缀namespace-prefix,带有前缀形式的标签和属性 ``prefix:sometag`` 将扩展为 ``{uri}sometag`` ,前缀由完整的URI替代。定义格式： ``<element xmlns:namespace-prefix="namespace_URL"`` 。

下面的存储有演员及其扮演的角色信息的XML文件(actors.xml)包含两种名称空间，一种是默认的名称空间，另一种是前缀为"fictional"的名称空间:
    
.. code-block:: xml
   :linenos:

    <?xml version="1.0"?>
    <actors xmlns:fictional="http://characters.example.com"
            xmlns="http://people.example.com">
        <actor>
            <name>John Cleese</name>
            <fictional:character>Lancelot</fictional:character>
            <fictional:character>Archie Leach</fictional:character>
        </actor>
        <actor>
            <name>Eric Idle</name>
            <fictional:character>Sir Robin</fictional:character>
            <fictional:character>Gunther</fictional:character>
            <fictional:character>Commander Clement</fictional:character>
        </actor>
    </actors>

解析actors.xml文件，并尝试使用findall方法获取actor节点数据::

    In [50]: import xml.etree.ElementTree as ET
    
    In [51]: tree = ET.parse('actors.xml')
    
    In [52]: actors_root = tree.getroot()
    
    In [53]: actors_root
    Out[53]: <Element '{http://people.example.com}actors' at 0x7fafe2880138>
    
    In [54]: actors_root.findall('actor')
    Out[54]: []

    In [55]: ET.dump(actors_root)                                                          
    <ns0:actors xmlns:ns0="http://people.example.com" xmlns:ns1="http://characters.example.com">
        <ns0:actor>
            <ns0:name>John Cleese</ns0:name>
            <ns1:character>Lancelot</ns1:character>
            <ns1:character>Archie Leach</ns1:character>
        </ns0:actor>
        <ns0:actor>
            <ns0:name>Eric Idle</ns0:name>
            <ns1:character>Sir Robin</ns1:character>
            <ns1:character>Gunther</ns1:character>
            <ns1:character>Commander Clement</ns1:character>
        </ns0:actor>
    </ns0:actors>
    
    In [56]: actors_root.tag
    Out[56]: '{http://people.example.com}actors'


说明：直接使用findall并没有获取到actor节点数据。在各标签前已经自动加上了前缀

第一种方式是在使用findall()或find()时手动加上{URI}到每一个标签或属性的xpath上面::

    In [57]: default_prefix = '{http://people.example.com}'                         
    
    In [58]: char_prefix = '{http://characters.example.com}'                        
    
    In [59]: for actor in actors_root.findall('{}actor'.format(default_prefix)): 
        ...:     name = actor.find('{}name'.format(default_prefix)) 
        ...:     print(name.text) 
        ...:     for char in actor.findall('{}character'.format(char_prefix)): 
        ...:         print(' |-->', char.text) 
        ...:                                                                        
    John Cleese
     |--> Lancelot
     |--> Archie Leach
    Eric Idle
     |--> Sir Robin
     |--> Gunther
     |--> Commander Clement

另一种方式是为搜索名称空间前缀创建一个字典，并在搜索功能中使用字典::

    In [60]: ns = {'real_person': 'http://people.example.com','role': 'http://characters.example.com'}
    
    In [61]: ns
    Out[61]:
    {'real_person': 'http://people.example.com',
     'role': 'http://characters.example.com'}
    
    In [62]: for actor in actors_root.findall('real_person:actor', namespaces=ns):
        ...:     name = actor.find('real_person:name', ns)
        ...:     print(name.text)
        ...:     for char in actor.findall('role:character', ns):
        ...:         print(' |-->', char.text)
        ...:
    John Cleese
     |--> Lancelot
     |--> Archie Leach
    Eric Idle
     |--> Sir Robin
     |--> Gunther
     |--> Commander Clement

- XPath支持， ``xml.etree.ElementTree`` 模块对XPath表达式支持比较有限，便于在树中定位元素，完整的XPath引擎超出了模块的范围。

XPath语法如下:

+------------------------+--------------------------------------+
|        语法            |               解释                   |
+========================+======================================+
|        tag             |  选中符合给定tag标签的全部Element元素|
+------------------------+--------------------------------------+
|        \*              | 星号，选中全部子Element元素          +
+------------------------+--------------------------------------+
|        \.              |  点号，选中当前Element元素           |
+------------------------+--------------------------------------+
|        //              | 选中同一级别的全部子Element元素      |
+------------------------+--------------------------------------+
|        \.\.            | 双点号，选中父节点Element元素        |
+------------------------+--------------------------------------+
|        [@attrib]       | 选中所有具有attrib属性节点Element元素|
+------------------------+--------------------------------------+


XPath的使用示例:

.. code-block:: python
   :linenos:
   :emphasize-lines: 18,24,37,43,52,65

    In [63]: ET.dump(root)                                                                       
    <data>
        <country name="Liechtenstein">
            <rank updated="yes">2</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor direction="E" name="Austria" />
            <neighbor direction="W" name="Switzerland" />
        </country>
        <country name="Singapore">
            <rank updated="yes">5</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor direction="N" name="Malaysia" />
        </country>
        <country name="Panama" other="other_attribute"><rank updated="yes" /></country></data>
    
    In [64]: root.findall(".")   # XPath中使用.点号搜索                                                                
    Out[64]: [<Element 'data' at 0x7fecb1819188>]
    
    In [65]: root.findall(".")[0].tag                                                            
    Out[65]: 'data'

    In [66]: root.findall("./country/neighbor")  # XPath使用点号和tag方式搜索
    Out[66]: 
    [<Element 'neighbor' at 0x7fecb1819278>,
     <Element 'neighbor' at 0x7fecb1819048>,
     <Element 'neighbor' at 0x7fecb1819408>]
    
    In [67]: for neighbor in root.findall("./country/neighbor"): 
        ...:     print(neighbor.get('name')) 
        ...:                                                                                     
    Austria
    Switzerland
    Malaysia

    In [68]: root.findall("./*")  # XPath使用点号和星号搜索所有root的子节点 
    Out[68]: 
    [<Element 'country' at 0x7fecb1819368>,
     <Element 'country' at 0x7fecb18190e8>,
     <Element 'country' at 0x7fecb2e51908>]

    In [69]: root.findall("*/year")  # XPath使用星号搜索所有year节点                      
    Out[69]: [<Element 'year' at 0x7fecb1819458>, <Element 'year' at 0x7fecb18193b8>]
    
    In [70]: for year in root.findall("*/year"): 
        ...:     print(year.text) 
        ...:                                                                                     
    2008
    2011

    In [71]: root.findall(".//rank") # 使用XPath点号和//语法，选中所有rank节点 
    Out[71]: 
    [<Element 'rank' at 0x7fecb1819138>,
     <Element 'rank' at 0x7fecb1819228>,
     <Element 'rank' at 0x7fecb185e6d8>]
    
    In [72]: for rank in root.findall(".//rank"): 
        ...:     print(rank.text) 
        ...:                                                                                     
    2
    5
    None

    In [73]: root.findall("./country/rank/..")  # 使用XPath点号，tag标签以及双点号查找父节点
    Out[73]:
    [<Element 'country' at 0x7fecb1819368>,
     <Element 'country' at 0x7fecb18190e8>,
     <Element 'country' at 0x7fecb2e51908>]


``xml.sax`` 解析XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``xml.dom`` 解析XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

参考：

- `csv — CSV File Reading and Writing <https://docs.python.org/3.6/library/csv.html>`_
- `xml.etree.ElementTree — The ElementTree XML API <https://docs.python.org/3/library/xml.etree.elementtree.html>`_
- `xml.sax — Support for SAX2 parsers <https://docs.python.org/3/library/xml.sax.html>`_
- `xml.dom — The Document Object Model API <https://docs.python.org/3/library/xml.dom.html>`_
- `Python XML操作 <https://www.cnblogs.com/AlwinXu/p/5483177.html>`_
