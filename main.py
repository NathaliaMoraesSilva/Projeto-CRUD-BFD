def update_task(task_id: int, new_name: str, task_list: list) -> None:


    for task in task_list:
        if task["id"] == task_id:
            print(f'A tarefa de nome {task["name"]} foi atualizada para "{new_name}"')
            task["name"] = new_name
            return
    print('Task não encontrada')
    

