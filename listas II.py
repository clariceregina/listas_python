livros_lidos = []
while True:
    print('Insira o nome do ' + str(len(livros_lidos) + 1) + '° livro lido: ')
    nome = input()
    if nome == '':
        break
    livros_lidos = livros_lidos + [nome] # concatenando listas
print('Os livros lidos foram: ')
for i in livros_lidos:
    print('  ' + i)