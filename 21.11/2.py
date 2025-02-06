def raiz():

    n1: int = int(input("Digite um número: "))

    if n1 > 0:
        print("A raiz quadrada é: ", n1**1/2)
    else:
        print("Número inválido. O número precisa ser positivo.")
        raiz()


raiz()