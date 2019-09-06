#字典类型
student ={1:'小明',5:'小张',3:'小李',4:'小贾'}
print(student[5])#数组可以索引下标-1 字典类型不行 字典索引的是Key
print(student)
student[6] = '我要自学网'#增 改（直接改）
print(student)
del student[1] #删除del  del student彻底删除字典
print(student)
student.clear()#清空字典里的所有数据
print(student)