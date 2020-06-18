# Aula 02 - Variáveis e Operadores Aritméticos

# 1. Operadores Aritméticos
a = 10
b = 5

# Operador de Soma (+)
soma = a + b
print(soma)

# Operador de Subtração (-)
subtracao = a - b
print(subtracao)

# Operador de Multiplicação (*)
multiplicacao = a*b
print(multiplicacao)

# Operador de Divisão (/)
divisao = a/b
print(divisao)

# Operador de Resto da Divisão (%)
resto = a%b
print(resto)

# 2. Tipos de Variáveis
# Variável do tipo inteiro
inteiro = 4
print(type(inteiro))    # <class 'int'>

# Variável do tipo float
decimal = 4.5
print(type(decimal))    # <class 'float'>

# Variável do tipo string
texto = "variável"
print(type(texto))      # <class 'str'>

# 3. Conversão de Variáveis
# Conversão de uma variável tipo inteiro em uma variável tipo string
x1 = 45
print(type(x1))         # <class 'int'>
x1 = str(x1)
print(x1)
print(type(x1))         # <class 'str'>

# Conversão de uma variável tipo inteiro em uma variável tipo float
x2 = 50
print(type(x2))         # <class 'int'>
x2 = float(x2)
print(x2)               # x2 = 50.0
print(type(x2))         # <class 'float'>

# Conversão de uma variável tipo float em uma variável tipo inteiro
x3 = 55.4
print(type(x3))         # <class 'int'>
x3 = int(x3)
print(x3)               # x2 = 55 => arrendondamento para cima
print(type(x3))         # <class 'float'>

# 4. Concatenação de variáveis tipo strings
# Método clássico
valor = 10
print(type(valor))      # <class 'int'>
# obs.: não é possível concatenar variáveis de tipos diferentes.
print('o valor é ' + str(valor))         # Output => o valor é 10

# Utilizando o comando ".format()"
resultado1 = 100
print('o resultado é {}'.format(resultado1))     # Output => o resultado é 100
# Não é preciso converter o tipo da variável para fazer a concatenação

resultado2 = 500
print('os resultados são {} e {}'.format(resultado1, resultado2))     # Output => os resultados são 100 e 500

print('os resultados são {r1} e {r2}'.format(r1 = resultado1, r2 = resultado2))     # Output => os resultados são 100 e 500

# 5. Interação com o usuário
y1 = input('Entre com o primeiro valor:\n')     # type(y1) = string
print(type(y1))
y2 = input('Entre com o segundo valor: \n')     # type(y2) = string
print(type(y2))

# Obs.: "\n" => quebra de linha

z1 = int(input('Entre com o primeiro valor:\n'))     # type(z1) = inteiro
print(type(z1))
z2 = int(input('Entre com o segundo valor: \n'))     # type(z2) = inteiro
print(type(z2))

z = z1 + z2
print(z)

