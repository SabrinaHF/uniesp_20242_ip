#Contexto: Sistema de senhas. 
#Questão: Peça ao usuário para inserir uma senha. 
#Se a senha for "Python123", imprima "Acesso concedido". Caso contrário, imprima "Acesso negado".

senha = input('Insira a senha: ')

if senha == 'Python123':
    print('Acesso concedido')
else:
    print('Acesso negado')