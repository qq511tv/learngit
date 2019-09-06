#猜数0~100游戏，并且给出大小提示 直至正确
import random
answer = random.randint(1,100)#生成0~100随机数
print(answer)
num = 0
#判断
while answer != int(num):
    num = input("===========请输入您猜测的数字===========")
    if int(num) > answer:
        print("***您输错了,输入的过大***")
    elif int(num) < answer:
        print("***您输错了,输入的过小***")

print("恭喜正确")