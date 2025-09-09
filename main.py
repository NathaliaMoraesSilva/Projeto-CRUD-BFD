from menu import exibir_menu, nova_tarefa, apresentar_tarefas, atualizar_tarefa, deletar_tarefa, buscar_tarefa_id
from db import criar_tabela

criar_tabela()

continua = True
while (continua):
    exibir_menu()
    escolha = int(input("Escolha a sua opção: "))

    match escolha:
        case 1:
            nova_tarefa()
        case 2:
            apresentar_tarefas()
        case 3:
            atualizar_tarefa()
        case 4:
            deletar_tarefa()
        case 5:
            buscar_tarefa_id()
        case 6:
            continua = False
            break
        case _:
            print("Opção não existe")