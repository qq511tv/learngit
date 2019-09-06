#正则表达式
import re  #正则表达式所在的包

str = 'abcdefghijklmn'

a = re.compile('ab')#compile只会从开头匹配，如果不是开头的字符串，那么将不会匹配成功
b = a.match(str)#match 匹配
print('被匹配的对象',b.string)
print('匹配上的字符串位置索引',b.span())
print('需要匹配的字符串',b.group())
print('===========================================================')

a1 = re.search('ab',str)#search可以匹配任意位置的字符串，会   对整个匹配对象进行扫描
print('被匹配的对象',a1.string)
print('匹配上的字符串位置索引',a1.span())
print(re.sub('ab','HELLO',str))#sub方法会对匹配到的内容进行替换（注意：是替换所有匹配到的内容），类似字符串的replace方法

regx = r'http://[\S]*jpg'
pattern = re.compile(regx)
getdata = re.findall(pattern,repr(str))
print('repr() 函数将对象转化为供解释器读取的形式。'+repr(str))
print(getdata)




