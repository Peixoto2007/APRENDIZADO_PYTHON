import json

print("Hello world")


class Cachorro:
 

    def __init__(self, nome , idade , raca):
        self.nome = nome 
        self.idade = idade
        self.raca = raca


    def imprimir(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Raça: {self.raca}")

cachorro1 = Cachorro("bob",14,"Vira-Lata")

cachorro1.imprimir()

dado1=(cachorro1.__dict__)


with open ("S.json","w")as arquivo:
    json.dump(dado1,arquivo, indent=2)
