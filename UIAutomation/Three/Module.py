#import time #全部导入
import random
from time import sleep #只导入time包里的sleep方法
from HomeWork.Student import Student#有层级的调用
#py优先找当前目录下的类，再找PYHOPPATH下的，再找默认安装的路径下
#print(time.ctime())
num = random.randint(100,100)
print(num)
sleep(5)
print("Sleep over!")

stu = Student("小芳","杭州")
