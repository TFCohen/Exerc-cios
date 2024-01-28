
soma = 0
media = 0
quantidade = 0
vetor = []
while True:
    
    numero = float(input ("Informe um numero:  "))
   
    quantidade = quantidade + 1
    
    vetor.append(numero)

    soma = soma + numero
    media = (soma/quantidade)
    
    if numero == 0:
        quantidade = quantidade - 1
        vetor.pop()
        break

print (f"Valor da soma é:{soma:.2f}")

print (f"Valor da média é:{media:.2f}")

print(len(vetor))
print(vetor)

