colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]  # lista de tuplas organizadas por cor e depois por tamanho.
print(tshirts)

# Que é a mesma coisa que fazer:
for color in colors: # Lógica parecida com a anterior mas fora da lista, apenas print de tuplas
    for size in sizes:
        print((color, size))

# Que é também:
tshirts = [(color, size) for size in sizes for color in colors] # lista de tuplas organizadas por tamanho e depois por cor.
print(tshirts)
