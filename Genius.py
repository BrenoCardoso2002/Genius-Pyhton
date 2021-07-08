# Importações utilizadas:
import sys
from random import randint
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5 import QtTest


# Função statica que sorteia um lado:
def SorteiaUmLado():
    Indice = randint(1, 4)
    # print(Indice)
    return Indice


# Classe da Janela:
class Janela(QWidget):
    def __init__(self):
        super(Janela, self).__init__()

        # dados da tela:
        self.topo = 0
        self.esquerda = 0
        self.largura = 520
        self.altura = 520
        self.titulo = 'Genius'
        self.setFixedSize(self.largura, self.altura)
        self.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.setStyleSheet('background-color: black;')

        # Variaveis do programa:
        self.Frase_do_topo = 'Ligue e/ou Desligue:'
        self.LigarTexto = 'Ligar'
        self.DesligarTexto = 'Desligar'
        self.TextoOff = 'Desligado'
        self.TextoOn = 'Ligado'
        self.Ordem = []
        self.TamLadoBotaoJogo = 150
        self.IndiceClick = 0
        # ColorButton:
        self.ButtonColorInitial = 'background-color: #F3F3F2;'
        self.ButtonColor1 = "QPushButton{background-color : #A9C4FA;}QPushButton::pressed{background-color : #0055FF;}QPushButton{font-size:26px; font:bold}"
        self.ButtonColor2 = "QPushButton{background-color : #FA9681;}QPushButton::pressed{background-color : #FF2D00;}QPushButton{font-size:26px; font:bold}"
        self.ButtonColor3 = "QPushButton{background-color : #F6FF8B;}QPushButton::pressed{background-color : #EBFF00;}QPushButton{font-size:26px; font:bold}"
        self.ButtonColor4 = "QPushButton{background-color : #B7FF9A;}QPushButton::pressed{background-color : #47F700;}QPushButton{font-size:26px; font:bold}"

        # label 1 (Frase inicial):
        label = QLabel(self)
        label.setText(self.Frase_do_topo)
        label.move(15, 10)
        label.resize(300, 40)
        label.setStyleSheet('QLabel {font:bold;font-size:26px;color:#FFFEFE}')

        # Botão 1 (Ligar jogo):
        self.Ligar = QPushButton(self)
        self.Ligar.setText(self.LigarTexto)
        self.Ligar.move(300, 20)
        self.Ligar.resize(90, 30)
        self.Ligar.setStyleSheet('QPushButton {background-color:#B0C4DE;font:bold;font-size:20px,}')
        self.Ligar.setEnabled(True)
        self.Ligar.clicked.connect(self.LigarJogo)

        # Botão 2 (Desligar jogo):
        self.Desligar = QPushButton(self)
        self.Desligar.setText(self.DesligarTexto)
        self.Desligar.move(400, 20)
        self.Desligar.resize(110, 30)
        self.Desligar.setStyleSheet('QPushButton {background-color:#B0C4DE;font:bold;font-size:20px}')
        self.Desligar.setEnabled(False)
        self.Desligar.clicked.connect(self.DesligarJogo)

        # Botão1 do Jogo Genius:
        self.Button1 = QPushButton(self)
        self.Button1.move(90, 100)
        self.Button1.resize(self.TamLadoBotaoJogo, self.TamLadoBotaoJogo)
        self.Button1.setEnabled(False)
        self.Button1.setStyleSheet(self.ButtonColorInitial)
        self.Button1.clicked.connect(self.ClickBotaoJogo1)
        self.Button1.setText('1')

        # Botão2 do Jogo Genius:
        self.Button2 = QPushButton(self)
        self.Button2.move(280, 100)
        self.Button2.resize(self.TamLadoBotaoJogo, self.TamLadoBotaoJogo)
        self.Button2.setEnabled(False)
        self.Button2.setStyleSheet(self.ButtonColorInitial)
        self.Button2.clicked.connect(self.ClickBotaoJogo2)
        self.Button2.setText('2')

        # Botão3 do Jogo Genius:
        self.Button3 = QPushButton(self)
        self.Button3.move(90, 280)
        self.Button3.resize(self.TamLadoBotaoJogo, self.TamLadoBotaoJogo)
        self.Button3.setEnabled(False)
        self.Button3.setStyleSheet(self.ButtonColorInitial)
        self.Button3.clicked.connect(self.ClickBotaoJogo3)
        self.Button3.setText('3')

        # Botão4 do Jogo Genius:
        self.Button4 = QPushButton(self)
        self.Button4.move(280, 280)
        self.Button4.resize(self.TamLadoBotaoJogo, self.TamLadoBotaoJogo)
        self.Button4.setEnabled(False)
        self.Button4.setStyleSheet(self.ButtonColorInitial)
        self.Button4.clicked.connect(self.ClickBotaoJogo4)
        self.Button4.setText('4')

        # Label Desligado:
        self.LabeOff = QLabel(self)
        self.LabeOff.setText(self.TextoOff)
        self.LabeOff.move(215, 450)
        self.LabeOff.setStyleSheet('QLabel {font:bold;font-size:20px;color:#FFFEFE}')
        self.LabeOff.setVisible(True)

        # Label Ligado:
        self.LabeOn = QLabel(self)
        self.LabeOn.setText(self.TextoOn)
        self.LabeOn.move(225, 450)
        self.LabeOn.setStyleSheet('QLabel {font:bold;font-size:20px;color:#FFFEFE}')
        self.LabeOn.setVisible(False)

        # Abre a Janela:
        self.CarregarJanela()

    # Função que Carrega a janela:
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.center()
        self.show()

    # Função que centraliza a tela:
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Função do evento do clique do botão 1:
    def LigarJogo(self):
        QtTest.QTest.qWait(1500)
        self.Ligar.setEnabled(False)
        self.Desligar.setEnabled(True)
        self.Button1.setEnabled(True)
        self.Button2.setEnabled(True)
        self.Button3.setEnabled(True)
        self.Button4.setEnabled(True)
        self.LabeOff.setVisible(False)
        self.LabeOn.setVisible(True)
        self.IndiceClick = 0
        self.LigarCorBotaoClickPress()
        self.FuncaoInciaVetor()
        self.PicaNaOrdem()

    # Função do evento do clique do botão 2:
    def DesligarJogo(self):
        self.Ligar.setEnabled(True)
        self.Desligar.setEnabled(False)
        self.Button1.setEnabled(False)
        self.Button2.setEnabled(False)
        self.Button3.setEnabled(False)
        self.Button4.setEnabled(False)
        self.DesligarCorBotao()
        self.FecharProgramaQuestion()

    # Função da questão (Deseja fechar o programa?):
    def FecharProgramaQuestion(self):
        # Cria a MsgBox
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle('ATENÇÃO!')
        box.setText('Deseja fechar o Programa?')
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setText('Sim')
        buttonN = box.button(QMessageBox.No)
        buttonN.setText('Não')
        box.exec_()
        # Condição que verifica qual botão da msgbox o usuario clicou:
        if box.clickedButton() == buttonY:
            # YES pressed
            sys.exit(exit(1))
        elif box.clickedButton() == buttonN:
            # NO pressed
            self.recomecadados()
        else:
            self.recomecadados()

    # recomeca uns dados do jogo:
    def recomecadados(self):
        self.IndiceClick = 0
        self.LabeOff.setVisible(True)
        self.LabeOn.setVisible(False)
        # Limpando Vetor da ordem:
        self.LimpandoVetor()

    # Fução que limpa o vetor reponsavel por armazenar a ordem:
    def LimpandoVetor(self):
        # print('Limpando ...')
        self.Ordem.clear()

    # Função de Clique dos botões do jogo (Botão 1):
    def ClickBotaoJogo1(self):
        # print('Botão 1 Click')
        self.IndiceClick += 1
        self.Valida_Click(1)

    # Função de Clique dos botões do jogo (Botão 2):
    def ClickBotaoJogo2(self):
        # print('Botão 2 Click')
        self.IndiceClick += 1
        self.Valida_Click(2)

    # Função de Clique dos botões do jogo (Botão 3):
    def ClickBotaoJogo3(self):
        # print('Botão 3 Click')
        self.IndiceClick += 1
        self.Valida_Click(3)

    # Função de Clique dos botões do jogo (Botão 4):
    def ClickBotaoJogo4(self):
        # print('Botão 4 Click')
        self.IndiceClick += 1
        self.Valida_Click(4)

    # Função que inicia o vetor com 3 clicks ao ligar o jogo
    def FuncaoInciaVetor(self):
        Numero = SorteiaUmLado()
        self.Ordem.append(Numero)
        Numero = SorteiaUmLado()
        self.Ordem.append(Numero)
        Numero = SorteiaUmLado()
        self.Ordem.append(Numero)
        # print(self.Ordem)

    # Liga cor dos botãos:
    def LigarCorBotaoClickPress(self):
        self.Button1.setStyleSheet(self.ButtonColor1)
        self.Button2.setStyleSheet(self.ButtonColor2)
        self.Button3.setStyleSheet(self.ButtonColor3)
        self.Button4.setStyleSheet(self.ButtonColor4)

    # Liga cor dos botãos:
    def DesligarCorBotao(self):
        self.Button1.setStyleSheet(self.ButtonColorInitial)
        self.Button2.setStyleSheet(self.ButtonColorInitial)
        self.Button3.setStyleSheet(self.ButtonColorInitial)
        self.Button4.setStyleSheet(self.ButtonColorInitial)

    # Pisca o botão na ordem:
    def PicaNaOrdem(self):
        self.EnabledButtonFalse()
        tamanho = len(self.Ordem)
        # texto = ''
        for Indice in range(tamanho):
            # print(Indice)
            Numero = self.Ordem[Indice]
            self.PisquueBotao(Numero)
            # print('Numero = {}'.format(Numero))
            # if Indice+1 == tamanho:
            # texto += '{}.'.format(Numero)
            # else:
            # texto += '{} - '.format(Numero)
        # print(texto)
        self.IndiceClick = 0
        self.EnabledButtonTrue()

    # Função que valida o click:
    def Valida_Click(self, Num):
        # print('Valida Click - {}'.format(Num))
        # print('Inidice - {}'.format(self.IndiceClick))
        Indice = self.IndiceClick - 1
        if Num != self.Ordem[Indice]:
            # print('Errou')
            self.VoceErrou()
        # else:
        # print('acertou')
        if (Indice + 1) == len(self.Ordem):
            Numero = SorteiaUmLado()
            self.Ordem.append(Numero)
            # print(self.Ordem)
            self.PicaNaOrdem()

    # Função executada quando o usuario erra a ordem dos click dos botões:
    def VoceErrou(self):
        # Cria a MsgBox
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle('Errou!')
        box.setText('Você errou!!!!\nDeseja fechar o Programa?')
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setText('Sim')
        buttonN = box.button(QMessageBox.No)
        buttonN.setText('Não')
        box.exec_()
        # Condição que verifica qual botão da msgbox o usuario clicou
        if box.clickedButton() == buttonY:
            # YES pressed
            sys.exit(exit(1))
        elif box.clickedButton() == buttonN:
            # NO pressed
            self.LabeOff.setVisible(True)
            self.LabeOn.setVisible(False)
            self.Ligar.setEnabled(True)
            self.Desligar.setEnabled(False)
            self.Button1.setEnabled(False)
            self.Button2.setEnabled(False)
            self.Button3.setEnabled(False)
            self.Button4.setEnabled(False)
            self.DesligarCorBotao()
            self.recomecadados()

    # Desativa os botões para a fala:
    def EnabledButtonFalse(self):
        self.Button1.setEnabled(False)
        self.Button2.setEnabled(False)
        self.Button3.setEnabled(False)
        self.Button4.setEnabled(False)

    # Ativa os botões para a fala:
    def EnabledButtonTrue(self):
        self.Button1.setEnabled(True)
        self.Button2.setEnabled(True)
        self.Button3.setEnabled(True)
        self.Button4.setEnabled(True)

    # Função do pisque:
    def PisquueBotao(self, Numero):
        # print('Botão {} está piscando!'.format(Numero))
        if Numero == 1:
            self.Button1.setStyleSheet("QPushButton{background-color : #0055FF;}QPushButton{font-size:26px; font:bold}")
            # print('Liga o Botão 1')
        elif Numero == 2:
            self.Button2.setStyleSheet("QPushButton{background-color : #FF2D00;}QPushButton{font-size:26px; font:bold}")
            # print('Liga o Botão 2')
        elif Numero == 3:
            self.Button3.setStyleSheet("QPushButton{background-color : #EBFF00;}QPushButton{font-size:26px; font:bold}")
            # print('Liga o Botão 3')
        elif Numero == 4:
            self.Button4.setStyleSheet("QPushButton{background-color : #47F700;}QPushButton{font-size:26px; font:bold}")
            # print('Liga o Botão 4')
        QtTest.QTest.qWait(750)
        self.Button1.setStyleSheet("QPushButton{background-color : #A9C4FA;}QPushButton{font-size:26px; font:bold}")
        # print('Desliga o Botão 1')
        self.Button2.setStyleSheet("QPushButton{background-color : #FA9681;}QPushButton{font-size:26px; font:bold}")
        # print('Desliga o Botão 2')
        self.Button3.setStyleSheet("QPushButton{background-color : #F6FF8B;}QPushButton{font-size:26px; font:bold}")
        # print('Desliga o Botão 3')
        self.Button4.setStyleSheet("QPushButton{background-color : #B7FF9A;}QPushButton{font-size:26px; font:bold}")
        # print('Desliga o Botão 4')
        QtTest.QTest.qWait(750)
        self.LigarCorBotaoClickPress()


# Inicializa a Tela:
application = QApplication(sys.argv)
Window = Janela()
sys.exit(application.exec_())
