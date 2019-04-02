.. _str:

python字符串处理
======================

.. contents:: 目录

python字符串
-------------------------------

- Python3中字符串是Unicode字符串而不是数组，这是与Python2相比最大的区别。
- Python2中需要区分普通的以字节为单位的字符串以及Unicode字符串。
- Python标准文本编码格式是UTF-8，这种编码方式简单快速，字符覆盖面广，出错率低。
- UTF-8动态编码方案：

  #. 为ASCII字符分配1字节；
  #. 为拉丁语系(除西里尔语)的语言分配2字节；
  #. 为其他的位于基本多语言平面的字符分配3字节；
  #. 为剩下的字符集分配4字节，这包括一些亚洲语言及符号。

- 如果你知道某个字符的Unicode ID，可以直接在Python字符串中引用这个ID获取对应字符。
- 可以使用\N{name}来引用某一字符，其中name为该字符的标准名称，在 `Unicode字符名称索引页 <https://www.unicode.org/charts/charindex.html>`_ 可以查到字符对应的标准名称。
- Python中的unicodedata模块提供了下面两个方向的转换函数：

  #. lookup() 接受不区分大小写的标准名称，返回一个Unicode字符。
  #. name() 接受一个Unicode字符，返回大写形式的名称。

从官网截取的部分字符标准名称对照表::


       Unicode® Character Name Index
    A
    Name, Alias, or Category	Chart Link
    A WITH ACUTE, LATIN CAPITAL LETTER	00C1
    A WITH ACUTE, LATIN SMALL LETTER	00E1
    A WITH BREVE, LATIN SMALL LETTER	0103
    A WITH CARON, LATIN SMALL LETTER	01CE
    A WITH CIRCUMFLEX, LATIN CAPITAL LETTER	00C2
    A WITH CIRCUMFLEX, LATIN SMALL LETTER	00E2
    A WITH DIAERESIS, LATIN CAPITAL LETTER	00C4
    A WITH DIAERESIS, LATIN SMALL LETTER	00E4
    A WITH DOT ABOVE, LATIN SMALL LETTER	0227
    A WITH DOT BELOW, LATIN SMALL LETTER	1EA1
    A WITH DOUBLE GRAVE, LATIN SMALL LETTER	0201
    A WITH GRAVE, LATIN CAPITAL LETTER	00C0

说明: 为了方便查阅，Unicode字符名称索引页列出的字符名称是经过修改的，因此与由unicodedata.name()得到的名称有所不同，如果需要将它们转换为真实的Unicode名称(Python使用的)，只需要将逗号舍去，并将逗号后面的内容移动到最前面即可。

unicodedata模块属性或方法::

    In [1]: import unicodedata                                                      
    
    In [2]: unicodedata. 
      bidirectional()    decomposition()    mirrored()         UCD               
      category()         digit()            name()             ucd_3_2_0         
      combining()        east_asian_width() normalize()        ucnhash_CAPI      
      decimal()          lookup()           numeric()          unidata_version    

    In [3]: unicodedata.lookup('A WITH ACUTE, LATIN CAPITAL LETTER')               
    ---------------------------------------------------------------------------
    KeyError                                  Traceback (most recent call last)
    <ipython-input-11-1bf6d86503ae> in <module>
    ----> 1 unicodedata.lookup('A WITH ACUTE, LATIN CAPITAL LETTER')
    
    KeyError: "undefined character name 'A WITH ACUTE, LATIN CAPITAL LETTER'"
    
    In [4]: unicodedata.lookup('LATIN CAPITAL LETTER A WITH ACUTE')                
    Out[4]: 'Á'


unicodedata模块的使用，check_unicode函数接受一个Unicode字符，查找它们对应的名称，再用这个名称查找对应的Unicode字符::

    In [1]: import unicodedata                                                      
    
    In [2]: def check_unicode(value): 
       ...:     name = unicodedata.name(value)  # 查找字符的名称 
       ...:     value2 = unicodedata.lookup(name)   # 查找名称对应的Unicode字符
       ...:     print('value="{}",name="{}",value2="{}"'.format(value, name, value2)
       ...: ) 
       ...:                                                                         
    
    In [3]: check_unicode('A')  # 纯ASCII字符
    value="A",name="LATIN CAPITAL LETTER A",value2="A"
    
    In [4]: check_unicode('$')  # ASCII标点符号
    value="$",name="DOLLAR SIGN",value2="$"
    
    In [5]: check_unicode('\u00a2')  # Unicode货币字符
    value="¢",name="CENT SIGN",value2="¢"
    
    In [6]: check_unicode('\u20ac')  # 欧元符号 
    value="€",name="EURO SIGN",value2="€"
    
    In [7]: check_unicode('\uffe5')  # 中国货币人民币元
    value="￥",name="FULLWIDTH YEN SIGN",value2="￥"
    
    In [8]: check_unicode('\u2630')  # 特殊符号 
    value="☰",name="TRIGRAM FOR HEAVEN",value2="☰"
    
    In [9]: check_unicode('\u2603')  # SNOWMAN字符 
    value="☃",name="SNOWMAN",value2="☃"

    In [10]: check_unicode('\u00e9') # 拉丁字母é
    value="é",name="LATIN SMALL LETTER E WITH ACUTE",value2="é"


python编码encode和解码decode
-------------------------------

- 编码是将字符串转化为一系列字节的过程。
- 解码是将字节序列转化为Unicode字符串的过程。


python字符串处理的常用方法
-------------------------------

python字符串有以下方法::

    >>> str='string'
    >>> str.
    str.capitalize(   str.endswith(     str.index(        str.isidentifier( str.istitle(      str.lstrip(       str.rindex(       str.split(        str.title(
    str.casefold(     str.expandtabs(   str.isalnum(      str.islower(      str.isupper(      str.maketrans(    str.rjust(        str.splitlines(   str.translate(
    str.center(       str.find(         str.isalpha(      str.isnumeric(    str.join(         str.partition(    str.rpartition(   str.startswith(   str.upper(
    str.count(        str.format(       str.isdecimal(    str.isprintable(  str.ljust(        str.replace(      str.rsplit(       str.strip(        str.zfill(
    str.encode(       str.format_map(   str.isdigit(      str.isspace(      str.lower(        str.rfind(        str.rstrip(       str.swapcase(

可以总结为以下几种类：

- 大小写转换类
- 判断是否类
- 两端填充类
- 索引计数类
- 字符截取与拼接类
- 字符替换类
- 字符查找类
- 翻译类
- 格式化类
- 编码类

大小写转换类
----------------------

大小写转换的方法如下::

    str.capitalize()            首字符大写，其他字符小写；原字符串并不会改变，生成新的字符串序列
                                >>> str1='abcdef'
                                >>> str1.capitalize()
                                'Abcdef'
                                >>> str1='abCdE'
                                >>> str1.capitalize()
                                'Abcde'                                
                                >>> str1
                                'abCdE'    
    str.title()                    标题化，首字母大写，其他字符小写
                                >>> str1='abCdE'
                                >>> str1.title()
                                'Abcde'
                                >>> str2='2sadDddE'
                                >>> str2.title()
                                '2Sadddde'    
    str.upper()                    将字符串转换为全部大写形式
                                >>> str1.upper()
                                'ABCDE'
    str.lower()                    将字符串转换为全部小写形式，汉语 & 英语环境下使用str.lower()没有问题
                                >>> str1.lower()
                                'abcde'
    str.casefold()                将字符串转换为全部小写形式，可以处理其他语言(如，德语)小写转化
                                德语中'ß'的小写是'ss'
                                >>> str1.casefold()
                                'one'
                                >>> str2.casefold()
                                '2two'
                                >>> s = 'ß'
                                >>> s
                                'ß'
                                >>> s.lower()
                                'ß'
                                >>> s.casefold()
                                'ss'                            
    str.swapcase()                字符串大小写翻转，大写变成小写，小写变成大写
                                >>> str2='2Two'
                                >>> str1='One'
                                >>> str1
                                'One'
                                >>> str2
                                '2Two'
                                >>> str1.swapcase()
                                'oNE'
                                >>> str2.swapcase()
                                '2tWO'
                                
                                
判断是否类
-------------------------
判断是否的方法如下::

    str.startswith(string)        判断是否以某指定字符串string开头
                                >>> str1='One'
                                >>> str1
                                'One'
                                >>> str1.startswith('o')
                                False
                                >>> str1.startswith('O')
                                True
                                >>> str1.startswith('On')
                                True
    str.endswith(string)        判断是否以某指定字符串string结尾
                                >>> str1='One'
                                >>> str1
                                'One'
                                >>> str1.endswith('e')
                                True
                                >>> str1.endswith('ne')
                                True
                                >>> str1.endswith('One')
                                True
                                >>> str1.endswith('one')
                                False                            
    str.isidentifier()            判断是否为有效标识符(有效标识符第一个字符串应该是字母或下划线，不能是数字或特殊符号)
                                >>> str1
                                'One'
                                >>> str2
                                '2Two'
                                >>> str3
                                '123'
                                >>> str1.isidentifier()
                                True
                                >>> str2.isidentifier()
                                False
                                >>> str3.isidentifier()
                                False
                                >>> str4='_ab'
                                >>> str4.isidentifier()
                                True
                                >>> str5='&adg'
                                >>> str5.isidentifier()
                                False                                
    str.istitle()                判断是否为标题化的字符串(即第一个字母需要为大写)
                                >>> str1
                                'One'
                                >>> str2
                                '2Two'
                                >>> str3
                                '123'
                                >>> str4
                                '&adg'
                                >>> str5
                                'abcd'
                                >>> str1.istitle()
                                True
                                >>> str2.istitle()
                                True
                                >>> str3.istitle()
                                False
                                >>> str4.istitle()
                                False
                                >>> str5.istitle()
                                False     
    str.isalnum()                判断是否为字母或数字
                                >>> str1
                                'One'
                                >>> str2
                                '2Two'
                                >>> str3
                                '123'
                                >>> str4
                                '&adg'
                                >>> str5
                                'abcd'
                                >>> str1.isalnum()
                                True
                                >>> str2.isalnum()
                                True
                                >>> str3.isalnum()
                                True
                                >>> str4.isalnum()
                                False
                                >>> str5.isalnum()
                                True                            
    str.islower()                判断是否为小写字母
                                >>> str1
                                'One'
                                >>> str2
                                '2Two'
                                >>> str3
                                '123'
                                >>> str4
                                '&adg'
                                >>> str5
                                'abcd'
                                >>> str1.islower()
                                False
                                >>> str2.islower()
                                False
                                >>> str3.islower()
                                False
                                >>> str4.islower()
                                True
                                >>> str5.islower()
                                True                                
    str.isupper()                判断是否为大写字母
                                >>> str1='abcde'
                                >>> str2='ABCDE'
                                >>> str3='1$abc'
                                >>> str4='1$ABC'
                                >>> str1.isupper()
                                False
                                >>> str2.isupper()
                                True
                                >>> str3.isupper()
                                False
                                >>> str4.isupper()
                                True    
    str.isnumeric()                判断是否为数字系列，不带小数点
                                >>> str1='123.456'
                                >>> str2='123456'
                                >>> str1.isnumeric()
                                False
                                >>> str2.isnumeric()
                                True
    str.isdecimal()                判断是否为数字系列，不带小数点
                                >>> str1
                                '123.456'
                                >>> str2
                                '123456'
                                >>> str1.isdecimal()
                                False
                                >>> str2.isdecimal()
                                True    
    str.isdigit()                判断是否为数字系列，不带小数点
                                >>> str1
                                '123.456'
                                >>> str2
                                '123456'
                                >>> str1.isdigit()
                                False
                                >>> str2.isdigit()
                                True    
    str.isspace()                判断所有字符是否为whitespace，即空格或tab键
                                >>> str1
                                '123.456'
                                >>> str2
                                '123456'
                                >>> str1.isspace()
                                False
                                >>> str2.isspace()
                                False
                                >>> strspace='  '
                                >>> strspace.isspace()
                                True
                                >>> strtab='    '
                                >>> strtab.isspace()
                                True
    str.isprintable()            是否可打印。tab键不可打印，返回False
                                >>> str1
                                '123.456'
                                >>> str2
                                '123456'
                                >>> str1.isprintable()
                                True
                                >>> str2.isprintable()
                                True
                                >>> strspace='  '
                                >>> strspace.isprintable()
                                True
                                >>> strtab='    '
                                >>> strtab.isprintable()
                                False                                
    
    str.isalpha()                是否为字母
                                >>> str1
                                '123.456'
                                >>> str2
                                '123456'
                                >>> str1.isalpha()
                                False
                                >>> str2.isalpha()
                                False
                                >>> strspace='  '
                                >>> strspace.isalpha()
                                False
                                >>> str4='abcd'
                                >>> str5='ABCD'
                                >>> str6='abcd32'
                                >>> str4.isalpha()
                                True
                                >>> str5.isalpha()
                                True
                                >>> str6.isalpha()
                                False                               
                                
                                
两端填充类
-----------------------
两端填充的方法如下::

    str.rjust(width[, fillchar])    右对齐，左侧填充字符，使新生成的字符串长度为width
                                若不指定fillchar字符，则默认在左侧填充空格，fillchar为单字符
                                >>> str1
                                '123.456'
                                >>> str2
                                '123456'
                                >>> str3
                                'III'
                                >>> str1.rjust(7)
                                '123.456'
                                >>> str1.rjust(8)
                                ' 123.456'
                                >>> str1.rjust(9)
                                '  123.456'
                                >>> str1.rjust(9,'*')
                                '**123.456'
                                >>> str3.rjust(6)
                                '   III'
                                >>> str3.rjust(6,'*')
                                '***III'
                                >>> str3.rjust(7,'*')
                                '****III'
    str.ljust(width[, fillchar])    左对齐，右侧填充字符，使新生成的字符串长度为width
                                若不指定fillchar字符，则默认在右侧填充空格，fillchar为单字符
                                >>> str1
                                '123.456'
                                >>> str2
                                '123456'
                                >>> str3
                                'III'
                                >>> str1.ljust(7)
                                '123.456'
                                >>> str1.ljust(8)
                                '123.456 '
                                >>> str1.ljust(9)
                                '123.456  '
                                >>> str1.ljust(9,'*')
                                '123.456**'
                                >>> str3.ljust(6)
                                'III   '
                                >>> str3.ljust(6,'*')
                                'III***'
                                >>> str3.ljust(7,'*')
                                'III****'                            
    str.center(width[, fillchar])    以当前字符串str为中心，在两侧填充字符，使新生成的字符串长度为width
                                若不指定fillchar字符，则默认在两侧填充空格，fillchar为单字符
                                >>> str1.center(8)
                                '123.456 '
                                >>> str1.center(9)
                                ' 123.456 '
                                >>> str2.center(9)
                                '  123456 '
                                >>> str2.center(8)
                                ' 123456 '
                                >>> str3.center(6,'*')
                                '*III**'
                                >>> str3.center(7,'*')
                                '**III**'
                                >>> str3.center(7,'*&')
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                TypeError: The fill character must be exactly one character long
                                >>> str3.center(7,'&')
                                '&&III&&'
                                >>> str3.center(8,'&')
                                '&&III&&&'
                                >>> str3.center(9,'&')
                                '&&&III&&&'
                                >>> str3.center(10,'&')
                                '&&&III&&&&'
    str.zfill(width)            将字符串str左侧填充0，使字符串长度为width
                                >>> c1='abcde'
                                >>> c1.zfill(5)
                                'abcde'
                                >>> c1.zfill(6)
                                '0abcde'
                                >>> c1.zfill(7)
                                '00abcde'
                                >>> c1.zfill(8)
                                '000abcde'
                                >>> c1.zfill(9)
                                '0000abcde'
                                >>> c2='abc ed'
                                >>> c2.zfill(10)
                                '0000abc ed'
                                
索引计数类
--------------------------
索引计数的方法如下::

    str.index(sub[, start[, end]]) 计算子字符串sub在str中的lowest最低索引号
                                若指定索引start和end时，则在索引start至end(不包括索引end)间进行查找
                                >>> c1
                                '1122333'
                                >>> c2
                                'ababcabab'
                                >>> c3
                                'AAAA'
                                >>> c1.index('1')
                                0
                                >>> c1.index('1',2)
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                ValueError: substring not found
                                >>> c1.index('1',1)
                                1
                                >>> c2.index('ab')
                                0
                                >>> c2.index('ab',2)
                                2
                                >>> c2.index('ab',2,3)
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                ValueError: substring not found
                                >>> c2.index('ab',2,4)
                                2
                                >>> c3.index('A')
                                0
                                >>> c3.index('A',1,4)
                                1
                                >>> c3.index('A',2,4)
                                2
                                >>> c3.index('A',3,4)
                                3
                                >>> c3.index('A',4,4)
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                ValueError: substring not found
    str.rindex(sub[, start[, end]])        计算子字符串sub在str中的highest最高索引号
                                >>> c3
                                'AAAA'
                                >>> c3.rindex('A')
                                3
                                >>> c3.rindex('A',0,3)
                                2
                                >>> c3.rindex('A',0,-1)
                                2
                                >>> c3.rindex('A',0,2)
                                1
                                >>> c3.rindex('A',0,1)
                                0
                                >>> c3.rindex('A',0,0)
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                ValueError: substring not found    
    str.count(sub[, start[, end]]) 计算子字符串sub在str中出现的次数
                                若指定索引start和end时，则在索引start至end(不包括索引end)间进行计数统计
                                >>> c1='1122333'
                                >>> c2='ababcabab'
                                >>> c3='AAAA'
                                >>> c1
                                '1122333'
                                >>> c2
                                'ababcabab'
                                >>> c3
                                'AAAA'
                                >>> c1.count('1')
                                2
                                >>> c1.count('2')
                                2
                                >>> c1.count('3')
                                3
                                >>> c2.count('a')
                                4
                                >>> c2.count('b')
                                4
                                >>> c2.count('c')
                                1
                                >>> c3.count('A')
                                4
                                >>> c1.count('1',1)
                                1
                                >>> c1.count('1',0,0)
                                0
                                >>> c1.count('1',0,1)
                                1
                                >>> c1.count('1',0,2)
                                2
                                >>> c1.count('2',0,2)
                                0
                                >>> c2.count('ab')
                                4
                                >>> c2.count('abc')
                                1                                                   
                                
                                
字符截取与拼接类
-----------------------
字符截取与拼接的方法如下::

    str.partition(sep) 从左向右开始匹配进行切割，以sep作为分隔符，返回 (head, sep, tail),返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
                                如果查找不到sep,则返回(str,'','')
    str.rpartition(sep) 从右向左开始匹配进行切割，以sep作为分隔符，返回 (head, sep, tail);
                                如果查找不到sep,则返回('','',str)
                                >>> c1='abcdcba'
                                >>> c1.partition('a')    # 第1个字符就是a,所以head=''
                                ('', 'a', 'bcdcba')
                                >>> c1.rpartition('a')     # 从右向左匹配，第1个字符就是a,所以tail=''
                                ('abcdcb', 'a', '')
                                >>> c1.partition('b')    
                                ('a', 'b', 'cdcba')
                                >>> c1.rpartition('b')
                                ('abcdc', 'b', 'a')
                                >>> c1.partition('c')
                                ('ab', 'c', 'dcba')
                                >>> c1.rpartition('c')
                                ('abcd', 'c', 'ba')
                                >>> c1.partition('x')    # 查找不到字符x,返回两个空的''
                                ('abcdcba', '', '')
                                >>> c1.rpartition('x')
                                ('', '', 'abcdcba')
    str.join(seq)                 使用字符串str将可迭代序列seq连接起来形成一个新的字符串
                                >>> str = "-";
                                >>> seq = ("a", "b", "c");
                                >>> str.join(seq)
                                'a-b-c'
                                >>> c3
                                'AAAA'
                                >>> "_".join(c3)
                                'A_A_A_A'
                                >>> str1='###'
                                >>> c3
                                'AAAA'
                                >>> str1.join(c3)
                                'A###A###A###A'
                                >>> str2="_*_"
                                >>> str2
                                '_*_'
                                >>> str2.join(c3)
                                'A_*_A_*_A_*_A'
                                >>> ';'.join(str1)
                                '#;#;#'
                                # 将列表中每个元素使用_下划线连接起来
                                >>> li = ['alex','eric','rain']
                                >>> li
                                ['alex', 'eric', 'rain']
                                >>> '_'.join(li)
                                'alex_eric_rain'
                                
    str.strip([chars])          移除字符串str两端的字符(默认是whitespace，空格或tab键)
                                如果指定字符串chars，则移除字符串str两端带有chars含有的字符的所有字符
                                # 定义5个字符串    
                                >>> str1='   abc '
                                >>> str1
                                '   abc '
                                >>> str2='\t  abc \t'
                                >>> str2
                                '\t  abc \t'
                                >>> str3='\t  abc \t'
                                >>> str3
                                '\t  abc \t'
                                >>> str4='000abcde000'
                                >>> str4
                                '000abcde000'
                                >>> str5='000 abc 000'
                                >>> str5
                                '000 abc 000'

                                # 以默认方式移除两端字符
                                >>> str1.strip()
                                'abc'
                                >>> str2.strip()
                                'abc'
                                >>> str3.strip()
                                'abc'
                                >>> str4.strip()
                                '000abcde000'
                                >>> str5.strip()
                                '000 abc 000'

                                # 指定chars为字符'0'，仅移除两端的字符'0'
                                >>> str1.strip('0')
                                '   abc '
                                >>> str2.strip('0')
                                '\t  abc \t'
                                >>> str3.strip('0')
                                '\t  abc \t'
                                >>> str4.strip('0')
                                'abcde'
                                >>> str5.strip('0')
                                ' abc '

                                # 指定chars为字符'0'和' '空格，
                                # 需要移除两端的字符'0'和空格，但此时的'\t'tab键不会被移除
                                >>> str1.strip('0 ')
                                'abc'
                                >>> str2.strip('0 ')
                                '\t  abc \t'
                                >>> str3.strip('0 ')
                                '\t  abc \t'
                                >>> str4.strip('0 ')
                                'abcde'
                                >>> str5.strip('0 ')
                                'abc'

                                # 指定chars为字符'0'和' '空格以及'\t'tab键，
                                # 需要移除两端的字符'0'和空格，且'\t'tab键也会被移除
                                >>> str1.strip('0 \t')
                                'abc'
                                >>> str2.strip('0 \t')
                                'abc'
                                >>> str3.strip('0 \t')
                                'abc'
                                >>> str4.strip('0 \t')
                                'abcde'
                                >>> str5.strip('0 \t')
                                'abc'
    str.lstrip([chars])            移除左侧的字符串，规格与str.strip()类似，但仅移除左侧的字符串
                                >>> str1.lstrip()
                                'abc '
                                >>> str2.lstrip()
                                'abc \t'
                                >>> str3.lstrip()
                                'abc \t'
                                >>> str4.lstrip()
                                '000abcde000'
                                >>> str5.lstrip()
                                '000 abc 000'
                                >>> str1.lstrip('0')
                                '   abc '
                                >>> str2.lstrip('0')
                                '\t  abc \t'
                                >>> str3.lstrip('0')
                                '\t  abc \t'
                                >>> str4.lstrip('0')
                                'abcde000'
                                >>> str5.lstrip('0')
                                ' abc 000'
                                >>> str1.lstrip('0 ')
                                'abc '
                                >>> str2.lstrip('0 ')
                                '\t  abc \t'
                                >>> str3.lstrip('0 ')
                                '\t  abc \t'
                                >>> str4.lstrip('0 ')
                                'abcde000'
                                >>> str5.lstrip('0 ')
                                'abc 000'
    str.rstrip([chars])            移除右侧的字符串，规格与str.strip()类似，但仅移除右侧的字符串
    str.split(sep=None, maxsplit=-1) 以分隔符sep对str字符串进行分隔，最多分隔maxsplit次
                                若不指定分隔符sep，则默认以whitespace(空格，换行\n，制表符\t)为分隔符；
                                若不指定最多分隔次数maxsplit，则全部分隔
                                >>> str1='0a\t b\tcb a0'
                                >>> str1
                                '0a\t b\tcb a0'
                                >>> str1.split()
                                ['0a', 'b', 'cb', 'a0']
                                >>> str1.split(None,2)
                                ['0a', 'b', 'cb a0']
                                >>> str1.split(None,1)
                                ['0a', 'b\tcb a0']
                                >>> str1.split(None,0)
                                ['0a\t b\tcb a0']
                                >>> str1.split(None,3)
                                ['0a', 'b', 'cb', 'a0']    
                                >>> str1.split('0')
                                ['', 'a\t b\tcb a', '']
                                >>> str1.split('0',1)
                                ['', 'a\t b\tcb a0']
                                >>> str1.split('0',2)
                                ['', 'a\t b\tcb a', '']
                                >>> str1.split('a')
                                ['0', '\t b\tcb ', '0']
                                >>> str1.split('b')
                                ['0a\t ', '\tc', ' a0']
    str.rsplit(sep=None, maxsplit=-1) 以分隔符sep对str字符串从结尾处进行分隔，最多分隔maxsplit次
                                若不指定分隔符sep，则默认以whitespace(空格，换行\n，制表符\t)为分隔符；
                                若不指定最多分隔次数maxsplit，则全部分隔
                                >>> str1.rsplit()
                                ['0a', 'b', 'cb', 'a0']
                                >>> str1.rsplit('0')
                                ['', 'a\t b\tcb a', '']
                                >>> str1.rsplit('0',1)
                                ['0a\t b\tcb a', '']
                                >>> str1.rsplit('a',1)
                                ['0a\t b\tcb ', '0']
                                >>> str1.split('a',1)
                                ['0', '\t b\tcb a0']
                                >>> str1.split('b',1)
                                ['0a\t ', '\tcb a0']
                                >>> str1.rsplit('b',1)
                                ['0a\t b\tc', ' a0']
    str.splitlines([keepends])        Python splitlines() 按照行('\r', '\r\n', \n')分隔，
                                返回一个包含各行作为元素的列表，
                                如果参数 keepends 为 False，不包含换行符;
                                如果为 True，则保留换行符。    
                                >>> str2='a\n\rb\nc\rd\r\ne'
                                >>> str2
                                'a\n\rb\nc\rd\r\ne'
                                >>> str2.split()
                                ['a', 'b', 'c', 'd', 'e']
                                >>> str2.splitlines()
                                ['a', '', 'b', 'c', 'd', 'e']
                                >>> str2.splitlines(True)
                                ['a\n', '\r', 'b\n', 'c\r', 'd\r\n', 'e']
                                
                                
字符替换类
-----------------
字符替换的方法如下::

    str.expandtabs(tabsize=8)    将tab键扩展为空格，若不指定tab大小，则默认以8个空格替换一个tab键
                                strtab = 'ab    b'
                                strspace = strtab.expandtabs()
                                print(strspace)
                                ab      c
                                print(strtab.expandtabs(tabsize=4))
                                ab  c
    str.replace(old, new[, count])    字符串替换，以new字符串替换str中的old字符串
                                如果指定count值，则仅替换前面count个匹配值
                                >>> c1='abcdcbadcba'
                                >>> c1.replace('a','A')
                                'AbcdcbAdcbA'
                                >>> c1.replace('a','A',2)
                                'AbcdcbAdcba'
                                >>> c1.replace('a','A',1)
                                'Abcdcbadcba'
                                >>> c1.replace('a','A',0)
                                'abcdcbadcba'
                                >>> c1.replace('a','A',3)
                                'AbcdcbAdcbA'                            
                                
字符查找类
---------------------
字符查找的方法如下::

    str.find(sub[, start[, end]])   查找最低索引，从左侧开始查找
                                >>> str1='0123456543210'
                                >>> str1
                                '0123456543210'
                                >>> str1.find('0')
                                0
                                >>> str1.find('1')
                                1
                                >>> str1.find('2')
                                2
                                >>> str1.find('3')
                                3
                                >>> str1.find('3',1)
                                3
                                >>> str1.find('3',5)
                                9
                                >>> str1.find('3',5,6)
                                -1
                                >>> str1.find('34',5,-1)
                                -1
                                >>> str1.find('32',5,-1)
                                9
    str.rfind(sub[, start[, end]])  查找最高索引，从右侧开始查找
                                >>> str1.rfind('0')
                                12
                                >>> str1.rfind('1')
                                11
                                >>> str1.rfind('2')
                                10
                                >>> str1.rfind('3')
                                9    
                                
                                
翻译类
--------------------
翻译的方法如下::
                                 
    str.translate(trantab)    使用翻译字典表trantab对字符串进行翻译
    str.maketrans(intab,outtab)或str.maketrans(dicttab) 创建翻译字典键值对intab:outtab，或以某字段dicttab构建翻译字典表
                                >>> intab='aeiou'
                                >>> outtab='12345'
                                >>> trantab = str.maketrans(intab,outtab)
                                >>> trantab
                                {97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
                                >>> str ="this is string example... wow!!"
                                >>> print(str.translate(trantab))
                                th3s 3s str3ng 2x1mpl2... w4w!!
                                >>> str2='abcdefabc'
                                >>> str2.translate(tr)
                                '\x01\x02\x03def\x01\x02\x03'
                                >>> dict1={'a':'1','b':2,'c':'3','d':'4'}
                                >>> ttab=str.maketrans(dict1)
                                >>> ttab
                                {97: '1', 98: 2, 99: '3', 100: '4'}
                                >>> str2.translate(ttab)
                                '1\x0234ef1\x023'
                                
                                
格式化类
----------------------
格式化的方法如下::

    str.format(*args, **kwargs)    format方法被用于字符串的格式化输出
                                # 通过手动编号或自动编号输出数据
                                >>> print('{0}+{1}={2}'.format('A','B','C')) # 手动编号，将format中字符依次填入
                                A+B=C
                                >>> print('{}+{}={}'.format('A','B','C'))  # 自动编号形式，按顺序将format的字段填充到相应的大括号{}对应处
                                A+B=C
                                >>> print('{1}+{0}={2}'.format('A','B','C')) # 手动编号，可改变format中字符的出现顺序
                                B+A=C
                                >>> print('{1}+{2}={0}'.format('A','B','C')) # 手动编号，可改变format中字符的出现顺序
                                B+C=A
                                # 手动编号与自动编号不能一起混用，否则会报错：
                                >>> print('{1}+{0}={}'.format('A','B','C'))
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                ValueError: cannot switch from manual field specification to automatic field numbering

                                # 输出字符串，在对应位置填入对应的值
                                >>> print('{} love to learn {}'.format('I','Python'))
                                I love to learn Python
                                >>> print('{0} love to learn {1}'.format('I','Python'))
                                I love to learn Python

                                # 输出变量字符串的值
                                >>> str1='string'
                                >>> str1
                                'string'
                                >>> print('The length of {0} is {1}'.format(str1,len(str1)))
                                The length of string is 6

                                # 通过列表索引设置输出参数
                                >>> list1=['a','b','c']
                                >>> list1
                                ['a', 'b', 'c']
                                >>> print('The string is {0[0]}+{0[1]}+{0[2]}'.format(list1))
                                The string is a+b+c
                                >>> print('The string is {0}{0}{0}'.format(list1))
                                The string is ['a', 'b', 'c']['a', 'b', 'c']['a', 'b', 'c']

                                # 通过字典设置输出参数
                                >>> dict1={'name':'Mei','lang':'Python'}
                                >>> dict1
                                {'name': 'Mei', 'lang': 'Python'}
                                >>> print('You name is {0[name]} and you love to learn {0[lang]}'.format(dict1))
                                You name is Mei and you love to learn Python
                                注：字典也可以通过以下关键字参数的方式传入

                                # 通过关键字参数作为传入参数，字典前加**
                                >>> dict1={'name':'Mei','lang':'Python'}
                                >>> dict1
                                {'name': 'Mei', 'lang': 'Python'}
                                >>> print('You name is {name} and you love to learn {lang}'.format(**dict1))
                                You name is Mei and you love to learn Python
                                # 通过关键字参数作为传入参数
                                >>> print('You name is {name} and you love to learn {lang}'.format(name='Mei',lang='Python'))
                                You name is Mei and you love to learn Python

                                # 字符填充与格式化
                                :[填充字符][对齐方式 <^>][宽度]
                                ^, <, > 分别是居中、左对齐、右对齐(默认)，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
                                # 右对齐，长度为1，左侧填充空格
                                >>> print('{0:1}'.format(3))
                                3
                                # 右对齐，长度为2，左侧填充空格
                                >>> print('{0:2}'.format(3))
                                 3
                                # 右对齐，长度为3，左侧填充空格
                                >>> print('{0:3}'.format(3))
                                  3
                                >>> print('{0:#3}'.format(3))
                                  3
                                # 右对齐，长度为3，左侧填充指定字符#
                                >>> print('{0:#>3}'.format(4))
                                ##4
                                # 右对齐，长度为3，左侧填充指定字符@
                                >>> print('{0:@>3}'.format(4))
                                @@4
                                # 右对齐，长度为3，左侧填充指定字符!
                                >>> print('{0:!>3}'.format(4))
                                !!4
                                # 右对齐，长度为3，左侧填充指定字符0
                                >>> print('{0:0>3}'.format(4))
                                004
                                # 右对齐，长度为3，左侧填充指定字符%
                                >>> print('{0:%>3}'.format(4))
                                %%4
                                # 右对齐，长度为3，左侧填充指定字符*
                                >>> print('{0:*>3}'.format(4))
                                **4
                                # 右对齐，长度为6，左侧填充指定字符*
                                >>> print('{0:*>6}'.format(4))
                                *****4
                                # 左对齐，长度为6，右侧填充指定字符*
                                >>> print('{0:*<6}'.format(4))
                                4*****
                                # 居中对齐，长度为6，左面两侧填充指定字符*
                                >>> print('{0:*^6}'.format(4))
                                **4***
                                # 居中对齐，长度为7，左面两侧填充指定字符*
                                >>> print('{0:*^7}'.format(4))
                                ***4***

                                # 数字格式化控制
                                >>> import math
                                >>> math.pi
                                3.141592653589793
                                >>> pi=math.pi
                                >>> pi
                                3.141592653589793
                                # 保留小数点后两位小数
                                >>> print('{:.2f}'.format(pi))
                                3.14
                                >>> print('{0:.2f}'.format(pi))
                                3.14
                                # 保留小数点后三位小数
                                >>> print('{:.3f}'.format(pi))
                                3.142
                                >>> print('{0:.3f}'.format(pi))
                                3.142
                                # 带符号保留小数点后三位小数
                                >>> print('{0:+.3f}'.format(-pi))
                                -3.142
                                >>> print('{0:+.3f}'.format(pi))
                                +3.142
                                # 输出整数
                                >>> print('{0:.0f}'.format(pi))
                                3
                                # 输出以逗号分隔的数字格式
                                >>> num=1234567890
                                >>> num
                                1234567890
                                >>> print('{0:,}'.format(num))
                                1,234,567,890

                                # 输出百分比的数字格式
                                >>> per = 0.6645
                                >>> print('{0:.2%}'.format(per))
                                66.45%
                                >>> print('{0:.1%}'.format(per))
                                66.5%

                                # 输出指数形式的数字格式
                                >>> bignum=pow(10,9)
                                >>> bignum
                                1000000000
                                >>> print('{0:.1e}'.format(bignum))
                                1.0e+09
                                >>> print('{0:.2e}'.format(bignum))
                                1.00e+09

                                # 进制转换
                                # b、d、o、x 分别是二进制(0b开头)、十进制、八进制(0o开头)、十六进制(0x或0X开头)
                                # 添加#井号后，输出字符会带相应的进制标识
                                >>> x=12
                                >>> print('{0:b}'.format(x))
                                1100
                                >>> print('{0:d}'.format(x))
                                12
                                >>> print('{0:o}'.format(x))
                                14
                                >>> print('{0:x}'.format(x))
                                c
                                >>> print('{0:X}'.format(x))
                                C
                                >>> print('{0:#o}'.format(x))
                                0o14
                                >>> print('{0:#b}'.format(x))
                                0b1100
                                >>> print('{0:#d}'.format(x))
                                12
                                >>> print('{0:#o}'.format(x))
                                0o14
                                >>> print('{0:#x}'.format(x))
                                0xc
                                >>> print('{0:#X}'.format(x))
                                0XC

                                # 输出大括号，使用大括号{}来转义大括号
                                >>> print("{0:#X}{{'abc'}}".format(x))
                                0XC{'abc'}
    str.format_map(dict1) 通过dict字典关键字参数输出，这种方式比format形式运行速度快。
                                    
                                # 通过关键字参数作为传入参数，字典前加**
                                >>> dict1={'name':'Mei','lang':'Python'}
                                >>> dict1
                                {'name': 'Mei', 'lang': 'Python'}
                                >>> print('You name is {name} and you love to learn {lang}'.format(**dict1))
                                You name is Mei and you love to learn Python
                                >>> print('You name is {name} and you love to learn {lang}'.format_map(dict1))
                                You name is Mei and you love to learn Python

                                # 计算两种方式运行所用的时间
                                import timeit
                                dict1 = {'name': 'Mei', 'lang': 'Python'}
                                start = timeit.default_timer()
                                print('You name is {name} and you love to learn {lang}'.format(**dict1))
                                end1 = timeit.default_timer()
                                print('You name is {name} and you love to learn {lang}'    _map(dict1))
                                end2 = timeit.default_timer()
                                print(str(end1-start))
                                print(str(end2-end1))
                                输出结果如下：
                                You name is Mei and you love to learn Python
                                You name is Mei and you love to learn Python
                                3.202066400183586e-05
                                1.0673554667278617e-05
                                
编码类
-----------------

- 编码是将字符串转化为一系列字节的过程。
- 解码是将字节序列转化为Unicode字符串的过程。

编码的方法如下::

    str.encode(encoding='utf-8', errors='strict')  按某种encoding格式进行编码，返回一个字节流bytes对象
    python3默认以utf-8对字符串进行编码，encode为编码，decode为解码。
                                >>> str1='我爱python'    
                                >>> str1
                                '我爱python'
                                >>> str1.encode()
                                b'\xe6\x88\x91\xe7\x88\xb1python'
                                >>> str1.encode(encoding='utf-8')
                                b'\xe6\x88\x91\xe7\x88\xb1python'
                                >>> byte_code1 = str1.encode('utf-8')
                                >>> byte_code1
                                b'\xe6\x88\x91\xe7\x88\xb1python'    
                                >>> byte_code1.decode('gb2312')
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                UnicodeDecodeError: 'gb2312' codec can't decode byte 0xe6 in position 0: illegal multibyte sequence
                                >>> byte_code1.decode('utf-8')
                                '我爱python'
                                >>> str2 = byte_code1.decode('utf-8')
                                >>> str2
                                '我爱python'
                                >>> str2.encode('gb2312')
                                b'\xce\xd2\xb0\xaepython'
                                >>> byte_code2 = str2.encode('gb2312')
                                >>> byte_code1
                                b'\xe6\x88\x91\xe7\x88\xb1python'
                                >>> byte_code2
                                b'\xce\xd2\xb0\xaepython'
                                >>> byte_code2 = str2.encode('gb2312')
                                >>> str3 = byte_code2.decode('utf-8')
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                UnicodeDecodeError: 'utf-8' codec can't decode byte 0xce in position 0: invalid continuation byte
                                >>> str3 = byte_code2.decode('gb2312')
                                >>> str3
                                '我爱python'
