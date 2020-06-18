# Aula 03 - Condicionais e Valores Lógicos

# Obs.: no Python é possível definir o início e o fim de um código através da identação.

# Exemplo 1
a = int(input('Primeiro Valor:\n'))
b = int(input('Segundo Valor:\n'))
c = int(input('Terceiro Valor:\n'))

if a > b:
    print('O maior número é {}'.format(a))      # instrução executada se a condição for verdadeira
print('Final do programa')                      # instrução executada independentemente da condição ser verdadeira ou não

if a > b:
    print('O maior número é {}'.format(a))      # instrução executada se a condição for verdadeira
else:
    print('O maior número é {}'.format(b))      # instrução executada se a condição não for verdadeira
print('Final do programa')                      # instrução executada independentemente da condição ser verdadeira ou não

if a > b:
    print('O maior número é {}'.format(a))      # instrução executada se a 1ª condição for verdadeira
elif b > c:                                     # elif = else + if
    print('O maior número é {}'.format(b))      # instrução executada se a 2ª condição for verdadeira
else:
    print('O maior número é {}'.format(c))      # instrução executada se nenhuma das condições forem verdadeiras
print('Final do programa')                      # instrução executada independentemente da condição ser verdadeira ou não

if a > b and a > c:
    print('O maior número é {}'.format(a))      # instrução executada se a 1ª condição for verdadeira
elif b > a and b > c:                           # elif = else + if
    print('O maior número é {}'.format(b))      # instrução executada se a 2ª condição for verdadeira
else:
    print('O maior número é {}'.format(c))      # instrução executada se nenhuma das condições forem verdadeiras
print('Final do programa')                      # instrução executada independentemente da condição ser verdadeira ou não

# Exemplo 2
resto_a = a % 2                     # resto da divisão de "a" por 2
resto_b = b % 2                     # resto da divisão de "b" por 2

if resto_a == 0:                    # se a for par, resto = 0. Caso contrário, resto != 0
    print('O número é par')
else:
    print('O número é ímpar')
print('Final do programa')

if resto_a == 0 and resto_b == 0:               # verifica se algum número é par
    print('Todos os números são pares')
elif resto_a == 0 and resto_b != 0:
    print('O número "a" é par')
elif resto_a != 0 and resto_b == 0:
    print('O número "b" é par')
else:
    print('Todos os números são ímpares')
print('Fim do programa')

if resto_a == 0 or resto_b == 0:
    print('Foi digitado um número par')
else:
    print('Não foi digitado um número par')
print('Fim do programa')

# Exemplo 3:
nota1 = float(input('Nota do Primeiro Trimestre:\n'))
if nota1 < 0 or nota1 > 10:
    nota1 = float(input('Você digitou errado a nota. Digite Novamente:\n'))

nota2 = float(input('Nota do Segundo Trimestre:\n'))
if nota2 < 0 or nota2 > 10:
    nota1 = float(input('Você digitou errado a nota. Digite Novamente:\n'))

nota3 = float(input('Nota do Terceiro Trimestre:\n'))
if nota3 < 0 or nota3 > 10:
    nota1 = float(input('Você digitou errado a nota. Digite Novamente:\n'))

nota4 = float(input('Nota do Quarto Trimestre:\n'))
if nota4 < 0 or nota4 > 10:
    nota1 = float(input('Você digitou errado a nota. Digite Novamente:\n'))

media = (nota1 + nota2 + nota3 + nota4) / 4
print('Média: {}'.format(media))

if media >= 6:
    print('Aprovado(a)')
elif media > 5 and media < 6:
    print('Recuperação')
else:
    print('Reprovado(a)')

print('Fim do programa')

