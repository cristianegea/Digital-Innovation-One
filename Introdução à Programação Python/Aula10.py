# Aula 10 - Utilização de informações de data, horário e relacionamento de datas diferentes

# 1. Acessar a data atual
from datetime import date, time, datetime, timedelta

data_atual = date.today()
print(data_atual)                               # output: 2020-06-04 => data no formato YYYY-MM-DD

print(type(data_atual))                         # <class 'datetime.date'>

print('fim da instrução 1A')

# Exibição da data para o formato brasileiro
# "strftime()" => transforma a data em uma string no formato informado entre ()
print(data_atual.strftime('%d/%m/%Y'))          # output: 04/06/2020
print(data_atual.strftime('%d-%m-%Y'))          # output: 04-06-2020
print(data_atual.strftime('%d/%m/%y'))          # output: 04/06/20
print(data_atual.strftime('%d-%m-%y'))          # output: 04/06/20

# %Y = ano com 4 dígitos (YYYY)
# %y = ano coom 2 dígitos (YY)

print('fim da instrução 1B')

# 2. Acessar o dia da semana
print(data_atual.strftime('%A %B %Y'))          # output: Thursday June 2020
# %A = nome completo do dia da semanda, %B = nome completo do mês, %Y = ano com 4 dígitos

print(type(data_atual.strftime('%A %B %Y')))    # <class 'str'>

print('fim da instrução 2')

# 3. Criação de horário
def trabalhando_com_time():
    horario = time(hour = 15, minute = 18, second = 30)
    print(horario)                              # output: 15:18:30
    print(type(horario))                        # output: <class 'datetime.time'>
    horario_str = horario.strftime('%H:%M:%S')  # output: 15:18:30
    print(horario_str)                          # output: <class 'str'>
    print(type(horario_str))  # output: <class 'function'>

trabalhando_com_time()
print(type(trabalhando_com_time))               # output: <class 'function'>

print('fim da instrução 3')

# 4. Acessando data e hora atual
def trabalhando_com_datetima():
    data_atual = datetime.now()
    print(data_atual)                               # output: 2020-06-04 21:02:01.720925
    print(type(data_atual))                         # output: <class 'datetime.datetime'>
    print(data_atual.strftime('%d/%m/%y'))          # output: 04/06/20
    print(type(data_atual.strftime('%d/%m/%y')))    # output: <class 'str'>
    print(data_atual.strftime('%H:%M:%S'))          # output: 21:05:07
    print(type(data_atual.strftime('%H:%M:%S')))    # output: <class 'str'>
    print(data_atual.strftime('%c'))                # output: Thu Jun  4 21:08:38 2020
    print(data_atual.day)                           # output: 4
    print(type(data_atual.day))                     # output: <class 'int'>
    print(data_atual.year)                          # output: 2020
    print(data_atual.hour)                          # output: 21
    print(data_atual.date())                        # output: 2020-06-04
    print(type(data_atual.date()))                  # output: <class 'datetime.date'>
    print(data_atual.weekday())                     # output: 3
    print(type(data_atual.weekday()))               # output: <class 'int'>
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])              # output: Quinta
    print(type(tupla[data_atual.weekday()]))        # output: <class 'str'>

trabalhando_com_datetima()

print('fim da instrução 4')

# 5. Criação de datas
data_criada = datetime(2018, 6, 20, 15, 18, 30)
print(data_criada)                                  # output: 2018-06-20 15:18:30
print(type(data_criada))                            # output: <class 'datetime.datetime'>

# 6. Conversão de data em string para formato "date"
data_string1 = '01/01/2019'
print(type(data_string1))                                         # output: <class 'str'>
data_convertida1 = datetime.strptime(data_string1, '%d/%m/%Y')
print(data_convertida1)                                          # output: 2019-01-01 00:00:00
print(type(data_convertida1))                                    # output: <class 'datetime.datetime'>

data_string2= '01/01/2019 12:20:22'
print(type(data_string2))                                         # output: <class 'str'>
data_convertida2 = datetime.strptime(data_string2, '%d/%m/%Y %H:%M:%S')
print(data_convertida2)                                          # output: 2019-01-01 12:20:22
print(type(data_convertida2))                                    # output: <class 'datetime.datetime'>

print('fim da instrução 5')

# Operações com datas
data_hoje = datetime.now()
print(data_hoje)                                                            # output: 2020-06-04 21:38:48.568332
nova_data1 = data_hoje - timedelta(days = 365)                              # tirando 1 ano da data_hoje
print(nova_data1)                                                           # output: 2019-06-05 21:38:48.568332
nova_data2 = data_hoje - timedelta(days = 365, hours = 2)                   # tirando 1 ano e 2 horas da data_hoje
print(nova_data2)                                                           # output: 2019-06-05 19:41:18.040179

print('fim da instrução 6')

