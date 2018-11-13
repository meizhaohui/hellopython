.. _02_quote_escape_character:

引号与转义符的使用
================================

.. contents:: 目录


概述  
--------------------
在python中使用引号包裹字符串或doc说明文档。


单引号  '                    
    使用单引号指示字符串，所有的空白都会原样保留
双引号  \"                    
    在双引号中的字符串与单引号的使用相同
三引号  \'\'\'  或  \"\"\"            
    利用三引号可以指示一个多行的字符串，在三引号中可以自由的使用单引号或双引号
    
**注意：以上引号在页面中显示不正常，以下面的代码显示为准。**

引号的使用
--------------------

    >>> 'Quote me on this'
    'Quote me on this'
    >>> "Quote me on this"
    'Quote me on this'
    >>> '''Quote me on this
    ... the second line
    ... the third line
    ... '''
    'Quote me on this\nthe second line\nthe third line\n'
    >>> """Quote me on this
    ... the second line
    ... the third line
    ... """
    'Quote me on this\nthe second line\nthe third line\n'
    >>> print('Quote me on this\nthe second line\nthe third line\n')
    Quote me on this
    the second line
    the third line
    >>> print('Quote me on this\nthe second line\nthe third line\n')
    Quote me on this
    the second line
    the third line

转义符
---------------

使用反斜杠\\作为转义符

\"	# 表示双引号

\\	# 表示反斜杠

\n	# 表示换行符

\\   # 行末单独一个反斜杠并不表示转义，而是字符串在下一行继续，并不是开始新的一行。
不使用转义符时，有时会发现错误，python不知道字符串从何处开始，何处结束。

    >>> print('this's is a line')
      File "<stdin>", line 1
        print('this's is a line')
                    ^
    SyntaxError: invalid syntax
    >>> print('this\'s is a line')
    this's is a line
    >>> print("this's is a line.\n"this is the other line"")
      File "<stdin>", line 1
        print("this's is a line.\n"this is the other line"")
                                      ^
    SyntaxError: invalid syntax
    >>> print("this's is a line.\n\"this is the other line\"")
    this's is a line.
    "this is the other line"
    >>>
    >>> print("this's is a line.\
    ... 'this is not the second line. this is the first line too'"
    ... )
    this's is a line.'this is not the second line. this is the first line too'

    
自然字符串
-------------------

如果您不希望一个字符串被转义，通过使用自然字符串可以解决这个问题。
    
自然字符串通过在字符串前面加上前缀r或R来批指定。

\\n 转义后表示换行。
    
    >>> print("this's is a line.\n")
    this's is a line.
    >>> print(r"this's is a line.\n")
    this's is a line.\n
    >>> print(R"this's is a line.\n")
    this's is a line.\n
