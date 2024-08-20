#Abrindo e lendo um arquivo com dados
with open("Colors.txt", 'r') as open_file:
    print('Colors.txt content:\n' + open_file.read())

