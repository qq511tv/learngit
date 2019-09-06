#数组
student =['Jack','Lock','Harry','Micle']
print(student)
print(student[0])
print(student[2])
print(student[-1])#访问最后一个元素
print(student[1:])#把索引下标为1之后的元素显示出来 查

student.append("51zxw")#添加素组 java的数组添加不了 一开始就定义了长度，但是ArryList可以 增
print(student)
student.insert(0,"hello")#指定位置插入 insert
print(student)
student[0] = "No.1"#修改指定元素的值 改
print(student)
student.pop(0)#删除指定元素，如不指定下标则删除末位 删
print(student)
student.clear()
print(student)
del student

