from time import ctime,sleep
#单线程
def talk():
    print("Start talk: %r" %ctime())
    sleep(2)

def write():
    print("Start write %r " %ctime())
    sleep(3)

if __name__=='__main__':#如果是自己调试时会运行
    talk()
    write()
    print("ALL end! %r"%ctime())
