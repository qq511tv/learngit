from xml.dom import minidom

#打开xml文件 打印元素节点
dom = minidom.parse('Class_info.xml')
root = dom.documentElement#获取文档对象的所有标签元素

print(root.nodeName)#根标签名称
print(root.nodeValue)#根标签中的值
print(root.nodeType)#根标签类型 节点是元素节点返回1 是属性节点返回2
