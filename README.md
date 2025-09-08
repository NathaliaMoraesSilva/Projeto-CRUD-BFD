
# Projeto-CRUD-BFD

# 📝 Sistema de Tarefas

Um sistema simples de gerenciamento de tarefas onde os usuários podem:
- Criar novas tarefas ✅
- Definir datas para conclusão 📅
- Marcar como concluídas 🟢
- Excluir tarefas ❌

## 🚀 Funcionalidades
- Cadastro de tarefas com título e data
- Listagem de todas as tarefas
- Atualização do status (pendente/concluída)
- Exclusão de tarefas

## 🛠️ Tecnologias utilizadas
- **Python** (lógica do sistema)
- **MySQL** (banco de dados para armazenar as tarefas)

## 📂 Estrutura do Projeto
1. Clone este repositório:
   bash
    git clone https://github.com/NathaliaMoraesSilva/Projeto-CRUD-BFD.git


2. Acesse a pasta do projeto:
    cd Projeto-CRUD-BFD
3. Configure o banco de dados MySQL:
    
    CREATE DATABASE tarefas;
    USE tarefas;

    CREATE TABLE tarefa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    data DATE,
    status BOOLEAN DEFAULT FALSE
);
