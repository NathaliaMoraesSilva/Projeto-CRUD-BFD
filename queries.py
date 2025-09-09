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
def atualizar_tarefa(nome,descricao):
    con = conectar()
    cur = con.cursor()
    cur.execute()
    con.commit()
    con.close()
