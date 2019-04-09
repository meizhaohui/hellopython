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

修改数据表为mysql，并查询数据库中的表::

    In [6]: connection                                                                                                     
    Out[6]: <pymysql.connections.Connection at 0x157594142e8>                                                              
                                                                                                                            
    In [7]: connection.select_db('mysql')                                                                                  
                                                                                                                            
    In [8]: cursor = connection.cursor()                                                                                   
                                                                                                                            
    In [9]: cursor.execute('show tables')                                                                                  
    Out[9]: 31                                                                                                             
                                                                                                                            
    In [10]: print(cursor.fetchall())                                                                                       
    [{'Tables_in_mysql': 'column_stats'}, {'Tables_in_mysql': 'columns_priv'}, {'Tables_in_mysql': 'db'}, {'Tables_in_mysql'
    : 'event'}, {'Tables_in_mysql': 'func'}, {'Tables_in_mysql': 'general_log'}, {'Tables_in_mysql': 'gtid_slave_pos'}, {'Ta
    bles_in_mysql': 'help_category'}, {'Tables_in_mysql': 'help_keyword'}, {'Tables_in_mysql': 'help_relation'}, {'Tables_in
    _mysql': 'help_topic'}, {'Tables_in_mysql': 'host'}, {'Tables_in_mysql': 'index_stats'}, {'Tables_in_mysql': 'innodb_ind
    ex_stats'}, {'Tables_in_mysql': 'innodb_table_stats'}, {'Tables_in_mysql': 'plugin'}, {'Tables_in_mysql': 'proc'}, {'Tab
    les_in_mysql': 'procs_priv'}, {'Tables_in_mysql': 'proxies_priv'}, {'Tables_in_mysql': 'roles_mapping'}, {'Tables_in_mys
    ql': 'servers'}, {'Tables_in_mysql': 'slow_log'}, {'Tables_in_mysql': 'table_stats'}, {'Tables_in_mysql': 'tables_priv'}
    , {'Tables_in_mysql': 'time_zone'}, {'Tables_in_mysql': 'time_zone_leap_second'}, {'Tables_in_mysql': 'time_zone_name'},
     {'Tables_in_mysql': 'time_zone_transition'}, {'Tables_in_mysql': 'time_zone_transition_type'}, {'Tables_in_mysql': 'tra
    nsaction_registry'}, {'Tables_in_mysql': 'user'}]                                                                       
                                                                                                                            
       
SQLAlchemy ORM对象关系映射处理数据库
--------------------------------------------


懒人包dataset处理数据库
--------------------------------------------


python3-memcached处理NoSQL非关系型数据库memcached
-----------------------------------------------------



redis模块处理NoSQL非关系型数据库Redis
-----------------------------------------------------


参考文献:

- `sqlite3 — DB-API 2.0 interface for SQLite databases <https://docs.python.org/3/library/sqlite3.html>`_
- `Welcome to PyMySQL’s documentation! <https://pymysql.readthedocs.io/en/latest/index.html>`_