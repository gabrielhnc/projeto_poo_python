from funcoes_interface import Funcoes

class Menu:
    #Metodo Construtor recebendo o banco
    def __init__(self, banco):
        self.funcoes = Funcoes(banco)

    #MENUS
    def exibir_menu_principal(self):
        while True:
            print('''
==== GESTÃO FUNCIONÁRIOS ====
1. Funcionários
2. Projetos
3. Alocações
4. Tipos
0. Sair
''')
            #Escolha do usuário
            escolha = input("Escolha uma opção: ")

            #Método é chamado com base na escolha
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
                print("Opção inválida, tente novamente.")

    def exibir_menu_funcionarios(self):
        while True:
            print('''
==== SUB MENU FUNCIONÁRIOS ====
1. Cadastrar Funcionário
2. Consultar Funcionários
3. Atualizar Salário
0. Voltar
''')
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.funcoes.cadastrar_funcionario()
            elif escolha == '2':
                self.funcoes.consultar_funcionarios()
            elif escolha == '3':
                self.funcoes.atualizar_salario()
            elif escolha == '0':
                break
            else:
                print("Opção inválida, tente novamente.")

    def exibir_menu_projetos(self):
        while True:
            print('''
==== SUB MENU PROJETOS ====
1. Criar Projeto
2. Consultar Projetos
0. Voltar
''')
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.funcoes.cadastrar_projeto()
            elif escolha == '2':
                self.funcoes.consultar_projetos()
            elif escolha == '0':
                break
            else:
                print("Opção inválida, tente novamente.")

    def exibir_menu_alocacoes(self):
        while True:
            print('''
==== SUB MENU ALOCAÇÕES ====
1. Criar Alocação
2. Consultar Alocações
0. Voltar
''')
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.funcoes.cadastrar_alocacao()
            elif escolha == '2':
                self.funcoes.consultar_alocacoes()
            elif escolha == '0':
                break
            else:
                print("Opção inválida, tente novamente.")

    def exibir_menu_tipos(self):
        while True:
            print('''
==== SUB MENU TIPOS ====
1. Criar Tipo
2. Consultar Tipos
0. Voltar
''')
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.funcoes.cadastrar_tipo()
            elif escolha == '2':
                self.funcoes.consultar_tipos()
            elif escolha == '0':
                break
            else:
                print("Opção inválida, tente novamente.")
