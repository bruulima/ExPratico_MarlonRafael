# 3 - Ao menos 1 método de cada classe deve receber parâmetros digitados pelo usuário (input).
# 4 - Faça com que ao menos 1 classe receba herança e polimorfismo.

from Passeios import Passeios
from CotacaoAgencias import CotacaoAgencias
from Turistas import Turistas

passeios = Passeios('Quatro Praias', 'Jeribucaçu', 'Rafting')
cotacaoAgencias = CotacaoAgencias('Nativos Turismo', 'JBC Turismo', 'Julian Guia')
turistas = Turistas('Bruna', 28, 1.63)


def lin():
    print('-' * 40)
lin()
print(' P A S S E I O ')
lin()

solicitacao1 = int(input('1 - Quatro Praias; 2 - Jeribucaçu; 3 - Rafting. Digite a opção desejada: '))
if solicitacao1 == 1:
    print ('Uau!! O passeio das Quatro Praias é perfeito!')
elif solicitacao1 == 2:
    print ('Maravilha! Já, já estaremos em Jeribucaçu. Vibe incrível!')
else:
    print ('R A D I C A L!!!! Se está procurando adrenalina fez a escolha certa: Rafting')
passeios.ConfirmacaoPasseio()
passeios.Periodo()
passeios.Transfer()


lin()
print(' A G Ê N C I A ')
lin()

cotacaoAgencias.QtGuia()
cotacaoAgencias.Transporte()
almoco = str(input('Deseja fazer parada para almoço? Digite SIM ou NÃO: '))
if almoco == 'SIM' or 'sim':
        print('O local de almoço será definido pelos integrantes do grupo no decorrer da viagem.')
else:
    print('Fica a vontade para levar sua marmita, tem onde esquentar na lancha! :)')


lin()
print(' T U R I S T A ')
lin()

turistas.Turista()
print(f'Sua altura é: {turistas.alturaTurista} e te permite fazer nossos passeios!')
turistas.ProtetorSolar()
turistas.Hidratar()
input('Digite uma nota para o serviço prestado de 0 a 10: ')
print('Agradecemos a preferência! Volte sempre :)')