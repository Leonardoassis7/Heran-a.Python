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

class Motocicleta (Veiculo):
    pass

class Carro (Veiculo):
    pass

class Caminhao (Veiculo):
    def __init__(self,cor, placa, numero_rodas, motor, carregado):
        super().__init__(cor, placa, numero_rodas, motor)
        self.carregado = carregado
  
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} está carregado")


#moto = Motocicleta("Branca", "gdk8a89", 2, "150cc")
#moto.ligar_motor()

#carro = Carro("Azul", "gdk8a99", 4, "4.0 bi-turbo")
#scarro.ligar_motor()

caminhao = Caminhao("Branca", "gdk8889", 8, "15.0 turbo", False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)