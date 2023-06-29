print('Iniciando o programa')
print('.'*60)
numero = input('digite um número: ') #A saída do input é tipo 'str'
numero = float(numero) #Converte o dado inserido pelo usuário em float

resultado = numero + 1 #Visto que a variável 'numero' foi convertida em float, o resultado é possível
print(resultado)