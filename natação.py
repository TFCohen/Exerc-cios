
idade = int(input("Informe a idade em anos:"))

#infantil A = 5 - 7 anos
#infantil B = 8-10 anos
#juvenil A = 11-13 anos
#juvenil B = 14-17 anos
#adulto = maiores de 18 anos


if idade > 0 and idade <= 4:
    print("não tem classificação.")
elif idade >= 5 and idade <=7:
      print("infantil A")
elif idade >= 8 and idade <=10:
      print("infantil B")
elif idade >= 11 and idade <=13:
      print("juvenil A")        
elif idade >= 14 and idade <=17:
      print("juvenil B")
elif idade >=18:
      print("adulto")      
else:                 
    print("Idade invalida.")   
print("Fim do programa")