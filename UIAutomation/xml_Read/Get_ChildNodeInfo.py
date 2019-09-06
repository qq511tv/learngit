#获取子标签
from xml.dom import minidom
dom = minidom.parse('Class_info.xml')
elements = dom.documentElement

tags = elements.getElementsByTagName('student')

print(tags[0].nodeName)
print(tags[0].nodeType)
print(tags[0].nodeValue)
#3-28完