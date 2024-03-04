class Estudante:
    escola = "Dio"  # atributo escola

    def __init__(self, nome, numero): # construtor init
        self.nome = nome
        self.numero = numero

    def __str__(self): # metodo str para fazer a representação da classe estudante
        return f"{self.nome} ({self.numero}) - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)    

aluno_1 = Estudante("Leonardo", 1) #instanciando os alunos
aluno_2 = Estudante ("Gustavo", 2)        
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"

mostrar_valores(aluno_1, aluno_2 ) 


# diferencia entre atributo de classe e atributo de instancia. ele é unico para cada objeto,
# exemplo se alterar o numero de matricula do aluno 1 ele não influenciar o numero de matricula do aluno 2.   

