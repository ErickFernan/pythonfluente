"""
>>> import array
>>> numbers = array.array('h', [-2,-1,0,1,2]) # o typecode 'h' cria um array de short integers (16bits).
>>> octets = bytes(numbers)
>>> octets
b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'
"""