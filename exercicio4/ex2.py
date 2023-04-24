numero1 = float(input("Digite o primeiro número:"))

numero2 = float(input("Digite o segundo número:"))

operacao = input("Digite a operacão matemática:")

soma = numero1 + numero2

subtracao = numero1 - numero2

multiplicaco = numero1 * numero2

divisao = numero1 / numero2

if  operacao == "+":
    print(soma)

elif operacao == "-":
    print(subtracao)

elif operacao == "*":
    print(multiplicaco)

elif operacao == "/":
    print(divisao)

else:
    print("Valor incorreto! Digite corretamente.")