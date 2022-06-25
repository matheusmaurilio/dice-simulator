#Esse programa simula o uso de um dado gerando um valor de 1 a 6

import random 
import PySimpleGUI as PSG

class Simulador_de_dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? "sim ou não" '
        #layout
        self.layout = [
            [PSG.Text('Jogar o dado? ')],
            [PSG.Button('sim'), PSG.Button('não')]
        ]
        
    def Iniciar(self): 
        #criar uma janela
        self.janela = PSG.Window('Simulador de Dado',self.layout)
        #ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        #fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim':
                self.GerarValorDado()
            elif self.eventos == "não":
                print('Obrigado por jogar! ')  
            else:
                print('Favor digitar sim ou não!')
        except:
            print('Ocorreu um erro com a sua resposta!')

    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = Simulador_de_dado()
simulador.Iniciar()