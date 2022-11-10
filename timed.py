import time

def timeme(func):
    def dec():
        start = time.time()
        func()
        end = time.time()
        print(f'Total time {end - start}')
    return dec
