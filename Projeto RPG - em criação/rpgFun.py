from random import randint
from math import sqrt
import sqlite3 as bd
 
engine = bd.connect('rpg.db')
r = engine.cursor()
ids = [x*2 + 1 for x in range(70)]

class Jogador():
    def __init__(self,nome,experiencia=23):
        self.aleatorio = randint(0,69)
        self.nome = nome
        self.id = ids[self.aleatorio]
        self.vivo = True
        self.heroi = None
        self.experiencia = experiencia


class Heroi():
    def __init__(self, nome, vida, forca, defesa, magia, agilidade):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.defesa = defesa
        self.magia = magia
        self.agilidade = agilidade


class Inimigo(Heroi):
    super.__init__



def getNomeHeroi():
    heroi = randint(1,10)
    sql = "SELECT NOME FROM HEROI WHERE ID = ?" 
    query = r.execute(sql,(heroi,))
    heroi = query.fetchone()
    return heroi[0]

def defineHeroi(jogador):
    nome = getNomeHeroi()
    sql = "SELECT VIDA, FORCA, DEFESA, MAGIA, AGILIDADE FROM HEROI WHERE NOME = ?"
    query = r.execute(sql,(nome,))
    statsHeroi = query.fetchone()
    heroi = Heroi(nome,statsHeroi[0],statsHeroi[1],statsHeroi[2],statsHeroi[3],statsHeroi[4])
    jogador.heroi = heroi

def escolheInimigo(nivel):
    ide = []
    if nivel == 1:
        for x in range(3):
            ide.append(randint(1,4)) 
        sql = "SELECT NOME, VIDA, FORCA, DEFESA, MAGIA, AGILIDADE FROM INIMIGOS WHERE ID = ?"
        query = r.execute(sql,(ide[0],))
        inimigo_temp = r.fetchone()
        query2 = r.execute(sql,(ide[1],))
        inimigo2_temp = r.fetchone()
        query3 = r.execute(sql,(ide[2],))
        inimigo3_temp = r.fetchone()
    elif nivel == 2:
        for x in range(3):
            ide.append(randint(4,7)) 
        sql = "SELECT NOME, VIDA, FORCA, DEFESA, MAGIA, AGILIDADE FROM INIMIGOS WHERE ID = ?"
        query = r.execute(sql,(ide[0],))
        inimigo_temp = r.fetchone()
        query2 = r.execute(sql,(ide[1],))
        inimigo2_temp = r.fetchone()
        query3 = r.execute(sql,(ide[2],))
        inimigo3_temp = r.fetchone()
    elif nivel == 3:
        for x in range(3):
            ide.append(randint(7,10)) 
        sql = "SELECT NOME, VIDA, FORCA, DEFESA, MAGIA, AGILIDADE FROM INIMIGOS WHERE ID = ?"
        query = r.execute(sql,(ide[0],))
        inimigo_temp = r.fetchone()
        query2 = r.execute(sql,(ide[1],))
        inimigo2_temp = r.fetchone()
        query3 = r.execute(sql,(ide[2],))
        inimigo3_temp = r.fetchone()
    else:
        for x in range(3):
            ide.append(randint(10,12)) 
        sql = "SELECT NOME, VIDA, FORCA, DEFESA, MAGIA, AGILIDADE FROM INIMIGOS WHERE ID = ?"
        query = r.execute(sql,(ide[0],))
        inimigo_temp = query.fetchone()
        query2 = r.execute(sql,(ide[1],))
        inimigo2_temp = query2.fetchone()
        query3 = r.execute(sql,(ide[2],))
        inimigo3_temp = query3.fetchone()
    inimigo = Inimigo(inimigo_temp[0],inimigo_temp[1],inimigo_temp[2],inimigo_temp[3],inimigo_temp[4],inimigo_temp[5])
    inimigo2 = Inimigo(inimigo2_temp[0],inimigo2_temp[1],inimigo2_temp[2],inimigo2_temp[3],inimigo2_temp[4],inimigo2_temp[5])
    inimigo3 = Inimigo(inimigo3_temp[0],inimigo3_temp[1],inimigo3_temp[2],inimigo3_temp[3],inimigo3_temp[4],inimigo3_temp[5])
    return inimigo, inimigo2, inimigo3

def escolheHabilidade(jogador):
        if jogador.experiencia != 0:
            pass




print("IDs: ")
print(ids)
jogador1 = Jogador("Thiago")
jogador2 = Jogador("David")
jogador3 = Jogador("Vinicius")

print("TESTE REGISTRO RPG:")
print("jogador 1:")
print("id ",jogador1.id,"nome: " ,jogador1.nome)
print("jogador 2:")
print("id ",jogador2.id,"nome: " ,jogador2.nome)
print("jogador 3:")
print("id ",jogador3.id,"nome: " ,jogador3.nome)
print('TESTE ASSOCIACAO DE HEROIS')
defineHeroi(jogador1)
defineHeroi(jogador2)
defineHeroi(jogador3)
print(f'jogador {jogador1.nome} com seu Heroi chamado {jogador1.heroi.nome}')
print(f'jogador {jogador2.nome} com seu Heroi chamado {jogador2.heroi.nome}')
print(f'jogador {jogador3.nome} com seu Heroi chamado {jogador3.heroi.nome}')
print("TESTE CLASSE HEROI")
print(f'Heroi {jogador1.heroi.nome} tem a vida {jogador1.heroi.vida} força {jogador1.heroi.forca} defesa {jogador1.heroi.defesa} magia {jogador1.heroi.magia} agilidade {jogador1.heroi.agilidade}')
print(f'Heroi {jogador2.heroi.nome} tem a vida {jogador2.heroi.vida} força {jogador2.heroi.forca} defesa {jogador2.heroi.defesa} magia {jogador2.heroi.magia} agilidade {jogador2.heroi.agilidade}')
print(f'Heroi {jogador3.heroi.nome} tem a vida {jogador3.heroi.vida} força {jogador3.heroi.forca} defesa {jogador3.heroi.defesa} magia {jogador3.heroi.magia} agilidade {jogador3.heroi.agilidade}')
print("TESTE ESCOLHA INIMIGOS")
en1,en2,en3 = escolheInimigo(1)
en4,en5,en6 = escolheInimigo(2)
en7,en8,en9 = escolheInimigo(3)
en10,en11,en12 = escolheInimigo(4)
print(f'Inimigo {en1.nome} tem a vida {en1.vida} força {en1.forca} defesa {en1.defesa} magia {en1.magia} agilidade {en1.agilidade}')
print(f'Inimigo {en2.nome} tem a vida {en2.vida} força {en2.forca} defesa {en2.defesa} magia {en2.magia} agilidade {en2.agilidade}')
print(f'Inimigo {en3.nome} tem a vida {en3.vida} força {en3.forca} defesa {en3.defesa} magia {en3.magia} agilidade {en3.agilidade}')
print(f'Inimigo {en4.nome} tem a vida {en4.vida} força {en4.forca} defesa {en4.defesa} magia {en4.magia} agilidade {en4.agilidade}')
print(f'Inimigo {en5.nome} tem a vida {en5.vida} força {en5.forca} defesa {en5.defesa} magia {en5.magia} agilidade {en5.agilidade}')
print(f'Inimigo {en6.nome} tem a vida {en6.vida} força {en6.forca} defesa {en6.defesa} magia {en6.magia} agilidade {en6.agilidade}')
print(f'Inimigo {en7.nome} tem a vida {en7.vida} força {en7.forca} defesa {en7.defesa} magia {en7.magia} agilidade {en7.agilidade}')
print(f'Inimigo {en8.nome} tem a vida {en8.vida} força {en8.forca} defesa {en8.defesa} magia {en8.magia} agilidade {en8.agilidade}')
print(f'Inimigo {en9.nome} tem a vida {en9.vida} força {en9.forca} defesa {en9.defesa} magia {en9.magia} agilidade {en9.agilidade}')
print(f'Inimigo {en10.nome} tem a vida {en10.vida} força {en10.forca} defesa {en10.defesa} magia {en10.magia} agilidade {en10.agilidade}')
print(f'Inimigo {en11.nome} tem a vida {en11.vida} força {en11.forca} defesa {en11.defesa} magia {en11.magia} agilidade {en11.agilidade}')
print(f'Inimigo {en12.nome} tem a vida {en12.vida} força {en12.forca} defesa {en12.defesa} magia {en12.magia} agilidade {en12.agilidade}')
engine.close