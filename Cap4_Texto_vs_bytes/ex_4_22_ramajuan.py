import re

re_numbers_str = re.compile(r'\d+')     # <1>
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')  # <2>
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"  # <3>
            " as 1729 = 1³ + 12³ = 9³ + 10³.")        # <4>

text_bytes = text_str.encode('utf_8')  # <5>

print(f'Text\n  {text_str!r}')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))      # <6>
print('  bytes:', re_numbers_bytes.findall(text_bytes))  # <7>
print('Words')
print('  str  :', re_words_str.findall(text_str))        # <8>
print('  bytes:', re_words_bytes.findall(text_bytes))    # <9>

"""
Text
  'Ramanujan saw ௧௭௨௯ as 1729 = 1³ + 12³ = 9³ + 10³.'
Numbers
  str  : ['௧௭௨௯', '1729', '1', '12', '9', '10']
  bytes: [b'1729', b'1', b'12', b'9', b'10']
Words
  str  : ['Ramanujan', 'saw', '௧௭௨௯', 'as', '1729', '1³', '12³', '9³', '10³']
  bytes: [b'Ramanujan', b'saw', b'as', b'1729', b'1', b'12', b'9', b'10']
"""
