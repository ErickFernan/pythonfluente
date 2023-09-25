board = [['_'] * 3 for _ in range(3)]
print(board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

"""
board[0][0] = ['doideira', 123123, 'abc']
print(board)
# [[['doideira', 123123, 'abc'], '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

Observe que diferentemente da multiplicação, a list comprehension gera valores
com refenrencias distintas, diferente do que acontece ao usar apenas o *
"""

board[1][2] = 'X'
print(board)

################################################################################

weird_board = [['_'] * 3] * 3
print(weird_board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

weird_board[1][2] = '0'
print(weird_board)
# [['_', '_', '0'], ['_', '_', '0'], ['_', '_', '0']]

"""
Observe, novamente, o problema com referenciamento que o * porde gerar ao criar
lista de listas, isto fica mais evidente no exemplo abaixo:
O exemplo acima se comporta como o código abaixo
"""

row = ['_'] * 3 # Concatena o mesmo row 3 vezes
board = []
for _ in range(3):
    board.append(row)
print(board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

board[2][0] = 'X'
print(board)
# [['X', '_', '_'], ['X', '_', '_'], ['X', '_', '_']]

"""
Em contrapartida, o exemplo abaixo, se comporta como a list comprehension:
"""

board = []
for _ in range(3):
    row = ['_'] * 3 # cada iteração cria um novo row
    board.append(row) # depois o concatena ao board
print(board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

board[2][0] = 'X'
print(board)
# [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]
