.. _re_module:

常用内建模块之正则表达式re模块
======================================

.. contents:: 目录

python 正则表达式re模块介绍
-----------------------------

正则表达式，英语：Regular Expression，在代码中常简写为regex、regexp或RE。

python中re模块是正则表达式模块，使用方法如下::

    import re                        # 导入re模块
    >>> re.
    re.A           re.L           re.Scanner(    re.X           re.findall(    re.search(     re.template(
    re.ASCII       re.LOCALE      re.T           re.compile(    re.finditer(   re.split(
    re.DEBUG       re.M           re.TEMPLATE    re.copyreg     re.fullmatch(  re.sre_compile
    re.DOTALL      re.MULTILINE   re.U           re.enum        re.functools   re.sre_parse
    re.I           re.RegexFlag(  re.UNICODE     re.error(      re.match(      re.sub(
    re.IGNORECASE  re.S           re.VERBOSE     re.escape(     re.purge(      re.subn(

    re.match(pattern, string, flags=0)    # 在字符串string开始处匹配pattern正则表达式规则，flags为匹配模式
                                        # 并返回一个匹配对应MatchObject，未匹配到则返回None。
                                        # 限制是只匹配字符串开头，其他位置不匹配，使用不方便。
        flags匹配模式可以是以下模块：
    re.A或re.ASCII        # 特殊的ASCII码可被解析匹配，如 \w, \W, \b, \B, \d, \D, \s and \S
    re.I或re.IGNORECASE    # 匹配时忽略大小写，如a与A等价
    re.M或re.MULTILINE    # 多行匹配，也即并不是只在第一行匹配
                        # 可理解为当存在^$匹配符，可匹配每行的行首或行尾
                        # 如果re.MULTILINE选项被指定，则会匹配字符串中换行符后面的位置
    re.X或re.VERBOSE    # 允许在正则表达式中使用注释，使得正则表达式更易读。模式中空格会被忽略，#井号后面的部分作为注释会被忽略。
    re.L或re.LOCALE        # 本地化，该模式仅用于字节模式，不鼓励使用。
    re.DEBUG            # 查看正则表达式的匹配过程
    re.S或re.DOTALL        # 使.点号匹配包括换行在内的所有字符
    re.U或re.UNICODE    # 使用统一码标志，python3中默认使用UNICODE进行匹配，不需要添加。

    re.compile(pattern, flags=0)    # 创建正则表达式模式对象；
                                    # pattern为正则表达式匹配规则，flags为匹配模式。
                                    # 当一个正则表达式需要多次匹配或更加复杂的匹配时，
                                    # 使用compile对模式进行编译，可加快匹配速度。
                                    # 对编译好的模式进行匹配。
                                    
    re.fullmatch(pattern, string, flags=0)    # 如果模式完全匹配字符串，则返回一个matchobject,不匹配则返回None
    re.search(pattern, string, flags=0)        # 将字符串的所有字符尝试与正则表达式匹配，如果匹配成功，返回matchobject，否则返回None。
                                            # 若有多个匹配成功，只返回第一个匹配结果
    re.split(pattern, string, maxsplit=0, flags=0)        # 通过正则表达式将字符串分割，匹配到符合的字符就把字符串分割一次；
                                                        # maxsplit没有赋值，找到几个匹配项就分割几次；
                                                        # 若maxsplit赋值小于匹配项个数，则分割maxsplit次。返回一个list。
    re.findall(pattern, string, flags=0)    # 查找整个字符串，返回所有的匹配项，返回一个列表list。
    re.finditer(pattern, string, flags=0)    # 查找整个字符串，返回所有的匹配项，返回一个迭代器callable_iterator对象。
    re.sub(pattern, repl, string, count=0, flags=0)        # 把string中所有符合pattern的字符串，替换成repl；
                                                        # count如赋值小于匹配项个数，则把前count个匹配项替换掉，其他字符不变。
                                                        # re.sub返回完成替换之后的字符串。
    re.subn(pattern, repl, string, count=0, flags=0)    # 把string中所有符合pattern的字符串，替换成repl；
                                                        # count如赋值小于匹配项个数，则把前count个匹配项替换掉，其他字符不变。
                                                        # re.subn返回元组，(完成替换之后的字符串,替换次数)。
    re.escape(string)                # 对字符串中除字母数字下划线外，其他所有字符串进行转义，都加上反斜杠。
    re.purge()                        # 清空正则表达式的缓存

使用re模块的步骤
----------------------

我们有必要对re模块中所包含的类及其工作流程进行一下简单的、整体性的说明，这讲有利于我们对下面内容的理解。

使用re模块进行正则匹配操作的步骤:

- 编写表示正则表达式规则的Python字符串str；
- 通过re.compile()函数编译该Python字符串获得一个正则表达式对象（Pattern Object）p；
- 通过正则表达式对象的p.match()或p.fullmatch()函数获取匹配结果--匹配对象（Match Object）m;
- 通过判断匹配对象m是否为空可知是否匹配成功，也可以通过匹配对象m提供的方法获取匹配内容。

使用re模块进行内容查找、替换和字符串分隔操作的步骤:

- 编写表示正则表达式规则的Python字符串str；
- 通过re.compile()函数编译该Python字符串获得一个正则表达式对象（Pattern Object）p；
- 通过正则表达式对象的p.search()或p.findall()或p.finditer()或p.sub()或p.subn()或p.split()函数完内容查找、替换和字符串分隔操作并获取相应的操作结果;

总结：

- 根据上面的描述可知，将一个表示正则表达式的Python字符串编译成一个正则表达式对象是使用正则表达式完成相应功能的首要步骤.
- re模块中用于完成正则表达式编译功能的函数为re.compile()。    

正则表达式中特殊的字符
-------------------------

正则表达式中特殊的字符::

    .    点号，在默认模式下，匹配除换行以外的任意字符。如果 DOTALL 标志被指定, 则匹配包括换行符在内的所有字符。
    ^    乘方运算符或脱字节符，在默认模式下匹配字符串的起始位置，在MULTILINE模式下也匹配换行符之后的位置。
    $    匹配字符串的末尾或者字符串末尾换行符之前的位置，在MULTILINE模式下还匹配换行符之前的位置。
    *    匹配前面重复出现的正则表达式零次或多次，尽可能多的匹配(greedy 贪婪型)。
    +    匹配前面RE 1次或多次(贪婪型，尽可能多的匹配)。
    ?    匹配前面的RE 0次或1次。
    *?,+?,??    '*'、'+'和'?'限定符是贪婪的；它们匹配尽可能多的文本。在限定符之后加上'?'将使得匹配以非贪婪的或最小的方式进行。
    {m}        表示精确匹配前面的正则表达式的m个拷贝，较少的匹配将导致整个表达式不能匹配。
    {m,n}    匹配前导正则表达式的m到n个重复，尝试匹配尽可能多的重复(greedy 贪婪型)。
    {m,}    匹配前导正则表达式的至少m次，尝试匹配尽可能多的重复(greedy 贪婪型)。
    {,n}    匹配前导正则表达式的至多n次，尝试匹配尽可能多的重复(greedy 贪婪型)。
    {m,n}?    匹配前导正则表达式的m到n个重复，尝试匹配尽可能少的重复(Non-greedy 非贪婪型)。
    \        对特殊符号进行转义
    []        用来表示一个字符集合。
            字符可以一个一个的列出来，如[abcd]，则可以匹配'a','b','c','d'。
            通过给出两个字符并用'-'分隔，可以给出一段范围的字符，如[a-z]匹配小写字母，[A-Z]匹配大写字母，[0-9]匹配0-9的数字。
            在集合内部，特殊字符将失去它们特殊的含义，如[(+*)]将匹配'(','+','*',')'。
            在集合中接受字符类别\s,\S,\w等。
            可以使用[^RE]作为字符集的补集，^必须为集合第一个字符，如[^a-z]可以匹配除小写字母外所有的字符。
    |        a|b 匹配a或b，(Non-greedy 非贪婪型)，匹配上正则a后，就不会再去尝试匹配正则b。
    (...)    被圆括号括起来的表达式将作为分组，分组表达式作为一个整体，后面可以接数量词，表达式中|仅在该组中有效。
            如(a-z|A-Z){2,3}表示匹配字母2至3次。
    (?aiLmsux)    给整个正则表达式设置相应的标记：re.A（ASCII码模式），re.I（忽略大小写），re.L（依赖区域设置）;
                re.M（多行模式），re.S（点号匹配所有字符），re.U（依赖Unicode），re.X（详细模式）
    (?:...)    # 当你要将一部分规则作为一个整体对它进行某些操作，可以使用(?:RE)将正则表达式RE包裹起来。
    (?P<name>...)    # 将RE字符串包裹进来作为一个命名组。
    (?P=name)        # 使用命名组进行匹配。匹配前面定义的命名组匹配到的字符串。
    (?#...)            # 添加备注，忽略指定的字符。
    (?='...')        # 如果指定的字符在匹配到的字符后面，才算匹配成功。s='Isaac Asimov'   m=re.findall("Isaac (?=Asimov)",s) 
    (?!...)            # 如果指定的字符不在匹配到的字符后面，才算匹配成功。s='Isaac Asimov'   m=re.findall("Isaac (?!Asimov)",s)
    (?<=...)         # 如果指定的字符在匹配到的字符前面，才算匹配成功。s='Isaac Asimov'   m=re.findall("(?<=Isaac )Asimov",s)
    (?<!...)        # 如果指定的字符不在匹配到的字符前面，才算匹配成功。s='Isaac Asimov'   m=re.findall("(?<!Isaac )Asimov",s)
    (?(id/name)yes|no)        #选择性匹配 (?(id/name)yes-pattern|no-pattern) 的作用是：
                                对于给出的id或者name，先尝试去匹配 yes-pattern部分的内容；
                                如果id或name条件不满足，则去匹配no-pattern部分的内容；no-pattern部分可以省略；
                                此处的name或id，是针对（当前位置的）条件性匹配之前的，某个已经通过group去分组的内容
                                如果是有命名的分组，即named group，则对应的该分组就有对应的name，即此处所指的就是对应的name；
                                如果是无命名的分组，即unnamed group，则对应的该分组也有对应的分组的编号，称为group的number，
                                也叫做id，对应的就是这里的id。
        *** 预定义字符集
    \\        匹配反斜杠
    \A        匹配字符串开头，同^
    \Z        匹配字符串结尾，同$
    \number    匹配相同编号的组的内容
    \b        匹配空字符串，仅在词的开头和结尾
    \B        匹配空字符串，不在词的开头和结尾，与\b相反
    \d        匹配数字,等同于[0-9]
    \D        匹配非数字，等同于\d的补集，即[^\d]
    \s        匹配whitespace字符串，同等于[ \t\n\r\f\v]
    \S        匹配非whitespace字符串，\s的补集，[^\s]
    \w        匹配字母，数字，下划线，等同于[a-zA-Z0-9_]
    \W        \w的补集


正则表达式示例如下。

使用re.match匹配首字符"I"
----------------------------------

使用re.match匹配首字符"I"::

    >>> string='i love to learn python. I am a Pythonista!'
    >>> string
    'i love to learn python. I am a Pythonista!'
    >>> pattern=r"I"
    >>> pattern
    'I'
    >>> p=re.compile(pattern)
    >>> p
    re.compile('I')
    >>> m=re.match(p,string)
    >>> m      # 未匹配到，因为首字符是小写的"i"

    # 增加忽略大小写的flag re.IGNORECASE
    >>> p=re.compile(pattern,re.IGNORECASE)
    >>> p
    re.compile('I', re.IGNORECASE)
    >>> m=re.match(p,string)
    >>> m
    <_sre.SRE_Match object; span=(0, 1), match='i'>      # 成功匹配上小写字母"i"。

    # 修改正则表达式尝试去匹配大小的"I"
    >>> pattern=r".*I"
    >>> pattern
    '.*I'
    >>> p=re.compile(pattern)
    >>> p
    re.compile('.*I')
    >>> re.match(p,string)
    <_sre.SRE_Match object; span=(0, 25), match='i love to learn python. I'>

使用fullmatch进行完全匹配
-----------------------------

使用fullmatch进行完全匹配::

    >>> re.fullmatch(r".*I.*!",string)    # 匹配任意字符，"I"，任意字符，"!"形成的字符串
    <_sre.SRE_Match object; span=(0, 42), match='i love to learn python. I am a Pythonista!'>

使用re.search进行搜索匹配
-----------------------------

使用re.search进行搜索匹配::

    >>> pattern=r"I"
    >>> p=re.compile(pattern,re.I)        # 带忽略大小写flag，仅返回第一次匹配到的小写"i"
    >>> re.search(p,string)
    <_sre.SRE_Match object; span=(0, 1), match='i'>
    >>> p=re.compile(pattern)            # 不带忽略大小写flag，匹配到大写"I"
    >>> re.search(p,string)
    <_sre.SRE_Match object; span=(24, 25), match='I'>

使用re.findall进行搜索匹配
---------------------------------

使用re.findall进行搜索匹配::

    >>> string
    'i love to learn python. I am a Pythonista!'
    >>> pattern
    'I'
    >>> re.findall(pattern,string)            # 不带忽略大小写flag，匹配到大写"I"
    ['I']
    >>> re.findall(pattern,string,re.I)        # 带忽略大小写flag，返回所有匹配到的小写"i"或大小"I"
    ['i', 'I', 'i']

re.finditer进行搜索匹配
-----------------------------------------------------------

使用re.finditer进行搜索匹配，返回callable_iterator对象::

    >>> m=re.finditer(pattern,string,re.I)
    >>> m
    <callable_iterator object at 0x000002DB1506D470>
    >>> for i in m:
    ...     print(i)
    ...
    <_sre.SRE_Match object; span=(0, 1), match='i'>
    <_sre.SRE_Match object; span=(24, 25), match='I'>
    <_sre.SRE_Match object; span=(37, 38), match='i'>

字符串分割
-----------------------

使用re.split(pattern, string, maxsplit=0, flags=0)进行字符分割::

    >>> string
    'i love to learn python. I am a Pythonista!'
    >>> pattern
    'I'
    >>> re.split(pattern,string)                                # 直接进行分割，分割了1次
    ['i love to learn python. ', ' am a Pythonista!']
    >>> re.split(pattern,string,flags=re.I)                        # 带flags 忽略大小写进行分割，分割了3次
    ['', ' love to learn python. ', ' am a Python', 'sta!']
    >>> re.split(pattern,string,2,re.I)                            # 带flags 忽略大小写，并指定最多分割2次进行分割，分割了2次
    ['', ' love to learn python. ', ' am a Pythonista!']
    >>> re.split(pattern,string,maxsplit=2,flags=re.I)            # 带flags 忽略大小写，并指定最多分割2次进行分割，分割了2次
    ['', ' love to learn python. ', ' am a Pythonista!']

字符串替换
------------------------

使用re.sub(pattern, repl, string, count=0, flags=0)对字符串进行替换::

    >>> string
    'i love to learn python. I am a Pythonista!'
    >>> pattern
    'I'
    >>> re.sub(pattern,'i',string)                    # 将大写"I"替换成小写"i"
    'i love to learn python. i am a Pythonista!'
    >>> re.sub(pattern,'MEI',string,flags=re.I)        # 带flags 忽略大小写，将匹配字符替换成"MEI"，共替换3处
    'MEI love to learn python. MEI am a PythonMEIsta!'
    >>> re.sub(pattern,'MEI',string,count=2,flags=re.I)    # 带flags 忽略大小写，将匹配字符替换成"MEI"，并指定只替换2次，共替换2处
    'MEI love to learn python. MEI am a Pythonista!'
    # 显示替换次数
    >>> re.subn(pattern,'MEI',string,count=2,flags=re.I)
    ('MEI love to learn python. MEI am a Pythonista!', 2)
    >>> re.subn(pattern,'MEI',string,count=1,flags=re.I)
    ('MEI love to learn python. I am a Pythonista!', 1)
    >>> re.subn(pattern,'MEI',string,flags=re.I)
    ('MEI love to learn python. MEI am a PythonMEIsta!', 3)

字符转义
--------------

使用re.escape将所有字符转义::

    >>> re.escape(string)
    'i\\ love\\ to\\ learn\\ python\\.\\ I\\ am\\ a\\ Pythonista\\!'

匹配行首行尾
---------------------

匹配行首行尾::

    >>> re.search('^i.*!$',string)
    <_sre.SRE_Match object; span=(0, 42), match='i love to learn python. I am a Pythonista!'>
    >>> re.findall('^i.*!$',string)
    ['i love to learn python. I am a Pythonista!']

重复匹配
-----------------

重复匹配::

    # 贪婪型匹配：
    >>> str='abbcccddddeeeee'
    >>> re.search('ab+',str)
    <_sre.SRE_Match object; span=(0, 3), match='abb'>
    >>> re.search('ab*',str)
    <_sre.SRE_Match object; span=(0, 3), match='abb'>
    >>> re.search('ab?',str)
    <_sre.SRE_Match object; span=(0, 2), match='ab'>
    # 非贪婪型匹配：
    >>> re.search('ab??',str)
    <_sre.SRE_Match object; span=(0, 1), match='a'>
    >>> re.search('ab*?',str)
    <_sre.SRE_Match object; span=(0, 1), match='a'>
    >>> re.search('ab+?',str)
    <_sre.SRE_Match object; span=(0, 2), match='ab'>
    # 匹配1次，匹配2次，或匹配m至n次，贪婪型匹配：
    >> re.search('ab{1}',str)
    <_sre.SRE_Match object; span=(0, 2), match='ab'>
    >>> re.search('ab{2}',str)
    <_sre.SRE_Match object; span=(0, 3), match='abb'>
    >>> re.search('ab{3}',str)
    >>> re.search('ab{1,3}',str)
    <_sre.SRE_Match object; span=(0, 3), match='abb'>
    >>> re.search('ab{1,2}',str)
    <_sre.SRE_Match object; span=(0, 3), match='abb'>
    >>> re.search('ab{0,2}',str)
    <_sre.SRE_Match object; span=(0, 3), match='abb'>
    # 匹配1次，匹配2次，或匹配m至n次，非贪婪型匹配：
    >>> re.search('ab{0,2}?',str)
    <_sre.SRE_Match object; span=(0, 1), match='a'>
    >>> re.search('ab{1,2}?',str)
    <_sre.SRE_Match object; span=(0, 2), match='ab'>

系列匹配
---------------

使用[]匹配系列::

    >>> string="123abc456def789ABC021"
    # 查找数字
    >>> re.findall('[0-9]',string)
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '2', '1']
    # 查找小写字母
    >>> re.findall('[a-z]',string)
    ['a', 'b', 'c', 'd', 'e', 'f']
    #  查找大写字母
    >>> re.findall('[A-Z]',string)
    ['A', 'B', 'C']
    #  查找大小写字母
    >>> re.findall('[a-zA-Z]',string)
    ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C']
    # 匹配非字母
    >>> re.findall('[^a-zA-Z]',string)
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '2', '1']
    12)、使用|进行或匹配
    >>> re.findall('[123]|[abc]',string)
    ['1', '2', '3', 'a', 'b', 'c', '2', '1']

分组匹配
-------------------

分组匹配::

    >>> string
    '123abc456def789ABC021'
    >>> re.findall('([0-9])([a-z])',string)
    [('3', 'a'), ('6', 'd')]
    >>> re.findall('([0-9])([a-zA-Z])',string)
    [('3', 'a'), ('6', 'd'), ('9', 'A')]
    >>> re.search('([0-9])([a-zA-Z])',string)
    <_sre.SRE_Match object; span=(2, 4), match='3a'>
    >>> re.findall('([0-9][a-zA-Z])',string)
    ['3a', '6d', '9A']

正则标记
-------------------

使用(?aiLmsux)设置正则标记::

    >>> re.findall('(?i)(ab)',string)
    ['ab', 'AB']
    >>> re.findall('(?x)[ab]',string)
    ['a', 'b']
    >>> re.findall('(?i)[ab]',string)
    ['a', 'b', 'A', 'B']

命名组匹配
------------------

使用(?<name>)和(?P=name)进行命名组匹配::

    >>> string='123abc123def456ghi456ki'
    >>> string
    '123abc123def456ghi456ki'
    # 使用(?P=num)匹配num组匹配到的字符串
    >>> re.findall("(?P<num>\d+)[a-z]*(?P=num)",string)
    ['123', '456']
    >>> string=u'标签：<a href="/tag/情侣电话粥/">情侣电话粥</a>'
    >>> re.search("<a href=\"/tag/(?P<name>.*)/\">(?P=name)</a>",string)
    <_sre.SRE_Match object; span=(3, 34), match='<a href="/tag/情侣电话粥/">情侣电话粥</a>'>
    >>> re.findall("<a href=\"/tag/(?P<name>.*)/\">(?P=name)</a>",string)
    ['情侣电话粥']

添加备注信息
----------------

添加备注信息::

    >>> import re
    >>> string='abdDeFgh'
    # 匹配小写字母
    >>> re.findall('[a-z]*(?#lower)',string)
    ['abd', '', 'e', '', 'gh', '']
    >>> re.search('[a-z]*(?#lower)',string)
    <_sre.SRE_Match object; span=(0, 3), match='abd'>
    # 匹配大写字母
    >>> re.search('[A-Z]*(?#upper)',string)
    <_sre.SRE_Match object; span=(0, 0), match=''>
    >>> re.findall('[A-Z]*(?#upper)',string)
    ['', '', '', 'D', '', 'F', '', '', '']

限定字符匹配
-------------

在需要匹配的字符前后有限定字符::

    (?='...')        # 如果指定的字符在匹配到的字符后面，才算匹配成功。s='Isaac Asimov'   m=re.findall("Isaac (?=Asimov)",s) 
    (?!...)            # 如果指定的字符不在匹配到的字符后面，才算匹配成功。s='Isaac Asimov'   m=re.findall("Isaac (?!Asimov)",s)
    (?<=...)         # 如果指定的字符在匹配到的字符前面，才算匹配成功。s='Isaac Asimov'   m=re.findall("(?<=Isaac )Asimov",s)
    (?<!...)        # 如果指定的字符不在匹配到的字符前面，才算匹配成功。s='Isaac Asimov'   m=re.findall("(?<!Isaac )Asimov",s)
    >>> s='Isaac Asimov'
    >>> s
    'Isaac Asimov'
    # 在'Isaac '之后有'Asimov'字符，匹配到
    >>> re.findall("Isaac (?=Asimov)",s)
    ['Isaac ']
    # 在'Isaac '之后没有'Asimov'字符，未匹配到
    >>> re.findall("Isaac (?!Asimov)",s)
    []
    # 在'Isaac '之后没有'Asimoev'字符，匹配到
    >>> re.findall("Isaac (?!Asimoev)",s)
    ['Isaac ']

    # 在'Asimov'之前有'Isaac '字符，匹配到
    >>> re.findall("(?<=Isaac )Asimov",s)
    ['Asimov']
    # 在'Asimov'之前没有'Isaacd'字符，未匹配到
    >>> re.findall("(?<=Isaacd)Asimov",s)
    []
    # 在'Asimov'之前不能包含'Isaac '字符，未匹配到
    >>> re.findall("(?<!Isaac )Asimov",s)
    []
    # 在'Asimov'之前不包含'Isaacd'字符，匹配到
    >>> re.findall("(?<!Isaacd)Asimov",s)
    ['Asimov']

选择性匹配
-----------------

选择性匹配::

    (?(id/name)yes|no)        #选择性匹配
        a、匹配邮箱
    s='<user1@mail1> user2@mail2 <user3@mail3> <user4@mail4 user5@mail5> <  user6@mail6  user7@mail7>'
    # 多个邮箱地址有的被<>或空格包裹起来，要取出所有的邮箱地址。
    # 通过分析可知：
    # 1、如果邮箱前面有<，则需要在其后可能是>，如<user1@mail1> 或 <user3@mail3>
    # 2、如果邮箱前面有<，则需要在其后可能是空格 ，如<user4@mail4 user5@mail5>中的user4@mail4
    # 3、如果邮箱前面没有<，则需要在其后可能是>，如<user4@mail4 user5@mail5>中的user5@mail5
    # 4、如果邮箱前面没有<，则需要在其后可能是空格 ，如user2@mail2
    即在邮箱前面或后面有0个或多个空格字符
    匹配邮箱：\w+@\w+  \w表示匹配字母，数字，下划线，等同于[a-zA-Z0-9_]
    再匹配邮箱前后可能产生的空格字符，\s*(\w+@\w+)\s*
    如果匹配到<，则后面需要匹配>或空格
    如果未匹配到<，则后面需要匹配>或空格
    所以正则表达式如下：
    >>> re.findall(r'(<)?\s*(\w+@\w+)\s*(?(1)[> ]|[> ])',s)
    [('<', 'user1@mail1'), ('', 'user2@mail2'), ('<', 'user3@mail3'), ('<', 'user4@mail4'), ('', 'user5@mail5'), ('<', 'user6@mail6'), ('', 'user7@mail7')]
        b、匹配标准数字
        以数字为例，标准数字格式如下，即：
    # 所有位都是数字，如0-9
    # 可以有小数点，如果有小数点的话，小数点后面有一至两个小数，如12.34合法，12.3合法，12.345不合法，12.不合法
    # 不能包含字母，以及除.小数点号以外其他的特殊字符
    # 最高位不能是0，0123不合法，123合法
    匹配步骤：
    # 1、匹配整数部分，[1-9]\d*，即起始位是1-9中的数字，后面可跟多位[0-9]间的数字
    # 2、匹配小数点，\. 使用转义符\进行转义
    # 3、匹配小数点后面的小数部分，\d{1,2}，即匹配数字1至2次
    # 4、如果匹配小数点，则要匹配小数后面的数字
    使用选择性匹配的正则如下：
    [1-9]\d*(\.)?(?(1)\d{1,2})
    如果注意到数字前后再不能用其他字符，则在最前面和最后面分别加上^，$作一下限定：
    ^[1-9]\d*(\.)?(?(1)\d{1,2})$
    如果将整数部分、小数点、小数部分进行分组。如下：
    foundValidNumStr = re.search("^(?P<integerPart>[1-9]\d*)(?P<foundPoint>\.)?(?P<decimalPart>(?(foundPoint)\d{1,2}))$", eachNumStr)

    详细可参考re_id_name.py
    re_id_name.py代码如下：
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    """
    【教程】详解Python正则表达式之： (?(id/name)yes-pattern|no-pattern) 条件性匹配
    https://www.crifan.com/detailed_explanation_about_python_regular_express_yes_or_no_conditional_match
     
    Version:    2012-11-17
    Author:     Crifan
    """
     
    import re
     
    #需求：
    #类似于检测（最多两位小数的）数字的合法性：
    #所有的字符都是数字
    #如果有小数点，那么小数点后面最多2位数字
    testNumStrList = {
        #合法的数字
        '12.34',
        '123.4',
        '1234',
         
        #非法的数字
        '1.234',
        '12.',
        '12.ab',
        '12.3a',
        '123abc',
        '123abc456',
        '01234',
    }
    for eachNumStr in testNumStrList:
        # eachNumStr='1.234'
        #下面这个是不严谨的，会导致：
        #1.234 -> 只会去判断234，所以检测出整数部分是234，无小数
        #123.4 -> 只会去判断4，所以检测出整数部分是4，无小数
        #123abc456 -> 只会去判断456，所以检测出整数部分是456，无小数
        #foundValidNumStr = re.search("(?P<integerPart>\d+)(?P<foundPoint>\.)?(?P<decimalPart>(?(foundPoint)\d{1,2}))$", eachNumStr)
         
        #下面这个也是不严谨的，会导致：
        #1.234 -> 只去判断1.23，所以检测出整数是1，小数是23
        #12. -> 只会去判断12，所以检测出整数是12，无小数
        #123abc456 -> 只会去判断123，所以检测出整数是123，无小数
        #12.ab -> 只会去判断12，所以检测出整数是12，无小数
        #123abc -> 只会去判断123，所以检测出整数是123，无小数
        #12.3a -> 只会去判断12.3，所以检测出整数是12，小数是3
        #foundValidNumStr = re.search("^(?P<integerPart>\d+)(?P<foundPoint>\.)?(?P<decimalPart>(?(foundPoint)\d{1,2}))", eachNumStr)
     
        #下面这个，更不严谨，会导致中间只要有数字，那么基本上都会去匹配到，和实际的期望，差距最大
        #foundValidNumStr = re.search("(?P<integerPart>\d+)(?P<foundPoint>\.)?(?P<decimalPart>(?(foundPoint)\d{1,2}))", eachNumStr)
     
        #下面这个才是正确的
        foundValidNumStr = re.search("^(?P<integerPart>[1-9]\d*)(?P<foundPoint>\.)?(?P<decimalPart>(?(foundPoint)\d{1,2}))$", eachNumStr)
        #也可以写成下面这样：
        #foundValidNumStr = re.search("^(?P<integerPart>\d+)(\.)?(?P<decimalPart>(?(2)\d{1,2}))$", eachNumStr); #这个也是同样的效果
         
        #print "foundValidNumStr=",foundValidNumStr;
        if(foundValidNumStr):
            integerPart = foundValidNumStr.group("integerPart")
            decimalPart = foundValidNumStr.group("decimalPart")
            print("eachNumStr=%s\tis valid numebr ^_^, integerPart=%s, decimalPart=%s"%(eachNumStr, integerPart, decimalPart))
        else:
            print("eachNumStr=%s\tis invalid number !!!"%(eachNumStr))

    执行re_id_name.py运行结果如下：
    eachNumStr=123abc456    is invalid number !!!
    eachNumStr=12.3a        is invalid number !!!
    eachNumStr=12.ab        is invalid number !!!
    eachNumStr=123abc       is invalid number !!!
    eachNumStr=01234        is invalid number !!!
    eachNumStr=1234 is valid numebr ^_^, integerPart=1234, decimalPart=
    eachNumStr=12.  is invalid number !!!
    eachNumStr=123.4        is valid numebr ^_^, integerPart=123, decimalPart=4
    eachNumStr=1.234        is invalid number !!!
    eachNumStr=12.34        is valid numebr ^_^, integerPart=12, decimalPart=34


使用特殊字符进行查找
-------------------------

使用特殊字符进行查找::

    >>> import string
    >>> s=string.printable
    >>> s
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    # 匹配开头字符0123
    >>> re.findall('\A0123',s)
    ['0123']
    # 匹配结尾字符\x0c
    >>> re.findall('\x0c\Z',s)
    ['\x0c']
    # 匹配数字
    >>> re.findall('\d',s)
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 匹配whitespace字符串
    >>> re.findall('\s',s)
    [' ', '\t', '\n', '\r', '\x0b', '\x0c']
    # 匹配非whitespace字符串
    >>> re.findall('\S',s)
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    # 匹配字母，数字，下划线，等同于[a-zA-Z0-9_]
    >>> re.findall('\w',s)
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
    # 匹配\w的补集
    >>> re.findall('\W',s)
    ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']


参考文献:

- Python 正则表达式入门（初级篇） https://www.cnblogs.com/chuxiuhong/p/5885073.html
- Python 正则表达式入门（中级篇） http://www.cnblogs.com/chuxiuhong/p/5907484.html
- python中的正则表达式（re模块） https://www.cnblogs.com/tina-python/p/5508402.html
- python官网指导  https://docs.python.org/3.6/library/re.html
- Python::re模块--在Python中使用正则表达式 https://www.cnblogs.com/now-fighting/p/4495841.html
- Python之正则表达式（re模块） https://www.cnblogs.com/yyds/p/6953348.html
- python 正则表达式 RE模块汇总记录 https://www.cnblogs.com/congyinew/p/6491268.html
- python re模块 https://www.cnblogs.com/MrFiona/p/5954084.html
- 详解Python正则表达式之： (?(id/name)yes-pattern|no-pattern) 条件性匹配 https://www.crifan.com/detailed_explanation_about_python_regular_express_yes_or_no_conditional_match/
- 以Python中的re模块为例，手把手教你，如何从无到有，写出相对复杂的正则表达式 https://www.crifan.com/how_to_write_your_own_complex_regular_expression_in_python_re/

