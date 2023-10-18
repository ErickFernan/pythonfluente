fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
# ['apple', 'banana', 'grape', 'raspberry']
print(fruits)
# ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits, reverse=True))
# ['raspberry', 'grape', 'banana', 'apple']
print(sorted(fruits, key=len))
# ['grape', 'apple', 'banana', 'raspberry'] # Por ter o mesmo tamanho grape e apple permanecem na posição original
print(sorted(fruits, key=len, reverse=True))
# ['raspberry', 'banana', 'grape', 'apple'] # Como a ordenação é estavel grape aparece antes de apple
print(fruits)
# ['grape', 'raspberry', 'apple', 'banana']
fruits.sort()
print(fruits)
# ['apple', 'banana', 'grape', 'raspberry']
