from xml.dom import minidom
#读取xml的 文本节点
dom = minidom.parse('Class_info.xml')
root = dom.documentElement

names = root.getElementsByTagName('name')
ages = root.getElementsByTagName('age')
citys = root.getElementsByTagName('city')

for i in range(4):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(citys[i].firstChild.data)
