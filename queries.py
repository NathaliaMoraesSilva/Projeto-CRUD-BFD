from db import conectar

def adicionar_tarefa(nome,descricao):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO tarefas (nome, descricao) VALUES (?, ?)", (nome, descricao))
    con.commit()
    con.close()

# -> Listar




# -> Remover
def remover_tarefa(id_tarefa):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    con.commit()
    con.close()

# -> Buscar id
def buscar_tarefa(id_tarefa):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, nome, descricao FROM tarefas WHERE id = ?", (id_tarefa,))
    con.commit()
    con.close()
    if id_tarefa is not None:
        return id_tarefa
    else:
        return None


# -> Editar



