# 1 - Instancie 3 classes diferentes com no mínimo 3 atributos cada e seus respectivos getters e setters.

class CotacaoAgencias():
    def __init__(self, AltoPadrao, MedioPadrao, BaixoPadrao, ):
        self.AltoPadrao = AltoPadrao
        self.MedioPadrao = MedioPadrao
        self.BaixoPadrao = BaixoPadrao

    def set_AltoPadrao(self, AltoPadrao):
        self.AltoPadrao = AltoPadrao
    def get_AltoPadrao(self):
        return self.AltoPadrao

    def set_MedioPadrao(self, MedioPadrao):
        self.MedioPadrao = MedioPadrao
    def get_MedioPadrao(self):
        return self.MedioPadrao

    def set_BaixoPadrao(self, BaixoPadrao):
        self.BaixoPadrao = BaixoPadrao
    def get_BaixoPadrao(self):
        return self.BaixoPadrao

# 2 - Faça 3 métodos para cada classe (não precisam ser métodos complexos).

    def QtGuia(self):
        print('Disponibilizaremos dois guias para acompanhá-lo(s) e explicar a história do local!')

    def Transporte(self):
        print('A aventura será no mar e no rio! Nossa lancha é totalmente equipada e nos levará a lugares mágicos!')
        
    def Refeicao(self):
        print('O local de almoço será definido pelos integrantes do grupo no decorrer da viagem.')
