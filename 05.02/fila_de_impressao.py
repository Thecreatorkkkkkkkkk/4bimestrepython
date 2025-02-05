def menu():
    fila_impressao = FiladeImpressao()
    #criando uma instância para a classe
    fila_impressao.configurar_inicial()
    #configurar os atributos de entrada/inicial
    while True:
        print("Opções:")
        print("1 - Adicionar um trabalho à fila de impressão...")
        print("2 - Imprimir o próximo trabalho à fila...")
        print("3 - Mostrar a fila de impressão...")
        print("4 - Sair do programa...")
        escolha = input("Escolha uma opção...")
    if escolha == "1":
          trabalho = input("Digite o nome do trabalho: ")
          fila_impressao.adicionar_trabaalho(trabalho)
    elif escolha == "2":
         fila_impressao.imprimir()    