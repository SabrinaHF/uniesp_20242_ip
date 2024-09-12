#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
#Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). 
#Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

num_conta = int(input('Informe número da conta do cliente: '))
saldo = float(input('Informe o valor de saldo do cliente: '))
debito = float(input('Informe o valor de débito do cliente: '))
credito = float(input('Informe o valor de crédito do cliente: '))

saldo_atual = saldo - debito + credito

if(saldo_atual>=0):
    print('Saldo positivo.')
else:
    print('Saldo negativo.')