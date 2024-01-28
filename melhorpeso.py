
#Tendo como dados de entrada a altura em metros e o
#sexo de uma pessoa ("M" masculino e "F"
#feminino), construa um programa que calcule
#seu peso ideal, utilizando as seguintes
#fórmulas:
#- para homens: (72.7*h)-58
#- para mulheres: (62.1*h)-44.7

altura = float(input("Informe a altura em metros:"))
sexo = str(input("Informe M para masculino e F para feminino:"))
peso = 0

if sexo =="M" or sexo == "m":
    peso = ((72.7)*altura)-58
    print(f'Peso ideal masculino é:{peso:.1f}')
elif sexo =="F" or sexo == "f":
   peso = ((62.1)*altura)-44.7
   print(f'Peso ideal feminino é:{peso:.1f}') 
else:
   print("Erro, favor iniciar novamente.")   
       
print("Fim do programa")

