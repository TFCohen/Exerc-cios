
#Com base nas tabelas-verdade, determine o resultado das expressões lógicas considerando que
#X = 1, A = 3, B = 5, C = 8 e D = 7

X = int(input= 1)
A = 3
B = 5
C = 8
D = 7


#a) não (X > 3)
if X < 3:
    print("verdade")
else:
    print("Falso")

#b) (X < 1) e não(B > D)
if X < 3 and X < D:
    print("verdade")
else:
    print("Falso")

#c) não(D < 0) e (C > 5)
#d) não(X > 3) ou (C < 7)
#e) (A > B) ou (C > B)

#f) X >= 2
#g) (X < 1) e (B >= D)
#h) (D < 0) ou (C > 5)
#i) não(D > 3) ou não(B < 7)
#j) (A > B) ou não(C > B)


numero = int(input("Informe um numéro:"))


if numero % 2 ==0:
    print("O numero é par:",numero)
else:                 
    print("O numero é impar:",numero)  
print("Fim do programa")
