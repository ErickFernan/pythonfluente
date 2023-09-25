lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # atribuição paralela
print(latitude)
# 33.9425
print(longitude)
# -118.408056
################################################################################
a = 5
b = 6
print(f'a={a}, b={b}')
# a=5, b=6
b, a = a, b # swap entre duas variáveis sem uma variável temporaria
print(f'a={a}, b={b}')
# a=6, b=5
################################################################################
print(divmod(20, 8)) # divisão inteira retornando quociente e resto
# (2, 4)
t = (20, 8)
print(divmod(*t))
# (2, 4)
quotient, remainder = divmod(*t)
print((quotient, remainder))
# (2, 4)
################################################################################
import os
_, filename = os.path.split('/home/erick/.ssh/idrsa.pub') # os.path.split() cria uma tupla (path, last_part) e o _ ignora o primeiro valor
print(filename)
# idrsa.pub

"""
Extra:
"Se você escreve softwartes internacionalizados, o simbolo _ não é uma boa variá
vel descartável, pois ele é tradicionalmente usado como um apelido para a função
gettext.gettext.
"""