class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
   
    @classmethod  # ele vai trasformar em um metodo de classe por isso que usa o "cls" e nao self 
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
           

    @staticmethod  # metodo estatico 
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_de_data_nascimento(1997, 7, 9, "Leonardo")
print(p.nome, p.idade)

print(Pessoa. e_maior_idade(17))
print(Pessoa.e_maior_idade(27))
