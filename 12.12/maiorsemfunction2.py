n = []

# Ler 10 valores digitados pelo usuário, e dizer em qual posição está o maior
for i in range(10):
    number = int(input("Digite valor: "))
    n.append(number)

posicao = 0
for i in range(10):
    if n[posicao] < n[i]:
        posicao = i


print(f"O maior número digitado é {n[posicao]} e está na posição {posicao}.")