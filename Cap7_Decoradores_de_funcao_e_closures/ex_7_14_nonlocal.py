# implementação falha:

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager

"""
>>> from Cap7_Decoradores_de_funcao_e_closures.ex_7_14_nonlocal import make_averager
>>> avg = make_averager()
>>> avg(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/erick/pythonfluente/Cap7_Decoradores_de_funcao_e_closures/ex_7_14_nonlocal.py", line 8, in averager
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
>>> 
"""

# O problema ocorre pois count += 1 é o mesmo que count = count + 1, ou seja estamos fazendo uma atribuição a count no corpo de averager
# portanto uma variável local, assim ela deixa de ser uma variável livre e passa a ser local.
#  Para resolver:

def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager

"""
>>> from Cap7_Decoradores_de_funcao_e_closures.ex_7_14_nonlocal import make_averager2
>>> avg = make_averager2()
>>> avg(10)
10.0
>>> avg(12)
11.0
>>> avg(11)
11.0
>>> avg(13)
11.5
>>> 
"""
