nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))
anoNascimento = int(input("Ano de Nascimento (aaaa): "))

print("Olá,", nome, sobrenome)

if idade >=18 and anoNascimento <= 2004:
    print("Você é MAIOR de idade, pois nasceu ANTES do ano 2004")
    
elif idade <=17 and anoNascimento >=2005:
        print("Você é MENOR de idade, pois nasceu DEPOIS do ano 2005")
    
else:
    print("Ops, divergencia de datas, digite novamente !! ")