.. _univeral_unique_identifier:

模块-UUID模块
======================

.. contents:: 目录

背景知识
----------------------

UUID: 通用唯一标识符 ( Universally Unique Identifier )，对于所有的UUID它可以保证在空间和时间上的唯一性。它是通过MAC地址，时间戳，命名空间，随机数，伪随机数来保证生成ID的唯一性，有着固定的大小( 128 bit )。 它的唯一性和一致性特点使得可以无需注册过程就能够产生一个新的UUID。UUID可以被用作多种用途，既可以用来短时间内标记一个对象，也可以可靠的辨别网络中的持久性对象。

为什么要使用UUID？
----------------------

很多应用场景需要一个id，但是又不要求这个id 有具体的意义，仅仅用来标识一个对象. 常见的例子有数据库表的id 字段。另一个例子是前端的各种UI库，因为它们通常需要动态创建各种UI元素，这些元素需要唯一的id ，这时候就需要使用UUID了。

最近使用Flask-WTF构建web网站时，使用uuid生成一个随机的文件名，用于保存用户上传的图片。


UUID模块基本介绍
----------------------

python的uuid模块提供UUID类和函数uuid1(), uuid3(), uuid4(), uuid5() 来生成1, 3, 4, 5各个版本的UUID。 ( 需要注意的是: **python中没有uuid2()这个函数**) 对UUID模块中最常用的几个函数总结如下:

- uuid.uuid1(\[node\[, clock_seq\]])  
    使用主机ID, 序列号, 和当前时间来生成UUID, 可保证全球范围的唯一性. 但由于使用该方法生成的UUID中包含有主机的网络地址, 因此 **可能危及隐私** 。

- uuid.uuid3(namespace, name)  
    通过计算命名空间和名字的MD5散列值来生成UUID, 可以保证同一命名空间中不同名字的唯一性和不同命名空间的唯一性, 但同一命名空间的同一名字生成的UUID相同。

- uuid.uuid4()
    通过随机数来生成UUID. 使用的是伪随机数有一定的重复概率。

- uuid.uuid5(namespace, name)  
    通过计算命名空间和名字的SHA-1散列值来生成UUID, 算法与 uuid.uuid3()相同。
    
UUID可能概率重复吗？
----------------------

参考https://bbs.csdn.net/topics/390045377 网站上MIceRice的说法，**概率重复的可能性非常非常非常的小，可以忽略不计**。

    与被陨石击中的机率比较的话，已知一个人每年被陨石击中的机率估计为170亿分之1，也就是说机率大约是0.00000000006 (6 x 10 -11)，等同于在一年内建立数十兆笔UUID并发生一次重复。换句话说，每秒产生10亿笔UUID，100年后只产生一次重复的机率是50%。如果地球上每个人都各有6亿笔UUID，发生一次重复的机率是50%。
    
UUID模块的使用
----------------------

- UUID.bytes 将UUID实例转成16字节字符串，转换后成bytes类型。
- UUID.hex 将UUID实例转成32个字符的十六进制字符串，转换后成str类型。
- uuid.NAMESPACE_DNS 指定此命名空间时，名称字符串是完全限定的域名。
- uuid.NAMESPACE_URL 指定此命名空间时，名称字符串是URL。

使用示例::

    In [1]: import uuid                                     
                                                            
    In [2]: uuid.uuid1()                                    
    Out[2]: UUID('5618a8d0-e8e6-11e8-aff6-fddbb68775a4')    
                                                            
    In [3]: uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')    
    Out[3]: UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')    
                                                            
    In [4]: uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')    
    Out[4]: UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')    
                                                            
    In [5]: uuid.uuid4()                                    
    Out[5]: UUID('348e2893-2e43-45a1-ad25-fcc7bdce796a')    

    In [6]: uuid.uuid4().hex
    Out[6]: '7e6d9aa5e3424455b4a6533b3094fb4f'

    In [7]: uuid.uuid4().bytes
    Out[7]: b'[a\\xda\\xafk\\xadEr\\x9d*\\rVq\\xb4\\xc1\\xea'

    
使用uuid产生随机文件名::

    #!/usr/bin/python3
    """
    @Author  : 梅朝辉 Meizhaohui
    @Email   : mzh.whut@gmail.com

    @Time    : 2018/11/15 22:58
    @File    : use_uuid.py
    @Version : 1.0
    @Interpreter: Python3.6.2
    @Software: PyCharm

    @Description:  使用UUID模块生成随机文件名
    """
    import os
    import uuid


    def random_filename(filename):
        # 获取扩展名
        extension = os.path.splitext(filename)[1]
        # uuid.uuid4().hex生成32位的随机字符
        # 生成随机文件名
        new_filename = uuid.uuid4().hex + extension
        return new_filename


    if __name__ == '__main__':
        filename = 'python.png'
        print(random_filename(filename))
        # output like: 606ab1d636b04e139d54ddaf8a177cfe.png


参考文献：

- Python_uuid 学习总结 https://www.cnblogs.com/lijingchn/p/5299000.html 
- 官方文档 https://docs.python.org/3/library/uuid.html
- UUID会重复吗 https://bbs.csdn.net/topics/390045377
