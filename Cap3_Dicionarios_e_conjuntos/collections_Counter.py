import collections

ct = collections.Counter('abracadabra')
print(ct)
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

ct.update('aaaaazzz')
print(ct)
# Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

print(ct.most_common(2))
# [('a', 10), ('z', 3)]
