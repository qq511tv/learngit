#多线程
from time import ctime,sleep
import threading
def talk(content,num):
    for i in range(num):
        print('正在说话，内容和时间是 %s %s'%(content,ctime()))
        sleep(2)

def write(content,num):
    for i in range(num):
        print('正在写，内容和时间是 %s %s'%(content,ctime()))
        sleep(3)

threads = []
t1 = threading.Thread(target = talk,args=('你好',2))
threads.append(t1)
t2 = threading.Thread(target = write,args=('好好学习，天天向上',3))
threads.append(t2)

if __name__ == '__main__':
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print('The end!')

