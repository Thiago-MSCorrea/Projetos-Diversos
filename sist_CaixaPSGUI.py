import PySimpleGUI as sg
import json 

with open("Produtos.json",'r') as produtosJson:
    produtos = json.load(produtosJson)

class JanelaCaixa():
    def __init__(self):
        self.ptotal = 0.0
        self.qtd = 0   
        layout = [[sg.Text('Nome do item:'),sg.InputText(key='Ent'),sg.Text('Quantidade:'), sg.Input(key='qtd')],
                [sg.Output(size=(150,30),background_color='lightgray'), sg.Button('Adicionar Item')],
                [sg.Text('Fechar sistema?'), sg.Button('Sim',key='S')]]

        self.janela = sg.Window('Caixa 01', layout)

    def imprime_erro1(self):
        print('Item fora da lista.')
        print('Por favor insira outro item')

    def imprime_erro2(self):
        print('Tipo inválido inserido.')
        print('Por favor insira um item válido.')

    def imprime_msg(self):
        print('Item adicionado com sucesso')
        print('Total do pedido: R$ %.2f | Total de itens: %d' % (self.ptotal, self.qtd))

    def adicionar_item(self,valores):
        try:
            if valores['Ent'] in produtos:
                self.ptotal += produtos[valores['Ent']] * int(valores['qtd'])
            if valores['Ent'] not in produtos:
                raise KeyError
        except KeyError:
            self.imprime_erro1()
        except TypeError:
            self.imprime_erro2()
        else:
            self.qtd += int(valores['qtd'])
            self.imprime_msg()

    def iniciar(self):
        while True:
            self.evento, self.valores = self.janela.Read()
            if self.evento == sg.WIN_CLOSED or self.evento == 'S':
                break
            if self.evento == 'Adicionar Item':
                self.adicionar_item(self.valores)


window = JanelaCaixa()
window.iniciar()
sg.Window.close()
