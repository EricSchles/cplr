from time import time

def fib(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def main():
    start = time()
    fib(3)
    end = time() - start
    print "fib(3) took",end,"seconds"
    start = time()
    fib(15)
    end = time() - start
    print "fib(15) took",end,"seconds"
    start = time()
    fib(50)
    end = time() - start
    print "fib(200) took",end,"seconds"
    
