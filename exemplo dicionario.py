estoque =[]

for x in range(2):
    produto = {}
    produto['nome'] = input("Informe o nome: ")
    produto['preco'] = float(input("Informe o preço: "))
    produto['quantidade'] = int(input("Informe a quantidade: "))

    estoque.append(produto)

print(estoque)

#listar pelo nome
for prod in estoque:
    print(prod['nome'])

#listar pelo nome
for p in estoque:
    print(f'{p['nome']}\t{p['preco']}\t{p['quantidade']}')
    