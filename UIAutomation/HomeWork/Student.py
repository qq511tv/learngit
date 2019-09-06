class Student():
    def __init__(self,name,city):
        self.name = name
        self.city = city
        print("学生名称是"+name+" 所在城市为"+city)

    def talk(self):
        print("你好")
    def test(self,ddyy):
        sum = int(ddyy)+int(10)
        print("所求和为："+str(sum))

