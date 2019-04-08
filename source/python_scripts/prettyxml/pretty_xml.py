#!/usr/bin/python3
"""
@Time    : 2019/4/8 20:29
@Author  : Mei Zhaohui
@Email   : mzh.whut@gmail.com
@File    : pretty_xml.py
@Software: PyCharm
"""
import xml.etree.ElementTree as ET


def prettyxml(element, indent='    ', newline='\n', level=0):
    """
    美化XML Element对象
    :param element: Element对象，写入文件时，推荐使用root
    :param indent: 缩进空格，默认4个空格
    :param newline: 换行符
    :param level: 缩进层次
    :return:
    """
    # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:  # 判断element是否有子元素
        if not element.text or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) \
                           + element.text.strip() + newline + indent * (level + 1)

    temp = list(element)  # 将elemnt转成list
    for subelement in temp:
        # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else:
            subelement.tail = newline + indent * level
        prettyxml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作


def main():
    """main function"""
    tree = ET.parse('data.xml')
    root = tree.getroot()
    prettyxml(root)
    tree.write('output.xml',
               encoding='utf-8',
               xml_declaration=True,
               method='xml',
               short_empty_elements=False)


if __name__ == '__main__':
    main()
