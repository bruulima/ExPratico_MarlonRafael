    # 1 - Instancie 3 classes diferentes com no mínimo 3 atributos cada e seus respectivos getters e setters.   
  
class Turistas:
    def __init__(self, nomeTurista, idadeTurista, alturaTurista):
        self.nomeTurista = nomeTurista
        self.idadeTurista = idadeTurista
        self.alturaTurista = alturaTurista

    def set_NomeTurista(self, nomeTurista):
        self.nomeTurista = nomeTurista
    def get_NomeTurista(self):
        return self.nomeTurista

    def set_IdadeTurista(self, idadeTurista):
        self.idadeTurista = idadeTurista
    def get_IdadeTurista(self):
        return self.idadeTurista

    def set_AlturaTurista(self, alturaTurista):
        self.alturaTurista = alturaTurista
    def get_AlturaTurista(self):
        return self.alturaTurista     

   
# 2 - Faça 3 métodos para cada classe (não precisam ser métodos complexos).

    def Turista(self):
        print(f'Seja bem-vindo (a), {self.nomeTurista}')

    def ProtetorSolar(self):
        print('Não deixe de usar o protetor solar! :)')

    def Hidratar(self):
        print('Reforçamos a necessidade de ingestão de água!!!')