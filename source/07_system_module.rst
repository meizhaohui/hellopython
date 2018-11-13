.. _07_system_module:

模块-sys模块
======================

.. contents:: 目录

模块基本介绍
----------------------
- 模块是可被重用的代码文件；模块文件名必须以.py结尾；模块可以从其他程序输入以便利用它的功能。

引用模块语法::
    
    import module_name
    from module_name import *
    from module_name import fun_name
    from module_name import var_name
    
tab键的使用
------------------
模块中经常会定义很多方法，但我们通常是很难记住模块的方法的具体的名称是如何写的，这时我们在自己电脑上面构建一个tab.py模块，使自己的编译器在按下tab键后有联想功能，列出所有相关的方法或常量变量等信息，提高自己的开发效率。

tab.py的内容如下::

    import sys
    import readline
    import rlcompleter
    import atexit
    import os
    # need install the readline module
    # windows install: pip install pyreadline
    # linux install: pip install readline
    # tab completion
    readline.parse_and_bind('tab: complete')
    # history file
    # windows
    histfile = os.path.join(os.environ['HOMEPATH'], '.pythonhistory')
    # linux
    # histfile = os.path.join(os.environ['HOME'], '.pythonhistory') 
    try:
        readline.read_history_file(histfile)
    except IOError:
        pass
    atexit.register(readline.write_history_file, histfile)
    del os, histfile, readline, rlcompleter

将tab.py存放在自己python的安装目录下的Lib目录下，如 *D:\\Program Files (x86)\\python3.6.2\\Lib* 打开命令行窗口，输入python进入python编译环境。

使用tab键的方法::

    C:\>python
    Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import tab
    >>> import os
    >>> os.      [此处输入.点号后按tab键]
    os.DirEntry(                os.chdir(                   os.getcwd(                  os.set_inheritable(
    os.F_OK                     os.chmod(                   os.getcwdb(                 os.spawnl(
    os.MutableMapping(          os.close(                   os.getenv(                  os.spawnle(
    os.O_APPEND                 os.closerange(              os.getlogin(                os.spawnv(
    os.O_BINARY                 os.cpu_count(               os.getpid(                  os.spawnve(
    os.O_CREAT                  os.curdir                   os.getppid(                 os.st
    os.O_EXCL                   os.defpath                  os.isatty(                  os.startfile(
    os.O_NOINHERIT              os.device_encoding(         os.kill(                    os.stat(
    os.O_RANDOM                 os.devnull                  os.linesep                  os.stat_float_times(
    os.O_RDONLY                 os.dup(                     os.link(                    os.stat_result(
    os.O_RDWR                   os.dup2(                    os.listdir(                 os.statvfs_result(

sys模块的使用
------------------

- sys模块是系统模块，sys是system的简写。包含了与python解释器和环境有关的函数。

使用上面的方法查看sys模块常用方法::

    C:\>python
    Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import tab
    >>> import sys
    >>> sys.
    sys.api_version                sys.getcheckinterval(          sys.modules
    sys.argv                       sys.getdefaultencoding(        sys.path
    sys.base_exec_prefix           sys.getfilesystemencodeerrors( sys.path_hooks
    sys.base_prefix                sys.getfilesystemencoding(     sys.path_importer_cache
    sys.builtin_module_names       sys.getprofile(                sys.platform
    sys.byteorder                  sys.getrecursionlimit(         sys.prefix
    sys.call_tracing(              sys.getrefcount(               sys.ps1
    sys.callstats(                 sys.getsizeof(                 sys.ps2
    sys.copyright                  sys.getswitchinterval(         sys.set_asyncgen_hooks(
    sys.displayhook(               sys.gettrace(                  sys.set_coroutine_wrapper(
    sys.dllhandle                  sys.getwindowsversion(         sys.setcheckinterval(
    sys.dont_write_bytecode        sys.hash_info                  sys.setprofile(
    sys.exc_info(                  sys.hexversion                 sys.setrecursionlimit(
    sys.excepthook(                sys.implementation             sys.setswitchinterval(
    sys.exec_prefix                sys.int_info                   sys.settrace(
    sys.executable                 sys.intern(                    sys.stderr
    sys.exit(                      sys.is_finalizing(             sys.stdin
    sys.flags                      sys.last_traceback             sys.stdout
    sys.float_info                 sys.last_type(                 sys.thread_info
    sys.float_repr_style           sys.last_value                 sys.version
    sys.get_asyncgen_hooks(        sys.maxsize                    sys.version_info
    sys.get_coroutine_wrapper(     sys.maxunicode                 sys.warnoptions
    sys.getallocatedblocks(        sys.meta_path                  sys.winver
    >>> sys.

sys模块常用方法::

    sys.argv 获取正在执行的命令行参数的参数列表(list)
    sys.argv[0]         为脚本pathname名称
    sys.argv[1]         用户为脚本第1个参数
    sys.argv[2]         用户为脚本第2个参数
    sys.path            python目录列表，供python从中查找第三方扩展模块
    sys.platform        当前环境的平台，linux环境为'linux'，windows环境为'win32'
    sys.stdin           标准输入
    sys.stdout          标准输出
    sys.stderr          标准错误输出
    sys.getdefaultencoding():       获取系统当前编码，python3.6.2中为'utf-8'。
    sys.getfilesystemencoding():    获取系统当前编码，python3.6.2中为'utf-8'。
    sys.exit(N)         异常退出时，返回码为N。正常退出时为0。如sys.exit(-1)  。
    sys.ps1             获取python交互运行时的初始提示符
    sys.ps2             获取python交互运行时的继行(块)提示符
    
    >>> sys.path
    ['', 'D:\\Program Files (x86)\\python3.6.2\\python36.zip', 'D:\\Program Files (x86)\\python3.6.2\\DLLs', 'D:\\Program Files (x86)\\python3.6.2\\lib', 'D:\\Program Files (x86)\\python3.6.2', 'D:\\Program Files (x86)\\python3.6.2\\lib\\site-packages']
    >>> sys.platform
    'win32'
    >>> sys.stdin
    <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
    >>> sys.stdout
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
    >>> sys.stderr
    <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
    >>> sys.getdefaultencoding()
    'utf-8'
    >>> sys.getfilesystemencoding()
    'utf-8'
    >>> sys.ps1
    '>>> '
    >>> sys.ps2
    '... '
        
    
下面使用一个例子来加深理解::

    #!/usr/bin/python3
    # -*- coding: utf-8 -*-
    """
    # @Time          : 2018/6/30 14:58
    # @Author        : 梅朝辉(meizhaohui)
    # @Email         : mzh.whut@gmail.com
    # @Filename      : sys_arguments.py
    # @Description   : 测试sys模块的使用，获取外部参数、退出码
    # @Software      : PyCharm
    # @Python Version: python3.6.2

    """
    import sys


    def sys_arguments():
        if len(sys.argv) == 3:
            print("You are greatly!")
            print("the script pathname is: {}".format(sys.argv[0]))
            print("the first argument is: {}".format(sys.argv[1]))
            print("the second argument is: {}".format(sys.argv[2]))
            sys.exit()
        else:
            print("Use method: python {} arg1 arg2".format(sys.argv[0]))
            sys.exit(-1)

    sys_arguments()
    
在命令行窗口执行::

    D:\data\python_scripts>python sys_arguments.py first second
    You are greatly!
    the script pathname is: sys_arguments.py
    the first arguement is: first
    the second arguement is: second

    D:\data\python_scripts>echo %errorlevel%   [ 梅朝辉备注：windows环境下获得执行cmd命令后的返回值的方法 ]
    0

    D:\data\python_scripts>python sys_arguments.py
    Use method: python sys_arguments.py arg1 arg2

    D:\data\python_scripts>echo %errorlevel%
    -1
    
import 与from ... import的区别
---------------------------------
    
- import module 只是加载一个模块，相当于"把车给我"，对于模块中的函数、变量等，每次调用需要"module.function"或"module.var_name"。
- from ... import ... 可以加载模块，且可以加载模块中的类、函数或者特定的成员，相当于"把车里面的矿泉水给我"。因有可能多种模块中存在同样名称的成员或类等，建议少使用此这种方式。
- from ... import ... as new_name 导入某模块并重命名为new_name。

如，下面这种使用import方式导入sys模块，需要使用sys模块中的platform时，必须带上sys::
    
    >>> import sys
    >>> print(sys.platform)
    win32

如，下面这种使用from ... import方式导入sys模块，导入后可以直接使用sys模块中的常量ps1/ps2/platform等，不需要加sys::

    from sys import path,argv,platform
    >>> from sys import platform,ps1,ps2
    >>> ps1
    '>>> '
    >>> ps2
    '... '
    >>> platform
    'win32'
    
如，下面这种使用from ... import ... as new_name方式导入sys模块中的常量copyright，并重命令为RT，直接输入RT就以打印出版权信息::

    >>> from sys import copyright as RT
    >>> RT
    'Copyright (c) 2001-2017 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'