from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def Ligar(self):
        pass

    @abstractmethod    
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass    

        

class ControleTV(ControleRemoto):
    def Ligar(self):
        print("Ligar a tv ...")
        print("ligada")

    def desligar(self):
        print("Desligar a tv ...")
        print("desligado")    

    @property
    def marca(self):
        return "LG"


class ControleArCondicionado( ControleRemoto):
    def Ligar(self):
        print("Ligar o Ar...")
        print("Ligado o Ar Condicionado")

    def desligar(self):
        print("Desligar o Ar...")
        print("desligado")   

    @property
    def marca(self):
        return "AOC"
    
controle = ControleTV()
controle.Ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.Ligar()
controle.desligar()
print(controle.marca)
