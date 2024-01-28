Valor_hora = float(input("Informe o valor hora do professor:"))
Horas_Trabalhadas = float(input("Informe as horas trabalhadas:"))
Valor_Hora_Extra = float(input("Informe o valor da hora extra:"))
Valor_Desconto = float(input("Informe o valor do desconto:"))

Valor_liquido =  (Valor_hora * Horas_Trabalhadas ) + Valor_Hora_Extra - Valor_Desconto

#valor líquido = (valor hora/aula * número de horas) + valor total de atividades extras - valor total do desconto

print("O valor liquido é:", Valor_liquido)
