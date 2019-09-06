#获取Childnode标签
#获取node的属性内的文本
from xml.dom import minidom
dom = minidom.parse('Student_info.xml')
elements = dom.documentElement
print(elements.nodeName,elements.nodeValue,elements.nodeType)

names = elements.getElementsByTagName('name')
logins = elements.getElementsByTagName('login')

for i in range(2):
    print(names[i].firstChild.data)
    print("登录账户为："+logins[i].getAttribute('username')+"登录密码为："+ logins[i].getAttribute('pwd'))


