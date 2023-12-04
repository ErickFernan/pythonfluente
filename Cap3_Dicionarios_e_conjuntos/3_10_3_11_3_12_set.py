# Um conjunto é uma coleção de objetos únicos. Um caso de uso básico é remover duplicações:

l = ['spam', 'spam', 'eggs', 'spam']
print(set(l))
# {'eggs', 'spam'}

print(list(set(l)))
# ['eggs', 'spam']

"3.10"

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

found = len(set(NEEDLES) & set(HAYSTACK))
print(found)
# 6

"3.11"

found = 0
for n in NEEDLES:
    if n in HAYSTACK:
        found += 1

print(found)
# 6

"3.11"

found = len(set(NEEDLES) & set(HAYSTACK))
print(found)
# 6
found = len(set(NEEDLES).intersection(HAYSTACK))
print(found)
# 6
