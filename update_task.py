def update_task(task_id: int = 0, new_name: str = '', task_list: list = []) -> None:
    if new_name.isspace():
        print('O nome da tarefa não pode ser vazio')
        return

    if task_id == 0:
        print('Id da tarefa não definido')
        return
    
    if task_list == []:
        print('Lista de tarefas vazia')
        return

    for task in task_list:
        if task["id"] == task_id:
            print(f'A tarefa de nome {task["name"]} foi atualizada para "{new_name}"')
            task["name"] = new_name
            return
    print('Task não encontrada')