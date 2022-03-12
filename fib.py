
from Pytrace import start_tracing

def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

def foo():
    raise Exception('generating exception')

with start_tracing():
    print("tu som")
    fib(4)
    print("tu som")
print("tu som")
with start_tracing():
    try:
        foo()
    except:
        pass