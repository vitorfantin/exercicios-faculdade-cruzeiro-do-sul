notas = []

while True:
    nota = float(input("digite a nota do aluno: "))
    notas.append(nota)
    resp = input("deseja continuar (s/n): ")
    if resp == "n" or resp == "N":
            break
notas.pop()
notas[0] = 3.5

for n in notas:
    print(n)
