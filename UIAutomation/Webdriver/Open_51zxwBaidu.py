#火狐浏览器驱动 需要把驱动放在python的安装目录
#谷歌浏览器驱动 需要把驱动放在python的安装目录
from selenium import webdriver
from time import sleep

#driver = webdriver.Firefox()#火狐 加载驱动
#driver = webdriver.Ie()#ie  ie驱动有很多坑 ie的兼容性问题
driver = webdriver.Chrome()#谷歌

driver.get("http://www.51zxw.net")
print(driver.title)
sleep(3)

driver.get("http://www.baidu.com")
print(driver.title)
sleep(2)

# driver.quit()