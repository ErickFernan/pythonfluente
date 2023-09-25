l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l[2:5] = [20,30]
print(l)
# [0, 1, 20, 30, 5, 6, 7, 8, 9]

del l[5:7]
print(l)
# [0, 1, 20, 30, 5, 8, 9]

l[3::2] = [11, 22]
print(l)
# [0, 1, 20, 11, 5, 22, 9]

l[2:5] = 100  # Vai dar erro, pois não é iterável
"""
Traceback (most recent call last):
  File "/home/erick/pythonfluente/Cap2_Colecao_de_sequencias/atribuicao_de_valores_a_fatias.py", line 17, in <module>
    l[2:5] = 100  # Vai dar erro, pois não é iterável
TypeError: can only assign an iterable
"""

l[2:5] = [100]
print(l)
# [0, 1, 100, 22, 9]
