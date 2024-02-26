@decorate
def target():
    print('running target()')

"tem o mesmo efeito que:"

def target():
    print('running target()')

target = decorate(target)

"não retorna o targe original mas sim ao devolvido por decorate(target)"

"""
>>> def deco(func):
...     def inner():
...             print('running inner()')
...     return inner
... 
>>> @deco
... def target():
...     print('running target()')
... 
>>> target()
running inner()
>>> target
<function deco.<locals>.inner at 0x7f4af4fdd510>
"""

# Outro Exemplo

"""
>>> def meu_decorador(funcao):
...     def funcao_decorada():
...         print("Antes de chamar a função original")
...         funcao()  # Chama a função original
...         print("Depois de chamar a função original")
...     return funcao_decorada
... 
>>> @meu_decorador
... def minha_funcao():
...     print("Esta é a função original")
... 
>>> minha_funcao()
Antes de chamar a função original
Esta é a função original
Depois de chamar a função original
>>> 
"""