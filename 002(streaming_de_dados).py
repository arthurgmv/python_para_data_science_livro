#Para grande volumes de dados, é possível fazer um streaming em vez de esperar
#todo volume de dados ser baixado.
with open("Colors.txt", 'r') as open_file:
    for observation in open_file:
        print("Reading data: " + observation)

