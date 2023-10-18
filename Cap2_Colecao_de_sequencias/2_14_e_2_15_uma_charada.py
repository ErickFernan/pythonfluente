t =  (1, 2, [30, 40])
t[2] += [50, 60]

"""
No console:
>>> t = (1,2,[30,40])
>>> t[2] += [50,60]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [30, 40, 50, 60])
"""

# Pode-se fazer a operação sem erros usando:
print(t[2].extend([50,60]))
"""
No console:
>>> t =  (1, 2, [30, 40])
>>> t[2].extend([50,60])
>>> t
(1, 2, [30, 40, 50, 60])
"""
