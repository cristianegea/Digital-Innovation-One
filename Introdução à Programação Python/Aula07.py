# Aula 07 - Construção de métodos, funções e classes

# Função => retorna um valor
# Método => não retorna um valor
# No Python, o método chama-se "definição" => identificado por "def"
# Uma classe pode agregar diversos métodos

# 1. Declaração de um método/função
def soma(x1, x2):           # definição do método para realizar uma soma
    return x1 + x2          # função para calcular a soma

print(soma(1, 2))           # x1 = 1 e x2 = 2 => output: 3
print(soma(3, 4))           # x1 = 3 e x2 = 4 => output: 7

print('fim da instrução - soma')

def subtracao(x3, x4):           # definição do método para realizar uma subtração
    return x3 - x4               # função para calcular a subtração

print(subtracao(10, 2))          # x3 = 10 e x4 = 2 => output: 8

print('fim da instrução - subtração')

def multiplicacao(x5, x6):           # definição do método para realizar uma multiplicação
    return x5 * x6                   # função para calcular a multiplicação

print(multiplicacao(10,2))

print('fim da instrução - multiplicação')

def divisao(x7, x8):           # mdefinição do método para realizar uma divisão
    return x7 / x8             # função para calcular a divisão

print(divisao(10, 2))

print('fim da instrução - divisão')

# 2. Conversão de um método em uma clásse
# por convenção, o nome da classe começa com a letra maiúscula.

# Exemplo 1
class Calculadora1:
    # é possível inicializar valores dentro de uma classe
    def __init__(self, num1, num2):     # sempre que a classe "Calculadora" for instanciada, obrigatoriamente deve passar pelo método "init"
        self.y1 = num1                  # o valor não passará pelas demais classes sem ter passado pelo "init" primeiro
        self.y2 = num2                  # "self" => serve para referenciar o próprio objeto
                                        # o método "init" é chamado automaticamente
                                        # os demais métodos são chamados manualmente
    def soma(self):
        return self.y1 + self.y2

    def subtracao(self):
        return self.y1 - self.y2

    def multiplicacao(self):
        return self.y1 * self.y2

    def divisao(self):
        return self.y1 / self.y2

    def resto(self):
        return self.y1 % self.y2

calculadora1 = Calculadora1(10, 2)                                           # instanciando uma classe com valores => num1 = 10 e num2 = 2
print('valor da soma: {}'.format(calculadora1.soma()))                       # output: 12
print('valor da subtração: {}'.format(calculadora1.subtracao()))             # output: 8
print('valor da multiplicação: {}'.format(calculadora1.multiplicacao()))     # output: 20
print('valor da divisão: {}'.format(calculadora1.divisao()))                 # output: 5.0
print('valor do resto da divisão: {}'.format(calculadora1.resto()))          # output: 0

print('fim da instrução - Calculadora1')

# Exemplo 2:
class Calculadora2:
    def __init__(self):                     # não há inicialização de valores dentro de uma classe
        pass                                # como o "init" não pode estar vazio, insiro o "pass"

    def soma(self, y1, y2):
        return y1 + y2

    def subtracao(self, y1, y2):
        return y1 - y2

    def multiplicacao(self, y1, y2):
        return y1 * y2

    def divisao(self, y1, y2):
        return y1 / y2

    def resto(self, y1, y2):
        return y1 % y2

calculadora2 = Calculadora2()                                                # instanciando uma classe sem informação de valores
                                                                             # os valores serão informados a cada operação
print('valor da soma: {}'.format(calculadora2.soma(10, 2)))                       # output: 12
print('valor da subtração: {}'.format(calculadora2.subtracao(10, 2)))             # output: 8
print('valor da multiplicação: {}'.format(calculadora2.multiplicacao(10, 2)))     # output: 20
print('valor da divisão: {}'.format(calculadora2.divisao(10, 2)))                 # output: 5.0
print('valor do resto da divisão: {}'.format(calculadora2.resto(10, 2)))          # output: 0

print('fim da instrução - calculadora2')

# Se não há valores a serem inicializados, é possível deixar a classe sem o "init"

# Exemplo 3:
class Calculadora3:
    def soma(self, y1, y2):
        return y1 + y2

    def subtracao(self, y1, y2):
        return y1 - y2

    def multiplicacao(self, y1, y2):
        return y1 * y2

    def divisao(self, y1, y2):
        return y1 / y2

    def resto(self, y1, y2):
        return y1 % y2

calculadora3 = Calculadora3()                                                # instanciando uma classe sem informação de valores
                                                                             # os valores serão informados a cada operação
print('valor da soma: {}'.format(calculadora3.soma(10, 2)))                       # output: 12
print('valor da subtração: {}'.format(calculadora3.subtracao(10, 2)))             # output: 8
print('valor da multiplicação: {}'.format(calculadora3.multiplicacao(10, 2)))     # output: 20
print('valor da divisão: {}'.format(calculadora3.divisao(10, 2)))                 # output: 5.0
print('valor do resto da divisão: {}'.format(calculadora3.resto(10, 2)))          # output: 0

print('fim da instrução - calculadora3')

# Exemplo 4:
class Televisao:
    def __init__(self):
        self.ligada = False                 # sempre que inicializar a tv, ela estará desligada
        self.canal = 5                      # sempre que inicializar a tv, ela estará estará no canal 5

    def power(self):                        # método de ligar a tv
        if self.ligada:                     # default: "self.ligada == True"
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):                        # método de aumentar o canal
        if self.ligada != True:                     # o canal será alterado somente se a tv estiver ligada
            self.canal += 1

    def diminui_canal(self):                        # método de diminuir o canal
        if self.ligada != True:                     # o canal será alterado somente se a tv estiver ligada
            self.canal -= 1

tv = Televisao()
print('tv está ligada? {}'.format(tv.ligada))               # output: False
tv.power()
print('tv está ligada? {}'.format(tv.ligada))               # output: True
tv.power()
print('tv está ligada? {}'.format(tv.ligada))               # output: False

print('canal atual: {}'.format(tv.canal))                   # output: 5

# Aumento de canal
tv.aumenta_canal()
tv.aumenta_canal()
print('novo canal: {}'.format(tv.canal))                   # output: 7

# Diminuição de canal
tv.diminui_canal()
tv.diminui_canal()
tv.diminui_canal()
print('novo canal: {}'.format(tv.canal))                   # output: 4

print('fim intrução - televisão')

# Exemplo 5
def contador_letras(lista_palavras):
    contador = []                                              # contador inicializa vazio
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

lista = ['cachorro', 'gato']
print(contador_letras(lista))

print('fim da instrução - contador')

# "if ___name___ == '___main___':" => o trecho somente será executado se for chamado pelo mesmo arquivo, caso contrário não será executado.
