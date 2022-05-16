n1 = 0
n2 = 0
resultado = 0

n1 = float(input("Digite N1: "))
operacao = input("Digite a operação : + - * / : ")
n2 = float(input("Digite N2: "))

if operacao == "+":
    resultado = n1+n2
    print("O Resultado é: ", resultado)
elif operacao == "-":
    resultado = n1-n2
    print("O resultado é: ", resultado)
elif operacao == "*":
    resultado = n1*n2
    print("O resultado é: ", resultado)
elif operacao == "/":
    resultado = n1/n2
    print("O resultado é: ", resultado)
else:
    print("Digite novamente, operação incorreto !")