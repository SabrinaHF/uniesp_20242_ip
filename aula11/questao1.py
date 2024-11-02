# 1. Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
# números repetidos no vetor VET e em que posições se encontram.

vet = []
num_repetido = []

print('\n')
print('*** Programa para ler 10 números e informar se existem números repetidos e em qual posição se encontram ***')
print('\n')

for i in range (10):
    
    vet.append(int(input(f'Informe o número da posição {i}: ')))

for i in range (len(vet)):
    
    for j in range (i+1, len(vet)):
        
        if vet[i] == vet[j]:
            
            if i not in num_repetido:
                num_repetido.append(i)
            
            if j not in num_repetido:
                num_repetido.append(j)
            

if num_repetido:
    print('\n')
    print(f'Existem números repetidos nas posições: {num_repetido}.')
else:
    print('\n')
    print('Não existem números repetidos!')
    
print('---')
