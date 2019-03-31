#!/usr/bin/python3
"""
@Time    : 2019/3/31
@Author  : Mei Zhaohui
@Email   : mzh.whut@gmail.com
@Filename: class_static_method.py
@Software: PyCharm
@Desc    : class method and static method
"""


class PrintName:
    """display the class method and static method"""
    count = 0

    def __init__(self, input_name):
        PrintName.count += 1
        # 为了隐藏内部特性，可以使用两个下划线开头去定义内部隐藏变量，如(__name)
        self.__name = input_name
        print("使用静态方法打印欢迎词：")
        PrintName.welcome()

    @property
    # @property 用于指示getter方法
    def name(self):
        print("inside the getter!")
        return self.__name

    @name.setter
    # @name.setter用于指示setter方法
    def name(self, input_name):
        print("inside the setter!")
        self.__name = input_name

    def print_name(self):
        print("Your name is :", self.__name)

    @classmethod
    # @classmethod类方法，作用于整个类
    def sum(cls):
        print("The sum is", cls.count)

    @staticmethod
    def welcome():
        print("Welcome to join us")


def main():
    one_object = PrintName('mei')
    print("获取名称:")
    print(one_object.name)
    print("重新设置名称:")
    one_object.name = 'meizhaohui'
    print("重新获取名称:")
    print(one_object.name)
    print("使用print_name方法打印名称:")
    one_object.print_name()
    print("使用类方法打印总人数:")
    PrintName.sum()
    print("=" * 50)
    two_object = PrintName('kawaii')
    print("获取名称:")
    print(two_object.name)
    print("使用类方法打印总人数:")
    PrintName.sum()
    print("=" * 50)
    three_object = PrintName('Manu Ginóbili')
    print("获取名称:")
    print(three_object.name)
    print("使用类方法打印总人数:")
    PrintName.sum()


if __name__ == '__main__':
    main()
