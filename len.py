"""
Programa que solicita ao usuário o seu primeiro nome e, de acordo com a quantidade
de letras, classifica em 'curto', 'normal' ou 'muito grande'
"""

nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome) #Atribui à variável o tamanho do nome digitado

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')