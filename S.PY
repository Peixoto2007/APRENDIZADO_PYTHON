print("Hello world")


class Pessoa: 
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def imprimir(self):
        print(self.nome , self.sobrenome)


p1 = Pessoa("Dyego","Alves") 

p1.imprimir()






