# DESATUALIZADO

## Sistema de Gestão de Funcionários 

## Descrição
Este projeto é um sistema para gerenciar informações sobre funcionários, projetos e alocações de funcionários em projetos, utilizando o paradigma de Programação Orientada a Objetos (POO) e integração com banco de dados **MySQL**. O sistema permite realizar as operações de cadastro, consulta e atualização de dados de funcionários, tipos de funcionários, projetos e alocações.

## Funcionalidades
- **Funcionários**: Cadastro, consulta e atualização de salários.
- **Projetos**: Cadastro e consulta de projetos.
- **Alocações**: Cadastro de alocação de funcionários em projetos com informações de carga horária e função no projeto.
- **Tipos de Funcionários**: Cadastro e consulta de diferentes tipos de funcionários (por exemplo, Gerente, Desenvolvedor).

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **MySQL**: Banco de dados para persistência de dados.
- **MySQL Workbench**: Ferramenta usada para modelagem lógica do banco de dados e criação das tabelas e da view.
- **Tabulate**: Biblioteca Python para exibição dos dados de forma tabular.

## Como Rodar o Sistema

### 1. Pré-requisitos

Certifique-se de que as seguintes ferramentas estão instaladas:

- **Python 3.x**: A linguagem de programação utilizada.
- **MySQL**: O banco de dados utilizado para persistir as informações.
- **MySQL Workbench**: Para o gerenciamento do banco de dados e visualização do modelo lógico.
- **Tabulate**: Para a formatação das consultas. Para instalar, execute:

    ```bash
    pip install tabulate
    ```

### 2. Banco de Dados

1. **Criar o Banco de Dados**: Execute o script SQL fornecido para criar o banco de dados no MySQL.

2. **População de Tabelas e View**: O banco de dados já foi populado com dados fictícios e inclui uma **view** para facilitar a consulta de alocações de funcionários. Essas etapas já foram realizadas em outro arquivo, mas devem ser executadas para garantir o funcionamento correto do sistema.

### 3. Rodando o Sistema

1. **Configurando o Banco de Dados no Código**: No arquivo principal do sistema, configure as credenciais do banco de dados:

    ```python
    banco = BancoDeDados(host="localhost", user="root", password="7002", database="gestaofuncionarios")
    ```

2. **Executando o Sistema**: Após configurar o banco de dados e as dependências, execute o script principal:

    ```bash
    python main.py
    ```

### 4. Funcionalidades do Sistema

O sistema oferece um menu interativo que permite realizar as seguintes ações:

- **Funcionários**: Cadastrar, consultar e atualizar salários dos funcionários.
- **Projetos**: Cadastrar e consultar projetos.
- **Alocações**: Cadastrar e consultar alocações de funcionários nos projetos.
- **Tipos de Funcionários**: Cadastrar e consultar os tipos de funcionários.
