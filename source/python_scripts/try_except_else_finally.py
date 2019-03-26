# Filename: try_except_else_finally.py
# Author: meizhaohui
def expt4(a, b):
    try:
        c = a/b
        print('the value is:{}'.format(c))
        return 'try'
    except ZeroDivisionError:
        print('程序出现异常，异常信息：被除数为0')
        return 'exceptZero'
    except TypeError:
        print('程序出现异常，异常信息：参数a或b的类型不支持，仅支持float或int类型')
        return 'exceptType'
    else:
        print('No exception')
        return 'else'
    finally:
        print('always display')
        # return 'finally'

if __name__ == '__main__':
    return_string = expt4(4, 0)
    print('return_string:{}'.format(return_string))

# def expt3(a, b):
#     try:
#         c = a/b
#         print('the value is:{}'.format(c))
#     except ZeroDivisionError:
#         print('程序出现异常，异常信息：被除数为0')
#     except TypeError:
#         print('程序出现异常，异常信息：参数a或b的类型不支持，仅支持float或int类型')
#     else:
#         print('No exception')
#     finally:
#         print('always display')
# expt3(4, 2)

# def expt2(a, b):
#     try:
#         c = a/b
#         print('the value is:{}'.format(c))
#     except ZeroDivisionError:
#         print('程序出现异常，异常信息：被除数为0')
#     except TypeError:
#         print('程序出现异常，异常信息：参数a或b的类型不支持，仅支持float或int类型')
# expt2(4, 2)


# def expt1(a, b):
#     try:
#         c = a/b
#         print('the value is:{}'.format(c))
#     except ZeroDivisionError:
#         print('程序出现异常，异常信息：被除数为0')
# 
# expt1(4,'')
