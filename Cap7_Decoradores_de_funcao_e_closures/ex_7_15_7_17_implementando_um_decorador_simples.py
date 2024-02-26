
# 7.15 - Um decorador simples para apresentar o tempo de execução das funções
import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

# 7.16 - Usando o decorador clock
@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6!=', factorial(6))

"""
**************************************** Calling snooze(.123)
[0.12320137s] snooze(0.123) -> None
**************************************** Calling factorial(6)
[0.00031558s] factorial(1) -> 1
[0.00036013s] factorial(2) -> 2
[0.00038478s] factorial(3) -> 6
[0.00041356s] factorial(4) -> 24
[0.00043463s] factorial(5) -> 120
[0.00047084s] factorial(6) -> 720
6!= 720
"""

# 7.17 - Um decorador clock melhorado
import functools

def clock(func):
    @functools
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arf_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwarg.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, *arg_str, result))
        return result
    return clocked