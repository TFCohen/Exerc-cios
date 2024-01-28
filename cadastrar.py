def cadastrar (vetor):
    aluno = {}
    aluno['nome'] = input("Informe o nome do aluno: ")
    aluno['disciplina'] = (input("Informe o nome da disciplina: "))
    aluno['nota1'] = float(input("Informe a primeira nota: "))
    aluno['nota2'] = float(input("Informe a segunda nota: "))
    aluno['nota3'] = float(input("Informe a terceira nota: "))
    aluno['nota4'] = float(input("Informe a quarta nota: "))
    vetor.append(aluno)

def listar(turma):
 for i in turma:
            print(i)
            media = (i['nota1'] + i['nota2'] + i['nota3'] + i['nota4'])/4
            if media >= 7:
                 situacao = "Aprovado"
            else:
                 situacao = "Reprovado"
            
            print("Media: ", media)
            print("Situação: " ,situacao)

def buscarnome(turma):
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

def alterar(turma):
    if posicao > -1:
       turma[posicao]['nome'] = input("Informe o nome do aluno: ")
       turma[posicao]['disciplina'] = (input("Informe o nome da disciplina: "))
       turma[posicao]['nota1'] = float(input("Informe a primeira nota: "))
       turma[posicao]['nota2'] = float(input("Informe a segunda nota: "))
       turma[posicao]['nota3'] = float(input("Informe a terceira nota: "))
       turma[posicao]['nota4'] = float(input("Informe a quarta nota: "))
    else:
       print("Não encontrado")     

def pesquisar(turma):
    pesquisa = input("Pesquisa nome do aluno: ")
    for i in turma:
           if i['nome'].lower() == pesquisa.lower():
             print(i)
           else:
             print("Nome não cadastrado")         