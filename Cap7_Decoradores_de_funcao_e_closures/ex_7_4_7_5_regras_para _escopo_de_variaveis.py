# 7.4

"""
>>> def f1(a):
...     print(a)
...     print(b)
... 
>>> f1(3)
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f1
NameError: name 'b' is not defined
>>> b = 6
>>> f1(3)
3
6
>>> 
"""

# 7.5

"""
>>> b = 6
>>> def f2(a):
...     print(a)
...     print(b)
...     b = 9
... 
>>> f2(3)
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f2
UnboundLocalError: local variable 'b' referenced before assignment
"""

# Observe a diferença

"""
>>> b = 6
>>> def f2(a):
...     print(a)
...     print(b)
... 
>>> f2(3)
3
6
>>> 
"""

# como b não foi definida dentro da função ela não é tratada como local, então 6 é printado aop contrario da primeira opção onde b é tratado como local
# Para fazer funcionar declarando b dentro e fora é preciso usar o global

"""
>>> b = 6
>>> def f3(a):
...     global b
...     print(a)
...     print(b)
...     b = 9
... 
>>> f3(3)
3
6
>>> b
9
>>> f3(3)
3
9
>>> b=30
>>> b
30
>>> f3(3)
3
30
>>> 
"""
