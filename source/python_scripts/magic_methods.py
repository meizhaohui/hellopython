#!/usr/bin/python3
"""
@Time    : 2019/3/31
@Author  : Mei Zhaohui
@Email   : mzh.whut@gmail.com
@Filename: magic_methods.py
@Software: PyCharm
@Desc    : Magic method
"""


class Word:
    """class word"""

    def __new__(cls, *args, **kwargs):
        """
        创建类，并返回类的实例，在创建类的对象时__new__方法首先被调用，然后再调用__init__方法
        在创建一个类的对象实例对象时，__new__必定会被调用，而__init__则不一定（pickle.load方式反序列化一个实例时不会调用）
        __new__方法需要返回该类的一个实例
        """
        print('Call __new__ method')
        return object.__new__(cls)

    def __init__(self, text):
        """
        可以理解__new__与__init__方法共同构成了构造函数
        __init__不能返回除None外的任何值
        __init__不需要指定return语句，直接隐式return None即可
        """
        print('Call __init__ method')
        self.__text = text

    def __del__(self):
        """
        析构函数
        在对象的生命周期结束时，__del__会被调用，可以将__del__理解为析构函数
        __del__定义的是当一个对象进行垃圾回收时候的行为
        x.__del__()并不是对del x的实现，但执行del x时会调用x.__del__()
        """
        print('Call __del__ method, {} will be deleted.'.format(self))

    def __str__(self):
        """
        实现类到字符串的转化，将一个类的实例变成字符串
        如果不定义__str__,则Python会去调用__repr__方法
        如果__repr__方法也找不到的话，则会将返回类的名称以及对象的内在地址
        如： Word: <__main__.Word object at 0x7efe3ad5fe48>
        __str__的返回结果可读性更强
        """
        print('Call __str__ method')
        # self.__class__.__name__ 代表着类的名称
        return '({}:{})'.format(self.__class__.__name__, self.__text)

    def __repr__(self):
        """
        实现类到字符串的转化，将一个类的实例变成字符串
        推荐每一个类至少添加__repr__方法，这样可以保证类到字符串的转化时始终有一个有效的转化方式
        """
        print('Call __repr__ method')
        return '({}:{})'.format(self.__class__.__name__, self.__text)

    def __len__(self):
        """
        定义当len(class_instance)被调用时的行为
        """
        print('Call __len__ method')
        return len(self.__text.replace(',', '').replace(' ', ''))

    def __add__(self, other):
        """
        two class instance add
        :param other: other class instance
        """
        print('Call __add__ method')
        return self.__text + ' and ' + other.__text

    def __eq__(self, other):
        """
        two class instance equal
        :param other: other class instance
        """
        print('Call __eq__ method')
        return self.__text.lower() == other.__text.lower()

    def __call__(self, text):
        """
        override () , class instance function
        replace the instance self to text
        """
        print('Call __call__ method')
        self.__text = text
        return self.__text


@Word
def test_call():
    print('test')


def main():
    """main function"""
    print('创建对象实例,将会调用__new__和__init__方法：')
    word1 = Word('I love Python')
    print('打印对象实例，将会调用__str__方法：')
    print('Word:', word1)
    print('=' * 30)
    print('调用__repr__方法：')
    print(repr(word1))
    print('调用__len__方法：')
    print(len(word1))
    print('创建对象实例,将会调用__new__和__init__方法：')
    word2 = Word('I love Go')
    print('调用__add__方法：')
    print(word1 + word2)
    print('创建对象实例,将会调用__new__和__init__方法：')
    word3 = Word('I LOVE PYTHON')
    print('调用__eq__方法：')
    print(word1 == word3)
    print('创建对象实例,将会调用__new__和__init__方法：')
    word4 = Word('I am the __call__ before')
    print('调用__call__方法：')
    word4('I am the __call__ after')
    test_call('ab')
    print('=' * 30)
    print('调用__del__方法，类对象并没有被删除：')
    word1.__del__()
    print('打印对象实例，将会调用__str__方法：')
    print('Word:', word1)
    print('使用del删除对象时，会调用__del__方法，类对象并没有被删除：')
    del word1
    print('程序运行完成后，会自动删除对象，结束对象的生命周期!')


if __name__ == '__main__':
    main()
