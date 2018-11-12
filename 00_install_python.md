# Python的安装



本文讲解python3.6.2的安装。

## Python下载地址


Python3.6.2安装文件的下载地址如下：https://www.python.org/downloads/release/python-362/

## CentOS上的安装方法


-   下载安装文件
```
    [root@localhost ~/download]# wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
```
-   解压
```
    [root@localhost ~/download]# tar -zxvf Python-3.6.2.tgz
```
-   安装readline-devel解决方向键、Backspace键出现特殊符号
```
    [root@localhost ~/download]# yum install readline-devel
```
-   检测你的安装平台的目标特征
```
    [root@localhost ~/download]# cd Python-3.6.2
    [root@localhost ~/download/Python-3.6.2]# ./configure 
```
-   安装
```
    [root@localhost ~/download/Python-3.6.2]# make
```
-   编译
```
    [root@localhost ~/download/Python-3.6.2]# make install
```
-   查看python3的版本
```
    [root@localhost ~/download/Python-3.6.2]# python -V
    Python 2.6.6
    [root@localhost ~/download/Python-3.6.2]# python3 -V
    Python 3.6.2
```
-    CentOS系统中默认自带有Python程序，且版本是较低版本的Python 
2.6.6，Python是Linux系统的基础软件，很多应用基于Python程序，不要随意改动系统的默认Python版本。
-   我们要使用Python 3.6.2时，可以使用python3启动:
```
    [root@localhost ~/download/Python-3.6.2]# python3
    Python 3.6.2 (default, Jun  8 2018, 22:28:47) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-18)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
```


为了更好的使用python程序，并且不影响系统的python2环境以及刚安装的python3环境，我们安装virtualenv创建隔绝的Python环境。

## python虚拟环境virtualenv的安装


-   安装:
```
    [root@localhost ~]# pip3 install virtualenv
    Collecting virtualenv
      Downloading https://files.pythonhosted.org/packages/b6/30/96a02b2287098b23b875bc8c2f58071c35d2efe84f747b64d523721dc2b5/virtualenv-16.0.0-py2.py3-none-any.whl (1.9MB)
        100% |████████████████████████████████| 1.9MB 5.9MB/s 
    Installing collected packages: virtualenv
    Successfully installed virtualenv-16.0.0

    [root@localhost ~]# virtualenv --version
    16.0.0
```

## python虚拟环境virtualenv的使用


-   创建virtual虚拟环境目录
```
    [blogsystem@localhost ~]$ mkdir venv
    [blogsystem@localhost ~]$ ls
    blogs_home  download  venv
```
-   创建virtual虚拟运行环境:
```
    [blogsystem@localhost ~]$ virtualenv venv
    Using base prefix '/usr/local'
    New python executable in /cloud/blogsystem/venv/bin/python3.6
    Also creating executable in /cloud/blogsystem/venv/bin/python
    Installing setuptools, pip, wheel...done.
```

> 如果加上参数\--no-site-packages，已经安装到系统Python环境中的所有第三方包都不会复制过来，会生成一个不带任何第三方包的"干净"的Python运行环境。

 ```
    [blogsystem@localhost ~]$ virtualenv --no-site-package env
    Using base prefix '/usr/local'
    New python executable in /cloud/blogsystem/env1/bin/python3.6
    Also creating executable in /cloud/blogsystem/env1/bin/python
    Installing setuptools, pip, wheel...done.
```


-   激活virtual虚拟运行环境venv.

```
    [blogsystem@localhost ~]$ source venv/bin/activate 
    (venv) [blogsystem@localhost ~]$ 
```
 
此时，命令行提示符发生了变化，有了(venv)前缀，表示当前处理名称为venv的python虚拟环境下。此时处于虚拟环境下，在该环境使用pip安装包，不会影响系统的Python环境，也不会影响他人的环境。


-   在虚拟环境venv下安装包
```
    (venv) [blogsystem@localhost ~]$ pip list
    Package    Version
    ---------- -------
    pip    10.0.1 
    setuptools 39.2.0 
    wheel      0.31.1 

    (venv) [blogsystem@localhost ~]$ pip install pymysql
    Collecting pymysql
      Downloading https://files.pythonhosted.org/packages/32/e8/222d9e1c7821f935d6dba8d4c60b9985124149b35a9f93a84f0b98afc219/PyMySQL-0.8.1-py2.py3-none-any.whl (81kB)
        100% |████████████████████████████████| 81kB 63kB/s 
    Installing collected packages: pymysql
    Successfully installed pymysql-0.8.1

    (venv) [blogsystem@localhost ~]$ pip list
    Package    Version
    ---------- -------
    pip    10.0.1 
    PyMySQL    0.8.1  
    setuptools 39.2.0 
    wheel      0.31.1 
```
-   导出虚拟环境venv下的所有包到requirements.txt文件
```
    (venv) [blogsystem@localhost ~]$ pip freeze > requirements.txt
    (venv) [blogsystem@localhost ~]$ ls
    blogs_home  download  requirements.txt  venv
    (venv) [blogsystem@localhost ~]$ cat requirements.txt 
    PyMySQL==0.8.1
```
-   在虚拟环境venv下卸载包
```
    (venv) [blogsystem@localhost ~]$ pip uninstall pymysql
    Uninstalling PyMySQL-0.8.1:
      Would remove:
        /cloud/blogsystem/venv/lib/python3.6/site-packages/PyMySQL-0.8.1.dist-info/*
        /cloud/blogsystem/venv/lib/python3.6/site-packages/pymysql/*
    Proceed (y/n)? y
      Successfully uninstalled PyMySQL-0.8.1
    (venv) [blogsystem@localhost ~]$ pip list
    Package    Version
    ---------- -------
    pip    10.0.1 
    setuptools 39.2.0 
    wheel      0.31.1 
```
-   退出虚拟环境venv:
```
    (venv) [blogsystem@localhost ~]$ deactivate 
    [blogsystem@localhost ~]$ 
```
-   删除虚拟环境venv，直接删除venv文件夹即可:
```
    [blogsystem@localhost ~]$ ls
    blogs_home  download  requirements.txt  venv
    [blogsystem@localhost ~]$ rm -rf venv/
    [blogsystem@localhost ~]$ ls
    blogs_home  download  requirements.txt
```
-   通过requirements.txt在虚拟环境中安装包:
``` {.sourceCode .shell}
[blogsystem@localhost ~]$ virtualenv venv
Using base prefix '/usr/local'
New python executable in /cloud/blogsystem/venv/bin/python3.6
Also creating executable in /cloud/blogsystem/venv/bin/python
Installing setuptools, pip, wheel...done.
[blogsystem@localhost ~]$ source venv/bin/activate
(venv) [blogsystem@localhost ~]$ pip list
Package    Version
---------- -------
pip    10.0.1 
setuptools 39.2.0 
wheel      0.31.1 
(venv) [blogsystem@localhost ~]$ pip install -r requirements.txt 
Collecting PyMySQL==0.8.1 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/32/e8/222d9e1c7821f935d6dba8d4c60b9985124149b35a9f93a84f0b98afc219/PyMySQL-0.8.1-py2.py3-none-any.whl
Installing collected packages: PyMySQL
Successfully installed PyMySQL-0.8.1
(venv) [blogsystem@localhost ~]$ pip list
Package    Version
---------- -------
pip    10.0.1 
PyMySQL    0.8.1  
setuptools 39.2.0 
wheel      0.31.1 
```


> 以上安装并没有配置pip安装所使用的源，默认为官方的源，受网络影响，有时安装可能会比较慢，同时，使用vitrualenv运行虚拟环境时，必须需要到特定的目录下才能启动虚拟环境，使用有些不便，下面针对以上两个问题，分别配置pip国内源，以及安装virtualenvwrapper来管理虚拟环境。


## pip国内镜像源配置


-   linux环境配置方法

更改默认配置，\~/.pip/pip.conf，一般这个文件需要自己创建:
```
    mkdir ~/.pip
    vim ~/.pip/pip.conf
```
在pip.conf文件中添加以下内容:
```
    [global]
    index-url = http://mirrors.aliyun.com/pypi/simple/
    [install]
    trusted-host = mirrors.aliyun.com
```
-   windows环境配置方法

在当前用户下目录，新建一个pip文件夹和pip.ini文件，并在pip.ini中添加以下内容:
```
    [global]
    index-url = http://mirrors.aliyun.com/pypi/simple/
    [install]
```
## pip常用命令


-   pip install package\_name 安装包
-   pip uninstall -y package\_name 卸载包
-   pip search package\_name 查询包名
-   pip list 列出安装了哪些包

## virtualenvwrapper的安装


-   linux环境配置方法

使用pip进行安装,可以发现pip源已经替换成的阿里云源:

    [root@localhost ~]# pip install virtualenvwrapper
    Looking in indexes: http://mirrors.aliyun.com/pypi/simple/
    Collecting virtualenvwrapper
      Downloading http://mirrors.aliyun.com/pypi/packages/2b/8c/3192e10913ad945c0f0fcb17e9b2679434a28ad58ee31ce0104cba3b1154/virtualenvwrapper-4.8.2-py2.py3-none-any.whl
    Requirement already satisfied: stevedore in /usr/local/lib/python3.6/site-packages (from virtualenvwrapper) (1.28.0)
    Requirement already satisfied: virtualenv in /usr/local/lib/python3.6/site-packages (from virtualenvwrapper) (16.0.0)
    Requirement already satisfied: virtualenv-clone in /usr/local/lib/python3.6/site-packages (from virtualenvwrapper) (0.3.0)
    Requirement already satisfied: six>=1.10.0 in /usr/local/lib/python3.6/site-packages (from stevedore->virtualenvwrapper) (1.11.0)
    Requirement already satisfied: pbr!=2.1.0,>=2.0.0 in /usr/local/lib/python3.6/site-packages (from stevedore->virtualenvwrapper) (4.0.4)
    Installing collected packages: virtualenvwrapper
    Successfully installed virtualenvwrapper-4.8.2

创建虚拟目录:

    [root@localhost ~]# mkdir virtual_env

在\~/.bashrc中末尾添加配置信息，并保存:

    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export WORKON_HOME=/root/virtual_env
    source /usr/local/bin/virtualenvwrapper.sh 

使配置信息的修改生效:

    [root@localhost ~]# source ~/.bashrc

-   windows环境配置方法

使用pip进行安装,可以发现pip源已经替换成的阿里云源:

    E:\meichaohui\sphinx_data\meizhaohui_blog>pip install virtualenvwrapper-win
    Looking in indexes: http://mirrors.aliyun.com/pypi/simple/
    Collecting virtualenvwrapper-win
      Downloading http://mirrors.aliyun.com/pypi/packages/f5/23/4cba98733b9122219ce67177d745e4984b524b867cf3728eaa807ea21919/virtualenvwrapper-win-1.2.5.tar.gz
    Requirement already satisfied: virtualenv in d:\program files (x86)\python3.6.2\lib\site-packages (from virtualenvwrapper-win) (16.0.0)
    Installing collected packages: virtualenvwrapper-win
      Running setup.py install for virtualenvwrapper-win ... done
    Successfully installed virtualenvwrapper-win-1.2.5

创建虚拟目录:

    在D:\data目录下创建虚拟目录virtualenv_home。

配置环境变量:

    依次打开 控制面板\系统和安全\系统\高级系统设置\高级\环境变量，添加环境变量WORKON_HOME

    变量名：WORKON_HOME
    变量值：D:\data\virtualenv_home

virtualenvwrapper的使用
=======================

-   linux环境virtualenvwrapper获取帮助:

    [root@localhost ~]# virtualenvwrapper

    virtualenvwrapper is a set of extensions to Ian Bicking's virtualenv
    tool.  The extensions include wrappers for creating and deleting
    virtual environments and otherwise managing your development workflow,
    making it easier to work on more than one project at a time without
    introducing conflicts in their dependencies.

    For more information please refer to the documentation:

        http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html

    Commands available:

      add2virtualenv: add directory to the import path

      allvirtualenv: run a command in all virtualenvs

      cdproject: change directory to the active project

      cdsitepackages: change to the site-packages directory

      cdvirtualenv: change to the $VIRTUAL_ENV directory

      cpvirtualenv: duplicate the named virtualenv to make a new one

      lssitepackages: list contents of the site-packages directory

      lsvirtualenv: list virtualenvs

      mkproject: create a new project directory and its associated virtualenv

      mktmpenv: create a temporary virtualenv

      mkvirtualenv: Create a new virtualenv in $WORKON_HOME

      rmvirtualenv: Remove a virtualenv

      setvirtualenvproject: associate a project directory with a virtualenv

      showvirtualenv: show details of a single virtualenv

      toggleglobalsitepackages: turn access to global site-packages on/off

      virtualenvwrapper: show this help message

      wipeenv: remove all packages installed in the current virtualenv

      workon: list or change working virtualenvs

-   windows环境virtualenvwrapper获取帮助:

    D:\data> virtualenvwrapper

     virtualenvwrapper is a set of extensions to Ian Bicking's virtualenv
     tool.  The extensions include wrappers for creating and deleting
     virtual environments and otherwise managing your development workflow,
     making it easier to work on more than one project at a time without
     introducing conflicts in their dependencies.

     virtualenvwrapper-win is a port of Dough Hellman's virtualenvwrapper to Windows
     batch scripts.

     Commands available:

       add2virtualenv: add directory to the import path

       cdproject: change directory to the active project

       cdsitepackages: change to the site-packages directory

       cdvirtualenv: change to the $VIRTUAL_ENV directory

       lssitepackages: list contents of the site-packages directory

       lsvirtualenv: list virtualenvs

       mkproject: create a new project directory and its associated virtualenv

       mkvirtualenv: Create a new virtualenv in $WORKON_HOME

       rmvirtualenv: Remove a virtualenv

       setprojectdir: associate a project directory with a virtualenv
       toggleglobalsitepackages: turn access to global site-packages on/off

       virtualenvwrapper: show this help message

       whereis: return full path to executable on path.

       workon: list or change working virtualenvs

::: {.note}
::: {.admonition-title}
Note
:::

通过上面的帮助，可以知道linux系统和windows系统上面virtualenvwrapper大部分命令相同，下面在windows上面使用virtualenvwrapper。
:::

-   virtualenvwrapper常用命令:

    * workon:列出虚拟环境列表
    * lsvirtualenv:列出虚拟环境列表
    * mkvirtualenv [virtualenv_name]:新建虚拟环境
    * workon [virtualenv_name]:切换虚拟环境
    * rmvirtualenv  [virtualenv_name]:删除虚拟环境
    * deactivate: 离开虚拟环境

示例:
```
    D:\data>workon

    Pass a name to activate one of the following virtualenvs:
    ==============================================================================
    venv

    D:\data>lsvirtualenv

    dir /b /ad "D:\data\virtualenv_home"
    ==============================================================================
    venv

    D:\data>mkvirtualenv venv_test
    Using base prefix 'd:\\program files (x86)\\python3.6.2'
    New python executable in D:\data\virtualenv_home\venv_test\Scripts\python.exe
    Installing setuptools, pip, wheel...done.

    (venv_test) D:\data>workon

    Pass a name to activate one of the following virtualenvs:
    ==============================================================================
    venv
    venv_test

    (venv_test) D:\data>lsvirtualenv

    dir /b /ad "D:\data\virtualenv_home"
    ==============================================================================
    venv
    venv_test

    (venv_test) D:\data>workon venv_test
    (venv_test) D:\data>pip install pymysql
    Looking in indexes: http://mirrors.aliyun.com/pypi/simple/
    Collecting pymysql
      Downloading http://mirrors.aliyun.com/pypi/packages/32/e8/222d9e1c7821f935d6dba8d4c60b9985124149b35a9f93a84f0b98afc219/PyMySQL-0.8.1-py2.py3-none-any.whl (81kB)
    100% |████████████████████████████████| 81kB 989kB/s
    Installing collected packages: pymysql
    Successfully installed pymysql-0.8.1

    (venv_test) D:\data>rmvirtualenv venv_test

    Deleted D:\data\virtualenv_home\venv_test

    (venv) D:\data>deactivate

    D:\data>
```
