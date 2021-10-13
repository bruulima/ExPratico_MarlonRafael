# 1 - Instancie 3 classes diferentes com no mínimo 3 atributos cada e seus respectivos getters e setters.
from Turistas import Turistas

class Passeios:
    def __init__(self, grupo, dupla, avulso):
        self.grupo = grupo
        self.dupla = dupla
        self.avulso = avulso

    def set_grupo(self, grupo):
        self.grupo = grupo
    def get_grupo(self):
        return self.grupo

    def set_dupla(self, dupla):
        self.dupla = dupla
    def get_dupla(self):
        return self.dupla

    def set_avulso(self, avulso):
        self.avulso = avulso
    def get_avulso(self):
        return self.avulso

# 2 - Faça 3 métodos para cada classe (não precisam ser métodos complexos).

    def Periodo(self):
        print('O passeio será das 9h as 17h.')

    def Transfer(self):
        print('Nosso transfer irá buscá-lo(s) na portaria do Hotel.')
        
    def ConfirmacaoPasseio(self):
        print('Agendamento concluído.')
