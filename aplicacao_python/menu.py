from funcoes_interface import Funcoes
import time
import sys
import pyfiglet

class Menu:
    # Método Construtor recebendo o banco
    def __init__(self, banco):
        self.funcoes = Funcoes(banco)

    def animacao_menu_principal(self, titulo):
        grande_titulo = pyfiglet.figlet_format(titulo, font="standard", width=70)
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
        self.animacao_menu_principal("MENU PRINCIPAL")

        while True:
            print("="*60)
            print("1. Funcionários")
            print("2. Projetos")
            print("3. Alocações")
            print("4. Cargos")
            print("5. Consulta Geral")
            print("0. Sair")
            print("="*60)
            # Escolha do usuário
            escolha = input("Escolha uma opção: ").strip()
            print("="*60)

            # Método é chamado com base na escolha
            if escolha == '1':
                self.exibir_menu_funcionarios()
            elif escolha == '2':
                self.exibir_menu_projetos()
            elif escolha == '3':
                self.exibir_menu_alocacoes()
            elif escolha == '4':
                self.exibir_menu_cargos()
            elif escolha == '5':
                self.animacao_menu("Consulta Geral")
                self.funcoes.consulta_geral()
                self.animacao_menu_principal("MENU PRINCIPAL")
            elif escolha == '0':
                print("\nSaindo do sistema...")
                time.sleep(2)
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")

    def exibir_menu_funcionarios(self):
        while True:
            self.animacao_menu("Funcionarios")
            print("="*60)
            print("1. Cadastrar Funcionário")
            print("2. Remover Funcionário")
            print("3. Consultar Funcionários")
            print("4. Atualizar Salário")
            print("5. Atualizar Cargo")
            print("0. Voltar")
            print("="*60)
            escolha = input("Escolha uma opção: ").strip()
            print("="*60)

            if escolha == '1':
                self.funcoes.cadastrar_funcionario()
            elif escolha == '2':
                self.funcoes.remover_funcionario()
            elif escolha == '3':
                self.funcoes.consultar_funcionarios()
            elif escolha == '4':
                self.funcoes.atualizar_salario()
            elif escolha == '5':
                self.funcoes.atualizar_cargo()
            elif escolha == '0':
                self.animacao_menu_principal("GESTAO DE FUNCIONARIOS")
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")

    def exibir_menu_projetos(self):
        while True:
            self.animacao_menu("Projetos")
            print("")
            print("="*60)
            print("1. Criar Projeto")
            print("2. Remover Projeto")
            print("3. Consultar Projetos")
            print("0. Voltar")
            print("="*60)
            escolha = input("Escolha uma opção: ").strip()
            print("="*60)

            if escolha == '1':
                self.funcoes.cadastrar_projeto()
            elif escolha == '2':
                self.funcoes.remover_projeto()
            elif escolha == '3':
                self.funcoes.consultar_projetos()
            elif escolha == '0':
                self.animacao_menu_principal("GESTAO DE FUNCIONARIOS")
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")

    def exibir_menu_alocacoes(self):
        while True:
            self.animacao_menu("Alocacoes")
            print("="*60)
            print("1. Criar Alocação")
            print("2. Remover Alocação")
            print("2. Consultar Alocações")
            print("0. Voltar")
            print("="*60)
            escolha = input("Escolha uma opção: ").strip()
            print("="*60)

            if escolha == '1':
                self.funcoes.cadastrar_alocacao()
            elif escolha == '2':
                self.funcoes.remover_alocacao()
            elif escolha == '3':
                self.funcoes.consultar_alocacoes()
            elif escolha == '0':
                self.animacao_menu_principal("GESTAO DE FUNCIONARIOS")
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")

    def exibir_menu_cargos(self):
        while True:
            self.animacao_menu("Cargos")
            print("")
            print("="*60)
            print("1. Criar Cargo")
            print("2. Remover Cargo")
            print("3. Consultar Cargos")
            print("0. Voltar")
            print("="*60)
            escolha = input("Escolha uma opção: ").strip()
            print("="*60)

            if escolha == '1':
                self.funcoes.cadastrar_cargo()
            elif escolha == '2':
                self.funcoes.remover_cargo()
            elif escolha == '3':
                self.funcoes.consultar_cargos()
            elif escolha == '0':
                self.animacao_menu_principal("GESTAO DE FUNCIONARIOS")
                break
            else:
                print("\n[!] OPÇÃO INVÁLIDA. Tente novamente.\n")
