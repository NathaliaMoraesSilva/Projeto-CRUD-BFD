from db import conectar

def adicionar_tarefa(nome,descricao):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO tarefas (nome, descricao) VALUES (?, ?)", (nome, descricao))
    con.commit()
    con.close()

#  ->listar_tarefas

def listar_tarefas():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM tarefas")
    tarefas = cur.fetchall()
    con.close()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return []
    else:
        return tarefas
   
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
def editar_tarefa(nome_novo, descricao_nova, id):
    con = conectar()
    cur = con.cursor()
    cur.execute('UPDATE tarefas SET nome = ?, descricao = ? WHERE id = ?', (nome_novo, descricao_nova, id))
    con.commit()
    con.close()
