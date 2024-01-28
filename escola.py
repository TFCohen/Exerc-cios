"""
1) Cadastra os registros
2) Lista as informações, nesse também deve ser informado a média e a situação desse aluno, 
se a média for maior ou igual a sete, deverá ser apresentar a palavra "Aprovado", senão "Reprovado".
3) Pesquisa pelo nome
4) Alteração. O programa solicitará o nome, se encontrar, o programa solicitará as informações 
(nome, disciplina, nota1, nota2, nota3, nota4)
5) Excluir. O programa também solicitará o nome para a exclusão
"""
turma =[]   

while True:
 
    opcao = int(input("Informe opção do Menu: 1-Cadastro, 2-Lista, 3-Pesquisar, 4-Alterar, 5-Excluir, 0- Fim: "))
    if opcao == 1:
         while True:
            aluno ={}
            aluno['nome'] = input("Informe o nome do aluno: ")
            aluno['disciplina'] = (input("Informe o nome da disciplina: "))
            aluno['nota1'] = float(input("Informe a primeira nota: "))
            aluno['nota2'] = float(input("Informe a segunda nota: "))
            aluno['nota3'] = float(input("Informe a terceira nota: "))
            aluno['nota4'] = float(input("Informe a quarta nota: "))
            turma.append(aluno)
            continuar = str(input("Deseja continuar? (S/N): "))
            if continuar != 'S' or continuar != 's':
             break

    elif opcao == 2:
         for i in turma:
            print(i)
            media = (i['nota1'] + i['nota2'] + i['nota3'] + i['nota4'])/4
            if media >= 7:
                 situacao = "Aprovado"
            else:
                 situacao = "Reprovado"
            
            print("Media: ", media)
            print("Situação: " ,situacao)

    elif opcao == 3:
        pesquisa = input("Pesquisa nome do aluno: ")
        for i in turma:
           if i['nome'].lower() == pesquisa.lower():
             print(i)
           else:
             print("Nome não cadastrado")  

    elif opcao == 4:
        pesquisa = input("Pesquisa nome do aluno para alterar: ")

        posicao = -1
        contador = 0         

        for i in turma:
           if i['nome'].lower() == pesquisa.lower():
                posicao = 1
                break
           contador = contador + 1

        if posicao > 1:
               turma[posicao]['nome'] = input("Informe o nome do aluno: ")
               turma[posicao]['disciplina'] = (input("Informe o nome da disciplina: "))
               turma[posicao]['nota1'] = float(input("Informe a primeira nota: "))
               turma[posicao]['nota2'] = float(input("Informe a segunda nota: "))
               turma[posicao]['nota3'] = float(input("Informe a terceira nota: "))
               turma[posicao]['nota4'] = float(input("Informe a quarta nota: "))

        else:
                print("Nome não cadastrado")  

    elif opcao == 5:
        pesquisa = input("Pesquisa nome do aluno para remover: ")

        posicao = -1
        contador = 0         

        for i in turma:
           if i['nome'].lower() == pesquisa.lower():
                posicao = 1
                break
           contador = contador + 1

        if posicao > -1:
            turma.pop(posicao)
            print("Nome excluido")
        else:
            print("Nome não cadastrado")  
   
    elif opcao == 9:
         pesquisa = input("Pesquisa nome do aluno: ")
         for i in turma:
          if i['nome'] == pesquisa:
           print(i)  

    elif opcao == 0:
        print("Fim do programa")  
        break