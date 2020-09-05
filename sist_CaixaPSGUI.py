import Produtos as P
import PySimpleGUI as sg


class JanelaCaixa():
    def __init__(self):
        self.ptotal = 0.0
        self.qtd = 0
        layout = [[sg.Text('Nome do item:'),sg.InputText(key='K'),sg.Text('Quantidade:'), sg.Input(key='qtd')],
                [sg.Output(size=(150,30),background_color='lightgray'), sg.Button('Adicionar Item')],
                [sg.Text('Fechar sistema?'), sg.Button('Sim',key='S')]]
               
    
        self.janela = sg.Window('Caixa 01', layout)
    def iniciar(self):
        while True:
            self.evento, self.valores = self.janela.Read()
            if self.evento == sg.WIN_CLOSED  or self.evento =='S':
                break
            if self.evento == 'Adicionar Item':
                try:
                    if self.valores['K'] in P.produtos:
                        self.ptotal += P.produtos[self.valores['K']] * int(self.valores['qtd'])
                    if self.valores['K'] not in P.produtos:
                        raise KeyError
                except KeyError:
                    print('Item fora da lista, sinto muito.')
                    print('Insira outro item, por favor')
                except TypeError:
                    print('Por favor, insira um item válido.')                 
                else:
                    self.qtd += int(self.valores['qtd'])
                    print('Item adicionado com sucesso')
                    total, qtdit = self.ptotal, self.qtd
                    print('Total do pedido: R$ %.2f | Total de itens: %d' % (total, qtdit))

            

window = JanelaCaixa()
window.iniciar()
sg.Window.close()