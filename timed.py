import time

def timeme(func):
    def dec():
        start = time.time()
        func()
        end = time.time()
        print(f'Total time X {end - start}')
    return dec