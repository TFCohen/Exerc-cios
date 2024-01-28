
matriz = []

while True:

 selecione = int(input ("Selecione 1 - cadastro, 2- agenda 9- sair:  "))

 if selecione == 1:
 
    nome = str(input("Informe o nome: "))
    telefone = str(input ("Informe o telefone:  "))
    email = str(input("Informe o e-mail: "))
      
    matriz.append([nome,telefone,email])
      
 elif selecione == 2:
        print(matriz)

 elif selecione == 9:
    print("Sair")
    break








