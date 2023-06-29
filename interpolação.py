nome = input('Digite seu nome: ')
ano_nascimento = int(input('Digite o ano que você nasceu: ')) #O 'int' está transformando a entrada de dados do usuário no tipo 'inteiro'

idade = 2023 - ano_nascimento
texto = '%s, você tem %i anos' % (nome, idade) 
#print(f'{nome}, você tem {idade} anos') o código acima faz a mesma operação
print(texto)


