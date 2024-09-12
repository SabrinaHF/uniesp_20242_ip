#Contexto: Avaliação de desempenho de um funcionário.
#Questão: Peça ao usuário para inserir o número de horas extras e o número de horas que o funcionário faltou. 
#Se a quantidade de horas extras for maior que as horas faltadas mais 50%, imprima "Bônus de R$ 500.00". 
#Caso contrário, imprima "Sem bônus".

horas_extras = int(input('Insira o número de horas extras: '))
horas_falta = int(input('Insira o número de horas faltadas: '))

if horas_extras>horas_falta+(horas_falta*0.5):
    print('Bônus de R$ 500.00.')
else:
    print('Sem bônus.')