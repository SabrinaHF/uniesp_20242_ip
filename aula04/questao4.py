#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))

if(valor1<valor2):
    print(valor1,valor2)
else:
    print(valor2,valor1)