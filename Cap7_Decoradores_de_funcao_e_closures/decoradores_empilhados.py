"""
Quando dois decoradores @d1 e @d2 são aplicados a uma função f nessa orderm, o resultado será o mesmo que f = d1(d2(f)).

ou seja:

@d1
@d2
def f():
    print('f')

é o mesmo que:

def f():
    print('f')

f = d1(d2(fj))
"""

# exemplo
"""
Em Python, os decoradores são funções que recebem outra função como argumento e retornam uma nova função modificada. O empilhamento de decoradores ocorre 
quando várias funções decoradoras são aplicadas a uma única função.

Quando você empilha decoradores em Python, a ordem em que os decoradores são aplicados importa. Eles são aplicados de baixo para cima. 
Isso significa que o decorador mais interno (o mais próximo da função original) é aplicado primeiro, seguido pelo próximo mais interno e assim por diante.

Aqui está um exemplo simples de empilhamento de decoradores em Python:
"""

def decorador1(funcao):
    def wrapper():
        print("Executando decorador 1")
        funcao()
    return wrapper

def decorador2(funcao):
    def wrapper():
        print("Executando decorador 2")
        funcao()
    return wrapper

@decorador1
@decorador2
def funcao_original():
    print("Executando função original")

funcao_original()

"""
Quando você chama `funcao_original()`, ela passa pela função decorada por `decorador2`, que por sua vez passa pela função decorada por `decorador1`, 
resultando na saída:

```
Executando decorador 1
Executando decorador 2
Executando função original
```
"""

# Detalhando o funcionamento
"""
Quando você chama funcao_original(), a primeira coisa que acontece é que a função funcao_original passa pelo decorador mais próximo, decorador2. 
Isso ocorre porque o decorador2 está mais próximo da função original no código fonte.

Dentro de decorador2, o wrapper é definido. Este é um novo envoltório que inclui a lógica adicional definida no decorador2 e, em seguida, 
chama a função original.

No wrapper de decorador2, primeiro é impressa a mensagem "Executando decorador 2", e em seguida a função original (funcao_original) é chamada.

Agora, a execução passa para dentro do wrapper de decorador1, porque decorador1 é o próximo na cadeia de empilhamento de decoradores. 
Aqui, novamente, um novo envoltório é definido (o wrapper de decorador1), com sua própria lógica adicional.

Dentro do wrapper de decorador1, é impressa a mensagem "Executando decorador 1", seguida pela chamada para a função original (funcao_original).

Por fim, dentro da função original, é impressa a mensagem "Executando função original".

Então, o fluxo de execução segue a ordem em que os decoradores foram aplicados: primeiro decorador2, depois decorador1, e finalmente a função original. 
Isso demonstra como os decoradores empilhados alteram o comportamento da função original conforme a execução passa por cada um deles.
""" 