symbols = '$¢£¥€¤'
tp = tuple(ord(symbol) for symbol in symbols) # ord mostra o unicode do carcter
print(tp)

import array
tp = array.array('I', (ord(symbol) for symbol in symbols)) # o I maiusculo é inteiro e imutável
print(tp)
