from funcoes_interface import Funcoes
import time
import sys
import pyfiglet

class Menu:
    # Método Construtor recebendo o banco
    def __init__(self, banco):
        self.funcoes = Funcoes(banco)

    def animacao_menu_principal(self, titulo):
        grande_titulo = pyfiglet.figlet_format(titulo, font="standard")
        for letra in grande_titulo:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(0.001)

    def animacao_menu(self, titulo):
        titulo_menu = pyfiglet.figlet_format(titulo, font="standard", width=100)
        for letra in titulo_menu:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(0.001)

    # MENUS
    def exibir_menu_principal(self):
        self.animacao_menu_principal("GESTAO DE FUNCIONARIOS")

        while True:
            print("="*30)
            print("1. Funcionários")
            print("2. Projetos")
            print("3. Alocações")
            print("4. Tipos")
            print("0. Sair")
            print("="*30)
            # Escolha do usuário
            escolha = input("Escolha uma opção: ").strip()

            # Método é chamado com base na escolha
            if escolha == '1':
                self.exibir_menu_funcionarios()
            elif escolha == '2':
                self.exibir_menu_projetos()
            elif escolha == '3':
                self.exibir_menu_alocacoes()
            elif escolha == '4':
                self.exibir_menu_tipos()
            elif escolha == '0':
                print("\nSaindo do sistema...")
                break
            else:
                print("\n[!] Opção inválida, tente novamente.\n")

    def exibir_menu_funcionarios(self):
        while True:
            self.animacao_menu("FUNCIONARIOS")
            print("="*30)
            print("1. Cadastrar Funcionário")
            print("2. Consultar Funcionários")
            print("3. Atualizar Salário")
            print("0. Voltar")
            print("="*30)
            escolha = input("Escolha uma opção: ").strip()
            print("="*30)

            if escolha == '1':
                self.funcoes.cadastrar_funcionario()
            elif escolha == '2':
                self.funcoes.consultar_funcionarios()
            elif escolha == '3':
                self.funcoes.atualizar_salario()
            elif escolha == '0':
                self.animacao_menu_principal("GESTAO DE FUNCIONARIOS")
                break
            else:
                print("\n[!] Opção inválida, tente novamente.\n")

    def exibir_menu_projetos(self):
        while True:
            print("="*30)
            self.animacao_menu("PROJETOS")
            print("1. Criar Projeto")
            print("2. Consultar Projetos")
            print("0. Voltar")
            print("="*30)
            escolha = input("Escolha uma opção: ").strip()
            print("="*30)

            if escolha == '1':
                self.funcoes.cadastrar_projeto()
            elif escolha == '2':
                self.funcoes.consultar_projetos()
            elif escolha == '0':
                self.animacao_menu_principal("GESTAO DE FUNCIONARIOS")
                break
            else:
                print("\n[!] Opção inválida, tente novamente.\n")

    def exibir_menu_alocacoes(self):
        while True:
            self.animacao_menu("ALOCACOES")
            print("="*30)
            print("1. Criar Alocação")
            print("2. Consultar Alocações")
            print("0. Voltar")
            print("="*30)
            escolha = input("Escolha uma opção: ").strip()
            print("="*30)

            if escolha == '1':
                self.funcoes.cadastrar_alocacao()
            elif escolha == '2':
                self.funcoes.consultar_alocacoes()
            elif escolha == '0':
                self.animacao_menu_principal("GESTAO DE FUNCIONARIOS")
                break
            else:
                print("\n[!] Opção inválida, tente novamente.\n")

    def exibir_menu_tipos(self):
        while True:
            self.animacao_menu("TIPOS")
            print("="*30)
            print("1. Criar Tipo")
            print("2. Consultar Tipos")
            print("0. Voltar")
            print("="*30)
            escolha = input("Escolha uma opção: ").strip()
            print("="*30)

            if escolha == '1':
                self.funcoes.cadastrar_tipo()
            elif escolha == '2':
                self.funcoes.consultar_tipos()
            elif escolha == '0':
                self.animacao_menu_principal("GESTAO DE FUNCIONARIOS")
                break
            else:
                print("\n[!] Opção inválida, tente novamente.\n")
