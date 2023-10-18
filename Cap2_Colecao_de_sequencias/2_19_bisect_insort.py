import bisect # binary search
import random


SIZE = 7

random.seed(1729) 
"""Define uma semente (seed) para o gerador de números aleatórios. 
Isso garante que a sequência de números aleatórios gerada seja a mesma sempre que o código for executado com a mesma semente."""

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
