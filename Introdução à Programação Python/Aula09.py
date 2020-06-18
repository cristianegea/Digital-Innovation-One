# Aula 09 - Gere, copie, mova, escreva e leia informações de arquivos externos

# 1. Criação de arquivo
arquivo = open('teste.txt', 'w')                     # w => permite escrever no arquivo

# o comando "open()" permite abrir em qualquer diretório, basta inserir o endereço do diretório
# se não for informado o local do diretório desejado, o arquivo será criado no mesmo diretório onde está o arquivo .py

# 2. Escrevendo no arquivo
arquivo.write('Meu primeiro texto')

# se não tiver nenhum texto, o comando "write()" vai escrever no arquivo.
# se já tiver alguma coisa escrita, o comando "write()" vai sobrepor o texto

# 3. Atualização do arquivo
arquivo = open('teste.txt', 'a')                    # a => permite atualizar o arquivo
arquivo.write('\nSegunda linha de texto')           # \n => quebra de linha
arquivo.write('\nTerceira linha de texto')

# 4. Fechamento do arquivo
arquivo.close()

# 5. Otimização do processo
def escrever(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

if __name__ == '__main__':
    escrever('Primeira linha\n')
    atualizar('Segunda linha\n')
    atualizar('Terceira linha\n')

# 6. Leitura de arquivo
def ler(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')                    # a => permite ler o arquivo
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    ler('teste.txt')

# 7. Exemplo
def atualizar_notas(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

# if __name__ == '__main__':
#     aluno = '\nCesar, 7, 9, 3, 8'
#     atualizar_notas('notas.txt', aluno)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    # Transformação de cada linha do arquivo em um item de uma lista
    aluno_nota = aluno_nota.split('\n')          # '\n' => identificador da quebra
    # print(aluno_nota)
    for x in aluno_nota:
        # Fragmentação de cada item da lista
        lista_nota = x.split(',')                # ',' => identificador da quebra
        # print(lista_nota)
        aluno = lista_nota[0]
        lista_nota.pop(0)                        # retirada do primeiro elemento da lista
        print(aluno)
        print(lista_nota)
        # Conversão das notas de string para interiro e cálculo da média das notas
        media = lambda notas: sum(int(i) for i in notas) / 4
        print(media(lista_nota))

# O comando split é usado para converter uma string em uma lista,
# Uma string delimitadora é definida para que cada índice da lista seja criada a partir da string inteira

if __name__ == '__main__':
    media_notas('notas.txt')

# Conversão em dicionário
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    # Transformação de cada linha do arquivo em um item de uma lista
    aluno_nota = aluno_nota.split('\n')          # '\n' => identificador da quebra
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        # Fragmentação de cada item da lista
        lista_nota = x.split(',')                # ',' => identificador da quebra
        aluno = lista_nota[0]
        lista_nota.pop(0)                        # retirada do primeiro elemento da lista
        # Conversão das notas de string para interiro e cálculo da média das notas
        media = lambda notas: sum(int(i) for i in notas) / 4
        lista_media.append({aluno:media(lista_nota)})
    return lista_media

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)

# 8. Cópia de arquivo
# Há bibliotecas no Python que precisam ser importadas
import shutil

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'diretorio')          # diretorio => caminho do diretório desejado

# 9. Movendo arquivo
def move_arquiv(nome_arquivo):
    shutil.move(nome_arquivo, 'diretorio')          # diretorio => caminho do diretório desejado)