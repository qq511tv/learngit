#txt文件的读写 csv文件的读写
f = open("stu_info.txt","r")
lines = f.readlines()
print(lines)#读取所有内容 写成一个行的列表

for line in lines:
    print(line.split(",")[0])#读取每行 以逗号为切割符切割每行 打印每行第一个
print("=====================================")

import csv
# #csv文件 ----读
# csv_file = csv.reader(open("Stu_info.csv","r"))
# #csv文件每一行会是一个以逗号分隔的列表
# for stu in csv_file:
#     print(stu)
#     print(stu[0])
# print("2=====================================2")
#写csv文件
stu = ["Marry","28","JingDeZheng"]
stu1 = ["Rom","23","ChengDu"]

out = open('Stu_info.csv','a',newline='')#a代表追加
csv_write = csv.writer(out,dialect="excel")#写入的目标和格式
#写入具体内容
csv_write.writerow(stu)
csv_write.writerow(stu1)
print("写入完成")#写的时候需要源文件关闭状态
