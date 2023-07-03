from Veiculo import Veiculo
from Drone import Drone
from Carro import Carro

class Pilha:
    def __init__(self):
        self.__itens = []
    
    def adicionar(self, item):
        self.__itens.append(item)
    
    def remover(self):
        if not self.vazia():
            return self.__itens.pop()
        else:
            print("Pilha vazia.")
    
    def vazia(self):
        return len(self.__itens) == 0
    
    def imprimir_pilha(self):
        if not self.vazia():
            for item in self.__itens:
                item.imprimir()
        else:
            print("Pilha vazia.")

def menu():
    print("1- Adicionar carro")
    print("2- Remover carro")
    print("3- Adicionar drone")
    print("4- Remover drone")
    print("5- Imprimir pilha de carros")
    print("6- Imprimir pilha de drones")

pilha_carros = Pilha()
pilha_drones = Pilha()

while True:
    menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        marca = input("Marca do carro: ")
        modelo = input("Modelo do carro: ")
        portas = int(input("Quantidade portas do carro: "))
        carro = Carro(marca, modelo, portas)
        pilha_carros.adicionar(carro)
        print("\nCarro adicionado na pilha\n")
    
    elif opcao == '2':
        carro_removido = pilha_carros.remover()
        if carro_removido:
            print("\nCarro removido da pilha\n")
            carro_removido.imprimir()
    
    elif opcao == '3':
        marca = input("Marca do drone: ")
        modelo = input("Modelo do drone: ")
        helices = int(input("Quantidade de helices do drone: "))
        drone = Drone(marca, modelo, helices)
        pilha_drones.adicionar(drone)
        print("\nDrone adicionado na pilha\n")
    
    elif opcao == '4':
        drone_removido = pilha_drones.remover()
        if drone_removido:
            print("\nDrone removido da pilha\n")
            drone_removido.imprimir()

    elif opcao == '5':
        pilha_carros.imprimir_pilha()
        
    elif opcao == '6':
        pilha_drones.imprimir_pilha()
