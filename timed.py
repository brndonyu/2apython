import time

def timeme(func):
    def dec():
        x = time.time()
        func()
        y = time.time()
        print('Total time X: ')
        print(y - x)
    return dec