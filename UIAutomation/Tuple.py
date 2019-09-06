#元组 定义后就不能改了
course = ('Chinese','Math','English','computer')
print(course)
print(course[-1])
print(course[1:3])
print(course[1:])#把索引下标为1之后的元素显示出来
print(course[:2])
#返回有多少个元素
print(len(course))
#要定义一个只有1个元素的元组，则需要在元素后面加逗号，用来消除数学歧义
t = (1,)
print(t)

score = (13,2,3,4,5,6)
print(max(score))#返回最大值


