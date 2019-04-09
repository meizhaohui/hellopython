.. _json_module:

模块-json模块
======================

.. contents:: 目录

json模块基本介绍
----------------------

- 存储数据结构到一个文件中称为 ``序列化(Serialize)`` ， 从文件中解析数据并存储到数据结构中称为 ``反序列化(Deserialize)`` 。
- JSON (JavaScript Object Notation) is a lightweight data interchange format是一种轻量级的数据交换格式。
- ``json.dumps`` 将Python数据类型转换成JSON字符串。

语法格式::

    json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

- ``json.dump`` 把Python数据类型转换成JSON字符串并存储在文件中(序列化)。

语法格式::

    json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw) 
    
- ``json.loads`` 把JSON字符串转换成Python数据类型。

语法格式::

    json.loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    
- `json.load`` 将文件中的JSON字符串转换成Python数据类型(反序列化)。

语法格式::

    json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    
    
引用json模块及帮助信息::
    
    In [1]: import json

    In [2]: json?
    Type:        module
    String form: <module 'json' from 'd:\\programfiles\\python362\\lib\\json\\__init__.py'>
    File:        d:\programfiles\python362\lib\json\__init__.py
    Docstring:
    JSON (JavaScript Object Notation) <http://json.org> is a subset of
    JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
    interchange format.

    :mod:`json` exposes an API familiar to users of the standard library
    :mod:`marshal` and :mod:`pickle` modules.  It is derived from a
    version of the externally maintained simplejson library.

    Encoding basic Python object hierarchies::

        >>> import json
        >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])  # 将列表转成JSON字符串
        '["foo", {"bar": ["baz", null, 1.0, 2]}]'
        >>> print(json.dumps("\"foo\bar"))
        "\"foo\bar"
        >>> print(json.dumps('\u1234'))
        "\u1234"
        >>> print(json.dumps('\\'))
        "\\"
        >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
        {"a": 0, "b": 0, "c": 0}
        >>> from io import StringIO
        >>> io = StringIO()  # 创建一个IO StringIO缓存对象
        >>> json.dump(['streaming API'], io)  # 将字符串列表写入到IO对象中
        >>> io.getvalue()  # 获取对象中的所有数据
        '["streaming API"]'                                                          
                                                                                     
    Compact encoding::                                                               
                                                                                     
        >>> import json                                                              
        >>> from collections import OrderedDict                                      
        >>> mydict = OrderedDict([('4', 5), ('6', 7)])                               
        >>> json.dumps([1,2,3,mydict], separators=(',', ':'))  # seperators分隔符是(item_separator, key_separator)的元组，默认(', ', ': ')                       
        '[1,2,3,{"4":5,"6":7}]'                                                      
                                                                                     
    Pretty printing::                                                                
                                                                                     
        >>> import json                                                              
        >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))  # 使用sort_keys表示对键进行排序，indent表示缩进4个空格
        {                                                                            
            "4": 5,                                                                  
            "6": 7                                                                   
        }                                                                            
                                                                                     
                                                                  
    Decoding JSON::

        >>> import json
        >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
        >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj  # 将JSON字符串转换成列表对象
        True
        >>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
        True
        >>> from io import StringIO
        >>> io = StringIO('["streaming API"]')
        >>> json.load(io)[0] == 'streaming API'
        True

    Specializing JSON object decoding::

        >>> import json
        >>> def as_complex(dct):
        ...     if '__complex__' in dct:
        ...         return complex(dct['real'], dct['imag'])  # 创建一个复数
        ...     return dct
        ...
        >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
        ...     object_hook=as_complex)  # 指定自定义解码的函数
        (1+2j)
        >>> from decimal import Decimal
        >>> json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
        True

    Specializing JSON object encoding::

        >>> import json
        >>> def encode_complex(obj):
        ...     if isinstance(obj, complex):
        ...         return [obj.real, obj.imag]
        ...     raise TypeError(repr(o) + " is not JSON serializable")
        ...
        >>> json.dumps(2 + 1j, default=encode_complex)
        '[2.0, 1.0]'
        >>> json.JSONEncoder(default=encode_complex).encode(2 + 1j)
        '[2.0, 1.0]'


    Using json.tool from the shell to validate and pretty-print::

        $ echo '{"json":"obj"}' | python -m json.tool
        {
            "json": "obj"
        }
        $ echo '{ 1.2:3.4}' | python -m json.tool
        Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

JSON字符串转Python数据类型对应关系表:

+-------------------+-------------+
|    JSON           |     Python  |
+===================+=============+
|    object         |     dict    |
+-------------------+-------------+
|    array          |     list    |
+-------------------+-------------+
|    string         |     str     |
+-------------------+-------------+
|    number (int)   |     int     |
+-------------------+-------------+
|    number (real)  |     float   |
+-------------------+-------------+
|    true           |     True    |
+-------------------+-------------+
|    false          |     False   |
+-------------------+-------------+
|    null           |     None    |
+-------------------+-------------+

Python数据类型转JSON字符串对应关系表:

+----------------------------------------+----------------+
|                  Python                |       JSON     |
+========================================+================+
|                  dict                  |      object    |
+----------------------------------------+----------------+
|                list, tuple             |       array    |
+----------------------------------------+----------------+
|                  str                   |     string     |
+----------------------------------------+----------------+
| int, float, int- & float-derived Enums |     number     |
+----------------------------------------+----------------+
|                  True                  |       true     |
+----------------------------------------+----------------+
|                  False                 |       false    |
+----------------------------------------+----------------+
|                  None                  |       null     |
+----------------------------------------+----------------+


json模块的操作如下::

    #!/usr/bin/python3                                                                                                                                                      
    # -*- coding: utf-8 -*-
    # ----------------------------------------------------------
    # @Time          : At 下午8:11 九月 06, 2018 
    # @Author        : 梅朝辉(meizhaohui)
    # @Email         : mzh.whut@gmail.com
    # @Filename      : ReadJson.py
    # @Description   : 处理json数据
    # @Software      : PyCharm
    # @Python Version: python3.6.2
    # ----------------------------------------------------------

    import json
    JSON_STRING = '{"username":"meizhaohui","password":"passwd"}'
    DICT_DATA = {"username": "meizhaohui", "ID":1, "password": "passwd"}
    class jsonAPI:
        def json_to_dict(self, json_string=JSON_STRING):
            """
            将JSON字符串转换成dict字典
            :param json_string: JSON字符串
            :return: dict
            """
            return json.loads(json_string)

        def dict_to_json(self, dict_data):
            """
            将dict字典转换成JSON字符串
            :param dict_data: dict字典
            :return: str
            """
            return json.dumps(dict_data)

        def json_file_to_dict(self, filename):
            """
            读取json文件到dict字典中
            :param filename:  json文件
            :return: dict
            """
            with open(filename) as file:
                return json.load(file)

        def write_json_to_file(self, filename, dict_data):
            """
            将数据转为json字符串并写入文件
            :param filename: 文件名
            :param dict_data: 字典数据
            :return: NoneType
            """
            with open(filename, 'w') as file:
                return json.dump(dict_data, file)

        def write_pretty_json_to_file(self, filename, dict_data):
            """
            将数据转为json字符串并写入文件
            :param filename: 文件名
            :param dict_data: 字典数据
            :return: NoneType
            """
            with open(filename, 'w') as file:
                # sort_keys 是否按key排序,默认False
                # indent 缩进长度，几个空格，建议用4或"    "四个空格
                # seperators分隔符是(item_separator, key_separator)的元组，默认(', ', ': ')
                # 第一个是每行键值对后的分隔符，第二个是每行键值对之间的分隔符
                return json.dump(dict_data, file, sort_keys=True, indent=4, separators=(',', ': '))


    if __name__ == "__main__":
        JAPI = jsonAPI()
        print(JAPI.json_to_dict(JSON_STRING))
        print(type(JAPI.json_to_dict(JSON_STRING)))
        print(JAPI.dict_to_json(DICT_DATA))
        print(type(JAPI.dict_to_json(DICT_DATA)))
        FILENAME='json_file.json'
        print(JAPI.json_file_to_dict(FILENAME))
        print(type(JAPI.json_file_to_dict(FILENAME)))
        NEW_JSON_FILE='new_json.json'
        print(type(JAPI.write_json_to_file(NEW_JSON_FILE, DICT_DATA)))
        PRETTY_JSON_FILE = 'pretty_json.json'
        print(type(JAPI.write_pretty_json_to_file(PRETTY_JSON_FILE, DICT_DATA)))


    """
    output as follow:

    {'username': 'meizhaohui', 'password': 'passwd'}
    <class 'dict'>
    {"username": "meizhaohui", "ID": 1, "password": "passwd"}
    <class 'str'>
    {'user_id': 1, 'username': 'meizhaohui', 'password': 'passwd'}
    <class 'dict'>
    <class 'NoneType'>
    <class 'NoneType'>


    json_file.json content:
    {
        "user_id":1,
        "username":"meizhaohui",
        "password":"passwd"
    }

    new_json.json content:
    {"username": "meizhaohui", "ID": 1, "password": "passwd"}

    pretty_json.json
    {
        "ID": 1,
        "password": "passwd",
        "username": "meizhaohui"
    }

    """    

参考文献:

- `json — JSON encoder and decoder <https://docs.python.org/3/library/json.html?highlight=json>`_