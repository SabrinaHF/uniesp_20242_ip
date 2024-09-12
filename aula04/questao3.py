#Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))

if(valor1>valor2):
    print(f'Maior valor: {valor1}')
else:
    print(f'Maior valor: {valor2}')   