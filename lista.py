if len(tarefas) == 0:
    print("Nenhuma tarefa cadastrada.")
else:
    print("--- Lista de Tarefas ---")
    for i in range(len(tarefas)):
        print(f"{i+1}. {tarefas[i]}")