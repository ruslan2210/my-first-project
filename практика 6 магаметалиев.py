tasks_id = []
tasks_title = []
tasks_desc = []
tasks_status = []

while True:
    print("\n1. Добавить задачу")
    print("2. Посмотреть задачи")
    print("3. Удалить задачу")
    print("4. Выход")
    
    choice = input("Выберите пункт: ")
    
    if choice == "1":
        t_id = len(tasks_id) + 1
        t_title = input("Введите название: ")
        t_desc = input("Введите описание: ")
        
        tasks_id.append(t_id)
        tasks_title.append(t_title)
        tasks_desc.append(t_desc)
        tasks_status.append("новая")
        print("Задача добавлена")
        
    elif choice == "2":
        if len(tasks_id) == 0:
            print("пусто")
        else:
            for i in range(len(tasks_id)):
                print("\nID:", tasks_id[i])
                print("Название:", tasks_title[i])
                print("Описание:", tasks_desc[i])
                print("Статус:", tasks_status[i])
                
    elif choice == "3":
        del_id = int(input("Введите ID задачи: "))
        if del_id in tasks_id:
            index = tasks_id.index(del_id)
            tasks_id.pop(index)
            tasks_title.pop(index)
            tasks_desc.pop(index)
            tasks_status.pop(index)
            print("Удалено")
        else:
            print("Такой задачи нет")
            
    elif choice == "4":
        break
    else:
        print("Ошибка")