import requests #Usa a biblioteca python requests
from datetime import datetime #Usa a biblioteca datetime

print('\n\n\n') #Imprime espaços antes do título

print('    SISTEMA DE COTAÇÃO DE MOEDAS\n')
data_atual = str(datetime.today())
print(f'Data atual: {data_atual}')
print('='*40)

#Chama a API de cotações
requisicao = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL'
).json() #Trata os dados em .json

print(f'Dólar: ')
print(f'Cotação: {requisicao["USDBRL"]["bid"]}')
print('Flutuação diária: ')
print(f'Mínima: {requisicao["USDBRL"]["low"]}\n'
      f'Máxima: {requisicao["USDBRL"]["high"]}')
print('='*40) #Imprime o sinal de igualdade 40 vezes na tela
print('Euro: ')
print(f'Cotação: {requisicao["EURBRL"]["bid"]}')
print('Flutuação diária: ')
print(f'Mínima: {requisicao["EURBRL"]["low"]}')
# print('='*40)
print(f'Máxima: {requisicao["EURBRL"]["high"]}\n\n\n')

