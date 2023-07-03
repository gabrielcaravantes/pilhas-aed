from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas
    
    def imprimir(self):
        super().imprimir()
        print(f"Portas: {self.__portas}")
        