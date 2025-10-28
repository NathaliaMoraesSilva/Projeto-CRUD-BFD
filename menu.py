import queries as q

class Tarefa():
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao


def exibir_menu():
    print('\n--- TaskCRUD - Gerenciador de Tarefas ---')
    print('1. Nova tarefa (CREATE - C)')
    print('2. Apresentar tarefas existentes (READ - R)')
    print('3. Atualizar uma tarefa (UPDATE - U)')
    print('4. Deletar uma tarefa (DELETE -D)')
    print('5 Buscar Tarefa por ID (READ - R)')
    print('6. Sair')
    print('-----------------------------------------')

def nova_tarefa():
    nome = input("Digite o nome da Tarefa: ")
    descricao = input("Digite a descrição da sua tarefa: ")

    if not nome or not descricao:
        print("Nome ou descrição vazia!")
        return
    
    q.adicionar_tarefa(Tarefa(nome, descricao))
    print("Tarefa adicionada com sucesso!")

def apresentar_tarefas():
    tarefas = q.listar_tarefas()
    if tarefas:
        for tarefa in tarefas:
            print(f"ID: {tarefa[0]} - Nome: {tarefa[1]} - Descrição: {tarefa[2]}")  # Usando índices
    else:
        print("Nenhuma tarefa encontrada.")

def atualizar_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja atualizar: "))
    novo_nome = input("Digite o novo nome da tarefa: ")
    nova_descricao = input("Digite a nova descrição da tarefa: ")
    
    if not novo_nome or not nova_descricao:
        print("Nome ou descrição vazia!")
        return
    
    q.editar_tarefa(novo_nome, nova_descricao, id_tarefa)

def deletar_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja deletar: "))
    confirmar = input(f"Você tem certeza que deseja excluir a tarefa {id_tarefa}? (s/n): ").lower()
    
    if confirmar == 's':
        q.remover_tarefa(id_tarefa)
    else:
        print("Operação cancelada.")

def buscar_tarefa_id():
    id_tarefa = int(input("Digite o ID da tarefa: "))
    tarefa = q.buscar_tarefa(id_tarefa)
    
    if tarefa is None:
        print("Tarefa nao existe!")
    else:
        print(f"ID: {tarefa[0]} - Nome: {tarefa[1]} - Descrição: {tarefa[2]}")