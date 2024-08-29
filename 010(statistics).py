import statistics

Lista = [1,2,3,4,5,5,6,7,8,9,10]

média = statistics.mean(Lista)
mediana = statistics.median(Lista)
moda = statistics.mode(Lista)

print(f'''
    A média da lista é {média}\b
    A mediana da  lista é {mediana}\b
    A moda da lista é {moda}
''')