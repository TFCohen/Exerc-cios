
#Faça um programa que imprima na tela apenas os números pares entre 1 e 50
#Resolução 1)
numero = 1
contador = 1
for contador in range (1,50):
    numero = contador

    if numero % 2 == 0:
        print(f'{numero} é par')

#Resolução 2)   
lista = []
for contador2 in range (1,51):
    if (contador2 % 2 == 0):
        lista.append(contador2)
 
print(f'são pares entre 1 e 50:{lista}')

#Resolução 3)
for contador3 in range (2,51,2):
     print (contador3)
