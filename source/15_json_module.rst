.. _15_json_module:

模块-json模块
======================

.. contents:: 目录

json模块基本介绍
----------------------
- JSON (JavaScript Object Notation) is a lightweight data interchange format是一种轻量级的数据交换格式。
- json dumps把数据类型转换成字符串
- dump把数据类型转换成字符串并存储在文件中
- loads把字符串转换成数据类型
- load把文件打开从字符串转换成数据类型


引用json模块语法::
    
    import json

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
                # indent 缩进长度，几个空格，建议用4或“    ”四个空格
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
