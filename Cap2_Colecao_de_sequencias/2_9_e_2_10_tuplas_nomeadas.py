from collections import namedtuple


City = namedtuple('City', 'name country population coordinates')
# City = namedtuple('City', ('name', 'country', 'population', 'coordinates')) # As duas formas são funcionais
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691997))
print(tokyo)
# City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691997))
print(tokyo.population)
# 36.933
print(tokyo.coordinates)
# (35.689722, 139.691997)
print(tokyo[1])
# JP

########################################################################################################################
# print(dir(City))

print(City._fields)
# ('name', 'country', 'population', 'coordinates')

Latlong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, Latlong(28.613889, 77.208889))
delhi = City._make(delhi_data) # City(*delhi_data) faria a mesma coisa
print(delhi._asdict())
# {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': Latlong(lat=28.613889, long=77.208889)}

for key, value in delhi._asdict().items():
    print(key + ':', value)
# name: Delhi NCR
# country: IN
# population: 21.935
# coordinates: (28.613889, 77.208889)