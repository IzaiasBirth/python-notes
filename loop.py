#Exercícios com while

# contador = 0 #Início da contagem
# while contador < 20: #Condição até wuando o laço se repete
#     contador += 1 #Incrementador da contagem
#     if contador % 2 == 0: #Condição de exclusão da contagem (se o número for par)
#         continue #Não será contado os números na condição acima
#     print(f'Número {contador}')


###########################################################################################

#Iteração de strings com while

# nome = 'Izaias Nascimento'
# novo_nome = '' #String vazia que será preenchida

# indice = 0 #Início do laço

# while indice < len(nome): #Condição para o laço (Enquanto o índice for menor que o tamanho do nome)
#     letra = (nome[indice]) #Variável que recebe a letra resultante da passagem de cada laço, ou seja, o índice da variável nome 
#     novo_nome += f'{letra}*' #Preenchimento (incremento) da variável 'novo_nome' com a variável 'letra' + o símbolo '*'
#     indice += 1 #Incremento do indice (contador); do contrário, resultaria num loop infinito

# print(novo_nome)


############################################################################################

# Calculadora com While
while True:
    numero_1 = float(input('Digite o primeiro número: '))
    operacao = input('Digite um operador(+-/*): ')
    numero_2 = float(input('Digite o segundo número: '))

    if operacao == '+':
        resultado = numero_1 + numero_2
        print(resultado)
        break
    elif operacao == '-':
        resultado = numero_1 - numero_2
        print(resultado)
        break
    elif operacao == '*':
        resultado = numero_1 * numero_2
        print(resultado)
        break
    elif operacao == '/':
        resultado = numero_1 / numero_2
        print(resultado)
        break
    else:
        print('operação inválida; informe os dados corretamente')

    sair = input('Sair [s]im: ').lower().startswith('s') #Opção de sair do programa se o usuário digitar 's' minúsculo ou qualquer coisa que inicia com 's'

    if sair is True:
        break

    # Código quebrando; tratar o erro...