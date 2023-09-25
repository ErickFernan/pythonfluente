"""
>>> mylist
[[1, 2], [1, 2], [1, 2]]
>>> mylist[2][1] = ['anao', 'mamaco', (56665, 6)]
>>> mylist
[[1, ['anao', 'mamaco', (56665, 6)]], [1, ['anao', 'mamaco', (56665, 6)]], [1, ['anao', 'mamaco', (56665, 6)]]]
>>>
"""

# Cuidado, pois neste modo é gerado copias da mesma lista que possuem a mesma referencia, caso você a modifique acessando
# dentro da lista todas serão modificas, diferentemente de modificar sem a acessar, pois você esta dando um outra referencia

"""
>>> mylist = [[1,2]] * 3
>>> mylist
[[1, 2], [1, 2], [1, 2]]
>>> mylist[1] = ['anao']
>>> mylist
[[1, 2], ['anao'], [1, 2]]
>>> mylist[2][1] = ['anao', 'mamaco', (56665, 6)]
>>> mylist
[[1, ['anao', 'mamaco', (56665, 6)]], ['anao'], [1, ['anao', 'mamaco', (56665, 6)]]]
"""