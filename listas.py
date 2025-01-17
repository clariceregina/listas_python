#1. Criar e acessar elementos fixos da lista:
#Crie uma lista chamada animais contendo os seguintes elementos: "gato", "cachorro", "papagaio", "elefante", "leão".
#Imprima o terceiro elemento da lista usando o índice apropriado.
#Imprima todos os elementos da lista.

animais = ['gato', 'cachorro', 'papagaio', 'elefante', 'leão']
print(animais[2])
print(animais)

#2. Lista dentro de lista
#Crie uma lista chamada matriz contendo duas sublistas:
#Imprima a primeira sublista inteira.
#Imprima o segundo elemento da segunda sublista.

matriz = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f']
]
print(matriz[0])
print(matriz[1][1])

#3. Tamanho da lista e índices negativos:
#Use a lista animais criada anteriormente.
#Imprima o tamanho total da lista animais.
#Acesse o último elemento da lista usando índice negativo.
#Acesse o terceiro elemento da lista a partir do final.

tamanho = len(animais)
print(tamanho)
print(animais[tamanho-1])
print(animais[tamanho-3])

#4. Encontrar a posição de um elemento na lista:
#Use a lista animais e encontre o índice do elemento "papagaio".
print(animais.index('papagaio'))

#5. Remover elementos pelo índice:
#Use a lista animais.
#Remova o elemento "elefante" pelo índice.

elefante = animais.index('elefante')
del animais[elefante]
print(animais)

#6. Adicionar elementos à lista:
#Adicione o elemento "tigre" ao final da lista animais usando append.
#Adicione o elemento "urso" na terceira posição da lista usando insert.

print()
animais.append('tigre')
print(animais)
animais.insert(2, 'urso')
print(animais)

#7. Ordenar a lista:
#Crie uma nova lista chamada numeros com os elementos: [42, 7, 23, 15, 9].
#Ordene a lista numeros em ordem crescente.
#Ordene a lista numeros em ordem decrescente.

numeros = [42, 7, 23, 15, 9]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)