# passo 4
# copiando a biblioteca usada e criando conexoes

import sqlite3 as lite
# criando conexao com banco de dados
con = lite.connect('dados.db')

# CRUD CREATE READ UPDATE DELETE

# inserir dados
dados = ['sofa', 'sala de estar', 'vaso que comprei no mercado',
         'marca x', '27/08/2022', '500,00', 'xxxx', 'c:imagens']
with con:
    cur = con.cursor()
    query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cur.execute(query, dados)

# Atualizar dados
atualizar_dados = ['sofa', 'cozinha', 'vaso que comprei no mercado',
                   'marca x', '27/08/2022', '500,00', 'xxxx', 'c:imagens', 1]
with con:
    cur = con.cursor()
    query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
    cur.execute(query, atualizar_dados)


# Deletar dados
deletar_dados = [1]
with con:
    cur = con.cursor()
    query = "DELETE FROM inventario WHERE id=?"
    cur.execute(query, deletar_dados)


# ver dados
ver_dados = []
with con:
    cur = con.cursor()
    query = "SELECT * FROM inventario"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        ver_dados.append(row)

print(ver_dados)
