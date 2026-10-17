"""TaskTracker - Gerenciador de tarefas em linha de comando (CLI).

Bootcamp II - Fase 2 (Entrega Intermediária).
Versão do commit 3: estrutura principal (menu e loop), sem validações.
"""


# ---------------------------------------------------------------------------
# Funcionalidades
# ---------------------------------------------------------------------------
def cadastrar_tarefa(tarefas):
    """Coleta os dados e adiciona uma nova tarefa à lista."""
    print("\n--- Cadastrar nova tarefa ---")
    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()
    prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip()
    data_limite = input("Data limite (ex.: DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    """Exibe todas as tarefas ou avisa que não há registros."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"  Título      : {tarefa['titulo']}")
        print(f"  Descrição   : {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade  : {tarefa['prioridade']}")
        print(f"  Data limite : {tarefa['data_limite'] or '(não informada)'}")
        print(f"  Status      : {tarefa['status']}")


# ---------------------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------------------
def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("\nOpção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()