import pyuca

coll = pyuca.Collator()
fruits = ['caju','atemoia','cajá','açaí','acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)

print(sorted_fruits)
# ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']

print(sorted(fruits))
# ['acerola', 'atemoia', 'açaí', 'caju', 'cajá']

# Observe a diferença na ordenação, isso ocorre por conta dos carecteres não-ASCII
# Sendo que no Brasil os acentos fazem diferença na ordenação apenas em palavras iguais
# por exemplo, avo e avó onde avó deve ser ordenada após avo.
