'''
Uma empresa precisa de um programa que realiza o cadastro de seus produtos, com os seguintes valores: nome, preço, quantidade.
A cada iteração deve perguntar se o usuário deseja continuar, a resposta for igual a 'n', o programa encerrará a execução.
No final, deverá ser apresentado o valor total do estoque e a quantidade de produtos cadastrados.
'''


quantidade = 0

while True:
    nome = str(input("Nome do produto: "))
    preco = float(input ("Preço do produto:  "))
    produto  = int(input("Informe a quntidade do produto: "))
    quantidade = quantidade + 1
    valorestoque = (preco * produto)
    estoquetotal = (preco * produto) + valorestoque
    opcao  = input("Deseja continuar s/n?").lower()
    if opcao == 'n':
        break

print (f"Valor total do estoque é:{estoquetotal:.2f}")

print (f"Quantidade de produtos no estoque é:{quantidade:.01f}")