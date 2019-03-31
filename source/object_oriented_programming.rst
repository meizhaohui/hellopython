.. _object_oriented_programming:

面向对象编程
======================

.. contents:: 目录

面向对象编程基础
-------------------

两种范型：

- 以指令为核心：围绕"正在发生什么"进行编写；面向过程编程：程序具有一系列的线性步骤，主体思想是代码作用于数据。
- 以数据为核心：围绕"将影响谁"进行编写；面向对象编程(OOP,object_oriented_programming)：围绕数据及为数据严格定义的接口来组织程序，用数据控制对代码的访问。

基本概念
-------------------
 
- 类创建一个新类型，而对象则是类的实例；类和对象是面向对象编程的两个主要方面。
- 对象或类的变量称为域；类的函数称为类的方法；域和方法合称为类的属性。
- 域有两种类型：实例变量，类变量。
- 类使用class关键字创建，如class ClassName:
- 类名使用大写字母开头的单词，如CapWords,ClassName。
- 方法的第一个参数一定是self，表示对象本身。
- 方法用关键字def定义，如def method_name(self[,keyword]):
- __init__方法在类的实例创建时，马上运行，可以对对象进行初始化。

类的示例::

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


输出结果如下::

    say hello & count the num
    Say Hello to someone
    (Initizlizing Hanmeimei)
    Hello，Hanmeimei,how are you?
    Sum is:1
    (Initizlizing Lilei)
    Hello，Lilei,how are you?
    Sum is:2
    
面向对象编程的原则
----------------------------

面向对象的模型机制有3个原则：封装、继承和多态

- 封装(Encapsulation)

  #. 隐藏实现方案细节；
  #. 将代码及其处理的数据绑定在一起的一种编程机制，用于保证程序和数据不受外部干扰且不会被误用。

- 继承(Inheritance)

  #. 一个对象获得另一个对象属性的过程；用于实现按层分类的概念
  #. 一个深度继承的子类继承了类层次中它的每个祖先的所有属性
  #. 如果某些类具有相同的属性，可以将这些属性提取出来，构建一个父类，然后使用子类继承父类
  #. 子类会继承父类的方法,子类会自动获取父类的所有方法
  #. 子类也可以覆盖(override)的方法，也可以添加父类中没有的方法
  #. 在子类中，可以使用super()方法获取父类的定义
  #. 在子类中父类的初始化方法并不会自动调用，必须显示调用它，可以使用如super().__init__(name)来进行调用
  #. 使用super()方法时，不用传入self，只用传入其他参数即可，如name
  #. 在子类中覆盖父类的__init__构造方法时，在子类中父类的构造方法并不会自动调用，必须使用super().__init__(arg)显示调用父类的构造方法

  
- 多态(Polymorphism)

  #. 一个子类型在任何需要父类型的场合可以被替换成父类型，即对象可以被视作是父类的实例，这种现象称为多态形象。
        
示例::

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
            super().__init__(name, age)  # 显式调用父类super()方法与使用上一行的代码等价，此时不用加self参数,子类构造方法会自动将self参数传递给父类
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

运行结果如下::

    (Initialized SchoolMember: John)
    (Initialized Teacher: John)
    Name is:John 
    Age is:24
    Salary is:10000
    (Initialized SchoolMember: Tim)
    (Initialized Teacher: Tim)
    Name is:Tim 
    Age is:18
    Fee is:7500       

说明： 示例中使用两种方法调用父类的方法，如方式1： super().__init__(name, age)  ，方式2：SchoolMember.__init__(self, name, age)，推荐使用方式1进行调用，这样就算修改父类的名称，子类的方法代码也不需要修改。

        
Python构造器__init__()方法
----------------------------------

- 创建实例时，Python会自动调用类中的__init__方法，以隐性地为实例提供属性。
- **__init__方法被称为构造器或构造方法**。
- 如果类中没有定义__init__方法，实例创建时仅是一个简单的名称空间。
- 创建实例时，实例接收的参数会自动传送到构造器中。

如::

    >>> class LoveLanguage:
    ...     def __init__(self,name,lang):
    ...         self.name=name
    ...         self.lang=lang
    ...     def tell(self):
    ...         print("Your name is {} and you love to learn {}".format(self.name,self.lang))
    ...
    >>> c1=LoveLanguage('mei','python')
    >>> c1.tell()
    Your name is mei and you love to learn python

命名空间
--------------------

- python可以使用locals()和globals()获取局部或全局命名空间的字典。
- locals()     # 返回局部命名空间内容的字典；
- globals()    # 返回全局命名空间内容的字典。

如::

    >>> def test(*args):
    ...     data='test locals()'
    ...     print(locals())
    ...     print('args',args)
    ...
    >>> test('a','b')
    {'data': 'test locals()', 'args': ('a', 'b')}
    args ('a', 'b')
    >>> globals()
    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>
    , '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'test': <function test at 0x0000000002A4D620>}

使用装饰器(decorator)定义属性的访问和设置
------------------------------------------------

下面的例子中定义两个不同的方法，它们都叫name()，但包含不同的修饰符:

- @property,用于指示getter方法；
- @name.setter,用于指示setter方法。
- 使用__定义变量可以将名称重整，以保护私有特性，如__name。实际上名称被重整为_ClassName__name这样的。

print_name.py代码如下::

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
    
    
    if __name__ == '__main__':
        main()

运行print_name.py结果如下::

    获取名称:
    inside the getter!
    mei
    重新设置名称:
    inside the setter!
    重新获取名称:
    inside the getter!
    meichaohui
    使用print_name方法打印名称:
    Your name is : meichaohui

类方法(class method)与静态方法(static method)
------------------------------------------------

- 在类的定义中，以self作为第一个参数的方法都是实例方法(instance method)。
- 实例方法在首个参数是self,当它被调用时，python会把调用该方法的对象作为self参数传入。
- 类方法(class method)作用于整个类，对类作出的任何改变会对它的所有实例对象产生影响。
- 在类定义内部，用前缀修饰符@classmethod指定的方法都是类方法。
- 与实例方法类似，类方法的第一个参数是类本身。在python中，这个参数常被写作cls，因为全称class是保留字。
        
- 静态方法，既不影响类也不影响类的对象。出现在类的定义中仅仅是为了方便。
- 静态方法(static method)用@staticmethod修饰符修饰，既不需要self参数也不需要class参数。
- 下面代码中的welcome方法是静态方法，sum方法是类方法。
        
class_static_method.py代码如下::

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

运行class_static_method.py结果如下::

    使用静态方法打印欢迎词：
    Welcome to join us
    获取名称:
    inside the getter!
    mei
    重新设置名称:
    inside the setter!
    重新获取名称:
    inside the getter!
    meizhaohui
    使用print_name方法打印名称:
    Your name is : meizhaohui
    使用类方法打印总人数:
    The sum is 1
    ==================================================
    使用静态方法打印欢迎词：
    Welcome to join us
    获取名称:
    inside the getter!
    kawaii
    使用类方法打印总人数:
    The sum is 2
    ==================================================
    使用静态方法打印欢迎词：
    Welcome to join us
    获取名称:
    inside the getter!
    Manu Ginóbili
    使用类方法打印总人数:
    The sum is 3


何时使用类和对象而不是模块
-----------------------------------

*    当你需要许多具有相似行为（方法）但不同状态（特性）的实例时，使用对象是最好的选择。
*    类支持继承，但模块不支持。
*    如果你想要保证实例的唯一性，使用模块是最好的选择。不管模块在程序中被引用多少次，始终只有一个实例被加载。
*    如果你有一系列包含多个值的变量，并且它们能作为参数传入不同的函数，那么最好将它们封装到类里面::

        举例：你可能会使用以size和color为键的字典代码一张彩色图片，你可以在程序中为每张图片创建不同的字典；
        并把它们作为参数传递给像scale()或者transform()之类的函数。
        但这么做的话，一旦你想要添加其他的键或者函数会变得非常麻烦。
        为了保证统一性，应该定义一个Image类，把size和color作为特性，把scale()和transform()定义为方法。
        这样一来，关于一张图片的所有数据和可执行的操作都存储在了统一的位置。
*    用最简单的方式解决问题。使用字典、列表和元组往往比使用模块更加简单、简洁且快速。而使用类则更为复杂。

**Python创始人Guido的建议**：

*    不要过度构建数据结构。尽量使用元组(以及命名元组)而不是对象。
*    尽量使用简单的属性域而不是getter/setter函数...，内置数据类型是你最好的朋友。
*    尽可能多地使用数字、字符串、元组、列表、集合以及字典。
*    多看看容器库提供的类型，尤其是双端队列(from collections import deque)。

         





                           
