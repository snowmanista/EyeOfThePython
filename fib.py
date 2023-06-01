import Pytrace_EyeOfThePython

# Pytrace_EyeOfThePython.OUTPUT = Pytrace_EyeOfThePython.ColorOutput(0)
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

with Pytrace_EyeOfThePython.start_tracing():
    fib(3)
    #f1()

with Pytrace_EyeOfThePython.start_tracing():
    try:
        foo()
    except:
        pass

