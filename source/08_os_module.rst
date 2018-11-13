.. _08_os_module:

模块-os模块
======================

.. contents:: 目录

os模块基本介绍
----------------------
- os模块包含操作系统功能。
- os模快提供了一个便携的方式去使用操作系统的相关功能。
+ 如果你只是想要读取或写入文件请参阅 open()
+ 如果你想要操作路径，请参阅 os.path 模块
+ 如果你想要在命令行上读取所有文件中的所有行，请参阅 fileinput 模块
+ 需要创建临时文件和目录，请参阅 tempfile 模块
+ 需要高级的文件和目录处理请参见 shutil 模块
+ 生成新进程和检索其结果，请参阅subprocess模块

引用os模块语法::
    
    import os
    
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
    >>> os.
    os.DirEntry(                os.R_OK                     os.errno                    os.getcwdb(                 os.readlink(                os.supports_dir_fd
    os.F_OK                     os.SEEK_CUR                 os.error(                   os.getenv(                  os.remove(                  os.supports_effective_ids
    os.MutableMapping(          os.SEEK_END                 os.execl(                   os.getlogin(                os.removedirs(              os.supports_fd
    os.O_APPEND                 os.SEEK_SET                 os.execle(                  os.getpid(                  os.rename(                  os.supports_follow_symlinks
    os.O_BINARY                 os.TMP_MAX                  os.execlp(                  os.getppid(                 os.renames(                 os.symlink(
    os.O_CREAT                  os.W_OK                     os.execlpe(                 os.isatty(                  os.replace(                 os.sys
    os.O_EXCL                   os.X_OK                     os.execv(                   os.kill(                    os.rmdir(                   os.system(
    os.O_NOINHERIT              os.abc                      os.execve(                  os.linesep                  os.scandir(                 os.terminal_size(
    os.O_RANDOM                 os.abort(                   os.execvp(                  os.link(                    os.sep                      os.times(
    os.O_RDONLY                 os.access(                  os.execvpe(                 os.listdir(                 os.set_handle_inheritable(  os.times_result(
    os.O_RDWR                   os.altsep                   os.extsep                   os.lseek(                   os.set_inheritable(         os.truncate(
    os.O_SEQUENTIAL             os.chdir(                   os.fdopen(                  os.lstat(                   os.spawnl(                  os.umask(
    os.O_SHORT_LIVED            os.chmod(                   os.fsdecode(                os.makedirs(                os.spawnle(                 os.uname_result(
    os.O_TEMPORARY              os.close(                   os.fsencode(                os.mkdir(                   os.spawnv(                  os.unlink(
    os.O_TEXT                   os.closerange(              os.fspath(                  os.name                     os.spawnve(                 os.urandom(
    os.O_TRUNC                  os.cpu_count(               os.fstat(                   os.open(                    os.st                       os.utime(
    os.O_WRONLY                 os.curdir                   os.fsync(                   os.pardir                   os.startfile(               os.waitpid(
    os.P_DETACH                 os.defpath                  os.ftruncate(               os.path                     os.stat(                    os.walk(
    os.P_NOWAIT                 os.device_encoding(         os.get_exec_path(           os.pathsep                  os.stat_float_times(        os.write(
    os.P_NOWAITO                os.devnull                  os.get_handle_inheritable(  os.pipe(                    os.stat_result(
    os.P_OVERLAY                os.dup(                     os.get_inheritable(         os.popen(                   os.statvfs_result(
    os.P_WAIT                   os.dup2(                    os.get_terminal_size(       os.putenv(                  os.strerror(
    os.PathLike(                os.environ                  os.getcwd(                  os.read(                    os.supports_bytes_environ

os模块的使用
------------------

os模块常用方法::

    >>> import os
    >>> os.
    os.abort()                  # 终止python编译器，此时会直接退出python环境
    os.chdir(path)              # 改变当前工作路径
    os.cpu_count()              # 返回CPU数量
    os.getcwd()                 # 返回当前工作路径
    os.environ                  # 返回系统环境变量
    os.getenv('key')            # 返回指定key键的系统环境变量的值
    os.putenv('key','value')    # 给某环境变量赋值，但不会直接影响系统环境变量，可通过os.environ修改环境变量
    os.getlogin()               # 返回当前登陆用户名
    os.getpid()                 # 返回当前进程的pid
    os.getppid()                # 返回当前进程的父进程的pid
    os.name                     # 字符串指示当前使用平台。win->'nt'; Linux->'posix'
    os.curdir                   # 当前工作目录 ('.')
    os.pardir                   # 获取当前目录的父目录字符串名：('..')
    os.sep                      # 路径分隔符。win->'\\'; Linux->'/'
    os.altsep                   # 备用路径名分隔符
    os.linesep                  # 当前平台所使用的行终止符，win->"\r\n"; Linux->"\n"
    os.extsep                   # 扩展文件分隔符'.'
    os.path                     # posixpath或ntpath的路径
    os.pathsep                  # 文件路径分隔符
    os.defpath                  # 默认的可执行文件的搜索路径
    os.devnull                  # 空设备的文件路径 
    os.get_terminal_size()      # 终端窗口大小
    os.get_exec_path()          # 返回在启动进程时将搜索命名可执行文件（类似于shell）的目录列表
    os.link(src, dst)           # 创建源地址src的硬链接目标地址dst
                                    # src:这是来源路径，原来存在的路径
                                    # dst:这是原来不存在的目标路径
    os.readlink(path)           # 返回软链接所指向的文件
    os.symlink(src, dst)        # 创建地址src的软链接目标地址dst
    os.access(path,mode)        # 检验path是否有mode模式的权限，返回True/False
                                # mode可以为os.F_OK/os.R_OK/os.W_OK/os.X_OK
    os.F_OK                         # 作为os.access()的mode参数，测试path是否存在。
    os.R_OK                         # 作为os.access()的mode参数，测试path是否可读。
    os.W_OK                         # 作为os.access()的mode参数，测试path是否可写。
    os.X_OK                         # 作为os.access()的mode参数，测试path是否可执行。
    os.kill(pid, signal)        # 发送一个信号signal给进程id为pid的进程
    import signal               # signal需要加载signal模块
                                # windows上，可调用signal.SIGABRT退出进程,signal.SIGILL杀死进程
    os.system(cmd)      # 执行系统命令，使用subprocess模块
    os.listdir(path)    # 返回path指定的文件夹包含的文件或文件夹的名字的列表
    os.scandir(path)    # 返回path指定的文件夹的DirEntry对象的迭代器。(注：仅显示path目录层级的文件或文件夹，不会递归显示子文件夹中的数据!)
                        # 当目录文件很多时，使用此方法运行得更快。
                        # 并提供操作系统返回的附加数据的简单方法,如:
                        # entry.inode()            # 返回条目的inode编号
                        # entry.is_dir(follow_symlinks=True)
                        # 如果此条目是指向目录的目录或符号链接，则返回True;
                        # 如果条目是或指向任何其他类型的文件，或者如果它不再存在，则返回False。
                        # 如果follow_symlinks是False，则只有在此条目是目录（没有符号链接）时返回True;
                        #     如果条目是任何其他类型的文件或者如果它不再存在，则返回False。
                        # entry.is_file(follow_symlinks=True)
                        # 如果此条目是指向文件的文件或符号链接，则返回True;
                        # 如果条目是或指向目录或其他非文件条目，或者如果它不再存在，则返回False。
                        # 如果follow_symlinks是False，则只有在此条目是文件（没有符号链接）时返回True;
                        #     如果条目是目录或其他非文件条目，或者如果它不再存在，则返回False。
                        # entry.is_symlink()
                        # 如果此条目是符号链接（即使已损坏），则返回True;
                        # 如果条目指向目录或任何类型的文件，或者如果它不再存在，则返回False。
                        # entry.name            # 条目的基本文件名
                        # entry.path            # 条目的完整路径名
                        # entry.stat()          # 获取目录或文件的状态描述器。
    os.mkdir(path[, mode])       # 创建一个目录
    os.makedirs(path[, mode])    # 递归文件夹创建函数
    os.remove(file_path)         # 移除文件,不能删除目录
    os.rmdir(dir_path)           # 删除path指定的空目录，不能删除非空目录
    os.removedirs(dir_path)      # 递归删除空目录，注意：当使用windows打开相应的目录时，删除结果可能不一样
    os.rename(src, dst)          # 重命名文件或目录
    os.renames(old, new)         # 递归重命名文件或目录
    os.replace(src, dst)         # 重命名文件或目录
    os.unlink(file_path)         # 移除文件
    os.stat(path)                # 返回path文件的文件信息。返回文件的信息：
                                    # st_mode - 文件信息的掩码，包含了文件的权限信息，文件的类型信息(是普通文件还是管道文件，或者是其他的文件类型)
                                    # st_ino - 文件的i-node值
                                    # st_dev - 设备信息
                                    # st_nlink - 硬连接数
                                    # st_uid - 用户ID
                                    # st_gid - 组ID
                                    # st_size - 文件大小，以byte为单位
                                    # st_atime - 文件最近的访问时间
                                    # st_mtime - 文件最近的修改时间
                                    # st_ctime - 文件状态信息的修改时间（不是文件内容的修改时间）
    os.utime(path,times)         # 修改文件的访问时间和修改时间。
                                    # 如果times参数为None，则设置文件的访问时间和修改时间为当前的时间。
                                    # 否则，如果times参数不为空，则times参数是一个二元组(atime, mtime)，用于设置文件的访问时间st_atime和修改时间st_mtime。
    os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
        # 以自顶向下遍历目录树或者以自底向上遍历目录树，对每一个目录都返回一个三元组(dirpath, dirnames, filenames)。
        # 三元组(dirpath，dirnames，filenames)：
                dirpath :   遍历所在目录树的位置，是一个字符串对象
                dirnames :  目录树中的子目录组成的列表，不包括("."和"..")
                filenames : 目录树中的文件组成的列表

        # 如果可选参数topdown = True或者没有指定，则起始目录的三元组先于其子目录的三元组生成(自顶向下生成三元组);
        # 如果topdown = False，则起始目录的三元组在其子目录的三元组生成后才生成(自底向上生成三元组)。
        # 当topdown = True，os.walk()函数会就地修改三元组中的dirnames列表(可能是使用del或者进行切片），然后再使用os.walk()递归地处理剩余在dirnames列表中的目录。这种方式有助于加快搜索效率，可以指定特殊的遍历顺序。当topdown = False的时候修改dirnames是无效的，因为在使用自底向上进行遍历的时候子目录的三元组是先于上一级目录的三元组创建的。
        # 默认情况下，调用listdir()返回的错误会被忽略，如果可选参数onerror被指定，则onerror必须是一个函数，该函数有一个OSError实例的参数，这样可以允许在运行的时候即使出现错误的时候不会打断os.walk()的执行，或者抛出一个异常并终止os.walk()的运行。
        # 默认情况下，os.walk()遍历的时候不会进入符号链接，如果设置了可选参数followlinks = True，则可以进入符号链接。
        # 注意：当设置followlinks = True时，可能会出现循环遍历，因为符号链接可能会出现自己链接自己的情况，而os.walk()不会意识到这一点。
        # 注意：如果传递过去的路径名是一个相对路径，则不会修改当前的工作路径。

使用os模块的示例::

    >>> os.environ
    environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'ANDROID': 'D:\\Program Files\\ADB\\adb', 'COMMON
    PROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\
    Common Files', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'FP_NO_HOST_CHECK': 'NO', 'HOMEDRIVE': 'C:', 'NUMBER_OF_PROCESSORS': '4', 'OS': 'Windows_NT', 'PATH': 'C:\\Windows\\system32;C:\\Windows', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64
    Family 6 Model 42 Stepping 7, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows'})
    >>> os.getenv('SYSTEMROOT')
    'C:\\Windows'
    >>> os.getlogin()
    'meizhaohui'
    >>> os.getpid()     # python.exe的进程id
    6524
    >>> os.getppid()	# cmd.exe的进程id
    6120
    >>> os.getcwd()
    'D:\\'
    >>> os.getcwdb()
    b'D:\\'
    >>> os.name
    'nt'
    >>> os.curdir
    '.'
    >>> os.pardir
    '..'
    >>> os.cpu_count()
    4
    >>> os.sep
    '\\'
    >>> os.altsep
    '/'
    >>> os.linesep
    '\r\n'
    >>> os.extsep
    '.'
    >>> os.path
    <module 'ntpath' from 'D:\\ProgramFiles\\Python3.6.2\\lib\\ntpath.py'>
    >>> os.pathsep
    ';'
    >>> os.defpath
    '.;C:\\bin'
    >>> os.devnull
    'nul'
    >>> os.get_terminal_size()
    os.terminal_size(columns=145, lines=40)
    >>> os.get_exec_path()              # 返回在启动进程时将搜索命名可执行文件（类似于shell）的目录列表
    ['D:\\Program Files (x86)\\python3.6.2\\Scripts', 'D:\\Program Files (x86)\\python3.6.2\\', 'C:\\Windows\\system32', 'C:\\Windows', 'C:\\WINDOWS\\system32', 'C:\\WINDOWS', 'C:\\WINDOWS\\System32\\Wbem', 'C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\', 'D:\\Program Files\\Git\\cmd', 'D:\\Program Files (x86)\\Pandoc\\', 'D:\\mei_softs\\jdk_8u172\\jre\\bin', 'C:\\WINDOWS\\System32\\OpenSSH\\', 'D:\\Softs\\adb1.0.32\\adb', '']
    >>> import signal
    >>> os.kill(1388,signal.SIGABRT)    # 退出某进程
    >>> os.kill(5948,signal.SIGILL)     # 杀掉某进程
    >>> os.chdir('tmp')
    >>> os.getcwd()
    'D:\\tmp'
    >>> os.listdir()
    ['dir1', 'dir1_symlink', 'sys.txt', 'test1.txt', 'test2.txt', 'test3.txt']
    >>> os.mkdir('dir2')
    >>> os.listdir()
    ['dir1', 'dir1_symlink', 'dir2', 'sys.txt', 'test1.txt', 'test2.txt', 'test3.txt']
    >>> os.makedirs('dir3/dir3_1')
    >>> os.listdir()
    ['dir1', 'dir1_symlink', 'dir2', 'dir3', 'sys.txt', 'test1.txt', 'test2.txt', 'test3.txt']
    >>> os.makedirs('dir4/dir4_1/dir4_11')

    >>> os.remove('dir5/test5.txt')
    >>> os.rmdir('dir5')
    >>> os.rmdir('dir5/dir5_1')
    >>> os.makedirs('dir5/dir5_2/dir5_2_1')
    >>> os.removedirs('dir5/dir5_2/dir5_2_1')
    >>> os.listdir()
    ['dir1', 'dir1_symlink', 'dir2', 'dir3', 'dir4', 'dir5', 'sys.txt', 'test1.txt', 'test2.txt', 'test3.txt']
    >>> os.rename('test3.txt','test33.txt')
    >>> os.listdir()
    ['dir1', 'dir1_symlink', 'dir2', 'dir3', 'dir4', 'dir5', 'sys.txt', 'test1.txt', 'test2.txt', 'test33.txt']
    >>> os.renames('dir5/dir5_2/dir5_2_1','dir5/dir52/dir521')
    >>> os.rename('dir4/dir4_1','dir4/dir41')
    >>> os.replace('dir4/dir41','dir4/dir441')
    >>> os.unlink('test33.txt')
    >>> os.unlink('dir3/dir3_1/test3_1.txt')

    >>> os.stat('test1.txt')
    os.stat_result(st_mode=33206, st_ino=2814749767125765, st_dev=120385, st_nlink=1, st_uid=0, st_gid=0, st_size=39, st_atime=1, st_mtime=3, st_ctime=1513519788)
    >>> os.utime('test1.txt')
    >>> os.stat('test1.txt')
    os.stat_result(st_mode=33206, st_ino=2814749767125765, st_dev=120385, st_nlink=1, st_uid=0, st_gid=0, st_size=39, st_atime=1514211306, st_mtime=1514211306, st_ctime=1513519788)
    
使用os模块创建软硬链接
-----------------------------------

可以使用os.link创建硬链接，os.symlink创建软链接。

- os.link(src, dst)           # 创建源地址src的硬链接目标地址dst
- os.symlink(src, dst)        # 创建地址src的软链接目标地址dst


**src:这是源路径，原来存在的路径**

**dst:这是原来不存在的目标路径**

**如果python报"OSError: symbolic link privilege not held"错误，说明权限不足，可以使用"以管理员身份运行"cmd窗口，再打开python尝试创建软硬链接。**

创建软硬链接示例::

    >>> import os
    >>> os.getcwd()
    'D:\\tmp'
    >>> os.listdir()
    ['a.txt', 'data.csv', 'dir1', 'dir2']
    >>> os.link('a.txt','a.hard')
    >>> os.listdir()
    ['a.hard', 'a.txt', 'data.csv', 'dir1', 'dir2']
    >>> os.symlink('a.txt','a.soft')
    >>> os.listdir()
    ['a.hard', 'a.soft', 'a.txt', 'data.csv', 'dir1', 'dir2']


   
**windows cmd命令中使用MKLINK可以创建软硬链接，具体命令如下**::

    C:\>mklink
    创建符号链接。

    MKLINK [[/D] | [/H] | [/J]] Link Target

            /D      创建目录符号链接。默认为文件
                    符号链接。
            /H      创建硬链接而非符号链接。
            /J      创建目录联接。
            Link    指定新的符号链接名称。
            Target  指定新链接引用的路径(相对或绝对)。
                
使用os.scandir()迭代器文件目录下文件目录信息
-------------------------------------------------

使用os.scandir(path)迭代器获取path目录下的文件或目录，并打印相关属性::

    #!/usr/bin/python3
    # -*- coding: utf-8 -*-
    """
    # @Time          : 2018/6/30 20:48
    # @Author        : 梅朝辉(meizhaohui)
    # @Email         : mzh.whut@gmail.com
    # @Filename      : subdirs.py
    # @Description   : 使用迭代器获取path目录下的文件或目录，并打印相关属性
    # @Software      : PyCharm
    # @Python Version: python3.6.2

    """


    def subdirs(path):
        """使用迭代器获取path目录下的文件或目录，并打印相关属性"""
        import os
        for entry in os.scandir(path):
            if not entry.name.startswith('.'):
                print("name:", entry.name)
                print("path:", entry.path)
                print("is_file:", entry.is_file(follow_symlinks=True))
                print("is_dir:", entry.is_dir(follow_symlinks=False))
                print("is_symlink:", entry.is_symlink())
                print("stat:", entry.stat())
                print("="*50, '\n')


    if __name__ == '__main__':
        subdirs('D:\\tmp')
        
运行结果如下::

    "D:\Program Files (x86)\python3.6.2\python.exe" D:/data/python_scripts/subdirs.py
    name: a.hard
    path: D:\tmp\a.hard
    is_file: True
    is_dir: False
    is_symlink: False
    stat: os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=4, st_atime=1530364793, st_mtime=1530366353, st_ctime=1530363449)
    ================================================== 

    name: a.soft
    path: D:\tmp\a.soft
    is_file: True
    is_dir: False
    is_symlink: True
    stat: os.stat_result(st_mode=33206, st_ino=562949953471395, st_dev=2661556261, st_nlink=3, st_uid=0, st_gid=0, st_size=4, st_atime=1530364793, st_mtime=1530366353, st_ctime=1530363449)
    ================================================== 

    name: a.txt
    path: D:\tmp\a.txt
    is_file: True
    is_dir: False
    is_symlink: False
    stat: os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=4, st_atime=1530364793, st_mtime=1530366353, st_ctime=1530363449)
    ================================================== 

    name: data.csv
    path: D:\tmp\data.csv
    is_file: True
    is_dir: False
    is_symlink: False
    stat: os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=67, st_atime=1520171736, st_mtime=1520178110, st_ctime=1520171736)
    ================================================== 

    name: dir1
    path: D:\tmp\dir1
    is_file: False
    is_dir: True
    is_symlink: False
    stat: os.stat_result(st_mode=16895, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=0, st_atime=1530363233, st_mtime=1530363233, st_ctime=1530363233)
    ================================================== 

    name: dir2
    path: D:\tmp\dir2
    is_file: False
    is_dir: True
    is_symlink: False
    stat: os.stat_result(st_mode=16895, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=0, st_atime=1530363286, st_mtime=1530363286, st_ctime=1530363286)
    ================================================== 
 
使用os.walk()遍历目录树
------------------------------------------------- 

- 递归遍历目录树，生成目录树下所有文件的路径信息

walkdir.py代码如下::

    #!/usr/bin/python3
    # -*- coding: utf-8 -*-
    """
    # @Time          : 2018/6/30 22:03
    # @Author        : 梅朝辉(meizhaohui)
    # @Email         : mzh.whut@gmail.com
    # @Filename      : walkdir.py
    # @Description   : 递归遍历目录树，打印出所有文件路径
    # @Software      : PyCharm
    # @Python Version: python3.6.2

    """


    def walkdir(path):
        import os
        for root, dirs, files in os.walk(path, followlinks=False):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))


    if __name__ == '__main__':
        walkdir("D:\\tmp")
    
运行后，输出结果如下::

    "D:\Program Files (x86)\python3.6.2\python.exe" D:/data/python_scripts/walkdir.py
    D:\tmp\a.hard
    D:\tmp\a.soft
    D:\tmp\a.txt
    D:\tmp\data.csv
    D:\tmp\dir1
    D:\tmp\dir2
    D:\tmp\dir1\1.txt
    D:\tmp\dir2\2.txt
    D:\tmp\dir2\dir22
    D:\tmp\dir2\dir22\22.txt
    D:\tmp\dir2\dir22\dir222
    D:\tmp\dir2\dir22\dir222\222.txt

    进程已结束,退出代码0
    
- 删除整个目录的文件和文件夹

使用os.walk递归获取文件夹下的文件或文件夹信息，从最底层(也就是最内层)开始向最顶层操作，先删除底层文件，里面文件夹空了后，才能删除空的文件夹。

removeOneDir.py代码如下::

    #!/usr/bin/python3
    # -*- coding: utf-8 -*-
    """
    # @Time          : 2018/6/30 22:13
    # @Author        : 梅朝辉(meizhaohui)
    # @Email         : mzh.whut@gmail.com
    # @Filename      : removeOneDir.py
    # @Description   : 删除整个目录的文件和文件夹
    # @Software      : PyCharm
    # @Python Version: python3.6.2

    """


    def remove_one_dir(top_path):
        # 删除顶层目录top_path下的所有文件
        import os
        if not os.path.exists(top_path):
            print(top_path, 'not exists')
            return
        if not os.path.isdir(top_path):
            print(top_path, 'not a dirpath')
            return
        # 删除文件夹时，先删除里层文件，使文件夹为空，再删除文件夹
        for dir_path, dirs, files in os.walk(top_path, topdown=False, followlinks=False):
            print('the first for dir_path:{} dirs:{} files:{}'.format(dir_path, dirs, files))
            for file in files:
                file_path = os.path.join(dir_path, file)
                print("delete file:", file_path)
                os.remove(file_path)
            print("delete folder:", dir_path)
            os.rmdir(dir_path)
        print(top_path, "have been deleted successfully!")


    if __name__ == '__main__':
        remove_one_dir("D:\\tmp")
        
运行后，输出结果如下::

    "D:\Program Files (x86)\python3.6.2\python.exe" D:/data/python_scripts/removeOneDir.py
    the first for dir_path:D:\tmp\dir1 dirs:[] files:['1.txt']
    delete file: D:\tmp\dir1\1.txt
    delete folder: D:\tmp\dir1
    the first for dir_path:D:\tmp\dir2\dir22\dir222 dirs:[] files:['222.txt']
    delete file: D:\tmp\dir2\dir22\dir222\222.txt
    delete folder: D:\tmp\dir2\dir22\dir222
    the first for dir_path:D:\tmp\dir2\dir22 dirs:['dir222'] files:['22.txt']
    delete file: D:\tmp\dir2\dir22\22.txt
    delete folder: D:\tmp\dir2\dir22
    the first for dir_path:D:\tmp\dir2 dirs:['dir22'] files:['2.txt']
    delete file: D:\tmp\dir2\2.txt
    delete folder: D:\tmp\dir2
    the first for dir_path:D:\tmp dirs:['dir1', 'dir2'] files:['a.hard', 'a.soft', 'a.txt', 'data.csv']
    delete file: D:\tmp\a.hard
    delete file: D:\tmp\a.soft
    delete file: D:\tmp\a.txt
    delete file: D:\tmp\data.csv
    delete folder: D:\tmp
    D:\tmp have been deleted successfully!

    进程已结束,退出代码0

os.path模块操作路径
--------------------------------

os.path模块主要处理文件路径、文件属性相关的事务。

- os.path模块的方法

使用tab键查看os.path的方法::

    C:\Users>python
    Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import os.path
    >>> os.path.
    os.path.abspath(                   os.path.getctime(                  os.path.realpath(
    os.path.altsep                     os.path.getmtime(                  os.path.relpath(
    os.path.basename(                  os.path.getsize(                   os.path.samefile(
    os.path.commonpath(                os.path.isabs(                     os.path.sameopenfile(
    os.path.commonprefix(              os.path.isdir(                     os.path.samestat(
    os.path.curdir                     os.path.isfile(                    os.path.sep
    os.path.defpath                    os.path.islink(                    os.path.split(
    os.path.devnull                    os.path.ismount(                   os.path.splitdrive(
    os.path.dirname(                   os.path.join(                      os.path.splitext(
    os.path.exists(                    os.path.lexists(                   os.path.splitunc(
    os.path.expanduser(                os.path.normcase(                  os.path.stat
    os.path.expandvars(                os.path.normpath(                  os.path.supports_unicode_filenames
    os.path.extsep                     os.path.os                         os.path.sys
    os.path.genericpath                os.path.pardir
    os.path.getatime(                  os.path.pathsep
    >>> os.path.

os.path模块常用方法::

    os.path.abspath(path)       # path的绝对路径(即完整路径)
    os.path.basename(path)      # 返回path路径的基名，即：
                                    #        如果path是文件夹则返回最后一级的文件夹名称；
                                    #        如果path是文件，则返回文件名称。
    os.path.dirname(path)       # 返回path路径的目录名
    os.path.commonpath(paths)   # 返回路径系列paths最长的公共子路径sub-path
    os.path.commonprefix(paths)     # 返回路径系列paths的公共前缀
    os.path.exists(path)            # 路径是否存在
    os.path.isabs(path)             # 路径是否是绝对路径
    os.path.isdir(path)             # 路径是否是目录
    os.path.isfile(path)            # 路径是否是文件
    os.path.islink(path)            # 路径是否是软链接(symbolic link)
    os.path.ismount(path)           # 路径是否是挂载点
    os.path.join(path,*paths)       # 将一个或多个路径合并成一个完整的路径
    os.path.split(path)             # 将路径分割，返回由其目录名和基名给成的元组
    os.path.splitext(path)          # 分割文件名，返回由文件名和扩展名组成的元组
    os.path.realpath(path)          # 返回指定文件的标准路径(absolute path)，而非软链接所在的路径
    os.path.getatime(filename)      # 返回文件最后一次的访问时间，从1970年1月1日已经经过多少秒
    os.path.getctime(filename)      # 返回文件最后一次的改变时间，从1970年1月1日已经经过多少秒
    os.path.getmtime(filename)      # 返回文件最后一次的修改时间，从1970年1月1日已经经过多少秒
    os.path.getsize(filename)       # 返回文件的大小
    
os.path模块的示例::

    >>> os.path.abspath('dir3')
    'D:\\tmp\\dir3'
    >>> os.path.abspath('3.txt')
    'D:\\tmp\\3.txt'
    >>> os.path.basename('dir3')
    'dir3'
    >>> os.path.dirname('dir3')
    ''
    >>> os.path.dirname('D:\\tmp\\dir3')
    'D:\\tmp'
    >>> os.path.basename('D:\\tmp\\dir3')
    'dir3'
    >>> os.path.commonpath(['D:\\tmp\\dir1','D:\\tmp\\dir2','D:\\tmp\\dir3','D:\\tmp\\test1.txt'])
    'D:\\tmp'
    >>> os.path.commonpath(['D:\\tmp\\dir1','D:\\tmp\\dir2','D:\\tmp\\dir3','D:\\test1.txt'])
    'D:\\'
    >>> os.path.commonprefix(['D:\\tmp\\dir1','D:\\tmp\\dir2','D:\\tmp\\dir3'])
    'D:\\tmp\\dir'
    >>> os.path.commonprefix(['D:\\tmp\\dir1','D:\\tmp\\dir2','D:\\tmp\\dir3','D:\\tmp\\test1.txt'])
    'D:\\tmp\\'
    >>> os.path.exists('dir2')
    True
    >>> os.path.exists('D:\\tmp\\dir2')
    True
    >>> os.path.isabs('D:\\tmp\\dir2')
    True
    >>> os.path.isabs('dir2')
    False
    >>> os.path.isdir('dir2')
    True
    >>> os.path.isdir('test2.txt')
    False
    >>> os.path.isfile('test2.txt')
    True
    >>> os.path.isfile('dir2')
    False
    >>> os.symlink('test2.txt','test2_symlink.txt')
    >>> os.path.islink('test2_symlink.txt')
    True
    >>> os.path.islink('test2.txt')
    False
    >>> os.path.ismount('/boot')
    True
    >>> os.path.ismount('/')    
    True
    >>> os.path.ismount('/tmp')
    False
    >>> os.path.join('D:\\','tmp\\dir2')
    'D:\\tmp\\dir2'
    >>> os.path.split("D:\\tmp\\test1.txt")
    ('D:\\tmp', 'test1.txt')
    >>> os.path.split("D:\\tmp")
    ('D:\\', 'tmp')
    >>> os.path.splitext("D:\\tmp\\test1.txt")
    ('D:\\tmp\\test1', '.txt')
    >>> os.path.splitext("test1.txt")
    ('test1', '.txt')
    >>> os.path.realpath('test2.txt')
    'D:\\tmp\\test2.txt'
    >>> os.getcwd()
    'D:\\tmp'
    >>> os.path.realpath('test2.txt')
    'D:\\tmp\\test2.txt'
    >>> os.path.relpath("D:\\")
    '..'
    >>> os.path.relpath("D:\\tmp")
    '.'
    >>> os.path.relpath("D:\\tmp\\test2.txt")
    'test2.txt'
    >>> os.path.relpath("D:\\tmp\\dir2\\22.txt")
    'dir2\\22.txt'
    >>> os.path.getatime('test2.txt')
    1514796590.3527365
    >>> os.path.getctime('test2.txt')
    1514796590.3527365
    >>> os.path.getmtime('test2.txt')
    1515160582.7379878
    >>> os.path.getsize('test2.txt')
    5
    >>> import time
    >>> time.ctime(os.path.getatime('test2.txt'))
    'Mon Jan  1 16:49:50 2018'
    >>> time.ctime(os.path.getctime('test2.txt'))
    'Mon Jan  1 16:49:50 2018'
    >>> time.ctime(os.path.getmtime('test2.txt'))
    'Fri Jan  5 21:56:22 2018'
    


