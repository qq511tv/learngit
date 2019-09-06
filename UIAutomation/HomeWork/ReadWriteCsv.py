import csv

#写入
stu001 = ['xiaoming','29','Student001']
stu002 = ['xiaojia','30','Student002']
stu003 = ['xiaofang','26','Student003']
writefile = open('Student.csv','a',newline='')
str2 = csv.writer(writefile,dialect='excel')
str2.writerow(stu001)
writefile.close()

# 读取
openfile = open('Student.csv','r')
str = openfile.readlines()
for a in str:
    print(a.split(','))
print('===========================================================')


