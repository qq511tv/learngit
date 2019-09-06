#异常
#try:
#    fileName = input("请输入您的文件名")
#    open("%s.txt" %fileName)
#except FileNotFoundError:
#    print("%s.txt文件在当前目录下未找到" %fileName)

# try:
#     stu = "java"
#     print(stu)
# except NameError:
#     print("stu 未定义")
'''
try:#BaseException所有异常的父类 可捕捉所有异常
    print(stu)
except BaseException:
    print("stu 未定义")

try:#BaseException所有异常的父类 可捕捉所有异常
    stu = "java"
    print(stu)
except BaseException as msg:#捕获系统的异常提示语句
    print(msg)
else:
    print("stu已经定义")#没有异常则会执行else里的内容
'''
# try:#BaseException所有异常的父类 可捕捉所有异常
#    # stu = "java"
#     print(stu)
# except BaseException as msg:#捕获系统的异常提示语句
#     print(msg)
# finally:
#     print("不管前面 总要执行这个")#没有异常则会执行else里的内容

#raise事先定义一个条件，满足则会抛出异常
def division(x,y):
    if y == 0:
        raise ZeroDivisionError("被除数不能为0")#raise只能用python的标准异常类来承接
    return  x/y

try:
    division(8,0)
except BaseException as msgg:
    print(msgg)

