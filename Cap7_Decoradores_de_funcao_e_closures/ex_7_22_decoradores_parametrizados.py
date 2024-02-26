# 7.22 - 

# registry = []

# def register(func):
#     print(f'running register({func})')
#     registry.append(func)
#     return func

# @register
# def f1():
#     print('running f1()')

# print('running main()')
# print('registry ->', registry)
# f1()


# 7.23 - conceituamente não é um decorador mas sim uma fábrica de decoradores
registry = set()
def register(active=True):
    def decorate(func):
        print(f'running register(active={active}->decorate({func}))')
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')

@register() 
def f2():
    print('running f2()')

def f3():
    print('running f3()')

