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
## Execução com Docker (Fase 3)

### Pré-requisitos

- Docker instalado e em execução

### Como construir a imagem

```bash
docker build -t tasktracker-app .
```

### Como rodar o container em modo isolado

```bash
docker run -it tasktracker-app
```

A flag `-it` mantém o terminal interativo, necessário porque a CLI usa `input()`.

### Como rodar via orquestração (Recomendado)

```bash
docker compose run --rm tasktracker-app
```

O `docker-compose.yml` configura `stdin_open: true` e `tty: true`, que mantêm a entrada de dados aberta e alocam um terminal virtual para o menu interativo.

### Decisões técnicas

- `python:3.11-slim`: imagem base leve.
- `PYTHONUNBUFFERED=1`: saída exibida imediatamente no terminal.
- `docker-compose.yml`: orquestra a execução interativa da CLI.