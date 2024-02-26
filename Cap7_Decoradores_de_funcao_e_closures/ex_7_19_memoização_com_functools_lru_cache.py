from clockdeco import clock

# 7.18 - A maneira recursiva bastante custosa de calcular o enésimo n da série de fibonacci

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(6))

"""
[0.00000048s] fibonacci(0) -> 0
[0.00000048s] fibonacci(1) -> 1
[0.00007296s] fibonacci(2) -> 1
[0.00000048s] fibonacci(1) -> 1
[0.00000048s] fibonacci(0) -> 0
[0.00000048s] fibonacci(1) -> 1
[0.00002122s] fibonacci(2) -> 1
[0.00004268s] fibonacci(3) -> 2
[0.00013804s] fibonacci(4) -> 3
[0.00000048s] fibonacci(1) -> 1
[0.00000048s] fibonacci(0) -> 0
[0.00000048s] fibonacci(1) -> 1
[0.00002003s] fibonacci(2) -> 1
[0.00004053s] fibonacci(3) -> 2
[0.00000024s] fibonacci(0) -> 0
[0.00000024s] fibonacci(1) -> 1
[0.00002027s] fibonacci(2) -> 1
[0.00000048s] fibonacci(1) -> 1
[0.00000024s] fibonacci(0) -> 0
[0.00000048s] fibonacci(1) -> 1
[0.00002027s] fibonacci(2) -> 1
[0.00004005s] fibonacci(3) -> 2
[0.00008011s] fibonacci(4) -> 3
[0.00014043s] fibonacci(5) -> 5
[0.00030732s] fibonacci(6) -> 8
8
"""

# 7.19 - Implementação mais rápida usando caching
import functools
#  from clockdeco import clock

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(6))

"""
[0.00000095s] fibonacci(0) -> 0
[0.00000119s] fibonacci(1) -> 1
[0.00015283s] fibonacci(2) -> 1
[0.00000167s] fibonacci(3) -> 2
[0.00021696s] fibonacci(4) -> 3
[0.00000119s] fibonacci(5) -> 5
[0.00027633s] fibonacci(6) -> 8
8
"""

"""
O decorador functools.lru_cache() é usado para memoização, que é uma técnica de otimização usada para armazenar em cache os resultados 
de chamadas de função, de modo que, se a mesma entrada for fornecida novamente, o resultado seja recuperado do cache em vez de ser recalculado.

No caso do seu código, a função fibonacci é decorada com @functools.lru_cache(), o que significa que o resultado de cada chamada para fibonacci 
será armazenado em cache. Se a mesma entrada (ou seja, o mesmo valor de n) for fornecida novamente, o resultado correspondente será recuperado do
cache em vez de calcular a sequência novamente.
"""