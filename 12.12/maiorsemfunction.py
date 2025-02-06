n = []

# Inicializar max_index com 0, pois a primeira posição é onde o maior valor pode estar inicialmente
max_index = 0

# Ler 10 valores digitados pelo usuário, e dizer em qual posição está o maior
for i in range(10):
    number = int(input("Digite valor: "))
    n.append(number)
    if n[i] > n[max_index]:
        max_index = i

print(f"O maior número é {n[max_index]} e está na posição {max_index + 1}.")


    



