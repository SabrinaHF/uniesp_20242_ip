# 2. Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
# a. Imprima o resultado da soma de todos os valores da matriz no terminal;
# b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

import random

matriz_a = []
matriz_b = []
soma = 0

for i in range(10):
    linha = []
    for j in range(10):
        linha.append(random.randint(10,20))
    matriz_a.append(linha)

for linha in matriz_a:
    for valor in linha:
        soma+=valor

print('\n')          
print('--------------- Matriz A ---------------')
print('\n')   
       
for linha in matriz_a:
    print(linha)

print('\n')
print(f'Resultada da soma de todos os valores da Matriz A: {soma}')


print('\n')          
print('--------------- Matriz B ---------------')
print('\n') 
print('--> Matriz B = Matriz A*3')
print('\n') 

for linha in matriz_a:
    nova_linha = []
    for valor in linha:
        novo_valor = valor*3
        nova_linha.append(novo_valor)
    matriz_b.append(nova_linha)

for nova_linha in matriz_b:
    print(nova_linha)

print('\n')  