# fatura
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                $ 4.95    2    $ 9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
SKU = slice(0, 6) # SKU é uma sigla que significa Stock Keeping Unit (Unidade de Manutenção de Estoque, em português). Na prática, é um código único de identificação atribuído a um produto, usado para classificar e organizar os itens de um estoque de acordo com suas características, como tamanho, cor, modelo e fabricante.
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 54)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
# print(line_items)
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# >>> tupla[-1:-6:-1] # Na ordem reversa ele não começa do 0 e sim do -1, então, ao invés de 0 -> 5 vira -1 -> -6
# (5, 4, 3, 2, 1)
