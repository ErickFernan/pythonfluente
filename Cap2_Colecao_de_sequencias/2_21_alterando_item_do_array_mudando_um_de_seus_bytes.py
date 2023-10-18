import array

numbers = array.array('h', [-2, -1, 0, 1, 2])  # Um array de números inteiros curtos ('h' representa "short") 

memv = memoryview(numbers)
"""
A função de um memoryview em Python é fornecer uma visualização (ou "janela") eficiente dos dados em uma sequência de bytes (como um objeto bytes, bytearray 
ou array.array). Essa visualização não cria uma cópia dos dados subjacentes, mas, em vez disso, permite que você acesse e manipule os dados diretamente. 
"""

print(len(memv))
# 5

print(memv[0])
# -2

memv_oct = memv.cast('B')
"""
Aqui, a visão de memória memv é convertida em uma visão de memória de bytes ('B' representa "byte"). 
Isso permite acessar os elementos do array como bytes individuais.
"""

print(memv_oct.tolist())
"imprime a visão de memória de bytes como uma lista de valores inteiros representando os bytes subjacentes dos valores do array numbers."
# [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]

memv_oct[5] = 3
print(numbers)
# array('h', [-2, -1, 1024, 1, 2])

print(memv_oct.tolist())
# [254, 255, 255, 255, 0, 4, 1, 0, 2, 0]
