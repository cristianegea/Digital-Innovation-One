# Aula 08 - Módulos, importação de classes, métodos e construção de funções anônimas (lambda)

# Os módulos são arquivos .py
# Os módulos podem interagir entre eles

# 1. Importação do módulo via "Python Console"
# Exemplo: importação do módulo "Aula07.py"
# No console, digite "Import Aula07" => todas as instruções do módulo serão executadas (sem precisar abrir o arquivo).

# Após importar determinado módulo, é possível acessar qualquer função e classe que estiverem contidos nele

# 2. Acessando a classe pós importação do módulo
# Exemplo: acessando a classe "Televisao" que está no módulo "Aula07.py"
# Para instanciar a classe, digite "televisao = Aula07.Televisao()"
# Para saber se a televisão está ligada, digite "televisao.ligada" => output: False (televisão está desligada)
# Para ligar a televisão, digite "televisao.power()"
# Para saber se a televisão está ligada, digite novamente "televisao.ligada" => output: True (televisão está ligada)

# 3. Importação da classe diretamente
# Exemplo: importação da classe "Televisao" que está no módulo "Aula07.py"
from Aula07 import Televisao                # Digitar no console ou em outro arquivo .py
televisao = Televisao()                     # Instanciando a classe

# 4. Acessando métodos diretamente
# Exemplo: acessando diretamente o método "contador_letras" que está no arquivo "Aula07.py"
from Aula07 import contador_letras

lista = ['cachorro', 'gato', 'elefante']            # como a lista não possui classe, não é preciso instanciá-la

print(contador_letras(lista))

print('fim da instrução')

# 5. Lambda
# Lambda => função anônima (forma de simplificar algo que será utilizado mais de 1 vez no código)
# obs.: uma função anônima não precisa receber nome

# lambda => função nativa do Python

# Lambda transforma uma função que possui algumas linhas em uma função com 1 linha

# Importante: lambda somente é eficiente para funções que podem ser resolvidas em 1 linha

# Exemplo: contador de letras do módulo "Aula07.py)
# Função original:
# def contador_letras(lista_palavras):
#     contador = []                                              # contador inicializa vazio
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador

# Função com lambda:
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

print('fim da instrução - lambda')

# Exemplo: calculadora
# Criação de um dicionário (possui um conjunto de funções)
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
    'resto': lambda a, b: a % b,
}

print(type(calculadora))                    # output: <class 'dict'>

soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']
resto = calculadora['resto']

print('Valor da Soma: {}'.format(soma(10, 5)))                      # output: 15
print('Valor da Subtração: {}'.format(subtracao(10, 5)))            # output: 5
print('Valor da Multiplicação: {}'.format(multiplicacao(10, 5)))    # output: 50
print('Valor da Divisão: {}'.format(divisao(10, 5)))                # output: 2.0
print('Valor da Resto da Divisão: {}'.format(resto(10, 5)))         # output: 0