# Projeto Django de Lista de Tarefas (Todo List)

Este é um projeto Django simples de Lista de Tarefas, onde você pode adicionar, listar e gerenciar tarefas. Ele consiste em duas páginas da web: "list_todos.html" e "register_todos.html". Abaixo, você encontrará instruções sobre como clonar e executar o projeto.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados em seu sistema:

- Python (versão 3.6 ou superior)
- Django (versão 3.0 ou superior)

## Clonando o Projeto

Para clonar o projeto em seu sistema local, execute o seguinte comando no terminal:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

Substitua `seu-usuario` pelo seu nome de usuário do GitHub e `nome-do-repositorio` pelo nome do seu repositório.

## Executando o Projeto

Siga estas etapas para executar o projeto:

1. Navegue até a pasta do projeto:

    ```bash
    cd nome-do-repositorio
    ```

2. Instale as dependências do projeto: Django

3. Aplique as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

4. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

5. Abra um navegador da web e acesse [http://localhost:8000/todos](http://localhost:8000/todos) para ver o projeto em execução.

## Contribuição

Sinta-se à vontade para contribuir, abrir problemas (issues) ou enviar pull requests para melhorar este projeto. Este projeto é uma ótima maneira de aprender e praticar Django.
