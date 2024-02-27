#class pai(base)
class Veiculo:
    def __init__(self, cor, placa, numero_rodas, motor):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        self.motor = motor
    
    def ligar_motor(self):
        print("ligando o motor")
        print("VrummVrumm..")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"  

class Motocicleta (Veiculo):
    pass

class Carro (Veiculo):
    pass

class Caminhao (Veiculo):
    def __init__(self,cor, placa, numero_rodas, motor, carregado):
        super().__init__(cor, placa, numero_rodas, motor)
        self.carregado = carregado
  
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("Branca", "gdk8a89", 2, "150cc")
carro = Carro("Azul", "gdk8a99", 4, "4.0 bi-turbo")
caminhao = Caminhao("Branca", "gdk8889", 8, "15.0 turbo", False)

print(moto)
print(carro)
print(caminhao)