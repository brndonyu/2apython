import time
def timestamp(func):
    def dec():
        str = time.ctime()
        print(str)
        func()
    return dec