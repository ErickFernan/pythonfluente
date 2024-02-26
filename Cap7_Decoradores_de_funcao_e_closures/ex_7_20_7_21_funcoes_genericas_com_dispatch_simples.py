# função inicial:

# import html
# def htmlize(obj):
#     content = html.escape(repr(obj))
#     return '<pre>{</pre}'.format(content)

# OBS:
"""
Em HTML, <pre> é uma tag usada para definir texto pré-formatado. Quando você envolve um texto com a tag <pre>, o navegador renderiza esse texto mantendo espaçamentos e quebras de linha exatamente como são definidos no código HTML.

Isso é útil quando você quer exibir blocos de texto onde a formatação é importante, como código-fonte, texto formatado em colunas ou qualquer conteúdo que precise manter sua estrutura visual original.

Por exemplo:

html
Copy code
<pre>
Texto
    com
        espaçamento
            pré-definido
                e quebras de linha
</pre>
Nesse caso, o texto seria exibido com todos os espaços e quebras de linha preservados, conforme definido no código HTML.
"""

# Modificando
"""
Agora vamos estender o código para que gere visualizações personalizadas para alguns tipos:

* str: substitui caracteres de quebra de linha por '<br>/n' e usa tags <p> em vez de <pre>

* int: mostra o número em decimal e em hexadecimal

*list: gera uma lista HTML, formatando cada item de aclordo com seu tipo.
"""

# 7.21

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'

"""
Neste contexto, _ está sendo usado como o nome de uma função específica para lidar com strings quando elas são passadas para htmlize. 
Este uso do _ é uma convenção que indica que esta função não é esperada ser usada fora do contexto do registro de htmlize. 
Isso é uma escolha de design do autor do código, que optou por usar _ como um nome curto e simples para esta função específica.
"""

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('n', '<br>\n')
    return f'<p>{content}</p>'

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)
    # return f'<pre>{n} (0x{n:x})</pre>'

"""
{0}: Este é um marcador de posição que indica onde o primeiro argumento passado para o método format() será inserido. 
O número dentro das chaves é a posição do argumento passado para o método format(). Aqui, n será inserido no lugar de {0}.

(0x{0:x}): Esta parte também usa formatação com .format(). O 0x é uma string literal, indicando que o número será formatado como hexadecimal. 
{0:x} é outro marcador de posição, indicando que o primeiro argumento passado para o método format() será formatado como um número hexadecimal.
"""

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


#Teste:

"""
>>> from Cap7_Decoradores_de_funcao_e_closures.ex_7_20_7_21_funcoes_genericas_com_dispatch_simples import *
>>> htmlize({1,2,3})
'<pre>{1, 2, 3}</pre>'
>>> htmlize(abs)
'<pre>&lt;built-in function abs&gt;</pre>'
>>> htmlize('Heimlich & Co.\n- a game')
'<p>Heimlich &amp; Co.\n- a game</p>'
>>> htmlize(42)
'<pre>42 (0x2a)</pre>'
>>> print(htmlize(['alpha', 66, {3,2,1}]))
<ul>
<li><p>alpha</p></li>
<li><pre>66 (0x42)</pre></li>
<li><pre>{1, 2, 3}</pre></li>
</ul>
>>> 
"""