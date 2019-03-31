#!/usr/bin/python3
"""
@Time    : 2019/3/31
@Author  : Mei Zhaohui
@Email   : mzh.whut@gmail.com
@Filename: class_inheritance.py
@Software: PyCharm
@Desc    : Class Inheritance

    使用一个程序来记录学校的教师和学生情况
    教师和学生有一些共同属性，如姓名、年龄；
    教师有专有属性，如薪水、课程；
    学生有专有属性，如班级、学费。

    创建一个共同的类SchoolMember，称为父类或超类，然后让教师和学生的类继承这个公共的类；
    教师使用Teacher类，称为子类，继承SchoolMember类；
    学生使用Student类，称为子类，继承SchoolMember类；
"""


class SchoolMember:
    """父类，基础类SchoolMember"""

    def __init__(self, name, age):
        """父类构造方法"""
        self._name = name  # 定义内部变量
        self._age = age  # 定义内部变量
        print("(Initialized SchoolMember: %s)" % self._name)

    def tell(self):
        """打印详情"""
        print("Name is:%s \nAge is:%s" % (self._name, self._age))


class Teacher(SchoolMember):
    """子类Teacher,继承父类SchoolMember"""

    def __init__(self, name, age, salary):
        """子类覆盖父类构造方法，新增一个salary参数"""
        super().__init__(name, age)  # 显式调用父类super()方法与使用上一行的代码等价，此时不用加self参数
        self._salary = salary
        print("(Initialized Teacher: %s)" % self._name)

    def tell(self):
        """子类覆盖父尖方法"""
        super().tell()  # 调用父类的tell方法
        print("Salary is:%s" % self._salary)


class Student(SchoolMember):
    """子类Student,继承父类SchoolMember"""

    def __init__(self, name, age, fee):
        """子类覆盖父类构造方法，新增一个fee参数"""
        SchoolMember.__init__(self, name, age)
        self._fee = fee
        print("(Initialized Teacher: %s)" % self._name)

    def tell(self):
        SchoolMember.tell(self)  # 调用父类的tell方法，将Student作为父类SchoolMember的一个实例
        print("Fee is:%s" % self._fee)


def main():
    """主方法"""
    teacher1 = Teacher('John', 24, 10000)
    teacher1.tell()
    student1 = Student('Tim', 18, 7500)
    student1.tell()


if __name__ == '__main__':
    main()
