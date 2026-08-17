passarinhos=[]
class passaro():

   

    def __init__(self, nome , raca , cor ,
     som):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.som = som

        dicionario_passaro = {"Nome" : self.nome ,"Raca" : self.raca , "Cor" : self.cor , "Som" : self.som }

        passarinhos.append(dicionario_passaro)

    def fazer_som(self):
        print(f"Cantando : {self.som}")

    def dados():
        print(passarinhos)


papagaio = passaro("loro","papagaios","Azul","pruuuuuu")
papagaio.fazer_som()

passaro.dados()
