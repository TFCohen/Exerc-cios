
from cadastrar import alterar, buscarnome, cadastrar, listar, pesquisar
from utils import menu

turma = []

while True :
    menu()

    opcao = int(input("Informe a opção: "))

    if opcao == 1:
       cadastrar(turma)
       print("Aluno Cadastrado.")
    
    elif opcao == 2:    
        listar(turma)
                
                  
    elif opcao == 3:  
        pesquisar(turma)
   
    elif opcao == 4:  
        nomebusca = input("Informe nome: ")
        posicao = -1
        i = 0
        for m in turma:
            if m['nome'].lower() == nomebusca.lower():
                    posicao = i
                    break
            i = i + 1

        alterar(turma)
    elif opcao == 5:
        pesquisa = input("Pesquisa nome do aluno para remover: ")
        buscarnome(turma)
    elif opcao == 9:  
        print("Fim do programa")  
        break
    

