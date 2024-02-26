registry = []

def register(func):
    print('runing register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('runing f1()')

@register
def f2():
    print('runing f2()')

def f3():
    print('runing f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()

"""
runing register(<function f1 at 0x7f19fee86200>)
runing register(<function f2 at 0x7f19fee86170>)
running main()
registry -> [<function f1 at 0x7f19fee86200>, <function f2 at 0x7f19fee86170>]
runing f1()
runing f2()
runing f3()
"""

# Se o nosso programa for importado em vez de  ser executado como script:

"""
>>> from Cap7_Decoradores_de_funcao_e_closures import ex_7_2_quando_python_executa_os_decoradores
runing register(<function f1 at 0x7f9bc38e5a20>)
runing register(<function f2 at 0x7f9bc38e5ab0>)
"""

# Pode-se tirar que os decoradores de função são executados assim que o módeulo é importado, porém
# as funções decoradas executam somente quando são explicitamente chamadas.
'tempo de importação (import time) X tempo de execução (runtime)'
