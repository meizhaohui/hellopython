#!/usr/bin/python3
"""
@Time    : 2019/3/31
@Author  : Mei Zhaohui
@Email   : mzh.whut@gmail.com
@Filename: person.py
@Software: PyCharm
@Desc    :  basic class
"""


class Person:
    """say hello & count the num"""  # 定义类的docstring
    num = 0  # 定义类变量

    # 定义类的方法
    # 初始化类
    def __init__(self, name):
        """initializes the person's data"""  # 定义方法的docstring
        self.name = name  # 定义实例变量
        print('(Initizlizing %s)' % self.name)
        Person.num += 1  # 对类的变量进行操作

    def say_hi(self):
        """Say Hello to someone"""
        print('Hello，%s,how are you?' % self.name)

    def print_all(self):
        """Count the sum"""
        print('Sum is:%s' % Person.num)


def main():
    """main function"""
    print(Person.__doc__)
    print(Person.say_hi.__doc__)

    person1 = Person('Hanmeimei')
    person1.say_hi()
    person1.print_all()
    person2 = Person('Lilei')
    person2.say_hi()
    person2.print_all()


if __name__ == '__main__':
    main()

