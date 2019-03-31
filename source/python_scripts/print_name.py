#!/usr/bin/python3
"""
@Time    : 2019/3/31
@Author  : Mei Zhaohui
@Email   : mzh.whut@gmail.com
@Filename: print_name.py
@Software: PyCharm
@Desc    : class property
"""


class PrintName:
    """print user name"""
    def __init__(self, input_name):
        """构造方法"""
        # 为了隐藏内部特性，可以使用两个下划线开头去定义内部隐藏变量，如(__name)
        self.__name = input_name

    @property  # @property 用于指示getter方法
    def name(self):
        """get the name attribute"""
        print("inside the getter!")
        return self.__name

    @name.setter  # @name.setter用于指示setter方法
    def name(self, input_name):
        """set the name attribute"""
        print("inside the setter!")
        self.__name = input_name

    def print_name(self):
        """print name"""
        print("Your name is :", self.__name)


def main():
    """main function"""
    pn_object1 = PrintName('mei')
    print("获取名称:")
    print(pn_object1.name)
    print("重新设置名称:")
    pn_object1.name = 'meichaohui'
    print("重新获取名称:")
    print(pn_object1.name)
    print("使用print_name方法打印名称:")
    pn_object1.print_name()
    print(pn_object1._PrintName__name)


if __name__ == '__main__':
    main()
