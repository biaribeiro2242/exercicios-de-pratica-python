idade = int(input("Digite a sua idade:"))

if idade < 16:
    print("não eleitor")

elif idade > 18 and idade < 65:
    print("Eleitor obriatório")

elif idade >= 16 and idade <= 18 or idade > 65:
    print("Eleitor facultativo")