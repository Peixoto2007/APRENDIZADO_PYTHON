import json
from jason_a import caminhoarquivo , Cachorro

with open(caminhoarquivo,'r')as arquivo:
    dados = json.load(arquivo)

    Cachorro1 = Cachorro (**dados[0])
    Cachorro2 = Cachorro (**dados[1])

    print(Cachorro1.nome, Cachorro1.idade,Cachorro1.raca)
    print(Cachorro2.nome, Cachorro2.idade,Cachorro2.raca)