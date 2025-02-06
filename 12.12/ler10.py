n = []
sumnegative = 0
for i in range(10):
    number = float(input("Digite a nota do aluno: "))
    n.append(number)

    #se nota menor que zero adiconar o valor a outra variave:
qnegative = 0
sumpositive = 0 
for number in n :
    if number < 0 :
        sumnegative += number
        qnegative += 1
    else:
        sumpositive += number

print(f"Quantidade de números negativos é: {qnegative} e a soma dos positivos é: {sumpositive}")
