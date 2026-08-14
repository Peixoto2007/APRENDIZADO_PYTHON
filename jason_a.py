import json

print("Hello world")

caminhoarquivo= "S.json"


class Cachorro:
 

    def __init__(self, nome , idade , raca):
        self.nome = nome 
        self.idade = idade
        self.raca = raca


    def imprimir(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Raça: {self.raca}")

cachorro1 = Cachorro("bob",14,"Vira-Lata")
cachorro2 = Cachorro("luiz",4,'shitzu')

cachorro1.imprimir()


Classe = Cachorro.__init__

print(Classe)
dados=(cachorro1.__dict__ , cachorro2.__dict__)


# with open (caminhoarquivo,"w")as arquivo:
#     json.dump(dados,arquivo, indent=2 )
