# TaskTracker

Aplicação de gerenciamento de tarefas em linha de comando (CLI), desenvolvida em Python 3 como parte do **Bootcamp II** (Fase 2 – Entrega Intermediária).

## Descrição funcional

O TaskTracker permite cadastrar tarefas e visualizá-las no terminal por meio de um menu contínuo:

1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação

Cada tarefa possui:

| Campo | Regra |
|---|---|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas. |
| Descrição | Texto livre. |
| Prioridade | Apenas `Alta`, `Média` (ou `Media`) e `Baixa`. |
| Data limite | Formato livre ou `DD/MM/AAAA`. |
| Status | Definido automaticamente como `Pendente`. |

Se não houver tarefas, a listagem informa que não existem registros no momento.

## Tecnologias utilizadas

- Python 3
- Git e GitHub (versionamento)

## Instalação e execução

Pré-requisito: Python 3 instalado.

```bash
git clone https://github.com/caioengsoftware/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

> Em alguns sistemas, use `python3 src/main.py` ou `py src/main.py`.

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Observações

Os dados ficam apenas em memória: ao encerrar a aplicação, as tarefas são perdidas.