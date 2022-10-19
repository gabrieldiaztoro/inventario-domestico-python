# passo 4
# copiando a biblioteca usada e criando conexoes

from re import I
import sqlite3 as lite
# criando conexao com banco de dados
con = lite.connect('dados.db')

# CRUD CREATE READ UPDATE DELETE

# inserir dados

def inserir_form(i):         
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

# Atualizar dados
def atualizar_form(i):

    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


# Deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query, i)


# ver dados
def ver_form(i):
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados            

# ver dados individual
def ver_item(id):
    ver_dados_individualmente = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individualmente.append(row)

#Criando novo arquivo view, indo para o frontend
