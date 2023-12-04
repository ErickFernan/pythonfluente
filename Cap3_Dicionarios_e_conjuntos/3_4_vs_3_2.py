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
            
            index.setdefault(word, []).append(location) # Obtém a lista de ocorrências para word ou definie-a com[] se não for encontrada; setdefault devolve o valor, portanto poderá ser atualizado sem exgir uma segunda busca.

# exibe em ordem alfabética
for word in sorted(index, key=str.upper): # No argumento key = sorted, não é chamado str.upper, é apenas uma referencia para que sorted possa utiliza-lo na ordenação
    print(word, index[word])
    
"""
python3 Cap3_Dicionarios_e_conjuntos/3_2_ex_dict_get_setdefault.py zen.txt 
"""