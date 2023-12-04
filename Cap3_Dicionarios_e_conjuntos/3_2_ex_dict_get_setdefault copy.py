"""
script não otimizado feito para mostrar um caso em que o 'dict.get' não é a maneira mais adequada  de tratar uma chave ausente
"""

import sys
import re

WORD_RE = re.compile('\w+') # A expressão regular \w+ é usada para encontrar palavras no texto. Essa expressão regular procura por uma ou mais ocorrências de caracteres alfanuméricos.

index = {} # O dicionário index é usado para armazenar as palavras como chaves e as posições (linha e coluna) como valores associados a essas palavras.
with open(sys.argv[1], encoding='utf-8') as fp: # O script lê um arquivo de texto fornecido como argumento de linha de comando (sys.argv[1]). O arquivo é lido linha por linha.
   
    """
    sys.argv[1] se refere ao segundo elemento na lista sys.argv, que contém os argumentos da linha de comando. No contexto deste script, sys.argv[0] seria o nome do 
    próprio script (por convenção) e sys.argv[1] seria o primeiro argumento fornecido na linha de comando, que é esperado ser o caminho do arquivo de texto que o script 
    irá processar.
    """
    
    for line_no, line in enumerate(fp, 1): # O script itera sobre as linhas do arquivo usando a função enumerate para obter tanto o número da linha quanto o conteúdo da linha.
        for match in WORD_RE.finditer(line): # Para cada linha, o script procura por palavras usando a expressão regular. O método finditer é utilizado para obter todos os matches na linha.
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # isto não é elegante; foi codificado desta forma para ilustrat uma questão
            occurrences = index.get(word, []) # Obtem a lista de ocorrências para word,ou [] se essa palavra não for encontrada
            occurrences.append(location) # Concatena a nova posição a occurrences
            index[word] = occurrences # Coloca occurrences alterado no dicionário index; isso implica uma segunda busca em index.

# exibe em ordem alfabética
for word in sorted(index, key=str.upper): # No argumento key = sorted, não é chamado str.upper, é apenas uma referencia para que sorted possa utiliza-lo na ordenação
    print(word, index[word])
    

"""
Este código precisa processar algum texto, por exemplo: 

python3 Cap3_Dicionarios_e_conjuntos/3_2_ex_dict_get_setdefault.py zen.txt 

Saída:

a [(19, 48), (20, 53)]
Although [(11, 1), (16, 1), (18, 1)]
ambiguity [(14, 16)]
and [(15, 23)]
are [(21, 12)]
aren [(10, 15)]
at [(16, 38)]
bad [(19, 50)]
be [(15, 14), (16, 27), (20, 50)]
beats [(11, 23)]
Beautiful [(3, 1)]
better [(3, 14), (4, 13), (5, 11), (6, 12), (7, 9), (8, 11), (17, 8), (18, 25)]
break [(10, 40)]
by [(1, 20)]
cases [(10, 9)]
complex [(5, 23)]
Complex [(6, 1)]
complicated [(6, 24)]
counts [(9, 13)]
dense [(8, 23)]
do [(15, 64), (21, 48)]
Dutch [(16, 61)]
easy [(20, 26)]
enough [(10, 30)]
Errors [(12, 1)]
explain [(19, 34), (20, 34)]
Explicit [(4, 1)]
explicitly [(13, 8)]
face [(14, 8)]
first [(16, 41)]
Flat [(7, 1)]
good [(20, 55)]
great [(21, 28)]
guess [(14, 52)]
hard [(19, 26)]
honking [(21, 20)]
idea [(19, 54), (20, 60), (21, 34)]
If [(19, 1), (20, 1)]
implementation [(19, 8), (20, 8)]
implicit [(4, 25)]
In [(14, 1)]
is [(3, 11), (4, 10), (5, 8), (6, 9), (7, 6), (8, 8), (17, 5), (18, 16), (19, 23), (20, 23)]
it [(15, 67), (19, 43), (20, 43)]
let [(21, 42)]
may [(16, 19), (20, 46)]
more [(21, 51)]
Namespaces [(21, 1)]
nested [(7, 21)]
never [(12, 15), (17, 20), (18, 10)]
not [(16, 23)]
Now [(17, 1)]
now [(18, 45)]
obvious [(15, 49), (16, 30)]
of [(1, 9), (14, 13), (21, 56)]
often [(18, 19)]
one [(15, 17), (15, 43), (21, 16)]
only [(15, 38)]
pass [(12, 21)]
Peters [(1, 27)]
practicality [(11, 10)]
preferably [(15, 27)]
purity [(11, 29)]
Python [(1, 12)]
re [(16, 58)]
Readability [(9, 1)]
refuse [(14, 27)]
right [(18, 38)]
rules [(10, 50)]
s [(19, 46), (21, 46)]
should [(12, 8), (15, 7)]
silenced [(13, 19)]
silently [(12, 26)]
Simple [(5, 1)]
Sparse [(8, 1)]
Special [(10, 1)]
special [(10, 22)]
t [(10, 20)]
temptation [(14, 38)]
than [(3, 21), (4, 20), (5, 18), (6, 19), (7, 16), (8, 18), (17, 15), (18, 32)]
that [(16, 10)]
The [(1, 1)]
the [(10, 46), (14, 4), (14, 34), (19, 4), (20, 4)]
There [(15, 1)]
those [(21, 59)]
Tim [(1, 23)]
to [(10, 37), (14, 49), (15, 61), (19, 31), (20, 31)]
ugly [(3, 26)]
Unless [(13, 1)]
unless [(16, 47)]
way [(15, 57), (16, 15)]
you [(16, 54)]
Zen [(1, 5)]

"""
