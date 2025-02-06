

class FiladeImpressao:


     def configurar_inicial(self):
          self.fila= []
     def adicionar_trabalho(self, trabalho):
          self.fila.append(trabalho)
          print(f"Trabalho '{trabalho}' adicionado à fila.")


     def processar_trabalho(self):
          if not self.estar_vazia():  #Verefica se a lista não está vazia
               trabalho = self.fila.pop(0)  #Remove o primeiro da fila

               print(f"Trabalho '{trabalho}' processado.")

          else:
               print("A fila está vazia!")

     def mostrar_fila(self):
          if self.estar_vazia(): #Verifica se a lista
               print("A fila está vazia!")
          else:
               print("Fila atual de impressão: ")
               for trabalho in self.fila:
                    print(f"-{trabalho}") # - Imprimir cada trabalho da lista
     

     def estar_vazia(self):
          return len(self.fila) == 0  # Se o comprimento da lista for 0, retorna True (fila vazia)

def menu():
     fila_impressao = FiladeImpressao()
     # criando uma instância para a classe
     fila_impressao.configurar_inicial()
     # configurar os atributos de entrada/inicial
     while True:
          print("Opções:")
          print("1 - Adicionar um trabalho à fila de impressão...")
          print("2 - Imprimir o próximo trabalho à fila...")
          print("3 - Mostrar a fila de impressão...")
          print("4 - Sair do programa...")
          escolha = input("Escolha uma opção...")
        
          if escolha == "1":
               trabalho = input("Digite o nome do trabalho: ")
               fila_impressao.adicionar_trabalho(trabalho)
          elif escolha == "2":
               fila_impressao.processar()
          elif escolha == "3":
               fila_impressao.mostrar_fila()
          elif escolha == "4":
               print("Programa encerrado!. . . ")
               break
          else:
               print("Opção inválida!")    
                    
                    
                    
                    
menu()