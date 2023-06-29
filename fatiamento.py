
print('\n') #Imprime espaços antes do título
print('     INFORMAÇÕES PESSOAIS')
print('='*35) #Imprime o sinal de igualdade 35 vezes
nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')
if idade and nome: #Condiciona a execução do programa a inclusão de duas entradas de dados
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}') #Fatiamento da variável 'nome' do início ao fim, passando de um em um de trás pra frente (-1)
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
    print(f'Seu nome tem {len(nome)} letras') #A função 'len' faz a contagem da quantidade de letras na variável 'nome'
    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
else:
    print('Desculpa, você deixou campos vazios')
print('\n')