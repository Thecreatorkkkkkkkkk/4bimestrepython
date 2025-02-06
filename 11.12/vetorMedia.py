"""""FAÇA UM PROGRAQMA QUE VAILER 5 NOTAS DE PROVA E ARMAZENAR
IMPRIMIR A MEDIA GERAL DA TURMA"""


nota = []

for i in range(5):
    notaunitaria = float(input("Digite a nota do aluno: "))
    nota.append(notaunitaria)

media = 0 


#O item "no" vai passar por todo o vetor "nota" e colocar dentro da media
for no in nota:
    media = media+ no

media = media/5

print(f"A média geral da turma é: {media}")