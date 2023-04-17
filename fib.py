
from Pytrace import start_tracing

def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))


def f1():
    f2()
    f3()
    f2()

def f2():
    f3()

def f3():
    pass


def foo():
    raise Exception('generating exception')

with start_tracing():
    fib(4)
    #f1()

with start_tracing():
    try:
        foo()
    except:
        pass