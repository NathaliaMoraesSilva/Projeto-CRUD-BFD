from db import conectar

def adicionar_tarefa(nome,descricao):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO tarefas (nome, descricao) VALUES (?, ?)", (nome, descricao))
    con.commit()
    con.close()

# -> Listar




# -> Remover







# -> Editar
def editar_tarefa(nome_novo, descricao_nova, id):
    con = conectar()
    cur = con.cursor()
    cur.execute('UPDATE tarefas SET nome = ?, descricao = ? WHERE id = ?', (nome_novo, descricao_nova, id))
    con.commit()
    con.close()
