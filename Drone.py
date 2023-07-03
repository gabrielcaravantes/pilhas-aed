from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, helices):
        super().__init__(marca, modelo)
        self._helices = helices
    
    def imprimir(self):
        super().imprimir()
        print(f"Número de helices: {self._helices}")
        