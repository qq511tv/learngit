#打印属性值 getAttribute获取属性标签
from xml.dom import minidom
dom = minidom.parse('Class_info.xml')
elements = dom.documentElement

logins = elements.getElementsByTagName('login')

for i in range(2):
    username = logins[i].getAttribute('username')
    print("账户为："+username)
    pwd = logins[i].getAttribute('password')
    print("密码为："+pwd)