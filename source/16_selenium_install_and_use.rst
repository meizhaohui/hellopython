.. _16_selenium_install_and_use:

Selenium安装与使用
================================

Python3.6.2下载 
--------------------------------
下载地址： https://www.python.org/downloads


python -V 查看python版本::

    D:\Desktop>python -V
    Python 3.6.2


selenium安装
--------------------------------

使用pip安装selenium::

    D:\Desktop>pip install selenium
    Collecting selenium
      Downloading https://files.pythonhosted.org/packages/5e/1f/6c2204b9ae14eddab615c5e2ee4956c65ed533e0a9986c23eabd801ae849/selenium-3.11.0-py2.py3-none-any.whl (943kB)
        100% |████████████████████████████████| 952kB 644kB/s
    Installing collected packages: selenium
    Successfully installed selenium-3.11.0


Pycharm 下载
-------------------------------
下载地址： https://www.7down.com/soft/4338.html

破解方法： http://www.imsxm.com/jetbrains-license-server.html    

chromedriver驱动下载
-------------------------------

chromedriver下载地址： http://chromedriver.storage.googleapis.com/index.html

下载完成后，将解压的chromedriver.exe文件复制到Python的安装目录中的Scripts文件夹中，如D:\\Program Files (x86)\\python3.6.2\\Scripts 文件夹下。

**chromedriver版本与chrome各版本如下表**：

+----------------------+--------------------+--------------------+
|   ChromeDriver版本   |  支持的Chrome版本  |     发布时间       |
+======================+====================+====================+
|  ChromeDriver v2.38  |      v65-67        |    2018-04-17      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.37  |      v64-66        |    2018-03-16      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.36  |      v63-65        |    2018-03-02      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.35  |      v62-64        |    2018-01-10      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.34  |      v61-63        |    2017-12-10      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.33  |      v60-62        |    2017-10-03      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.32  |      v59-61        |    2017-08-30      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.31  |      v58-60        |    2017-07-21      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.30  |      v58-60        |    2017-06-07      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.29  |      v56-58        |    2017-04-04      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.28  |      v55-57        |    2017-03-09      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.27  |      v54-56        |    2016-12-23      |
+----------------------+--------------------+--------------------+
|  ChromeDriver v2.26  |      v53-55        |    2016-12-09      |
+----------------------+--------------------+--------------------+

用 Chrome 浏览器来测试::

    #!/usr/bin/env python
    #coding=utf-8     #解决编码问题
    """
    @python version: python3.6.2
    @author: 'meichaohui'
    @contact: mzh.whut@gmail.com
    @software: PyCharm
    @filename: openweb.py
    @time: 2017/10/5 22:35
    @version: V1.0
    """
    # 引入selenium测试工具中的webdriver模块
    from selenium import webdriver
    # 使用Chrome驱动
    browser = webdriver.Chrome()
    # 打开百度主页
    print('窗口最大化')
    browser.maximize_window()
    browser.get('http://www.baidu.com/')
    # 打印页面标题
    print('当前页面标题',browser.title)
    print('当前页面地址',browser.current_url)
    browser.find_element_by_id("kw").send_keys("hopewait") # 查找到id为kw的输入框，并输入关键字
    browser.find_element_by_id('su').click() #查找到id为su的按钮，并进行点击
    print('退出！')
    browser.quit()


运行后，控制台输出如下::

    "D:\Program Files (x86)\python3.6.2\python.exe" D:/data/python_scripts/seleniumProjects/openweb.py
    窗口最大化
    当前页面标题 百度一下，你就知道
    当前页面地址 https://www.baidu.com/
    退出！

    进程已结束,退出代码0
   
 