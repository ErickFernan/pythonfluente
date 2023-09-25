symbols = '$¢£¥€¤'
beyound_ascii = [ord(s) for s in symbols if ord(s) > 127] # ord mostra o unicode do carcter
print(beyound_ascii)

beyound_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyound_ascii)