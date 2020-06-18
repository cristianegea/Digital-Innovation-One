# Aula 04 - Laços de repetição e Condicionais

# 1. Comando 'FOR'
# Exemplo 1: imprimir os 100 primeiros números
# Do zero até o 99
for x in range(100):                # declaração de uma variável dentro do 'FOR'
    print(x)                        # cada vez que o 'FOR' passa por um número, ele é embutido na variável "x"

print('Fim do programa')

# Do 1 até o 100
for x in range(1, 101):
    print(x)

print('Fim do programa')

# Exemplo 2: encontrar os números primos do zero até 100
a = int(input('Entre com um número:\n'))

div = 0                              # valor inicial da variável "div"
for x in range(1, a+1):              # o 'FOR' vai percorrer do 1 até "a + 1"
    resto = a % x
    print(x, resto)
    if resto == 0:
        div = div + 1                # contabiliza a quantidade de números primos
                                     # somente há 2 momento em que o resto = 0, dividindo pelo número 1 e dividindo por ele próprio
    # outra forma de escrever "div = div + 1" é "div += 1"

if div == 2:
    print('O número {} é primo'.format(a))
else:
    print('O número {} não é primo'.format(a))

print('Fim do programa')

# Exemplo 3: imprimir números primos no intervalo entre 0 e 100
b = int(input('Entre com um valor:\n'))

for num in range(b + 1):
    div = 0
    for x in range(1, num + 1):              # um 'FOR' dentro de outro 'FOR'
        resto = num % x
        # print(x, resto)
        if resto == 0:
            div = div + 1
    if div == 2:
        print(num)

print('Fim do programa')

# 2. Comando 'WHILE' (utilizado para forçar uma repetição até que uma afirmação seja verdadeira)
# Exemplo 1
c = 0
while c < 10:
    print(c)            # a instrução será exectada enquando a condição for verdadeira.
    c = c + 1           # outra forma de escrever é "c += 1"

# Exemplo 2
nota = float(input('Insira a nota:\n'))

while nota < 0 or nota > 10:               # Enquanto a nota for maior que 10
    nota = float(input('Nota inválida. Insira a nota correta:\n'))

print('Fim do programa')

# Exemplo 3
nota1 = float(input('Nota do Primeiro Trimestre:\n'))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input('Nota inválida. Insira a nota correta:\n'))

nota2 = float(input('Nota do Segundo Trimestre:\n'))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input('Nota inválida. Insira a nota correta:\n'))

nota3 = float(input('Nota do Terceiro Trimestre:\n'))
while nota3 < 0 or nota3 > 10:
    nota3 = float(input('Nota inválida. Insira a nota correta:\n'))

nota4 = float(input('Nota do Quarto Trimestre:\n'))
while nota4 < 0 or nota4 > 10:
    nota4 = float(input('Nota inválida. Insira a nota correta:\n'))

media = (nota1 + nota2 + nota3 + nota4) / 4
print('Média: {}'.format(media))

if media >= 6:
    print('Aprovado(a)')
elif media > 5 and media < 6:
    print('Recuperação')
else:
    print('Reprovado(a)')

print('Fim do programa')