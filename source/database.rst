.. _database:

数据库处理
============================================

.. contents:: 目录

sqlite3处理SQLite数据库
--------------------------------------------

安装SQLite，请参照 `SQLite 安装 <http://www.runoob.com/sqlite/sqlite-installation.html>`_ 。

安装完成后将SQLite安装路径加入到环境变量Path中。

在命令行打开sqlite3，并查看帮助信息::

    $ sqlite3                                                                          
    SQLite version 3.27.2 2019-02-25 16:06:06                                          
    Enter ".help" for usage hints.                                                     
    Connected to a transient in-memory database.                                       
    Use ".open FILENAME" to reopen on a persistent database.                           
    sqlite> .help                                                                      
    .archive ...             Manage SQL archives                                       
    .auth ON|OFF             Show authorizer callbacks                                 
    .backup ?DB? FILE        Backup DB (default "main") to FILE                        
    .bail on|off             Stop after hitting an error.  Default OFF                 
    .binary on|off           Turn binary output on or off.  Default OFF                
    .cd DIRECTORY            Change the working directory to DIRECTORY                 
    .changes on|off          Show number of rows changed by SQL                        
    .check GLOB              Fail if output since .testcase does not match             
    .clone NEWDB             Clone data into NEWDB from the existing database          
    .databases               List names and files of attached databases                
    .dbconfig ?op? ?val?     List or change sqlite3_db_config() options                
    .dbinfo ?DB?             Show status information about the database                
    .dump ?TABLE? ...        Render all database content as SQL                        
    .echo on|off             Turn command echo on or off                               
    .eqp on|off|full|...     Enable or disable automatic EXPLAIN QUERY PLAN            
    .excel                   Display the output of next command in a spreadsheet       
    .exit ?CODE?             Exit this program with return-code CODE                   
    .expert                  EXPERIMENTAL. Suggest indexes for specified queries       
    .fullschema ?--indent?   Show schema and the content of sqlite_stat tables         
    .headers on|off          Turn display of headers on or off                         
    .help ?-all? ?PATTERN?   Show help text for PATTERN                                
    .import FILE TABLE       Import data from FILE into TABLE                          
    .imposter INDEX TABLE    Create imposter table TABLE on index INDEX                
    .indexes ?TABLE?         Show names of indexes                                     
    .limit ?LIMIT? ?VAL?     Display or change the value of an SQLITE_LIMIT            
    .lint OPTIONS            Report potential schema issues.                           
    .load FILE ?ENTRY?       Load an extension library                                 
    .log FILE|off            Turn logging on or off.  FILE can be stderr/stdout        
    .mode MODE ?TABLE?       Set output mode                                           
    .nullvalue STRING        Use STRING in place of NULL values                        
    .once (-e|-x|FILE)       Output for the next SQL command only to FILE              
    .open ?OPTIONS? ?FILE?   Close existing database and reopen FILE                   
    .output ?FILE?           Send output to FILE or stdout if FILE is omitted          
    .print STRING...         Print literal STRING                                      
    .progress N              Invoke progress handler after every N opcodes             
    .prompt MAIN CONTINUE    Replace the standard prompts                              
    .quit                    Exit this program                                         
    .read FILE               Read input from FILE                                      
    .restore ?DB? FILE       Restore content of DB (default "main") from FILE          
    .save FILE               Write in-memory database into FILE                        
    .scanstats on|off        Turn sqlite3_stmt_scanstatus() metrics on or off          
    .schema ?PATTERN?        Show the CREATE statements matching PATTERN               
    .selftest ?OPTIONS?      Run tests defined in the SELFTEST table                   
    .separator COL ?ROW?     Change the column and row separators                      
    .sha3sum ...             Compute a SHA3 hash of database content                   
    .shell CMD ARGS...       Run CMD ARGS... in a system shell                         
    .show                    Show the current values for various settings              
    .stats ?on|off?          Show stats or turn stats on or off                        
    .system CMD ARGS...      Run CMD ARGS... in a system shell                         
    .tables ?TABLE?          List names of tables matching LIKE pattern TABLE          
    .testcase NAME           Begin redirecting output to 'testcase-out.txt'            
    .timeout MS              Try opening locked tables for MS milliseconds             
    .timer on|off            Turn SQL timer on or off                                  
    .trace ?OPTIONS?         Output each SQL statement as it is run                    
    .vfsinfo ?AUX?           Information about the top-level VFS                       
    .vfslist                 List all available VFSes                                  
    .vfsname ?AUX?           Print the name of the VFS stack                           
    .width NUM1 NUM2 ...     Set column widths for "column" mode                       
    sqlite>                                                                            

- ``sqlite3.connect(database)`` 连接数据库

连接数据库database，如果数据库database不存在，则会创建数据库database，并返回Connection object::

    In [1]: import sqlite3                             
                                                       
    In [2]: conn = sqlite3.connect('data.db')          
                                                       
    In [3]: conn                                       
    Out[3]: <sqlite3.Connection at 0x230e4801e30>      

同时也发现生成了文件data.db。

也可以在内存中创建数据库::

    In [4]: conn_mem = sqlite3.connect(':memory:')

    In [5]: conn_mem
    Out[5]: <sqlite3.Connection at 0x230e4a84e30>
    
- ``sqlite3.cursor()`` 创建游标对象
    
一旦建立了Connection连接，就可以创建一个Cursor对象::

    In [6]: curs = conn.cursor()

    In [7]: curs
    Out[7]: <sqlite3.Cursor at 0x230e4b39340>
    
- ``sqlite3.Cursor.execute(sql[, parameters])`` 执行SQL语句
    
通过调用Cursor对象的execute()方法来执行SQL命令::
    
    # 创建数据表stocks
    In [8]: curs.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
    Out[8]: <sqlite3.Cursor at 0x230e4b39340>

    # 插入一条数据到表stocks中
    In [9]: curs.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    Out[9]: <sqlite3.Cursor at 0x230e4b39340>

- ``sqlite3.Connection.commit(sql[, parameters])``  提交当前的事务

将创建数据表stocks和插入数据事务提交到数据库::

    In [10]: conn.commit()

此时数据库中就新建了表stocks，并有一条数据，查询数据库里面的信息::

    $ sqlite3 data.db                                                  
    SQLite version 3.27.2 2019-02-25 16:06:06                              
    Enter ".help" for usage hints.                                         
    sqlite> .header on                                                     
    sqlite> .mode column                                                   
    sqlite> .tables                                                        
    stocks                                                                 
    sqlite> select * from stocks;                                          
    date        trans       symbol      qty         price                  
    ----------  ----------  ----------  ----------  ----------             
    2006-01-05  BUY         RHAT        100.0       35.14                  
    sqlite>                                                                
    
- ``sqlite3.Connection.close()``  关闭数据库连接，在关闭数据库连接前，请确保所有的事务都被commit()提交，close()不会自动调用commit()提交事务

关闭数据库连接，可以发现在关闭数据库连接后，再去执行execute去查询数据库信息会报 ``ProgrammingError`` 异常:

.. code-block:: python
    :linenos:
    :emphasize-lines: 15
   
    In [11]: conn.close()

    In [12]: conn
    Out[12]: <sqlite3.Connection at 0x230e4801e30>

    In [13]: curs
    Out[13]: <sqlite3.Cursor at 0x230e4b39340>

    In [14]: curs.execute("SELECT * FROM stocks")
    ---------------------------------------------------------------------------
    ProgrammingError                          Traceback (most recent call last)
    <ipython-input-14-9a842a1f84e1> in <module>
    ----> 1 curs.execute("SELECT * FROM stocks")

    ProgrammingError: Cannot operate on a closed database.
    
重新连接数据库::

    In [15]: conn = sqlite3.connect('data.db')                                                                              
                                                                                                                            
    In [16]: curs = conn.cursor()                                                                                           
 
为防止数据库注入攻击，不要使用Python字符串操作::

    # Never do this -- insecure!   这种方式不安全
    In [17]: symbol = 'RHAT'                                                                                                
    
    # ``SELECT`` 查询语句
    In [18]: curs.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)                                              
    Out[18]: <sqlite3.Cursor at 0x230e4b392d0>                                                                              

- ``sqlite3.Cursor.fetchone()`` 获取查询结果集中的下一行数据，没有数据的话返回None

查询一行数据::

    In [19]: print(curs.fetchone())                                                                                         
    ('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)                                                                             
  
应该使用?问号作为占位符，并使用tuple元组作为第二个参数::

    # Do this instead   使用元组以及?问号占位符
    In [20]: t = ('RHAT',)                                                                                                  
                                                                                                                            
    In [21]: curs.execute('SELECT * FROM stocks WHERE symbol=?', t)                                                         
    Out[21]: <sqlite3.Cursor at 0x230e4b392d0>                                                                              
                                                                                                                            
    In [22]: print(curs.fetchone())                                                                                         
    ('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)                                                                             
    
    # Larger example that inserts many records at a time
    In [23]: purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00), ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00), ('2006-04-06', 'SELL', 'IBM', 500, 53.00),]                                                                              

- ``sqlite3.Cursor.executemany(sql, seq_of_parameters)`` 对seq_of_parameters中的所有参数进行映射生成SQL语句，并执行SQL命令

将purchases中的数据映射到 ``INSERT`` 插入语句中::

    In [24]: curs.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)                                           
    Out[24]: <sqlite3.Cursor at 0x230e4b392d0>                                                                              
                                                                                                                            
    In [25]: curs.execute('SELECT * FROM stocks')                                                                           
    Out[25]: <sqlite3.Cursor at 0x230e4b392d0>                                                                              
     
- ``sqlite3.Cursor.fetchone()`` 获取查询结果集中的下一行数据，没有数据的话返回 ``None``

查询一行数据::
     
    In [26]: print(curs.fetchone())                                                                                         
    ('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)                                                                             

- ``sqlite3.Cursor.fetchall()`` 获取查询结果集中所有（剩余）的行，返回一个列表，没有数据的话返回 ``None``

查询剩余行的数据::
    
    In [27]: print(curs.fetchall())                                                                                         
    [('2006-03-28', 'BUY', 'IBM', 1000.0, 45.0), ('2006-04-05', 'BUY', 'MSFT', 1000.0, 72.0), ('2006-04-06', 'SELL', 'IBM', 500.0, 53.0)]
    
- 要在执行SELECT语句后检索数据，可以将游标视为 ``iterator`` 迭代器，调用游标的 ``fetchone()`` 方法以检索单个匹配行，或调用 ``fetchall()`` 以获取所有匹配行的列表。

下面将游标作为一个 ``iterator`` 迭代器::

    In [28]: for row in curs.execute('SELECT * FROM stocks ORDER BY price'):
        ...:     print(row)
        ...:
    ('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)
    ('2006-03-28', 'BUY', 'IBM', 1000.0, 45.0)
    ('2006-04-06', 'SELL', 'IBM', 500.0, 53.0)
    ('2006-04-05', 'BUY', 'MSFT', 1000.0, 72.0)
    
提交事务，将新插入的三行数据保存到数据库中::

    In [29]: conn.commit()
    
- ``sqlite3.Connection.total_changes``  返回自打开数据库连接以来已修改，插入或删除的数据库行的总数。

查询插入的数据行数::

    In [30]: conn.total_changes
    Out[30]: 3

在SQLite3中查询数据::

    sqlite> select * from stocks order by price;                       
    date        trans       symbol      qty         price              
    ----------  ----------  ----------  ----------  ----------         
    2006-01-05  BUY         RHAT        100.0       35.14              
    2006-03-28  BUY         IBM         1000.0      45.0               
    2006-04-06  SELL        IBM         500.0       53.0               
    2006-04-05  BUY         MSFT        1000.0      72.0               
    sqlite>                                                            
    
- ``sqlite3.Cursor.executescript(sql_script)`` 将SQL语句写成脚本，并执行脚本，会直接COMMIT提交事务。它首先发出一个COMMIT语句，然后执行它作为参数获取的SQL脚本。

以下脚本先创建person表和book表，并向book表中插入一条数据::

    In [31]: curs.executescript("""
        ...:     create table person(
        ...:         firstname,
        ...:         lastname,
        ...:         age
        ...:     );
        ...:
        ...:     create table book(
        ...:         title,
        ...:         author,
        ...:         published
        ...:     );
        ...:
        ...:     insert into book(title, author, published)
        ...:     values (
        ...:         'Dirk Gently''s Holistic Detective Agency',
        ...:         'Douglas Adams',
        ...:         1987
        ...:     );
        ...:     """)
    Out[31]: <sqlite3.Cursor at 0x230e4b392d0>

在SQLite3中查询数据::

    sqlite> .tables                                                          
    book    person  stocks                                                   
    sqlite> select * from book;                                              
    title                                    author         published        
    ---------------------------------------  -------------  ----------       
    Dirk Gently's Holistic Detective Agency  Douglas Adams  1987             
    sqlite>                                                                  
    
说明执行 ``curs.executescript(sql_script)`` 脚本不需要另外手动提交事务。

- Connection objects可以用作自动提交或回滚事务的 ``with`` 上下文管理器。 如果发生异常，则回滚事务; 否则，提交事务成功

使用 ``with`` 上下文管理器，自动提交事务::

    In [1]: import sqlite3

    In [2]: auto_conn = sqlite3.connect(":memory:")
    
    # 定义firstname unique唯一不能重复
    In [3]: auto_conn.execute("create table person (id integer primary key, firstname varchar unique)")
    Out[3]: <sqlite3.Cursor at 0x1ea33f65650>
    
    # 第一次自动提交事务，并插入数据到数据库中
    In [4]: with auto_conn:
       ...:     auto_conn.execute("insert into person(firstname) values (?)", ("Joe",))
       ...:

    In [5]: curs = auto_conn.cursor()

    In [6]: curs.execute('select * from person')
    Out[6]: <sqlite3.Cursor at 0x1ea33f65c00>
    
    # 查询刚才的with上下文是否插入数据
    In [7]: curs.fetchone()
    Out[7]: (1, 'Joe')
    
    # 再次使用上下文插入数据，会产生 ``sqlite3.IntegrityError`` 异常，使用try except捕获异常
    In [8]: try:
       ...:     with auto_conn:
       ...:         auto_conn.execute("insert into person(firstname) values (?)", ("Joe",))
       ...: except sqlite3.IntegrityError:
       ...:     print("couldn't add Joe twice")
       ...:
    couldn't add Joe twice
    
    # 关闭连接
    In [9]: auto_conn.close()

pymysql处理mysql数据库
--------------------------------------------

- 安装pymysql:  ``pip install PyMySQL==0.7.5``

- 安装MariaDB，MariaDB下载链接： https://downloads.mariadb.org/， 安装请参考 `MariaDB安装与使用 <https://www.cnblogs.com/oukele/p/9590965.html>`_

- 准备数据库数据表

创建数据库data和数据表users::

    $ mysql -uroot -proot
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 9
    Server version: 10.3.14-MariaDB mariadb.org binary distribution

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | test               |
    +--------------------+
    4 rows in set (0.001 sec)

    MariaDB [(none)]> create database data;
    Query OK, 1 row affected (0.001 sec)

    MariaDB [(none)]> show databases;         
    +--------------------+                    
    | Database           |                    
    +--------------------+                    
    | data               |                    
    | information_schema |                    
    | mysql              |                    
    | performance_schema |                    
    | test               |                    
    +--------------------+                    
    5 rows in set (0.001 sec)                 
                                              
    MariaDB [(none)]> use data;               
    Database changed

    MariaDB [data]> show tables;
    Empty set (0.001 sec)    

    MariaDB [data]> CREATE TABLE `users` (
        -> `id` int(11) NOT NULL AUTO_INCREMENT,
        -> `email` varchar(255) COLLATE utf8_bin NOT NULL,
        -> `password` varchar(255) COLLATE utf8_bin NOT NULL,
        -> PRIMARY KEY (`id`)
        -> ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
        -> AUTO_INCREMENT=1 ;
    Query OK, 0 rows affected (0.059 sec)

    MariaDB [data]> show tables;
    +----------------+
    | Tables_in_data |
    +----------------+
    | users          |
    +----------------+
    1 row in set (0.000 sec)

    MariaDB [data]> select * from users;
    Empty set (0.000 sec)    

- ``pymysql.connect`` 连接数据库

语法::

    pymysql.connections.Connection(host=None, user=None, password='', database=None, port=0, unix_socket=None, charset='', sql_mode=None, read_default_file=None, conv=None, use_unicode=None, client_flag=0, cursorclass=<class 'pymysql.cursors.Cursor'>, init_command=None, connect_timeout=10, ssl=None, read_default_group=None, compress=None, named_pipe=None, autocommit=False, db=None, passwd=None, local_infile=False, max_allowed_packet=16777216, defer_connect=False, auth_plugin_map=None, read_timeout=None, write_timeout=None, bind_address=None, binary_prefix=False, program_name=None, server_public_key=None)
    
    Parameters:	

        host – Host where the database server is located  数据库服务主机
        user – Username to log in as  登陆用户名
        password – Password to use.  登陆密码
        database – Database to use, None to not use a particular one.  数据库名称
        port – MySQL port to use, default is usually OK. (default: 3306)  端口号
        bind_address – When the client has multiple network interfaces, specify the interface from which to connect to the host. Argument can be a hostname or an IP address.
        unix_socket – Optionally, you can use a unix socket rather than TCP/IP.
        read_timeout – The timeout for reading from the connection in seconds (default: None - no timeout)
        write_timeout – The timeout for writing to the connection in seconds (default: None - no timeout)
        charset – Charset you want to use.  编码格式
        sql_mode – Default SQL_MODE to use.
        read_default_file – Specifies my.cnf file to read these parameters from under the [client] section.
        conv – Conversion dictionary to use instead of the default one. This is used to provide custom marshalling and unmarshalling of types. See converters.
        use_unicode – Whether or not to default to unicode strings. This option defaults to true for Py3k.
        client_flag – Custom flags to send to MySQL. Find potential values in constants.CLIENT.
        cursorclass – Custom cursor class to use.
        init_command – Initial SQL statement to run when connection is established.
        connect_timeout – Timeout before throwing an exception when connecting. (default: 10, min: 1, max: 31536000)
        ssl – A dict of arguments similar to mysql_ssl_set()’s parameters.
        read_default_group – Group to read from in the configuration file.
        compress – Not supported
        named_pipe – Not supported
        autocommit – Autocommit mode. None means use server default. (default: False)  自动提交事务
        local_infile – Boolean to enable the use of LOAD DATA LOCAL command. (default: False)
        max_allowed_packet – Max size of packet sent to server in bytes. (default: 16MB) Only used to limit size of “LOAD LOCAL INFILE” data packet smaller than default (16KB).
        defer_connect – Don’t explicitly connect on construction - wait for connect call. (default: False)
        auth_plugin_map – A dict of plugin names to a class that processes that plugin. The class will take the Connection object as the argument to the constructor. The class needs an authenticate method taking an authentication packet as an argument. For the dialog plugin, a prompt(echo, prompt) method can be used (if no authenticate method) for returning a string from the user. (experimental)
        server_public_key – SHA256 authentication plugin public key value. (default: None)
        db – Alias for database. (for compatibility to MySQLdb)  数据库名称
        passwd – Alias for password. (for compatibility to MySQLdb)  登陆密码
        binary_prefix – Add _binary prefix on bytes and bytearray. (default: False)


连接MariaDB服务，使用data数据库::

    In [1]: import pymysql

    In [2]: connection = pymysql.connect(host='localhost',  
       ...: user='root',
       ...: password='root',
       ...: db='data',
       ...: charset='utf8',
       ...: cursorclass=pymysql.cursors.DictCursor)

    In [3]: connection
    Out[3]: <pymysql.connections.Connection at 0x15759136518>

- ``connection.cursor(cursor=None)`` 创建游标对象
- ``connection.commit()`` 提交事务
- ``connection.close()`` 关闭连接

创建游标，并执行SQL语句::

    In [4]: try:
       ...:     with connection.cursor() as cursor:  # 创建游标
       ...:         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"  # 构建SQL插入语句
       ...:         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))  # 执行SQL语句
       ...:
       ...:     connection.commit()  # 提交事务
       ...: finally:
       ...:     connection.close()  # 关闭连接
       ...:
       
在MariaDB中查询数据::

    MariaDB [data]> select * from users;
    +----+----------------------+-------------+
    | id | email                | password    |
    +----+----------------------+-------------+
    |  1 | webmaster@python.org | very-secret |
    +----+----------------------+-------------+
    1 row in set (0.000 sec)

    MariaDB [data]>

- ``pymysql.cursors.Cursor.fetchone()``  查询一行数据

查询刚才插入的数据::

    In [5]: with connection.cursor() as cursor:
        ...:     sql = "SELECT id, password FROM  users WHERE email= %s "
        ...:     cursor.execute(sql, ('webmaster@python.org'))
        ...:     print(cursor.fetchone())
        ...:
    {'id': 1, 'password': 'very-secret'}
    
- ``connection.select_db(db)`` 修改当前正在处理的数据库
- ``pymysql.cursors.Cursor.fetchall()``  查询剩余行的所有数据

修改数据表为mysql，并查询数据库中的表::

    In [6]: connection                                                                                                     
    Out[6]: <pymysql.connections.Connection at 0x157594142e8>                                                              
                                                                                                                            
    In [7]: connection.select_db('mysql')                                                                                  
                                                                                                                            
    In [8]: cursor = connection.cursor()                                                                                   
                                                                                                                            
    In [9]: cursor.execute('show tables')                                                                                  
    Out[9]: 31                                                                                                             
                                                                                                                            
    In [10]: cursor.fetchone()
    Out[10]: ('column_stats',)

    In [11]: cursor.fetchall()
    Out[11]:
    (('columns_priv',),
     ('db',),
     ('event',),
     ('func',),
     ('general_log',),
     ('gtid_slave_pos',),
     ('help_category',),
     ('help_keyword',),
     ('help_relation',),
     ('help_topic',),
     ('host',),
     ('index_stats',),
     ('innodb_index_stats',),
     ('innodb_table_stats',),
     ('plugin',),
     ('proc',),
     ('procs_priv',),
     ('proxies_priv',),
     ('roles_mapping',),
     ('servers',),
     ('slow_log',),
     ('table_stats',),
     ('tables_priv',),
     ('time_zone',),
     ('time_zone_leap_second',),
     ('time_zone_name',),
     ('time_zone_transition',),
     ('time_zone_transition_type',),
     ('transaction_registry',),
     ('user',))

在MariaDB中查询数据::

    MariaDB [data]> use mysql;                 
    Database changed                          
    MariaDB [mysql]> show tables;             
    +---------------------------+             
    | Tables_in_mysql           |             
    +---------------------------+             
    | column_stats              |             
    | columns_priv              |             
    | db                        |             
    | event                     |             
    | func                      |             
    | general_log               |             
    | gtid_slave_pos            |             
    | help_category             |             
    | help_keyword              |             
    | help_relation             |             
    | help_topic                |             
    | host                      |             
    | index_stats               |             
    | innodb_index_stats        |             
    | innodb_table_stats        |             
    | plugin                    |             
    | proc                      |             
    | procs_priv                |             
    | proxies_priv              |             
    | roles_mapping             |             
    | servers                   |             
    | slow_log                  |             
    | table_stats               |             
    | tables_priv               |             
    | time_zone                 |             
    | time_zone_leap_second     |             
    | time_zone_name            |             
    | time_zone_transition      |             
    | time_zone_transition_type |             
    | transaction_registry      |             
    | user                      |             
    +---------------------------+             
    31 rows in set (0.001 sec)                
                                              
    MariaDB [mysql]>                          
       
SQLAlchemy ORM对象关系映射处理数据库
--------------------------------------------

- ``Object Relational Mapper``   对象关系映射，ORM将数据库中的表与面向对象语言中的类建立了一种对应关系。这样，我们要操作数据库，数据库中的表或者表中的一条记录就可以直接通过操作类或者类实例来完成。

- 查看SQLAlchemy的版本

通过  ``sqlalchemy.__version__``  查看SQLAlchemy的版本::


    In [1]: import sqlalchemy

    In [2]: sqlalchemy.__version__
    Out[2]: '1.3.2'

- 使用 ``create_engine()`` 连接数据库。
- ``echo=True`` 参数表明开启SQLAlchemy日志记录，启用后会生成所有SQL语句。
- ``create_engine()`` 的返回值是Engine的一个实例，它表示数据库的核心接口，使用不同的数据库处理模块处理的dialect最后生成的Engine实例不同。
- 当第一次使用 ``create_engine()`` 连接时，引擎实际上还没有尝试连接到数据库(Lazy Connecting懒惰连接)。只有在第一次要求它对数据库执行任务时才会连接数据库。
- 第一次调用 ``Engine.execute()`` 或 ``Engine.connect()`` 这样的方法时，Engine会建立与数据库的真实DBAPI连接，然后用于发出SQL。
- 通常不会直接使用 ``Engine`` ，而是通过使用ORM来间接使用 ``Engine`` 。

使用 ``create_engine()`` 连接数据库。以下是连接内存数据库SQLite::

    In [3]: from sqlalchemy import create_engine

    In [4]: engine = create_engine('sqlite:///:memory:', echo=True)

    In [5]: engine
    Out[5]: Engine(sqlite:///:memory:)

引擎Engine的方法和属性::

    engine.
             begin()                  dialect                  drop                     execution_options       logging_name             run_callable             transaction
             connect                  dispatch                 echo                     get_execution_options   name                     scalar                   update_execution_options
             contextual_connect       dispose                  engine                   has_table               pool                     schema_for_object        url
             create                   driver                   execute                  logger                  raw_connection           table_names

查看engine的一些属性::

    In [6]: engine.url                                                        
    Out[6]: sqlite:///:memory:                                                
                                                                           
    In [7]: engine.driver                                                     
    Out[7]: 'pysqlite'                                                        
                                                                           
    In [8]: engine.engine                                                     
    Out[8]: Engine(sqlite:///:memory:)                                        
                                                                           
    In [9]: engine.logger                                                     
    Out[9]: <sqlalchemy.log.InstanceLogger at 0x225a2ac98d0>                  
                                                                           
    In [10]: engine.name                                                      
    Out[10]: 'sqlite'                                                         
                                                                           
    In [11]: engine.logging_name                                              
                                                                           
    In [12]: engine.echo                                                      
    Out[12]: True                                                             

    In [13]: engine.pool
    Out[13]: <sqlalchemy.pool.impl.SingletonThreadPool at 0x225a2ac3eb8>

    In [14]: engine.dialect
    Out[14]: <sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite at 0x225a27b1f60>
    
- Engine是任何SQLAlchemy应用程序的起点。 它是实际数据库及其DBAPI的基础，通过 ``Pool`` 连接池和 ``Dialect`` 方言传递给SQLAlchemy应用程序，该 ``Dialect`` 方言描述了如何与特定类型的数据库/DBAPI组合进行通信。

SQLAlchemy Engine的架构如下:

.. image:: ./_static/images/sqla_engine_arch.png

- SQLAlchemy ``create_engine()`` 函数基于数据库URL(Database Url)来生成 ``Engine`` 对象，URL通常包含 ``username用户名`` ,  ``password密码`` , ``hostname主机名`` , ``database name数据库名称`` 以及用于其他配置的可选关键字参数。

数据库URL的典型形式是::

    dialect+driver://username:password@host:port/database

- dialect方言是SQLAlchemy方言的标识名称，如sqlite, mysql, postgresql, oracle,或mssql。
- driver是使用全小写字母连接到数据库的DBAPI的名称。
- URL中特殊的字符需要使用URL编码。
    
可以使用urllig模块生成字符的URL编码::

    In [1]: import urllib

    In [2]: urllib.parse.quote_plus('kx%jj5/g')
    Out[2]: 'kx%25jj5%2Fg'

MYSQL dialect方言示例::

    # default
    engine = create_engine('mysql://scott:tiger@localhost/foo')

    # mysqlclient (a maintained fork of MySQL-Python)
    engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')

    # PyMySQL
    engine = create_engine('mysql+pymysql://scott:tiger@localhost/foo')

SQlite dialect方言示例::

    # 相对路径
    # sqlite://<nohostname>/<path>
    # where <path> is relative:
    engine = create_engine('sqlite:///foo.db')

    # 绝对路径
    # Unix/Mac - 4 initial slashes in total
    engine = create_engine('sqlite:////absolute/path/to/foo.db')

    # Windows
    engine = create_engine('sqlite:///C:\\path\\to\\foo.db')

    # Windows alternative using raw string
    engine = create_engine(r'sqlite:///C:\path\to\foo.db')
    
    # 在内存中创建数据库
    engine = create_engine('sqlite://')
    engine = create_engine('sqlite:///:memory:')

其他数据库如 ``PostgreSQL`` 、 ``Oracle`` 、 ``Microsoft SQL Server`` 等请参考  `Database Urls <https://docs.sqlalchemy.org/en/13/core/engines.html?highlight=database%20url#database-urls>`_ 。

- 声明映射。使用ORM时，配置过程首先描述我们将要处理的数据库表，然后定义我们自己的类，这些类将映射到这些表。在现代SQLAlchemy中，这两个任务通常使用称为Declarative的系统一起执行，这允许我们创建包含指令的类，以描述它们将映射到的实际数据库表。
- 使用 ``declarative_base()`` 函数创建基类。

创建基类::

    >>> from sqlalchemy.ext.declarative import declarative_base    
                                                                   
    >>> Base = declarative_base()                                  
                                                                   
    >>> Base                                                       
    sqlalchemy.ext.declarative.api.Base                            

- 基于 ``Base`` 基类可以定义任意多的映射类。
- 定义映射类时，需要指定表的名称(table name)，列名(names of columns)以及数据类型(datatypes of columns)。
- 类定义时需要定义  ``__tablename__``  属性，表明表的名称。
- 类定义时需要至少一个 ``Column`` 列，用于定义表的主键，SQLAlchemy不会自动确认哪列是主键，并使用 ``primary_key=True`` 表明该字段是主键。
- ``__repr__()`` 方法是可选的(optional)，用于改善打印实例输出。
- 通过声明系统构建的映射类定义的有关表的信息，称为表元数据。
- 映射类是一个 ``Table对象`` ，可以通过检查 ``__table__`` 属性来看到这个对象。

定义一个User类，并映射到user表中去::

    >>> from sqlalchemy import Column, Integer, String

    >>> class User(Base):
    ...     __tablename__ = 'users'
    ...
    ...     id = Column(Integer, primary_key=True)
    ...     name = Column(String)
    ...     fullname = Column(String)
    ...     nickname = Column(String)
    ...
    ...     def __repr__(self):
    ...         return "<User(name='%s', fullname='%s', nickname='%s')>" % (
    ...             self.name, self.fullname, self.nickname)
    ...

    >>> User
    __main__.User

    >>> User.__table__
    Table('users', MetaData(bind=None), Column('id', Integer(), table=<users>, primary_key=True, nullable=False), Column('name', String(), table=<users>), Column('fullname', String(), table=<users>), Column('nickname', String(), table=<users>), schema=None)

- ``Table对象`` 是一个名为 ``MetaData`` 的较大集合的成员。使用 ``Declarative`` 声明时，可以使用声明性基类的 ``.metadata`` 属性来使用此对象。
- 调用 ``MetaData.create_all()`` 方法来创建数据表。

使用 ``MetaData.create_all()`` 方法来创建数据表::

    >>> Base.metadata
    MetaData(bind=None)
    
    >>> Base.metadata.create_all(engine)
    2019-04-16 22:20:12,488 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
    2019-04-16 22:20:12,489 INFO sqlalchemy.engine.base.Engine ()
    2019-04-16 22:20:12,490 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
    2019-04-16 22:20:12,490 INFO sqlalchemy.engine.base.Engine ()
    2019-04-16 22:20:12,491 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("users")
    2019-04-16 22:20:12,492 INFO sqlalchemy.engine.base.Engine ()
    2019-04-16 22:20:12,493 INFO sqlalchemy.engine.base.Engine
    CREATE TABLE users (
            id INTEGER NOT NULL,
            name VARCHAR,
            fullname VARCHAR,
            nickname VARCHAR,
            PRIMARY KEY (id)
    )
    
    
    2019-04-16 22:20:12,494 INFO sqlalchemy.engine.base.Engine ()
    2019-04-16 22:20:12,495 INFO sqlalchemy.engine.base.Engine COMMIT
    
    >>>
    
由于在定义engine时，开启了 ``echo=True`` 功能，因此在创建表时会显示生成的日志信息。

- 实例化映射类就可以创建一个表对象。

创建User实例::

    >>> ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
    
    >>> ed_user
    <User(name='ed', fullname='Ed Jones', nickname='edsnickname')>
    
    >>> ed_user.name
    'ed'
    
    >>> ed_user.fullname
    'Ed Jones'
    
    >>> ed_user.nickname
    'edsnickname'
    
    >>> str(ed_user.id)
    'None'

虽然在构建函数中未指定id的值，但是当我们访问它时，id属性仍然会产生None值。SQLAlchemy的检测通常在首次访问时为列映射属性生成此默认值。

- 创建Session会话，通过Session处理数据库。
- 使用 ``sessionmaker`` 创建Session会话。
- 如果创建了Engine对象engine，在创建Session时可以指定Engine对象。

创建Session会话::

    >>> from sqlalchemy.orm import sessionmaker
    
    >>> Session = sessionmaker(bind=engine)
    
    >>> session = Session()
    
    >>> Session
    sessionmaker(class_='Session', bind=Engine(sqlite:///:memory:), autoflush=True, autocommit=False, expire_on_commit=True)
    
    >>> session
    <sqlalchemy.orm.session.Session at 0x12ede8477b8>

- 万一之前没有定义Engine对象engine，可以分步定义Session会话。

分步定义Session会话::

    >>> Session = sessionmaker()
    
    >>> Session.configure(bind=engine)  # once engine is available
    
    >>> session = Session()

- 将实例数据写入到Session会话中，此时Session实例处于挂起(pending)状态，尚未发起任何SQL，并且该对象尚未由数据库中的行表示。
- 在未使用  ``session.commit()`` 方法前数据不会提交到数据库。
- 使用 ``session.add(instance)`` 方法添加一条数据。
- 使用 ``session.add_all(instances)`` 方法添加多条数据。

将一条数据写入到Session会话中::

    >>> session.add(ed_user)

上面分写入1条数据。

- 使用 ``Query`` 对象查询数据。

查询数据::

    >>> our_user = session.query(User).filter_by(name='ed').first()
    2019-04-16 22:55:04,858 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2019-04-16 22:55:04,861 INFO sqlalchemy.engine.base.Engine INSERT INTO users (name, fullname, nickname) VALUES (?, ?, ?)
    2019-04-16 22:55:04,862 INFO sqlalchemy.engine.base.Engine ('ed', 'Ed Jones', 'eddie')
    2019-04-16 22:55:04,863 INFO sqlalchemy.engine.base.Engine INSERT INTO users (name, fullname, nickname) VALUES (?, ?, ?)
    2019-04-16 22:55:04,864 INFO sqlalchemy.engine.base.Engine ('wendy', 'Wendy Williams', 'windy')
    2019-04-16 22:55:04,866 INFO sqlalchemy.engine.base.Engine INSERT INTO users (name, fullname, nickname) VALUES (?, ?, ?)
    2019-04-16 22:55:04,867 INFO sqlalchemy.engine.base.Engine ('mary', 'Mary Contrary', 'mary')
    2019-04-16 22:55:04,868 INFO sqlalchemy.engine.base.Engine INSERT INTO users (name, fullname, nickname) VALUES (?, ?, ?)
    2019-04-16 22:55:04,870 INFO sqlalchemy.engine.base.Engine ('fred', 'Fred Flintstone', 'freddy')
    2019-04-16 22:55:04,872 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name = ?
     LIMIT ? OFFSET ?
    2019-04-16 22:55:04,872 INFO sqlalchemy.engine.base.Engine ('ed', 1, 0)

    >>> our_user
    <User(name='ed', fullname='Ed Jones', nickname='eddie')>

    >>> ed_user is our_user
    True
    
- 使用 ``session.new`` 获取挂起的数据。
- 使用 ``session.dirty`` 获取脏数据。

获取挂起数据或脏数据::

    >>> session.dirty
    IdentitySet([])

    >>> session.new
    IdentitySet([])

再添加多条数据::

    >>> session.add_all([
    ...      User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    ...      User(name='mary', fullname='Mary Contrary', nickname='mary'),
    ...      User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

上面写入3条数据。

再获取挂起数据或脏数据::

    >>> session.dirty
    IdentitySet([])

    >>> session.new
    IdentitySet([<User(name='wendy', fullname='Wendy Williams', nickname='windy')>, <User(name='mary', fullname='Mary Contrary', nickname='mary')>, <User(name='fred', fullname='Fred Flintstone', nickname='freddy')>])

修改Ed’s nickname::

    >>> ed_user.nickname = 'eddie'

再获取挂起数据或脏数据::

    >>> session.dirty
    IdentitySet([<User(name='ed', fullname='Ed Jones', nickname='eddie')>])

    >>> session.new
    IdentitySet([<User(name='wendy', fullname='Wendy Williams', nickname='windy')>, <User(name='mary', fullname='Mary Contrary', nickname='mary')>, <User(name='fred', fullname='Fred Flintstone', nickname='freddy')>])
    



- 使用  ``session.commit()`` 方法将数据提交到数据库。

提交数据，并查询数据::

    >>> session.commit()
    2019-04-17 20:04:58,364 INFO sqlalchemy.engine.base.Engine UPDATE users SET nickname=? WHERE users.id = ?
    2019-04-17 20:04:58,365 INFO sqlalchemy.engine.base.Engine ('eddie', 1)
    2019-04-17 20:04:58,365 INFO sqlalchemy.engine.base.Engine INSERT INTO users (name, fullname, nickname) VALUES (?, ?, ?)
    2019-04-17 20:04:58,365 INFO sqlalchemy.engine.base.Engine ('wendy', 'Wendy Williams', 'windy')
    2019-04-17 20:04:58,365 INFO sqlalchemy.engine.base.Engine INSERT INTO users (name, fullname, nickname) VALUES (?, ?, ?)
    2019-04-17 20:04:58,365 INFO sqlalchemy.engine.base.Engine ('mary', 'Mary Contrary', 'mary')
    2019-04-17 20:04:58,366 INFO sqlalchemy.engine.base.Engine INSERT INTO users (name, fullname, nickname) VALUES (?, ?, ?)
    2019-04-17 20:04:58,367 INFO sqlalchemy.engine.base.Engine ('fred', 'Fred Flintstone', 'freddy')
    2019-04-17 20:04:58,367 INFO sqlalchemy.engine.base.Engine COMMIT
    
    >>> ed_user.id
    2019-04-16 22:58:59,226 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2019-04-16 22:58:59,227 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.id = ?
    2019-04-16 22:58:59,227 INFO sqlalchemy.engine.base.Engine (1,)
    1
    
- 查询数据库数据信息
- 通过 ``Session`` 的 ``query()`` 方法创建一个 ``Query`` 对象。
- ``Query`` 对象的常用方法见示例，详细可参考官网 `Query API <https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query>`_

查询users表中的name和fullname相关的数据::

    >>> users = session.query(User.name, User.fullname)

    >>> users
    <sqlalchemy.orm.query.Query at 0x17a37ee4048>

    >>> users.column_descriptions  # 返回有关此Query将返回的列的元数据
    [{'name': 'name',
      'type': String(),
      'aliased': False,
      'expr': <sqlalchemy.orm.attributes.InstrumentedAttribute at 0x17a37ddb570>,
      'entity': __main__.User},
     {'name': 'fullname',
      'type': String(),
      'aliased': False,
      'expr': <sqlalchemy.orm.attributes.InstrumentedAttribute at 0x17a37ddb620>,
      'entity': __main__.User}]
      
    >>> users.count()   # 返回此Query将返回的行数
    2019-04-18 20:55:52,252 INFO sqlalchemy.engine.base.Engine SELECT count(*) AS count_1
    FROM (SELECT users.name AS users_name, users.fullname AS users_fullname
    FROM users) AS anon_1
    2019-04-18 20:55:52,252 INFO sqlalchemy.engine.base.Engine ()
    4

    >>> users.all()  # 查询所有的数据
    2019-04-18 20:56:30,732 INFO sqlalchemy.engine.base.Engine SELECT users.name AS users_name, users.fullname AS users_fullname
    FROM users
    2019-04-18 20:56:30,733 INFO sqlalchemy.engine.base.Engine ()
    [('ed', 'Ed Jones'),
     ('wendy', 'Wendy Williams'),
     ('mary', 'Mary Contrary'),
     ('fred', 'Fred Flintstone')]
     
    >>> users.first()  # 返回第一个查询结果
    2019-04-18 21:00:58,964 INFO sqlalchemy.engine.base.Engine SELECT users.name AS users_name, users.fullname AS users_fullname
    FROM users
     LIMIT ? OFFSET ?
    2019-04-18 21:00:58,967 INFO sqlalchemy.engine.base.Engine (1, 0)
    ('ed', 'Ed Jones')

    >>> users.limit(2)  # 限制查询个数
    <sqlalchemy.orm.query.Query at 0x17a39d407b8>

    >>> users.limit(2).all()
    2019-04-18 21:03:01,424 INFO sqlalchemy.engine.base.Engine SELECT users.name AS users_name, users.fullname AS users_fullname
    FROM users
     LIMIT ? OFFSET ?
    2019-04-18 21:03:01,425 INFO sqlalchemy.engine.base.Engine (2, 0)
    [('ed', 'Ed Jones'), ('wendy', 'Wendy Williams')]

    >>> users.order_by(User.name)  # 按User.name排序
    <sqlalchemy.orm.query.Query at 0x17a37e10470>

    >>> users.order_by(User.name).all()
    2019-04-18 21:06:00,393 INFO sqlalchemy.engine.base.Engine SELECT users.name AS users_name, users.fullname AS users_fullname
    FROM users ORDER BY users.name
    2019-04-18 21:06:00,394 INFO sqlalchemy.engine.base.Engine ()
    [('ed', 'Ed Jones'),
     ('fred', 'Fred Flintstone'),
     ('mary', 'Mary Contrary'),
     ('wendy', 'Wendy Williams')]

    >>> users.filter(User.name == 'mary')  # 过滤数据
    <sqlalchemy.orm.query.Query at 0x17a37e04898>

    >>> users.filter(User.name == 'mary').first()
    2019-04-18 21:24:54,028 INFO sqlalchemy.engine.base.Engine SELECT users.name AS users_name, users.fullname AS users_fullname
    FROM users
    WHERE users.name = ?
     LIMIT ? OFFSET ?
    2019-04-18 21:24:54,029 INFO sqlalchemy.engine.base.Engine ('mary', 1, 0)
    ('mary', 'Mary Contrary')
    
    >>> users.filter_by(name='mary')   # 通过key关键字过滤数据
    <sqlalchemy.orm.query.Query at 0x17a3a0567f0>

    >>> users.filter_by(name='mary').first()
    2019-04-18 21:25:55,339 INFO sqlalchemy.engine.base.Engine SELECT users.name AS users_name, users.fullname AS users_fullname
    FROM users
    WHERE users.name = ?
     LIMIT ? OFFSET ?
    2019-04-18 21:25:55,340 INFO sqlalchemy.engine.base.Engine ('mary', 1, 0)
    ('mary', 'Mary Contrary')
     
    >>> first_user = session.query(User).get(1)  # 通过primary key主键返回对象实例

    >>> first_user
    <User(name='ed', fullname='Ed Jones', nickname='edsnickname')>
    
        >>> for name, fullname in session.query(User.name, User.fullname):
    ...     print(name, fullname)
    ...
    2019-04-18 21:40:18,566 INFO sqlalchemy.engine.base.Engine SELECT users.name AS users_name, users.fullname AS users_fullname
    FROM users
    2019-04-18 21:40:18,567 INFO sqlalchemy.engine.base.Engine ()
    ed Ed Jones
    wendy Wendy Williams
    mary Mary Contrary
    fred Fred Flintstone

    >>> for row in session.query(User, User.name).all():
    ...     print(row.User, row.name)  # 查询到的对象可以像普通Python对象对待
    ...
    2019-04-18 21:42:28,394 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    2019-04-18 21:42:28,395 INFO sqlalchemy.engine.base.Engine ()
    <User(name='ed', fullname='Ed Jones', nickname='edsnickname')> ed
    <User(name='wendy', fullname='Wendy Williams', nickname='windy')> wendy
    <User(name='mary', fullname='Mary Contrary', nickname='mary')> mary
    <User(name='fred', fullname='Fred Flintstone', nickname='freddy')> fred

    >>> for row in session.query(User.name.label('name_label')).all():  # 可以为查询的column列设置标签名
    ...     print(row.name_label)  # 使用标签名
    ...
    2019-04-18 21:43:22,465 INFO sqlalchemy.engine.base.Engine SELECT users.name AS name_label
    FROM users
    2019-04-18 21:43:22,466 INFO sqlalchemy.engine.base.Engine ()
    ed
    wendy
    mary
    fred

    >>> from sqlalchemy.orm import aliased

    >>> user_alias = aliased(User, name='aliasuser')  # 定义别名，即将User类设置别名为aliasuser

    >>> user_alias
    <AliasedClass at 0x17a37e04c88; User>

    >>> for row in session.query(user_alias, user_alias.name).all():
    ...     print(row.aliasuser)
    ...
    2019-04-18 21:50:09,776 INFO sqlalchemy.engine.base.Engine SELECT aliasuser.id AS aliasuser_id, aliasuser.name AS aliasuser_name, aliasuser.fullname AS aliasuser_fullname, aliasuser.nickname AS aliasuser_nickname
    FROM users AS aliasuser
    2019-04-18 21:50:09,776 INFO sqlalchemy.engine.base.Engine ()
    <User(name='ed', fullname='Ed Jones', nickname='edsnickname')>
    <User(name='wendy', fullname='Wendy Williams', nickname='windy')>
    <User(name='mary', fullname='Mary Contrary', nickname='mary')>
    <User(name='fred', fullname='Fred Flintstone', nickname='freddy')>
    
    >>> for u in session.query(User).order_by(User.id)[1:3]:  # 使用LIMIT和OFFSET偏移量
    ...      print(u)
    ...
    2019-04-18 21:52:48,402 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users ORDER BY users.id
     LIMIT ? OFFSET ?
    2019-04-18 21:52:48,403 INFO sqlalchemy.engine.base.Engine (2, 1)
    <User(name='wendy', fullname='Wendy Williams', nickname='windy')>
    <User(name='mary', fullname='Mary Contrary', nickname='mary')>
    
    >>> for user in session.query(User).filter(User.name=='ed').filter(User.fullname=='Ed Jones'):  # 多次过滤
    ...     print(user)
    ...
    2019-04-18 21:55:14,653 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name = ? AND users.fullname = ?
    2019-04-18 21:55:14,654 INFO sqlalchemy.engine.base.Engine ('ed', 'Ed Jones')
    <User(name='ed', fullname='Ed Jones', nickname='edsnickname')>
    
- 常用过滤运算符
- ``equals``  == 相等
- ``not equals`` != 不相等
- ``LIKE`` like (大小写敏感)像
- ``ILIKE`` ilike (大小写不敏感)像
- ``IN`` in\_ 在其中
- ``NOT IN`` ~ in\_ 不在其中
- ``IS NULL`` == None 为空
- ``IS NOT NULL`` != None 不为空
- ``AND`` 多级过滤或使用and_()
- ``OR`` 多级过滤或使用or_()
- ``MATCH``  match匹配，match()使用特定于数据库的MATCH或CONTAINS函数; 它的行为会因后端而异，并且在某些后端(例如SQLite)上不可用。

过滤运算示例::

    >>> myquery = session.query(User)

    >>> myquery
    <sqlalchemy.orm.query.Query at 0x17a39b57908>

    >>> myquery.filter(User.name == 'ed')
    <sqlalchemy.orm.query.Query at 0x17a39d59dd8>

    >>> myquery.filter(User.name == 'ed').all()  # 相等
    2019-04-18 22:05:45,169 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name = ?
    2019-04-18 22:05:45,172 INFO sqlalchemy.engine.base.Engine ('ed',)
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>]

    >>> myquery.filter(User.name != 'ed').all()  # 不相等
    2019-04-18 22:06:37,084 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name != ?
    2019-04-18 22:06:37,085 INFO sqlalchemy.engine.base.Engine ('ed',)
    [<User(name='wendy', fullname='Wendy Williams', nickname='windy')>,
     <User(name='mary', fullname='Mary Contrary', nickname='mary')>,
     <User(name='fred', fullname='Fred Flintstone', nickname='freddy')>]
     
    >>> myquery.filter(User.name.like('%ed%')).all()  # (区分大小写)像
    2019-04-18 22:07:11,593 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name LIKE ?
    2019-04-18 22:07:11,594 INFO sqlalchemy.engine.base.Engine ('%ed%',)
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>,
     <User(name='fred', fullname='Fred Flintstone', nickname='freddy')>]
     
    >>> myquery.filter(User.name.ilike('%ed%')).all() # (不区分大小写)像
    2019-04-18 22:07:49,114 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE lower(users.name) LIKE lower(?)
    2019-04-18 22:07:49,115 INFO sqlalchemy.engine.base.Engine ('%ed%',)
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>,
     <User(name='fred', fullname='Fred Flintstone', nickname='freddy')>]
     
    >>> myquery.filter(User.name.in_(['ed', 'wendy', 'jack'])).all()  # 在其中
    2019-04-18 22:09:00,462 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name IN (?, ?, ?)
    2019-04-18 22:09:00,463 INFO sqlalchemy.engine.base.Engine ('ed', 'wendy', 'jack')
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>,
     <User(name='wendy', fullname='Wendy Williams', nickname='windy')>]

    >>> myquery.filter(~User.name.in_(['ed', 'wendy', 'jack'])).all()  # 不在其中
    2019-04-18 22:10:06,110 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name NOT IN (?, ?, ?)
    2019-04-18 22:10:06,111 INFO sqlalchemy.engine.base.Engine ('ed', 'wendy', 'jack')
    [<User(name='mary', fullname='Mary Contrary', nickname='mary')>,
     <User(name='fred', fullname='Fred Flintstone', nickname='freddy')>]
     
    >>> myquery.filter(User.name == None).all()  # 是空
    2019-04-18 22:11:13,807 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name IS NULL
    2019-04-18 22:11:13,808 INFO sqlalchemy.engine.base.Engine ()
    []

    >>> myquery.filter(User.name != None).all()  # 非空
    2019-04-18 22:11:19,570 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name IS NOT NULL
    2019-04-18 22:11:19,571 INFO sqlalchemy.engine.base.Engine ()
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>,
     <User(name='wendy', fullname='Wendy Williams', nickname='windy')>,
     <User(name='mary', fullname='Mary Contrary', nickname='mary')>,
     <User(name='fred', fullname='Fred Flintstone', nickname='freddy')>]
     
    >>> from sqlalchemy import and_

    >>> myquery.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
    <sqlalchemy.orm.query.Query at 0x17a39d54f98>

    >>> myquery.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones')).all()  # AND且操作
    2019-04-18 22:12:24,261 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name = ? AND users.fullname = ?
    2019-04-18 22:12:24,261 INFO sqlalchemy.engine.base.Engine ('ed', 'Ed Jones')
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>]

    >>> myquery.filter(User.name == 'ed', User.fullname == 'Ed Jones').all()
    2019-04-18 22:13:35,250 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name = ? AND users.fullname = ?
    2019-04-18 22:13:35,251 INFO sqlalchemy.engine.base.Engine ('ed', 'Ed Jones')
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>]

    >>> from sqlalchemy import or_

    >>> myquery.filter(or_(User.name == 'ed', User.name == 'wendy'))
    <sqlalchemy.orm.query.Query at 0x17a39d4ac88>

    >>> myquery.filter(or_(User.name == 'ed', User.name == 'wendy')).all()  # OR或操作
    2019-04-18 22:14:16,643 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE users.name = ? OR users.name = ?
    2019-04-18 22:14:16,645 INFO sqlalchemy.engine.base.Engine ('ed', 'wendy')
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>,
     <User(name='wendy', fullname='Wendy Williams', nickname='windy')>]

- 使用文本SQL
- 可以使用 ``text()`` 来构建文本SQL
    
使用文本SQL::

    >>> myquery.filter(text("id<3")).order_by(text('id')).all()
    2019-04-18 22:22:06,749 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE id<3 ORDER BY id
    2019-04-18 22:22:06,750 INFO sqlalchemy.engine.base.Engine ()
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>,
     <User(name='wendy', fullname='Wendy Williams', nickname='windy')>]
     
    >>> for user in myquery.filter(text("id<3")).order_by(text('id')).all():
    ...     print(user.id, user.name)
    ...
    2019-04-18 22:22:54,586 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE id<3 ORDER BY id
    2019-04-18 22:22:54,587 INFO sqlalchemy.engine.base.Engine ()
    1 ed
    2 wendy
    
- 可以在字符串的SQL中使用冒号来指定绑定参数，需要使用 ``params()`` 方法。

使用冒号绑定参数::

    >>> myquery.filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(User.id).one()
    2019-04-18 22:25:20,752 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.nickname AS users_nickname
    FROM users
    WHERE id<? and name=? ORDER BY users.id
    2019-04-18 22:25:20,752 INFO sqlalchemy.engine.base.Engine (224, 'fred')
    <User(name='fred', fullname='Fred Flintstone', nickname='freddy')>
    
- 要使用完全基于字符串的语句，需要将完整语句的 ``text()`` 传递给 ``from_statement()`` 函数。
- 如果没有其他说明符，字符串SQL中的列将根据名称与模型列匹配。

例如下面我们只使用星号表示加载所有列::

    >>> myquery.from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()
    2019-04-18 22:30:43,455 INFO sqlalchemy.engine.base.Engine SELECT * FROM users where name=?
    2019-04-18 22:30:43,455 INFO sqlalchemy.engine.base.Engine ('ed',)
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>]

- 匹配名称上的列适用于简单的情况，但在处理包含重复列名的复杂语句或使用不易与特定名称匹配的匿名ORM构造时可能会变得难以处理。

查询指定列的数据::

    >>> stmt = text("SELECT name, id, fullname, nickname FROM users where name=:name")

    >>> stmt = stmt.columns(User.name, User.id, User.fullname, User.nickname)

    >>> myquery.from_statement(stmt).params(name='ed').all()
    2019-04-18 22:34:44,974 INFO sqlalchemy.engine.base.Engine SELECT name, id, fullname, nickname FROM users where name=?
    2019-04-18 22:34:44,975 INFO sqlalchemy.engine.base.Engine ('ed',)
    [<User(name='ed', fullname='Ed Jones', nickname='edsnickname')>]

通过将SQLite数据保存到本地文件sqlalchemy.db中，创建数据库信息::

    >>> from sqlalchemy import create_engine

    >>> engine = create_engine('sqlite:///sqlalchemy.db')

    >>> from sqlalchemy.ext.declarative import declarative_base

    >>> Base = declarative_base()

    >>> from sqlalchemy import Column, Integer, String

    >>> class User(Base):
    ...     __tablename__ = 'users'
    ...
    ...     id = Column(Integer, primary_key=True)
    ...     name = Column(String)
    ...     fullname = Column(String)
    ...     nickname = Column(String)
    ...
    ...     def __repr__(self):
    ...         return "<User(name='%s', fullname='%s', nickname='%s')>" % (
    ...             self.name, self.fullname, self.nickname)
    ...

    >>> User
    __main__.User

    >>> Base.metadata.create_all(engine)

    >>> ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

    >>> from sqlalchemy.orm import sessionmaker

    >>> Session = sessionmaker(bind=engine)

    >>> session = Session()

    >>> session.add(ed_user)

    >>> session.add_all([
    ...     User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    ...     User(name='mary', fullname='Mary Contrary', nickname='mary'),
    ...     User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

    >>> session.commit()

    >>> users = session.query(User.name, User.fullname)

    >>> users.all()
    [('ed', 'Ed Jones'),
     ('wendy', 'Wendy Williams'),
     ('mary', 'Mary Contrary'),
     ('fred', 'Fred Flintstone')]

- 统计数量
- 使用 ``Query`` 对象的 ``count()`` 方法。
- 使用 ``sqlalchemy`` 的 ``func`` 构造器的 ``count()`` 方法，这种方法对子查询更方便。

统计查询数据的数量::

    >>> session.query(User).filter(User.name.like('%ed')).count()
    2

    >>> from sqlalchemy import func

    >>> session.query(func.count(User.name), User.name).group_by(User.name).all()
    [(1, 'ed'), (1, 'fred'), (1, 'mary'), (1, 'wendy')]
    
    >>> session.query(func.count('*')).select_from(User).scalar()  # 使用select_from方法计数，等价于在数据库中执行"SELECT count(*) FROM table"
    4

    >>> session.query(func.count(User.id)).scalar()  # 如果我们直接用User主键表示计数，则可以删除select_from()的用法
    4
    
- 建立相对关系(Relationship)。
- 建立双向关系：在 ``relationship()`` 指令中，参数 ``relationship.back_populates`` 被指定为引用补充属性名称，通过这样做，每个 ``relationship()`` 可以建立两个类之间的双向关系。
- 使用双向关系时，在一个方向上添加的元素会自动在另一个方向上可见。

考虑添加第二张表address，用于存储用户的邮件地址，定义一个Address类，建立一个 ``one to many`` 一对多的关系模型::

    >>> from sqlalchemy import ForeignKey

    >>> from sqlalchemy.orm import relationship

    >>> class Address(Base):
    ...     __tablename__ = 'addresses'
    ...     id = Column(Integer, primary_key=True)  # 设置id为主键
    ...     email_address = Column(String, nullable=False)  # 设置email地址为String类型，非空
    ...     user_id = Column(Integer, ForeignKey('users.id'))  # 设置user_id，外键是users表中的id
    ...
    ...     user = relationship("User", back_populates="addresses")  # 建立相对关系，告诉ORM使用Address.user属性将Address类本身链接到User类，使用Address.user则可以访问到地址对应的User类
    ...
    ...     def __repr__(self):
    ...         return "<Address(email_address='%s')>" % self.email_address
    ...

    >>> User.addresses = relationship("Address", order_by=Address.id, back_populates="user")  # 将User.addresses映射到Address类的id属性上，通过User.addresses可以获取到用户所有的邮件地址的id列表

    >>> Address
    __main__.Address

    >>> User
    __main__.User
    
    >>> Base.metadata.create_all(engine)
    
创建表了后，在SQLite3中查看已经新建了addresses表::

    sqlite>
    sqlite> .table
    addresses  users
    sqlite>

使用相关对象，创建一个新的User实例，并添加邮件地址::

    >>> jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')

    >>> jack.addresses
    []

    >>> jack.addresses = [Address(email_address='jack@google.com'), Address(email_address='j25@yahoo.com')]

    >>> jack.addresses[0]
    <Address(email_address='jack@google.com')>

    >>> jack.addresses[1]
    <Address(email_address='j25@yahoo.com')>

    >>> jack.addresses[0].user
    <User(name='jack', fullname='Jack Bean', nickname='gjffdd')>

    >>> jack.addresses[1].user
    <User(name='jack', fullname='Jack Bean', nickname='gjffdd')>

- 添加数据到数据库时，会使用 ``cascading`` 级联会话同时添加对象到数据库。

将用户jack添加到数据库中，由于级联操作，会自动将Address地址相关数据添加到数据库::

    >>> session.add(jack)

    >>> session.commit()

在SQLite3中查看users表和addresses表信息::

    sqlite> select * from addresses;        
    1|jack@google.com|5                     
    2|j25@yahoo.com|5                       
    sqlite> select * from  users;           
    1|ed|Ed Jones|edsnickname               
    2|wendy|Wendy Williams|windy            
    3|mary|Mary Contrary|mary               
    4|fred|Fred Flintstone|freddy           
    5|jack|Jack Bean|gjffdd                 
    sqlite>                                 
    
- 使用 ``join`` 进行联合查询。
- 使用 ``Query.join()`` 方法最容易实现实际的SQL JOIN语法。

使用 ``Query.filter()`` 在User和Address之间构造一个简单的隐式连接，并使用 ``Query.join()`` 方法实现连接:

.. code-block:: python
    :linenos:
    :emphasize-lines: 11
    
    >>> for u, a in session.query(User, Address).\
    ...                     filter(User.id==Address.user_id).\
    ...                     filter(Address.email_address=='jack@google.com').\
    ...                     all():
    ...     print(u)
    ...     print(a)
    ...
    <User(name='jack', fullname='Jack Bean', nickname='gjffdd')>
    <Address(email_address='jack@google.com')>

    >>> session.query(User).join(Address).\
    ...         filter(Address.email_address=='jack@google.com').\
    ...         all()
    [<User(name='jack', fullname='Jack Bean', nickname='gjffdd')>]
    
``Query.join()`` 知道如何在User和Address之间进行连接，因为它们之间只有一个外键。

如果没有外键或有多个外键时，使用以下方式来进行连接::

    query.join(Address, User.id==Address.user_id)    # explicit condition [ 明确的条件] 
    query.join(User.addresses)                       # specify relationship from left to right [ 从左到右指定关系] 
    query.join(Address, User.addresses)              # same, with explicit target [ 同样，有明确的目标] 
    query.join('addresses')                          # same, using a string [ 同样，使用字符串] 
    
- 使用 ``aliased`` 对表名进行重命名。这样可以对表名使用一次或多次。

对Address表进行重命名::

    >>> for username, email1, email2 in \
    ...     session.query(User.name, adalias1.email_address, adalias2.email_address). \
    ...     join(adalias1, User.addresses).join(adalias2, User.addresses). \
    ...     filter(adalias1.email_address=='jack@google.com'). \
    ...     filter(adalias2.email_address=='j25@yahoo.com'):
    ...     print(username, email1, email2)
    ...
    jack jack@google.com j25@yahoo.com
    
- 使用 ``session.delete(instance)`` 删除instance实例数据。
- SQLAlchemy不会自动级联删除(SQLAlchemy doesn’t assume that deletes cascade)，必须要明确指定才会 ``cascade`` 级联删除。
- 级联操作相关请参考官网说明 `SQLAlchemy 1.3 Documentation:Cascades <https://docs.sqlalchemy.org/en/13/orm/cascades.html#unitofwork-cascades>`_

删除用户jack::

    >>> jack
    <User(name='jack', fullname='Jack Bean', nickname='gjffdd')>

    >>> session.delete(jack)

    >>> session.query(User).filter_by(name='jack').count()
    0

    >>> session.query(Address).filter(Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])).count()
    2

在SQLite3中查看users表和addresses表信息::

    sqlite> select * from addresses;        
    1|jack@google.com|5                     
    2|j25@yahoo.com|5                       
    sqlite> select * from  users;           
    1|ed|Ed Jones|edsnickname               
    2|wendy|Wendy Williams|windy            
    3|mary|Mary Contrary|mary               
    4|fred|Fred Flintstone|freddy           
    5|jack|Jack Bean|gjffdd                 
    sqlite>  
    
说明此时jack并没有被删除掉。

使用 ``session.commit()`` 提交事务::

    >>> session.commit()

再在SQLite3中查看users表和addresses表信息::


    sqlite> select * from addresses;        
    1|jack@google.com|5                     
    2|j25@yahoo.com|5                       
    sqlite> select * from  users;           
    1|ed|Ed Jones|edsnickname               
    2|wendy|Wendy Williams|windy            
    3|mary|Mary Contrary|mary               
    4|fred|Fred Flintstone|freddy           
    sqlite> 
    
说明jack用户已经从数据库中删除掉，但其email邮箱信息并不会自动删除。

懒人包dataset处理数据库
--------------------------------------------

在Python中，数据库并不是存储大量结构化数据的最简单的解决方案。dataset提供了一个简单的抽象层(可以删除大多数直接的SQL语句而无需完整的ORM模型)，本质上，数据库可以像JSON文件或NoSQL存储一样使用。

- dataset的安装

使用pip安装::

    $ pip install dataset
    Looking in indexes: http://mirrors.aliyun.com/pypi/simple/
    Collecting dataset
      Downloading http://mirrors.aliyun.com/pypi/packages/d5/02/a4c77a15d004f1307a579e577974fa9292a63e93abff3e40ad993cf597c7/dataset-1.1.2-py2.py3-none-any.whl
    Collecting alembic>=0.6.2 (from dataset)
      Downloading http://mirrors.aliyun.com/pypi/packages/fc/42/8729e2491fa9b8eae160d1cbb429f61712bfc2d779816488c25cfdabf7b8/alembic-1.0.9.tar.gz (1.0MB)
        100% |████████████████████████████████| 1.0MB 3.9MB/s
    Requirement already satisfied: six>=1.11.0 in d:\programfiles\python362\lib\site-packages (from dataset) (1.12.0)
    Requirement already satisfied: sqlalchemy>=1.1.2 in d:\programfiles\python362\lib\site-packages (from dataset) (1.3.2)
    Collecting Mako (from alembic>=0.6.2->dataset)
      Downloading http://mirrors.aliyun.com/pypi/packages/a1/bb/f4e5c056e883915c37bb5fb6fab7f00a923c395674f83bfb45c9ecf836b6/Mako-1.0.9.tar.gz (459kB)
        100% |████████████████████████████████| 460kB 10.3MB/s
    Collecting python-editor>=0.3 (from alembic>=0.6.2->dataset)
      Downloading http://mirrors.aliyun.com/pypi/packages/c6/d3/201fc3abe391bbae6606e6f1d598c15d367033332bd54352b12f35513717/python_editor-1.0.4-py3-none-any.whl
    Requirement already satisfied: python-dateutil in d:\programfiles\python362\lib\site-packages (from alembic>=0.6.2->dataset) (2.8.0)
    Requirement already satisfied: MarkupSafe>=0.9.2 in d:\programfiles\python362\lib\site-packages (from Mako->alembic>=0.6.2->dataset) (1.1.1)
    Installing collected packages: Mako, python-editor, alembic, dataset
      Running setup.py install for Mako ... done
      Running setup.py install for alembic ... done
    Successfully installed Mako-1.0.9 alembic-1.0.9 dataset-1.1.2 python-editor-1.0.4
    
- 使用dataset。

导入dataset包::

    >>> import dataset

- 使用 ``dataset.connect`` 创建数据库连接。
- ``dataset`` \_\_init\_\_文件中只有一个方法 ``connect``。

\_\_init\_\_文件内容::

    import os
    import warnings
    from dataset.database import Database
    from dataset.table import Table
    from dataset.util import row_type

    # shut up useless SA warning:
    warnings.filterwarnings(
        'ignore', 'Unicode type received non-unicode bind param value.')
    warnings.filterwarnings(
        'ignore', 'Skipping unsupported ALTER for creation of implicit constraint')

    __all__ = ['Database', 'Table', 'freeze', 'connect']
    __version__ = '1.1.2'


    def connect(url=None, schema=None, reflect_metadata=True, engine_kwargs=None,
                reflect_views=True, ensure_schema=True, row_type=row_type):
        """ Opens a new connection to a database.

        *url* can be any valid `SQLAlchemy engine URL`_.  If *url* is not defined
        it will try to use *DATABASE_URL* from environment variable.  Returns an
        instance of :py:class:`Database <dataset.Database>`. Set *reflect_metadata*
        to False if you don't want the entire database schema to be pre-loaded.
        This significantly speeds up connecting to large databases with lots of
        tables. *reflect_views* can be set to False if you don't want views to be
        loaded.  Additionally, *engine_kwargs* will be directly passed to
        SQLAlchemy, e.g.  set *engine_kwargs={'pool_recycle': 3600}* will avoid `DB
        connection timeout`_. Set *row_type* to an alternate dict-like class to
        change the type of container rows are stored in.::

            db = dataset.connect('sqlite:///factbook.db')

        .. _SQLAlchemy Engine URL: http://docs.sqlalchemy.org/en/latest/core/engines.html#sqlalchemy.create_engine
        .. _DB connection timeout: http://docs.sqlalchemy.org/en/latest/core/pooling.html#setting-pool-recycle
        """
        if url is None:
            url = os.environ.get('DATABASE_URL', 'sqlite://')

        return Database(url, schema=schema, reflect_metadata=reflect_metadata,
                        engine_kwargs=engine_kwargs, reflect_views=reflect_views,
                        ensure_schema=ensure_schema, row_type=row_type)

- dataset ``connect`` url需要按SQLAlchemy engine URL方式定义database_url。
- 可以定义一个环境变量 ``DATABASE_URL`` 来设置url。

数据库URL的典型形式是::

    dialect+driver://username:password@host:port/database

- dialect方言是SQLAlchemy方言的标识名称，如sqlite, mysql, postgresql, oracle,或mssql。
- driver是使用全小写字母连接到数据库的DBAPI的名称。
- URL中特殊的字符需要使用URL编码。

- 使用 ``dataset.connect(url)`` 来连接数据库引擎。

我们使用SQLite3将数据库保存到dataset.db文件中::

    >>> db = dataset.connect('sqlite:///dataset.db')

    >>> db
    <Database(sqlite:///dataset.db)>

- 使用 ``get_table(table_name, primary_id=None, primary_type=None)`` 或 ``create_table(table_name, primary_id=None, primary_type=None)`` 加载表或创建表，如果表不存在则会创建表。
- 使用 ``db[table_name]`` 也可以加载或创建表。

指定数据库中的表时，可以使用类似于字典的语法，当表不存在时，会默认建表::

    >>> table = db.get_table('user')

    >>> table
    <Table(user)>

    >>> table1 = db['user']

    >>> table1
    <Table(user)>

    >>> id(table) == id(table1)
    True

    >>> db['population']
    <Table(population)>

    >>> table2 = db['population']

    >>> table2
    <Table(population)>

在SQLite3中查看user表和population表信息::

    sqlite> .table                         
    population  user                       
    sqlite> .schema user                   
    CREATE TABLE user (                    
            id INTEGER NOT NULL,           
            PRIMARY KEY (id)               
    );                                     
    sqlite> .schema population             
    CREATE TABLE population (              
            id INTEGER NOT NULL,           
            PRIMARY KEY (id)               
    );                                     
    sqlite>                                
    
创建表时指主键和主键类型::

    >>> table_population2 = db.create_table('population2', 'age')  # 指定age为主键

    >>> table_population2
    <Table(population2)>

    >>> table_population3 = db.create_table('population3', primary_id='city', primary_type=db.types.text)  # 指定city为主键，主键类型为text类型

    >>> table_population3
    <Table(population3)>

    >>> table_population4 = db.create_table('population4', primary_id='city', primary_type=db.types.string(25)) # 指定city为主键，主键类型为string类型(对应varchar(25))

    >>> table_population4
    <Table(population4)>

再在SQLite3中查看表信息::

    sqlite> .table                                                
    population   population2  population3  population4  user      
    sqlite> .schema population2                                   
    CREATE TABLE population2 (                                    
            age INTEGER NOT NULL,                                 
            PRIMARY KEY (age)                                     
    );                                                            
    sqlite> .schema population3                                   
    CREATE TABLE population3 (                                    
            city TEXT NOT NULL,                                   
            PRIMARY KEY (city)                                    
    );                                                            
    sqlite> .schema population4                                   
    CREATE TABLE population4 (                                    
            city VARCHAR(25) NOT NULL,                            
            PRIMARY KEY (city)                                    
    );                                                            
    sqlite>                                                       

- 对 ``Table`` 对象使用 ``insert(row, ensure=None, types=None)`` 插入数据，row为字典数据，返回插入行的primary key号。
- 如果row字典中的键不在表中，则会自动创建相应的column列。

插入一行数据::

    >>> table.insert(dict(name='John Doe', age=46, country='China'))
    1

再在SQLite3中查看user表信息，使用 ``.headers on`` 打开表头header，并使用 ``.mode column`` 打开column列模式::

    sqlite> .headers on
    sqlite> .mode column
    sqlite> select * from user;
    id          name        age         country
    ----------  ----------  ----------  ----------
    1           John Doe    46          China
    sqlite> .schema user
    CREATE TABLE user (
            id INTEGER NOT NULL, name TEXT, age INTEGER, country TEXT,
            PRIMARY KEY (id)
    );
    sqlite>

可以发现列 ``name`` 和 ``country`` 被自动加入到表中。

再插入一行数据::

    >>> table.insert(dict(name='Edmond Dantes', age=37, country='France', gender='male'))
    2

再在SQLite3中查看user表信息::

    sqlite> .schema user
    CREATE TABLE user (
            id INTEGER NOT NULL, name TEXT, age INTEGER, country TEXT, gender TEXT,
            PRIMARY KEY (id)
    );
    sqlite> select * from user;  --在默认的情况下，每列至少10个字符宽。太宽的数据将被截取。你可以用“.width”命令来调整列宽。
    id          name        age         country     gender
    ----------  ----------  ----------  ----------  ----------
    1           John Doe    46          China
    2           Edmond Dan  37          France      male
    sqlite> .width 12 20  -- 改变第一列的宽度为12字符，改变第二列的宽度为20字符
    sqlite> select * from user;
    id            name                  age         country     gender
    ------------  --------------------  ----------  ----------  ----------
    1             John Doe              46          China
    2             Edmond Dantes         37          France      male
    sqlite> select * from user where name="Edmond Dantes";
    id            name                  age         country     gender
    ------------  --------------------  ----------  ----------  ----------
    2             Edmond Dantes         37          France      male
    
可以发现新列gender被自动添加进数据库。


- 对 ``Table`` 对象使用 ``update(row, keys, ensure=None, types=None, return_count=False)`` 更新数据，row为字典数据，返回更新行的总行数。
- 如果row字典中的键不在表中，则会自动创建相应的column列。

更新John的年龄为47岁::

    >>> table.update(dict(name='John Doe', age=47), ['name'])
    1

再在SQLite3中查看user表信息::

    sqlite> select * from user;                                             
    id            name                  age         country     gender      
    ------------  --------------------  ----------  ----------  ----------  
    1             John Doe              47          China                   
    2             Edmond Dantes         37          France      male        
    sqlite>   

可以发现John Doe的年龄已经从46岁变成47岁了。

发现John Doe的性别没有指定，更新一下::

    >>> table.update(dict(name='John Doe', gender='famale'), ['name'])
    1

再在SQLite3中查看user表信息::

    sqlite> select * from user;                                              
    id            name                  age         country     gender       
    ------------  --------------------  ----------  ----------  ----------   
    1             John Doe              47          China       famale       
    2             Edmond Dantes         37          France      male         
    sqlite>                                                                  
    
性别补充好了，又发现可以补充一个email邮箱的字段::

    >>> table.update(dict(id=1, email='john@python.org'),['id'])
    1

    >>> table.update(dict(id=2, email='edmond@python.org'),['id'])
    1

再在SQLite3中查看user表信息::

    sqlite> select * from user;
    id            name                  age         country     gender      email
    ------------  --------------------  ----------  ----------  ----------  ---------------
    1             John Doe              47          China       famale      john@python.org
    2             Edmond Dantes         37          France      male        edmond@python.o
    sqlite>

说明在update时如果列不存在的时候也可以自动加入到数据库中。

不指定具体对哪一行进行更新::

    >>> table.update(dict(age=30),['id'])
    2

再在SQLite3中查看user表信息::

    sqlite> select * from user;                                                                         
    id            name                  age         country     gender      email                       
    ------------  --------------------  ----------  ----------  ----------  ---------------             
    1             John Doe              30          China       famale      john@python.org             
    2             Edmond Dantes         30          France      male        edmond@python.o             
    sqlite>                                                                                             

说明此时对所有的行进行更新，将age全部设置为30岁。

- 使用Transactions事务上下文管理器。

使用 ``with`` 上下文管理器::

    >>> with db:
    ...     db['user'].insert(dict(name='John Doe', age=46, country='China'))
    ...

再在SQLite3中查看user表信息::

    sqlite> select * from user;
    id          name        age         country     gender      email
    ----------  ----------  ----------  ----------  ----------  ---------------
    1           John Doe    32          China       famale      john@python.org
    2           Edmond Dan  32          France      male        edmond@python.o
    3           John Doe    46          China

- 通过调用  ``begin()`` 、 ``commit()`` 、 ``rollback()``  以及使用 ``try..except`` 捕获异常。

使用 ``try..except`` 捕获异常::

    >>> db = dataset.connect('sqlite:///dataset.db')

    >>> db.begin()

    >>> try:
    ...     db['user'].update(dict(id=3,name='John King', gender='male', email='king@python.org'), ['id'])
    ...     db.commit()
    ... except:
    ...     db.rollback()
    ...

再在SQLite3中查看user表信息::

    sqlite> select * from user;                                                    
    id          name        age         country     gender      email              
    ----------  ----------  ----------  ----------  ----------  ---------------    
    1           John Doe    32          China       famale      john@python.org    
    2           Edmond Dan  32          France      male        edmond@python.o    
    3           John King   46          China       male        king@python.org    
    sqlite>                                                                        

可以看到第三行数据已经更新。

- 检索数据库和表。
- ``db.tables`` 查看数据库中所有的表信息。
- ``db[table_name].columns`` 查看数据库表中所有字段信息。
- ``len(db[table_name])`` 统计表中的数据行数。

查看表信息和表字段信息::

    >>> db.tables
    ['population', 'population2', 'population3', 'population4', 'user']

    >>> db['user'].columns
    ['id', 'name', 'age', 'country', 'gender', 'email']

    >>> db['population'].columns
    ['id']

    >>> len(db['user'])
    3

    >>> len(db['population'])
    0

- ``Table.all()`` 获取所有数据。
-  如果我们只想迭代表中的所有行，我们可以省略 ``all()`` 。

获取表中的所有数据::

    >>> table
    <Table(user)>

    >>> table.all()
    <dataset.util.ResultIter at 0x251a25e9d30>

    >>> users = table.all()

    >>> users
    <dataset.util.ResultIter at 0x251a2643c88>

    >>> for user in users:
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 2), ('name', 'Edmond Dantes'), ('age', 32), ('country', 'France'), ('gender', 'male'), ('email', 'edmond@python.org')])
    OrderedDict([('id', 3), ('name', 'John King'), ('age', 46), ('country', 'China'), ('gender', 'male'), ('email', 'king@python.org')])

    >>> for user in table:
    ...     print(user['name'], user['age'], user['country'])
    ...
    John Doe 32 China
    Edmond Dantes 32 France
    John King 46 China

- ``Table.find()`` 查找所有特定条件的数据。
- ``Table.find_one()`` 查找所有特定条件的数据，但仅返回一条数据。
- 使用 ``_limit`` 关键字参数可以限定返回的数据个数。
- 使用 ``order_by`` 关键字参数可以对查找的结果进行排序。

通过 ``find`` 或 ``find_one`` 获取数据::

    >>> chinese_users = table.find(country='China')

    >>> chinese_users
    <dataset.util.ResultIter at 0x251a2bd97b8>

    >>> for user in chinese_users:
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 3), ('name', 'John King'), ('age', 46), ('country', 'China'), ('gender', 'male'), ('email', 'king@python.org')])
    
    >>> table.find_one(country='China')
    OrderedDict([('id', 1),
                 ('name', 'John Doe'),
                 ('age', 32),
                 ('country', 'China'),
                 ('gender', 'famale'),
                 ('email', 'john@python.org')])

    >>> for user in table.find(country='China', _limit=1):  # 限定输出1条结果
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])

    >>> for user in table.find(country='China', _limit=2):  # 限定输出2条结果
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 3), ('name', 'John King'), ('age', 46), ('country', 'China'), ('gender', 'male'), ('email', 'king@python.org')])

    >>> for user in table.find(country='China', order_by='age'):  # 按age年龄进行升序排列
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 3), ('name', 'John King'), ('age', 46), ('country', 'China'), ('gender', 'male'), ('email', 'king@python.org')])

    >>> for user in table.find(country='China', order_by='-age'):  # 按age年龄进行降序排列
    ...     print(user)
    ...
    OrderedDict([('id', 3), ('name', 'John King'), ('age', 46), ('country', 'China'), ('gender', 'male'), ('email', 'king@python.org')])
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    
    >>> for user in table.find(country='France', age=32):
    ...     print(user)
    ...
    OrderedDict([('id', 2), ('name', 'Edmond Dantes'), ('age', 32), ('country', 'France'), ('gender', 'male'), ('email', 'edmond@python.org')])
    
    >>> table.find(id=[1, 3])
    <dataset.util.ResultIter at 0x251a2bf82b0>

    >>> for user in table.find(id=[1, 3]):
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 3), ('name', 'John King'), ('age', 46), ('country', 'China'), ('gender', 'male'), ('email', 'king@python.org')])


- 在 ``find`` 或 ``find_one`` 中使用比较运算符(comparison operators)。

可使用的运算符包括::

    gt, >
    lt, <
    gte, >=
    lte, <=
    !=, <>, not
    between, ..

使用比较运算符::

    >>> for user in table.find(age={'>=': 40}):
    ...     print(user)
    ...
    OrderedDict([('id', 3), ('name', 'John King'), ('age', 46), ('country', 'China'), ('gender', 'male'), ('email', 'king@python.org')])

    >>> for user in table.find(age={'gt': 40}):
    ...     print(user)
    ...
    OrderedDict([('id', 3), ('name', 'John King'), ('age', 46), ('country', 'China'), ('gender', 'male'), ('email', 'king@python.org')])

    >>> for user in table.find(age={'lt': 40}):
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 2), ('name', 'Edmond Dantes'), ('age', 32), ('country', 'France'), ('gender', 'male'), ('email', 'edmond@python.org')])

    >>> for user in table.find(age={'<': 40}):
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 2), ('name', 'Edmond Dantes'), ('age', 32), ('country', 'France'), ('gender', 'male'), ('email', 'edmond@python.org')])

    >>> for user in table.find(age={'between':[30,40]}):
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 2), ('name', 'Edmond Dantes'), ('age', 32), ('country', 'France'), ('gender', 'male'), ('email', 'edmond@python.org')])

    >>> for user in table.find(age={'..':[30,40]}):
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 2), ('name', 'Edmond Dantes'), ('age', 32), ('country', 'France'), ('gender', 'male'), ('email', 'edmond@python.org')])

- ``Table.distinct()`` 获取一列或多列的唯一行。

如获取所有的国家信息::
    
    >>> table.distinct('country')
    <dataset.util.ResultIter at 0x251a2df57f0>

    >>> for country in table.distinct('country'):
    ...     print(country)
    ...
    OrderedDict([('country', 'China')])
    OrderedDict([('country', 'France')])
    
    >>> for age in table.distinct('age'):
    ...     print(age)
    ...
    OrderedDict([('age', 32)])
    OrderedDict([('age', 46)])

    >>> for age_country in table.distinct('age','country'):
    ...     print(age_country)
    ...
    OrderedDict([('age', 32), ('country', 'China')])
    OrderedDict([('age', 32), ('country', 'France')])
    OrderedDict([('age', 46), ('country', 'China')])

    >>> for age in table.distinct('age',country='China'):
    ...     print(age)
    ...
    OrderedDict([('age', 32)])
    OrderedDict([('age', 46)])
    

- 使用 ``db.query(SQL_STRING)`` 运行自定义SQL字符串SQL_STRING。

统计每个国家的用户数量::

    >>> result = db.query('SELECT country, COUNT(*) c FROM user GROUP BY country')
    ... for row in result:
    ...    print(row['country'], row['c'])
    ...
    China 2
    France 1

    >>> result = db.query('SELECT country, COUNT(*) AS count FROM user GROUP BY country')
    ... for row in result:
    ...    print(row['country'], row['count'])
    ...
    China 2
    France 1
    
- ``Table.delete(*clauses, **filters)`` 从表中删除行数据。
- If no arguments are given, all records are deleted. 即 ``如果没指定参数，所有的行数据都会会删除`` ！！！

在表中删除行数据::

    >>> user_king = table.find_one(name='John King')

    >>> user_king
    OrderedDict([('id', 3),
                 ('name', 'John King'),
                 ('age', 46),
                 ('country', 'China'),
                 ('gender', 'male'),
                 ('email', 'king@python.org')])
             
    >>> table.delete(name='John King')
    True
    
    >>> for user in table.all():
    ...     print(user)
    ...
    OrderedDict([('id', 1), ('name', 'John Doe'), ('age', 32), ('country', 'China'), ('gender', 'famale'), ('email', 'john@python.org')])
    OrderedDict([('id', 2), ('name', 'Edmond Dantes'), ('age', 32), ('country', 'France'), ('gender', 'male'), ('email', 'edmond@python.org')])


再在SQLite3中查看user表信息::

    sqlite> select * from user;
    id          name        age         country     gender      email
    ----------  ----------  ----------  ----------  ----------  ---------------
    1           John Doe    32          China       famale      john@python.org
    2           Edmond Dan  32          France      male        edmond@python.o
    sqlite>

不设置参数，使用delete删除::

    >>> table.delete()
    True

    >>> for user in table.all():
    ...     print(user)
    ...

再在SQLite3中查看user表信息::

    sqlite> select * from user;
    sqlite>

已经查询不到数据，说明user表已经被清空了。

- ``Table.drop_column(name)`` 从表中删除指定列。
- SQLite不支持删除列。

尝试删除列::

    >>> table.columns
    ['id', 'name', 'age', 'country', 'gender', 'email']

        >>> table.drop_column('email')
        ---------------------------------------------------------------------------
        RuntimeError                              Traceback (most recent call last)
        <ipython-input-79-1932daeb597f> in <module>
        ----> 1 table.drop_column('email')

        RuntimeError: SQLite does not support dropping columns.

提示 ``RuntimeError`` 异常。

memcached的使用
-----------------------------------------------------

- Memcached是一个自由开源的，高性能，分布式内存对象缓存系统。
- Memcached是一种基于内存的key-value存储，用来存储小块的任意数据（字符串、对象）。这些数据可以是数据库调用、API调用或者是页面渲染的结果。 

linux下安装Memcached 参见https://www.runoob.com/memcached/window-install-memcached.html 。

安装依赖包::

    [root@localhost ~]# yum install libevent libevent-devel -y
    
安装Memcached::

    [root@localhost ~]# yum install memcached -y

查看memcached的帮助信息::

    [root@localhost ~]# memcached -h
    memcached 1.4.15
    -p <num>      TCP port number to listen on (default: 11211)
    -U <num>      UDP port number to listen on (default: 11211, 0 is off)
    -s <file>     UNIX socket path to listen on (disables network support)
    -a <mask>     access mask for UNIX socket, in octal (default: 0700)
    -l <addr>     interface to listen on (default: INADDR_ANY, all addresses)
                  <addr> may be specified as host:port. If you don't specify
                  a port number, the value you specified with -p or -U is
                  used. You may specify multiple addresses separated by comma
                  or by using -l multiple times
    -d            run as a daemon
    -r            maximize core file limit
    -u <username> assume identity of <username> (only when run as root)
    -m <num>      max memory to use for items in megabytes (default: 64 MB)
    -M            return error on memory exhausted (rather than removing items)
    -c <num>      max simultaneous connections (default: 1024)
    -k            lock down all paged memory.  Note that there is a
                  limit on how much memory you may lock.  Trying to
                  allocate more than that would fail, so be sure you
                  set the limit correctly for the user you started
                  the daemon with (not for -u <username> user;
                  under sh this is done with 'ulimit -S -l NUM_KB').
    -v            verbose (print errors/warnings while in event loop)
    -vv           very verbose (also print client commands/reponses)
    -vvv          extremely verbose (also print internal state transitions)
    -h            print this help and exit
    -i            print memcached and libevent license
    -P <file>     save PID in <file>, only used with -d option
    -f <factor>   chunk size growth factor (default: 1.25)
    -n <bytes>    minimum space allocated for key+value+flags (default: 48)
    -L            Try to use large memory pages (if available). Increasing
                  the memory page size could reduce the number of TLB misses
                  and improve the performance. In order to get large pages
                  from the OS, memcached will allocate the total item-cache
                  in one large chunk.
    -D <char>     Use <char> as the delimiter between key prefixes and IDs.
                  This is used for per-prefix stats reporting. The default is
                  ":" (colon). If this option is specified, stats collection
                  is turned on automatically; if not, then it may be turned on
                  by sending the "stats detail on" command to the server.
    -t <num>      number of threads to use (default: 4)
    -R            Maximum number of requests per event, limits the number of
                  requests process for a given connection to prevent 
                  starvation (default: 20)
    -C            Disable use of CAS
    -b <num>      Set the backlog queue limit (default: 1024)
    -B            Binding protocol - one of ascii, binary, or auto (default)
    -I            Override the size of each slab page. Adjusts max item size
                  (default: 1mb, min: 1k, max: 128m)
    -S            Turn on Sasl authentication
    -o            Comma separated list of extended or experimental options
                  - (EXPERIMENTAL) maxconns_fast: immediately close new
                    connections if over maxconns limit
                  - hashpower: An integer multiplier for how large the hash
                    table should be. Can be grown at runtime if not big enough.
                    Set this based on "STAT hash_power_level" before a 
                    restart.
    [root@localhost ~]#                                                      

启动memecached::

    [root@localhost ~]# memcached -u root -p 11211 -m 64m -d

    启动选项说明:
    -u root 以root用户运行Memcache(如果不使用此选项，则会提示can't run as root without the -u switch)
    -p 11211 是设置Memcache监听的端口为11211
    -m 64m 是分配给Memcache使用的内存数量，单位是64MB
    -d 是启动一个守护进程

安装telnet工具::

    [root@localhost ~]# yum install telnet-server telnet -y


使用 ``telnet HOST PORT`` 连接memcached服务，HOST、PORT是运行memcached的主机和端口。

连接memcached服务::

    [root@localhost ~]# telnet 127.0.0.1 11211
    Trying 127.0.0.1...
    Connected to 127.0.0.1.
    Escape character is '^]'.
    
说明已经连接上memcached服务。

或者HOST使用localhost也可以::

    [root@localhost ~]# telnet localhost 11211
    Trying ::1...
    Connected to localhost.
    Escape character is '^]'.
    
在连接上memcached服务后，就可以执行memcached命令了。
    
memcached的存储命令
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``set`` 命令，用于将value值存储到key键中，如果key已经存在，则会更新key的value值。

语法如下::

    set key flags exptime bytes [noreply] 
    value 
    
    参数说明:
    key：键值 key-value 结构中的 key，用于查找缓存值。
    flags: 可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息。
    exptime: 在缓存中保存键值对的时间长度(以秒为单位，0 表示永远)。
    bytes: 在缓存中存储的字节数。
    noreply: 可选参数，该参数告诉服务器不需要返回数据。
    value: 键值 key-value 结构中的 value，存储的值，始终位于第二行。

设置一个键值对::
    
    set firstkey 0 900 15
    hello,memcached
    STORED
    get firstkey
    VALUE firstkey 0 15
    hello,memcached
    END
    set firstkey 0 900 16      <-- 说明：此处是对firstkey键的value值进行更新
    hello,memcached!
    STORED
    get firstkey
    VALUE firstkey 0 16
    hello,memcached!
    END
    
    其中：
    key键为firstkey
    flags为0
    exptime过期时间900s
    bytes存储字节数15
    value存储的值为hello,memcached

设置过期时间::

    set secondkey 0 30 6            <-- 说明：设置过期时间为30秒
    hello!
    STORED
    get secondkey                   <-- 说明：在30s内能够获取到secondkey的值
    VALUE secondkey 0 6
    hello!
    END
    get secondkey                   <-- 说明：在30s内能够获取到secondkey的值
    VALUE secondkey 0 6
    hello!
    END
    get secondkey                   <-- 说明：在30s内能够获取到secondkey的值
    VALUE secondkey 0 6
    hello!
    END
    get secondkey                   <-- 说明：在30s内能够获取到secondkey的值
    VALUE secondkey 0 6
    hello!
    END
    get secondkey                   <-- 说明：超过30s后，获取不到secondkey的值，说明secondkey已经过期
    END

设置无返回数据::

    set noreplykey 0 900 6 noreply
    123456            <-- 说明：设置成功后，并没有返回STORED
    get noreplykey
    VALUE noreplykey 0 6
    123456
    END
    
- 存储正确时，输出信息为 ``STORED`` ，表示已经存储成功。
- 存储失败时，输出信息为 ``ERROR`` ，表示存储失败。

键值设置错误时的输出::

    set test 0 900 6
    1234567890            <-- 说明：此处输入的值是10byte，而缓存存储只指定存储字节数是6byte，超过允许的范围
    CLIENT_ERROR bad data chunk
    ERROR
    set test 0 900 6
    1234
    56                    <-- 说明：此处指定存储字节数是6byte，但存储值分两行写，也导致存储错误
    CLIENT_ERROR bad data chunk
    ERROR

- ``add`` 命令，将value存储在指定的key键中。
- 如果key存在，且未过期，则不会更新数据，并返回响应 ``NOT_STORED``。
- 如果key存在，且已经过期，则会更新数据。
- 如果key不存在，则会添加数据，作用同 ``set`` 。

语法如下::

    add key flags exptime bytes [noreply] 
    value 
    
    参数说明:
    key：键值 key-value 结构中的 key，用于查找缓存值。
    flags: 可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息。
    exptime: 在缓存中保存键值对的时间长度(以秒为单位，0 表示永远)。
    bytes: 在缓存中存储的字节数。
    noreply: 可选参数，该参数告诉服务器不需要返回数据。
    value: 键值 key-value 结构中的 value，存储的值，始终位于第二行。

设置一个键值对::
    
    get firstkey                  <-- 说明：能够获取到firstkey的值
    VALUE firstkey 0 16
    hello,memcached!
    END
    get seondkey                  <-- 说明：不能够获取到secondkey的值，因为secondkey键已经过期
    END
    add firstkey 0 900 5          <-- 说明：尝试对firstkey键进行更新，未能成功
    hello
    NOT_STORED                    <-- 说明：返回NOT_STORED
    add secondkey 0 900 5         <-- 说明：尝试对secondkey键进行更新，成功
    hello
    STORED                        <-- 说明：返回STORED
    add thirdkey 0 900 5          <-- 说明：尝试对thirdkey键进行更新，成功，因为thirdkey键不存在，所以相当于设置键值对
    hello
    STORED                        <-- 说明：返回STORED
    get firstkey                  <-- 说明：获取到firstkey的值，但值未更新
    VALUE firstkey 0 16
    hello,memcached!
    END
    get secondkey                  <-- 说明：获取到secondkey的值，但值已经更新
    VALUE secondkey 0 5
    hello
    END
    get thirdkey                  <-- 说明：获取到thirdkey的值，但值已经更新
    VALUE thirdkey 0 5
    hello
    END























python3-memcached处理NoSQL非关系型数据库memcached
-----------------------------------------------------



redis模块处理NoSQL非关系型数据库Redis
-----------------------------------------------------


参考文献:

- `sqlite3 — DB-API 2.0 interface for SQLite databases <https://docs.python.org/3/library/sqlite3.html>`_
- `Welcome to PyMySQL’s documentation! <https://pymysql.readthedocs.io/en/latest/index.html>`_
- `SQLAlchemy 1.3 Documentation: Object Relational Tutorial <https://docs.sqlalchemy.org/en/13/orm/tutorial.html>`_
- `SQLAlchemy 1.3 Documentation: Working with Engines and Connections <https://docs.sqlalchemy.org/en/13/core/connections.html#sqlalchemy.engine.Engine.execute>`_
- `SQLAlchemy 1.3 Documentation: Engine Configuration <https://docs.sqlalchemy.org/en/13/core/engines.html#sqlalchemy.create_engine>`_
- `SQLAlchemy 1.3 Documentation: Database Urls <https://docs.sqlalchemy.org/en/13/core/engines.html?highlight=database%20url#database-urls>`_
- `SQLAlchemy 1.3 Documentation: Query API <https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query>`_
- `dataset: databases for lazy people <https://dataset.readthedocs.io/en/latest/>`_
- `dataset: databases for lazy people: API documentation <https://dataset.readthedocs.io/en/latest/api.html>`_
- `dataset: databases for lazy people: Quickstart <https://dataset.readthedocs.io/en/latest/quickstart.html>`_
- `Python的"懒人"包DataSet解析 <https://cloud.tencent.com/developer/article/1376850>`_
