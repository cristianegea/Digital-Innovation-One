# Aula 06: Organização de conjuntos e subconjuntos aritméticos de elementos

# Conjuntos => identificados por {}

# 1. Criação de conjuntos
conjunto = {1, 2, 3, 4}
print(type(conjunto))               # <class 'set'>

# Nos conjuntos não há problemas de duplicidade (mesmo que o número esteja repetido, quando der um print() não aparecerá o número em duplicidade)
conjunto1 = {1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7}
print(conjunto1)                    # output: {1, 2, 3, 4, 5, 6, 7}

# 2. Adicionando elementos em um conjunto
print(conjunto)                     # output: {1, 2, 3, 4}
conjunto.add(5)                     # adição do elemento 5 ao conjunto
print(conjunto)                     # output: {1, 2, 3, 4, 5}

# 3. Removendo elementos de um conjunto
print(conjunto)                     # output: {1, 2, 3, 4, 5}
conjunto.discard(2)                 # remoção do elemento 2 do conjunto
print(conjunto)                     # output: {1, 3, 4, 5}

# 4. Operações entre conjuntos
conjunto2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto3 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

# União
uniao = conjunto2.union(conjunto3)    # união do conjunto 3 ao conjunto 2
print('União: {}'.format(uniao))      # output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
                                      # ignorou a duplicidade dos números

print('fim da instrução')

# Intersecção
interseccao = conjunto2.intersection(conjunto3)    # interseção entre o conjunto 2 e o conjunto 3
print('Intersecção: {}'.format(interseccao))       # output: {5, 6, 7, 8, 9, 10}

print('fim da instrução')

# Diferença
diferenca1 = conjunto2.difference(conjunto3)        # diferença entre o conjunto 2 e o conjunto 3
print('Diferença 1: {}'.format(diferenca1))         # output: {0, 1, 2, 3, 4}

print('fim da instrução')

diferenca2 = conjunto3.difference(conjunto2)        # diferença entre o conjunto 3 e o conjunto 2
print('Diferença 2: {}'.format(diferenca2))         # output: {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

print('fim da instrução')

# Diferença Simétrica (não considera os elementos em comum entre os conjuntos) => complementar da interseção
diferenca_simetrica = conjunto2.symmetric_difference(conjunto3)     # diferença entre o conjunto 2 e o conjunto 3
print('Diferença Simétrica: {}'.format(diferenca_simetrica))        # output: {0, 1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

print('fim da instrução')

# Obs.: se os conjuntos forem iguais o output será "set()" => conjunto vazio

# 5. Operações de Pertinência
conjunto4 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
conjunto5 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# O output será um objeto tipo booleano (true ou false)

# Subconjuntos
subconjunto1 = conjunto5.issubset(conjunto4)
print('O conjunto 5 está contido no conjunto 4? {}'.format(subconjunto1))        # output: True

print('fim da instrução')

subconjunto2 = conjunto4.issubset(conjunto5)
print('O conjunto 4 está contido no conjunto 5? {}'.format(subconjunto2))        # output: False

print('fim da instrução')

# Superconjuntos => lógica inversa dos subconjuntos
superconjunto1 = conjunto5.issuperset(conjunto4)
print('O conjunto 5 contém o conjunto 4? {}'.format(superconjunto1))        # output: False

print('fim da instrução')

superconjunto2 = conjunto4.issuperset(conjunto5)
print('O conjunto 4 contém o conjunto 5? {}'.format(superconjunto2))        # output: True

print('fim da instrução')

# Obs.: Se o conjunto A é subconjunto do conjunto B, então o conjunto B é superconjunto de A

# 6. Remoção de duplicidade em listas
listaA = ['cachorro', 'cachorro', 'cachorro', 'gato', 'gato', 'gato', 'gato', 'elefante', 'elefante']

# Para retirar a duplicidade dos elementos em uma lista, basta converter esta lista em conjunto
# Lembrete: conjunto não aceita duplicidade

conjuntoLA = set(listaA)                 # conversão da lista "listaA" para o conjunto "conjuntoLA"
print(conjuntoLA)                        # output: {'gato', 'cachorro', 'elefante'} => exclusão das duplicidades

print('fim da instrução')

listaB = list(conjuntoLA)                # conversão do conjunto "conjuntoLA" para a lista "listaB"
print(listaB)                            # output: ['elefante', 'cachorro', 'gato']

print('fim da instrução')

conjunto1 = {4, 8, 12, 16}
conjunto2 = {5, 10, 15, 20}

teste = conjunto1.union(conjunto2)
print(teste)