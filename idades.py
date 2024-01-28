

idade = int(input("Informe a idade em anos:"))

#até 12 anos = criança
# 13 a 17 = adolescente
# 18 a 59 = adulto
# 60 ou mais = idoso


if idade > 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <=17:
      print("Adolescente")
elif idade >= 18 and idade <=59:
      print("Adulto")        
elif idade >=60:
      print("Idoso")
else:                 
    print("Idade invalida.")   
print("Fim do programa")

