#Solicite ao usuário um valor numérico, inteiro ou real (float), e verifique se ele é maior ou menor que 10. 
#O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

num = float(input('Informe um valor: '))

if(num<10):
    print(f'Valor {num} é menor que 10.')
else:
    print(f'Valor {num} é maior que 10.')
    