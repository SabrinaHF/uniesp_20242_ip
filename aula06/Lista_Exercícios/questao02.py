# Faça um programa que calcule as tabuadas dos números de 1 a 10 e armazene o resultado em um arquivo de texto.

num = 1
sub = 1

for i in range (1,11):
    
    print(f'\n-- Tabuada do número {i} --\n')
    
    for i in range (1,11):
        
        print(f'{i} + {num} = {i+num}')
        
    print('\n')
    
    for i in range (1,11):
        
        print(f'{(sub+i)} - {num} = {(sub+i)-num}')
        
    print('\n')   
    
    for i in range (1,11):
        
        print(f'{i} x {num} = {i*num}')
        
    print('\n')
    
    for i in range (1,11):
        
        print(f'{(sub*i)} / {num} = {(sub*i)/num:.0f}')
        
    print('\n')
    
    num+=1   
    sub+=1