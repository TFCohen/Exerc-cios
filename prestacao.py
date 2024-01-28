"""
Faça que fará o cálculo do valor de uma prestação em atraso, utilizando a fórmula abaixo
PRESTAÇÃO = Valor + (Valor * (Taxa / 100) * Tempo)
"""

Valor = float(input("Informe o Valor:"))
Taxa = float(input("Informe a Taxa:"))
Tempo = float(input("Informe o tempo em dias:"))


prestacao = Valor + ( Valor * (Taxa /100) * Tempo )

print("O valor da prestação é:", prestacao)
