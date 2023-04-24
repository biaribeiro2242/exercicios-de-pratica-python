n = int(input("Digite a quantidade de números a serem lidos"))

soma_positivos = 0
soma_negativos = 0
soma = 0

for i in range(n):
    num = int(input("Digite um número:"))
    if num > 0:
        soma_positivos += num
    elif num < 0:
        soma_negativos += num

    else:
        soma += num

print("A soma dos números positivos é:", soma_positivos)
print("A soma dos números negativos é:", soma_negativos)
print("A soma total dos números é:", soma)