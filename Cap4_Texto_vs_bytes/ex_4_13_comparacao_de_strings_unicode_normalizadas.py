"""
IMPORTANTE: Eu me esqueci que arquivos python não podem começar com número pois torna-se impossível fazer import.

Em Python, os nomes de arquivos (e também identificadores, como nomes de variáveis) não podem começar com números por uma questão de convenção e para evitar 
ambiguidades na interpretação do código.

Ao permitir que os nomes de arquivos começassem com números, poderia haver confusão entre eles e números utilizados em expressões matemáticas ou outras operações. 
Além disso, começar um nome de arquivo com um número poderia levar a ambiguidades na interpretação do código, já que o interpretador Python poderia confundir o nome 
do arquivo com um número literal.

Por exemplo, se você tivesse um arquivo chamado 123file.py, o Python poderia interpretar erroneamente 123 como um número inteiro e tentar realizar operações com ele.

Para manter a clareza e a consistência no código Python, é uma prática recomendada começar os nomes de arquivos (e identificadores em geral) com letras ou underscores 
(_). Essa convenção ajuda a evitar problemas potenciais de interpretação e torna o código mais legível para os programadores.
"""

from unicodedata import normalize

def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())

"""
>>> from Cap4_Texto_vs_bytes.ex_4_13_comparacao_de_strings_unicode_normalizadas import nfc_equal, fold_equal
>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s1 == s2
False
>>> nfc_equal(s1, s2)
True
>>> nfc_equal('A', 'a')
False
>>> s3 = 'Straße'
>>> s4 = 'strasse'
>>> s3 == s4
False
>>> nfc_equal(s3, s4)
False
>>> fold_equal(s3, s4)
True
>>> fold_equal(s1, s2)
True
>>> fold_equal('A', 'a')
True
"""
    