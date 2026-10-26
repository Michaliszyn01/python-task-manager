"""Small terminal task manager. Tasks intentionally remain in memory."""
from __future__ import annotations


def list_tasks(tasks: list[str], output=print) -> None:
    if not tasks:
        output("Ainda não há tarefas.")
        return
    for number, task in enumerate(tasks, 1):
        output(f"{number}. {task}")


def main(read=input, output=print) -> None:
    tasks: list[str] = []
    output("Gerenciador de tarefas")
    while True:
        try:
            option = read("1 Adicionar | 2 Listar | 3 Remover | 4 Sair: ").strip()
        except (EOFError, KeyboardInterrupt):
            output("\nAté mais!")
            return
        if option == "4":
            output("Até mais!")
            return
        if option == "1":
            try:
                task = read("Qual tarefa deseja adicionar? ").strip()
            except (EOFError, KeyboardInterrupt):
                output("\nAté mais!")
                return
            if task:
                tasks.append(task)
                output("Tarefa adicionada.")
            else:
                output("A tarefa não pode ficar vazia.")
        elif option == "2":
            list_tasks(tasks, output)
        elif option == "3":
            if not tasks:
                output("Ainda não há tarefas para remover.")
                continue
            list_tasks(tasks, output)
            try:
                index = int(read("Número da tarefa para remover: ")) - 1
            except ValueError:
                output("Informe um número válido.")
                continue
            except (EOFError, KeyboardInterrupt):
                output("\nAté mais!")
                return
            if 0 <= index < len(tasks):
                output(f"Tarefa removida: {tasks.pop(index)}")
            else:
                output("Número fora da lista.")
        else:
            output("Escolha uma opção entre 1 e 4.")


if __name__ == "__main__":
    main()
