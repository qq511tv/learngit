#往txt文件里写东西
writetxt = open('Student.txt','a')
writetxt.write('Sparrow,27,HangZhou'+'\n')
writetxt.close()
#读取Student.txt文件内容
readtxt = open('Student.txt')
str = readtxt.readlines()
print(str)
for i in str:
    print(i.split(",")[0])

#往csv文件里写东西
writecsv = open('Student.csv','a')
writecsv.write('Sparrow,27,HangZhou'+'\n')
writecsv.close()
#读取csv文件
readcsv = open('Student.csv')
strcsv = readcsv.readlines()
print(strcsv)
for i in strcsv:
    print(i.split(',')[0])
