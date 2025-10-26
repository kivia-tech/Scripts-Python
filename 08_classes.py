# 08 - Classes e Objetos
# Base da Programação Orientada a Objetos (POO)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

aluna = Pessoa("Kivia", 24)
aluna.apresentar()
