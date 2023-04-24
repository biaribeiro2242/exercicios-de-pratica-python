valorA = float(input("Digite um valor de 0 a 10:"))
valorB = float(input("Digite outro valor de 0 a 10:"))
valorC = float(input("Digite o último valor de 0 a 10:"))

abc = valorA, valorB, valorC

print(abc)

print("Crescente:", sorted(abc))

print("Decrescente:", sorted(abc, reverse=True))