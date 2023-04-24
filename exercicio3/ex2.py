valor = float(input("Digite o valor da compra:"))

desconto = valor * 20/100

valorDescontado = valor - desconto

if valor>= 200:
    print("O valor da compra com desconto ficou", valorDescontado)

else:
    print("O valor da compra ficou:",valor)