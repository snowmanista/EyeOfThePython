import sys
from contextlib import contextmanager

class DefaultOutput:
    def __init__(self, counter):
        self.counter = counter

    def entry(self, separator, func_name, frame):
        print(f'{separator * self.counter}-->{func_name}({str(frame.f_locals)}) line: {frame.f_lineno}')
        self.counter += 1

    def exit(self, separator, func_name, frame, arg):
        self.counter -= 1
        print(separator * self.counter, "<-- ", func_name, "(", str(frame.f_locals), ") res =", arg, "line: ",frame.f_lineno)

    def exception(self, frame, func_name):
        print("Tracing exception on line ", frame.f_lineno, "of ", func_name, "(", str(frame.f_locals), ")")

class ColorOutput:
    def __init__(self, counter):
        self.counter = counter

    def entry(self, separator, func_name, frame):
        print(f'{bcolors.OK}{separator * self.counter}-->{func_name}({str(frame.f_locals)}) line: {frame.f_lineno} {bcolors.RESET}')
        self.counter += 1

    def exit(self, separator, func_name, frame, arg):
        self.counter -= 1
        print(separator * self.counter, bcolors.WARNING + "<-- ", func_name, "(", str(frame.f_locals), ") res =", arg,"line: ", frame.f_lineno, bcolors.RESET)

    def exception(self, frame, func_name):
        print(bcolors.FAIL + "Tracing exception on line ", frame.f_lineno, "of ", func_name, "(", str(frame.f_locals), ")", bcolors.RESET)

class FileOutput:

    def __init__(self, counter):
        self.counter = counter
        self.f = open("fib_output.txt", "w")

    def entry(self, separator, func_name, frame):
        if self.counter==0:
            self.f = open("fib_output.txt", "a")
            self.f.write(f'{separator * self.counter}-->{func_name}({str(frame.f_locals)}) line: {frame.f_lineno}\n')
        else:
            self.f = open("fib_output.txt", "a")
            self.f.write(f'{separator * self.counter}-->{func_name}({str(frame.f_locals)}) line: {frame.f_lineno}\n')
        self.counter += 1


    def exit(self, separator, func_name, frame, arg):
        self.counter -= 1
        self.f = open("fib_output.txt", "a")
        self.f.write(f'{separator * self.counter}<--{func_name}({str(frame.f_locals)}) res = {arg} line: {frame.f_lineno}\n')
        if self.counter==0:
            self.f.close()

    def exception(self, frame, func_name):
        self.f.write(f'Tracing exception on line {frame.f_lineno} of {func_name}({str(frame.f_locals)})\n')

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLO


def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    separator = '\t'

    if event == 'call':
        OUTPUT.entry(separator, func_name, frame)
        return trace_calls_and_returns

    elif event == 'return':
        OUTPUT.exit(separator, func_name, frame, arg)

    elif event == 'exception':
        OUTPUT.exception(frame, func_name)

    return



@contextmanager
def start_tracing():
    get_trace = sys.gettrace()
    print("This is the name of the script: ", sys.argv[0])
    print("Number of arguments: ", len(sys.argv))
    print("The arguments are: ", str(sys.argv))
    sys.settrace(trace_calls_and_returns)
    yield
    sys.settrace(get_trace)

OUTPUT = ColorOutput(0)
