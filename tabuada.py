
'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
5 X 10 = 50
'''

quantidade=0
multiplicador=0
numero = int(input("Informe um numéro de 1 a 10: "))

for contador in range (1,11):
    quantidade = quantidade + 1
    multiplicador = quantidade * numero
    
    print(f'A tabuada de {numero} vezes {quantidade} igual: {multiplicador}')
    