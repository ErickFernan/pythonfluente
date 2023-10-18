l = [1, 2, 3]
print(id(l))  

# 140643669385792 --> ID da lista inicial

l *= 2
print(l)
# [1, 2, 3, 1, 2, 3]
print(id(l))
# 140643669385792 --> Mesmo objeto com novos itens acrescentados
# Obs: Listas imlementam __iadd__
"""
l = list()
>>> dir(l)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
 '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
 '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

t= (1, 2, 3)
print(id(t))
# 140643669461888 --> ID da tupla inicial

t *= 2
print(t)
# (1, 2, 3, 1, 2, 3)
print(id(t))
# 140643679823392 --> Foi criada uma nova tupla
# Obs: Tuplas não implementam __iadd__ é utilizado o __add__ e assim outro objeto é criado
"""
t = tuple()
>>> dir(t)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
 '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
 'count', 'index']
"""

"""
OBS.:
    No primeiro caso o *= comporta-se como um extend então no mesmo objeto.
    No seundo caso um a = a + b, onde há uma validação de a + b e o rtesultado é add em a que é um novo objeto.
"""
