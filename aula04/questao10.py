#Contexto: Determinação do tipo de triângulo. 
#Questão: Peça ao usuário para inserir três lados de um triângulo e determine se é um triângulo equilátero, isósceles ou escaleno.

lado_a = int(input('Insira a medida do 1º lado do triângulo: '))
lado_b = int(input('Insira a medida do 2º lado do triângulo: '))
lado_c = int(input('Insira a medida do 3º lado do triângulo: '))

if lado_a==lado_b and lado_b==lado_c:
    print('O triângulo é equilátero!')
elif lado_a==lado_b or lado_b==lado_c or lado_a==lado_c:
    print('O triângulo é isósceles!')
else:
    print('O triângulo é escaleno!') 