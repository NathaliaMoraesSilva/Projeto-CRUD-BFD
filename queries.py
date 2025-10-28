from db import conectar


def adicionar_tarefa(tarefa):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO tarefas (nome, descricao) VALUES (?, ?)", (tarefa.nome, tarefa.descricao))
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
        return []
    else:
        return tarefas
   
# -> Remover
def remover_tarefa(id_tarefa):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM tarefas WHERE id = ?", (id_tarefa,))
    tarefa = cur.fetchone()

    if tarefa:
        cur.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
        con.commit()
        print(f"Tarefa {id_tarefa} deletada com sucesso!")
    else:
        print(f"Tarefa com ID {id_tarefa} não encontrada!")

    con.close()

# -> Buscar id
def buscar_tarefa(id_tarefa):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, nome, descricao FROM tarefas WHERE id = ?", (id_tarefa,))
    tarefa = cur.fetchone()  
    con.close()

    return tarefa
    
# -> Editar
def editar_tarefa(nome_novo, descricao_nova, id):
    con = conectar()
    cur = con.cursor()
    cur.execute('UPDATE tarefas SET nome = ?, descricao = ? WHERE id = ?', (nome_novo, descricao_nova, id))
    con.commit()
    con.close()
