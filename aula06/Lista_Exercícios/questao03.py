# Faça um programa que receba um número e que calcule a tabuada desse número, e armazene o resultado em um arquivo de texto.

numero = int(input('Informe um número para tabuada: '))


sub = 1
div = 1

print(f'\n-- Tabuada do {numero} --\n')

for i in range (1,11):
    
    print(f'{i}+{numero} = {i+numero}')
    
print('\n')

for i in range (1,11):
    
    print(f'{sub+i}-{numero} = {(sub+i)-numero}')
    sub+=1
    
print('\n')

for i in range (1,11):
    
    print(f'{div}/{numero} = {i/numero}')
    div+=1
    
print('\n')

for i in range (1,11):
    
    print(f'{i}*{numero} = {i*numero}')

print('\n')
