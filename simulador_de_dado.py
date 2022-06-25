#Esse programa simula o uso de um dado gerando um valor de 1 a 6

import random 
import PySimpleGUI as PSG

class Simulador_de_dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? "s ou n" '

    def Iniciar(self): 
        msg = input(self.mensagem)
        try:
            if msg == "s":
                self.GerarValorDado()
            elif msg == "n":
                print('Obrigado por jogar! ')  
            else:
                print('Favor digitar s ou n !')
        except:
            print('Ocorreu um erro com a sua resposta!')

    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = Simulador_de_dado()
simulador.Iniciar()