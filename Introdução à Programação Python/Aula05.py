# Aula 05 - Organização de dados em uma lista ou tupla e realização de operações com elas

# I. Listas
# Listas => identificadas por []

# 1. Criação de listas
lista_int = [1, 3, 5, 7]                            # lista de números inteiros primos
print(type(lista_int))                              # <class 'list'>

lista_animal = ['cachorro', 'gato', 'elefante']     # lista de animais (strings)
print(type(lista_animal))                           # <class 'list'>

# É possível ter variáveis de tipos diferentes em uma mesma lista

lista_mix = [1, 'cachorro', 3, 'gato', 5, 'elefante', 7]
print(lista_mix)
print(type(lista_mix))                              # <class 'list'>

# Boas práticas: somente variáveis do mesmo tipo em uma mesma lista

# 2. Extração de elementos em uma lista
# Dentro de uma lista, a posição inicial do elemento é zero
# lista = [posição 0, posição 1, posição 2, posição 3, ...]
print(lista_mix[1])              # output: cachorro
print(lista_mix[0])              # output: 1

# 3. Utilização de laço de repetição ('FOR') para percorrer elementos de uma lista
for x in lista_animal:
    print(x)                        # exibição de todos os elementos da lista
print('Fim do programa')

soma = 0
for x in lista_int:
    soma += x                       # soma acumulada
    print(soma)
print('Fim do programa')

# 4. Operações com elementos em uma lista
# soma de todos os elementos da lista
print(sum(lista_int))               # só funciona se todos os elementos da lista forem numéricos

# maior elemento em uma lista
print(max(lista_int))               # aplicação em lista com elementos numéricos
print((max(lista_animal)))          # aplicação em lista com strings => maior valor = string começada com a letra com a maior posição no alfabeto

# menor elemento em uma lista
print(min(lista_int))               # aplicação em lista com elementos numéricos
print((min(lista_animal)))          # aplicação em lista com strings => menor valor = string começada com a letra com a menor posição no alfabeto

# multiplicação dos elemento em uma lista
lista_nova = lista_animal * 3       # cada sequência de elementos será repetida 3 vezes

# 5. Validação de elementos em uma lista
animal = input('Insira o elemento:\n')

if animal in lista_animal:
    print('existe este elemento na lista')
else:
    print('não existe este elemento na lista')

print('fim do programa')

# 6. Inclusão/remoção de elementos em uma lista
animal = input('Insira o elemento:\n')

# Inclusão
if animal in lista_animal:
    print('Existe este elemento na lista')
else:
    print('Existe este elemento na lista. Necessária inclusão')
    lista_animal.append(animal)                     # inclusão de elemento na lista
    print(lista_animal)

print('fim do programa')

# Exclusão
print(lista_animal)                 # lista com todos os elementos

lista_animal.pop()                  # lista sem o último elemento
print(lista_animal)
# Obs.: "pop()" retira sempre o último elemento da fila

lista_animal.pop(0)                  # lista sem o primeiro elemento
print(lista_animal)

# Obs.: ".remove()" => retira o elemento da lista pelo seu nome
print(lista_mix)                    # lista com todos os elementos
lista_mix.remove('cachorro')        # remoção do elemento 'cachorro'
print(lista_mix)

# Ordenação dos elemento em uma lista
lista_a = [32, 56, 23, 48, 91, 6, 100, 1]
lista_b = ['cachorro', 'gato', 'mula', 'capivara', 'anta', 'lobo']

print(lista_a)                         # sem ordenação
lista_a.sort()                         # elementos ordenados => ordem crescente
print(lista_a)
lista_a.reverse()                      # elementos ordenados => ordem decrescente
print(lista_a)

print(lista_b)                         # sem ordenação
lista_b.sort()                         # elementos ordenados => ordem alfabética
print(lista_b)
lista_b.reverse()                      # elementos ordenados => ordem alfabética inversa
print(lista_b)

# II. Tuplas
# Uma tupla é imutável (não consigo modificar valores), enquanto uma lista é mutável (consigo modificar valores).
# Tupplas => identificadas por ()

# Criação de tuplas
tupla = (1, 10, 12, 14)
print(type(tupla))                        # <class 'tuple'>

print(len(tupla))                         # contagem de elementos em uma tupla

# Conversão de lista em tupla
print(type(lista_animal))                  # <class 'list'>
lista_animal = tuple(lista_animal)         # conversão da lista em tupla
print(type(lista_animal))                  # <class 'tuple'>

# Conversão de tupla em lista
print(type(tupla))                          # <class 'tuple'>
tupla = list(tupla)
print(type(tupla))                          # <class 'list'>


