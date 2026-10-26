tarefas = []

while (True):
    print("olá esse é o gerenciador de tarefas")
    opções = int(input("os gerenciador tem tres opções: 1, 2, 3, 4:"))

    if opções == 4:
        break
    elif opções == 1:
        tarefas.append((input("Quais são as tarefas de hj?")))
        print(tarefas)
    elif opções == 2:
        if not tarefas:
            print("Ainda não tem nenhuma tarefa salva")
        else:
            for numero, tarefa in enumerate(tarefas, start=1):
                print(f"{numero}. {tarefa}")
    elif opções == 3:
        remover = input("você deseja tirar alguma tarefa?")
        if remover == "sim":
            if not tarefas:
                print("você ainda não tem nenhuma tarefa") 
            else:
               for numero, tarefa in enumerate(tarefas, start=1):
                    print(f"{numero}. {tarefa}")
            numero_remover = int(input("Digite o número da tarefa que deseja remover: "))
            tarefas.pop(numero_remover - 1)                              
    else:
        print(opções) 