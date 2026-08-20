class caneta:
    
    def __init__(self,cor):
        self.cor= cor

    @property
    def get_cor(self):
        return self.cor


canetinha = caneta('azul')
canetas = caneta('vermelhas')
print(canetinha.get_cor)
print(canetas.get_cor)












