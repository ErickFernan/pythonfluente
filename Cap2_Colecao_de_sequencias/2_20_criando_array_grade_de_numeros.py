from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(type(floats))

"""
tipo 'd' é para double precision

A dupla precisão, também conhecida como double-precision em inglês, é um formato de representação numérica utilizado em computação e matemática. 
No contexto de números de ponto flutuante, a dupla precisão é um formato que oferece uma alta precisão numérica em comparação com formatos de 
precisão simples (float).

Em computação, a dupla precisão é geralmente representada em 64 bits, onde os números são armazenados com uma parte para o sinal, uma parte para o expoente 
e uma parte para a mantissa (ou fração). Essa representação permite uma gama muito maior de valores possíveis e uma precisão muito maior do que a precisão simples,
que é representada em 32 bits.
"""

print(floats[-1])
# 0.36172935192322997

fp = open('floats.bin', 'wb')  # Escrita binária ('wb').
print(type(fp))
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')  # Leitura binária ('rb').
print(type(fp))
floats2.fromfile(fp, 10**7)
fp.close()

print(floats2[-1])
# 0.36172935192322997

print(floats2 == floats)
# True

print(floats[0:100])


"""
Aproveitando o tópico anterior para cria-los de forma odernada com bisect insort:
"""
import bisect

floats = array('d')
for _ in range(10**4):
    bisect.insort(floats, random())

# floats = array('d', (bisect.insort(floats, random()) for _ in range(10**4))) 
"Veja observação ao final do código"

fp = open('floats.bin', 'wb')  # Escrita binária ('wb').

floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')  # Leitura binária ('rb').

floats2.fromfile(fp, 10**4)
fp.close()

print(floats[0:100])

"""
por que esse funciona:
floats = array('d', (random() for i in range(10**7)))
e esse não?
floats = array('d', (bisect.insort(floats, random()) for _ in range(10**4)))

O primeiro código funciona porque você está criando um array diretamente com os resultados da expressão gerada por uma generator expression. 
A generator expression gera valores randomicos de forma independente e cria o array diretamente com esses valores.

O segundo código não funciona como esperado porque você está tentando usar bisect.insort em uma generator expression dentro do mesmo contexto em que está tentando
criar o array. A função bisect.insort não retorna um valor, ela insere elementos em um array existente e, como resultado, não pode ser usada diretamente em uma 
generator expression para criar um array. A generator expression não lida com a inserção ordenada de elementos em um array, pois seu foco é gerar valores, 
não modificar um array existente.

A inserção ordenada usando bisect.insort deve ser realizada em um loop separado ou usando outras estruturas de controle antes de criar o array. 
O código precisa de um loop para inserir elementos ordenadamente e, depois disso, você pode criar o array a partir dos valores inseridos.

No primeiro código, não há a necessidade de inserção ordenada, pois você está criando o array diretamente a partir dos valores gerados independentemente pela 
generator expression. Portanto, esses dois trechos de código têm propósitos diferentes e a forma como o bisect.insort é usado faz com que o segundo código não 
funcione como desejado.
"""
