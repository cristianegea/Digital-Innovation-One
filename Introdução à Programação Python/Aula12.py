# Aula 12 - Instalaçã e utilização de pacotes e realização de requisição com requests

# External Libraries/<Python 3.8>/site-packages => local onde estão instalados os pacotes.

# pacote "pip" => possibilita instalação de pacotes
# comando "pip --version" (no terminal) => mostra a versão do "pip" instalado
# comando "pip --help" (no terminal) => mostra visão geral do "pip"
# comando "pip --freeze" (no terminal) => mostra os pacotes que estão instalados
# comando "pip --upgrade" (no terminal) => atualiza a versão do "pip"

# pacote "requests" => possibilita fazer requisições HTTP
# url da documentação: https://requests.readthedocs.io/en/master/
# comando para instalação do pacote "requests": "pip install requests" (no terminal)
# comando para importação do pacote "requests": "import requests" (no python)

# 1. Requisição via API
# viacep.com.br/ws/01001000/json/ => API onde é possível consultar dados passando determinado número de cep
import requests
response = requests.get('http://viacep.com.br/ws/01001000/json/')
print(response.status_code)                 # validação do API => 200 = API válido / 400 = API inválido
print(response.text)                        # exibe o conteúdo da API
print(type(response.text))                  # <class 'str'>

print('fim da instrução 1')

# para acessar as informações é preciso converter os dados em dicionário
print(response.json())                      # exibe os dados no formato dicionário
print(type(response.json()))                # <class 'dict'>
dados_cep = response.json()
print(dados_cep['logradouro'])              # exibe apenas a informação do logradouro

print('fim da instrução 2')

# Otimizando o processo
def retorna_dados_cep(cep):
    response = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    dados_cep = response.json()
    print(dados_cep['cep'])
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    print(dados_cep['bairro'])
    print(dados_cep['localidade'])
    print(dados_cep['uf'])
    print(dados_cep['unidade'])
    print(dados_cep['ibge'])
    print(dados_cep['gia'])
    return dados_cep

retorna_dados_cep('22041001')

print('fim da instrução 3')

# 2. Requisição via URL
def retorna_response(url):
    response = requests.get(url)
    return response.text

response = retorna_response('https://globallab.org/en/')
print(response)                                             # exibe a estrutura HTML da página



