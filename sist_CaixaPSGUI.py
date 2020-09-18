import PySimpleGUI as sg


class JanelaCaixa():
    def __init__(self):
        self.ptotal = 0.0
        self.qtd = 0
        self.produtos = {'tomate': 0.77, 'laranja pera': 0.67, 'maça': 1.66, 'banana prata': 1.16,
 'banana nanica': 1.01, 'manga palmer': 3.0, 'mamao papaia': 4.0, 'mamao formosa': 10.0,
  'mexerica': 0.67, 'cenoura': 0.84, 'chuchu': 2.5, 'abacate': 2.0, 'berinjela': 2.0, 
  'alface': 2.75, 'batata': 1.4, 'leite': 3.5, 'arroz 1kg': 3.8, 'cebola': 0.53, 
  'queijo fresco kg': 28.6}
  
        layout = [[sg.Text('Nome do item:'),sg.InputText(key='K'),sg.Text('Quantidade:'), sg.Input(key='qtd')],
                [sg.Output(size=(150,30),background_color='lightgray'), sg.Button('Adicionar Item')],
                [sg.Text('Fechar sistema?'), sg.Button('Sim',key='S')]]

        self.janela = sg.Window('Caixa 01', layout)

    def imprime_msg(self):
        if KeyError:
            print('Item fora da lista, sinto muito.')
            print('Insira outro item, por favor')
        elif TypeError:
            print('Por favor, insira um item válido.')
        else:
            print('Item adicionado com sucesso')
            print('Total do pedido: R$ %.2f | Total de itens: %d' % (self.ptotal, self.qtd))

    def adicionar_item(self):
            try:
                if self.valores['K'] in self.produtos:
                    self.ptotal += self.produtos[self.valores['K']] * int(self.valores['qtd'])
                if self.valores['K'] not in self.produtos:
                    raise KeyError
            except KeyError:
                self.imprime_msg()
            except TypeError:
                self.imprime_msg()
            else:
                self.qtd += int(self.valores['qtd'])
                self.imprime_msg()

    def iniciar(self):
        while True:
            self.evento, self.valores = self.janela.Read()
            if self.evento == sg.WIN_CLOSED or self.evento == 'S':
                break
            if self.evento == 'Adicionar Item':
                self.adicionar_item()


window = JanelaCaixa()
window.iniciar()
self.janela.close()