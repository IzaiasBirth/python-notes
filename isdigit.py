"""
Faça um programa que peça ao usuário para digitar um número inteiro. Informe se esse número é par ou ímpar.
Caso o usuário não digite um númerro inteiro, informr que não é um número inteiro.
"""
while True: #Envolve o código em um laço
    numero = input('Digite um número inteiro: ')
    if numero.isdigit(): #Verifica se o valor digitado é um número
        numero = int(numero) #Se o dado for um número, é transformado em 'int' (inteiro)
        if numero % 2 == 0: #Verifica se o resto da divisão do número por 2 é '0', o que o torna par
            print(f'{numero} é par!')
        else:
            print(f'{numero} é ímpar!')
        break #Interrompe o laço
    else:
        print(f'{numero} não é inteiro!')

        


