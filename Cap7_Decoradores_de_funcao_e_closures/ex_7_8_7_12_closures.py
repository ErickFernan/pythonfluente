# 7.8 - implementação baseada em classe

class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

"""
>>> from Cap7_Decoradores_de_funcao_e_closures.ex_7_8_7_12_closures import Averager
>>> avg = Averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> 
"""

# 7.9 - implementação funcional

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value) #  series é considerado uma variável livre (free variable)
        total = sum(series)
        return total/len(series)

    return averager

"""
>>> from Cap7_Decoradores_de_funcao_e_closures.ex_7_8_7_12_closures import make_averager
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__
(<cell at 0x7fec3ca5b2b0: list object at 0x7fec3c9c3240>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> 
"""

# Obs.: Note que a única situação em que uma funbção pode precisar lidar com variáveis externas que não sejam globais é quando ela está aninhada em outra função