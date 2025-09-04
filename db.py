import sqlite3

DB_NAME = "tarefa.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT
    )
    """)

    con.commit()
    con.close()