from xml.dom import minidom
dom = minidom.parse('Student_info.xml')
elements = dom.documentElement

print(elements.nodeName)
print(elements.nodeType)
print(elements.nodeValue)

names = elements.getElementsByTagName('name')
ages = elements.getElementsByTagName('age')
sexs = elements.getElementsByTagName('sex')

for i in range(3):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(sexs[i].firstChild.data)