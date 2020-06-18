# Aula 11 - Gerenciando e criando exceções customizadas com try, except, else e finally

# 1. Tratamento de exceção
# documentação sobre exceções: https://docs.python.org/3/library/exceptions.html

# Exemplo 1
try:                            # tudo o que estiver dentro do "try" vai entrar no tratamento de exceção
    divisao = 10 / 0            # Gerando um erro
except ZeroDivisionError:       # "ZeroDivisionError" => classe de exceções
    print('não é possível realizar a operação')

print('fim da instrução 1')

# 2. Encadeamento de exceções
# há uma hierarquia entre as exceções encadeadas, de modo que no topo devem estar os filhos e na base deve estar o pai

# Exemplo 2
lista = [1, 10]
try:
    divisao = 10 / 1
    numero = lista[3]                               # Gerando um erro
except ZeroDivisionError:                           # "ZeroDivisionError" => classe de exceções
    print('não é possível realizar a operação')
except:                                             # tratamento genérico de qualquer tipo de erro
    print('erro desconhecido')

print('fim da instrução 2')

# Exemplo 3
lista = [1, 10]
try:
    divisao = 10 / 1
    numero = lista[3]                                       # Gerando um erro
except ZeroDivisionError:                                   # "ZeroDivisionError" => classe de exceções
    print('não é possível realizar a operação')
except IndexError:                                          # "IndexError" => classe de exceções
    print('erro ao acessar um índice inválido da lista')

print('fim da instrução 3')

# Exemplo 4
lista = [1, 10]
try:
    divisao = 10 / 1
    numero = lista[1]
    x = a                                                   # Gerando um erro
except ZeroDivisionError:                                   # "ZeroDivisionError" => classe de exceções
    print('não é possível realizar a operação')
except IndexError:                                          # "IndexError" => classe de exceções
    print('erro ao acessar um índice inválido da lista')
except BaseException as ex:                                 # "BaseException" => exceção de base => pai de todas as exceções
    print('erro desconhecido => erro: {}'.format(ex))

# todas as exceções têm pai e filho => "BaseException" é o pai de todas as exceções
# se não tiver exceções especificadas, todas as exceções cairão no "BaseException"
# "BaseException" => indicado para tratar uma exceção ainda não prevista

print('fim da instrução 4')

# 3. Else
# else => executa o código quando não ocorrer nenhuma exceção (quando não há ocorrência de erro dentro do "try"
# se alguma exceção ocorrer, o else não será executado

# Exemplo 4
lista = [1, 10]
try:
    divisao = 10 / 1
    numero = lista[1]
    x = 4                                                   # Gerando um erro
except ZeroDivisionError:                                   # "ZeroDivisionError" => classe de exceções
    print('não é possível realizar a operação')
except IndexError:                                          # "IndexError" => classe de exceções
    print('erro ao acessar um índice inválido da lista')
except BaseException as ex:                                 # "BaseException" => exceção de base => pai de todas as exceções
    print('erro desconhecido => erro: {}'.format(ex))
else:
    print('executa quando não há exceção')                  # instrução executada quando não há exceção (quando não há ocorrência de erro dentro do "try"

print('fim da instrução 5')

# Exemplo 5:
lista = [1, 10]
try:
    divisao = 10 / 1
    numero = lista[1]
    x = a                                                   # Gerando um erro
except ZeroDivisionError:                                   # "ZeroDivisionError" => classe de exceções
    print('não é possível realizar a operação')
except IndexError:                                          # "IndexError" => classe de exceções
    print('erro ao acessar um índice inválido da lista')
except BaseException as ex:                                 # "BaseException" => exceção de base => pai de todas as exceções
    print('erro desconhecido => erro: {}'.format(ex))
else:
    print('executa quando não há exceção')                  # instrução executada quando não há exceção

print('fim da instrução 6')

# 4. Finally
# finally => executa independentemente se ocorrer ou não exceção
# independentemente da ocorrência de erro dentro do "try", o "finally" sempre será executado

# Exemplo 6:
lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]
    x = a                                                   # Gerando um erro
except ZeroDivisionError:                                   # "ZeroDivisionError" => classe de exceções
    print('não é possível realizar a operação')
except IndexError:                                          # "IndexError" => classe de exceções
    print('erro ao acessar um índice inválido da lista')
except BaseException as ex:                                 # "BaseException" => exceção de base => pai de todas as exceções
    print('erro desconhecido => erro: {}'.format(ex))
else:
    print('executa quando não há exceção')                  # instrução executada quando não há exceção
finally:
    arquivo.close()
    print('fechando o arquivo')

print('fim da instrução 7')

# 5. Personalizando uma exceção
# Exemplo 7:
while True:                      # executa for verdadeiro as instruções abaixo serão executadas => coloca as instruções em loop
    try:
        x = float(input('Entre com uma nota de 0 a 10:\n'))
        print(x)
        break                   # se as 2 instruções acima forem verdadeiras, o "break" forçará a interrupção do "while true"
                                # se der erro em algumas instruções acima, cairá na exceção e o "break" será ignorado
    except ValueError:
        print('Valor digitado inválido. Deve-se digitar apenas números.')

print('fim da instrução 8')

# 6. Criação de uma classe de exceção
# Exemplo 8:
class Error(Exception):                     # classe "Error" é uma classe de exceção, que já exciste no Python
    pass

class InputError(Error):                    # por convenção, o nome de classe de exceção deve terminar com "Error"
                                            # classe "InputError" é uma classe personalizada (não é nativa do Python), que herda da classe "Error"
    def __init__(self, message):            # personalização da classe "InputError"
        self.message = message              # personalização da mensagem de erro

while True:
    try:
        x = float(input('Entre com uma nota de 0 a 10:\n'))
        print(x)
        if x > 10:                                                          # força a ocorrência de um erro (erro de entrada)
            raise InputError('nota não pode ser maior do que 10')
        elif x < 0:
            raise InputError('nota não pode ser menor do que 0')
        break
    except ValueError:
        print('Valor digitado inválido. Deve-se digitar apenas números.')
    except InputError as ex:                                                # exceção do erro gerado
        print(ex)                                                           # exibição da mensagem de erro personalizada

print('fim da instrução 9')


