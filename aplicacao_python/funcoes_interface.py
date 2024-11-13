import time
from alocacao import Alocacao
from funcionario import Funcionario
from projeto import Projeto
from tipo import Tipo

class Funcoes:
    def __init__(self, banco):
        self.banco = banco


#FUNÇÕES DE CADASTRO

    def cadastrar_tipo(self):
        descricao = input("\nDigite o tipo: ")
        informacao_adicional = input(f"Informaçoes adicionais do tipo {descricao}: ")
        tipo = Tipo(descricao, informacao_adicional)
        self.banco.cadastrar_tipo(tipo)


    def cadastrar_funcionario(self):
        nome = input("\nDigite o nome do funcionário: ")
        
        #Validação para o CPF
        while True:
            cpf = input("Digite o CPF do funcionário (11 números): ")
            #Verifica se o CPF contém 11 dígitos e é numérico
            if not (cpf.isdigit() and len(cpf) == 11):
                print("CPF INVÁLIDO! Tente novamente.")
            #Verifica se o CPF já existe no banco de dados
            elif self.banco.consultar_funcionario_por_cpf(cpf):
                print("Erro: CPF já cadastrado no sistema. Tente outro CPF.")
            else:
                break  #CPF válido e único encontrado

        #Validação para o salário
        while True:
            try:
                salario = float(input("Digite o salário do funcionário: "))

                if salario <= 0:
                    print("\nErro! Salário deve ser maior que 0.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número para o salário.")

        idtipo = self.validar_idtipo()

        funcionario = Funcionario(nome, cpf, salario, idtipo)
        self.banco.cadastrar_funcionario(funcionario)


    def cadastrar_projeto(self):
        nome = input("\nDigite o nome do projeto: ")
        descricao = input("Digite a descrição do projeto: ")
        projeto = Projeto(nome, descricao)
        self.banco.cadastrar_projeto(projeto)


    def cadastrar_alocacao(self):
        print("\n=== Funcionários ===")
        print("Consultando Funcionários...")
        time.sleep(1)
        self.banco.consultar_funcionarios()
        
        #Validação para o ID do funcionário
        while True:
            try:
                idfuncionario = int(input("\nDigite o ID do funcionário a ser alocado: "))
                break 
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para o ID do funcionário.")

        print("\n=== Projetos ===")
        print("Consultando projetos...")
        time.sleep(1)
        self.banco.consultar_projetos()
        
        #Validação para o ID do projeto
        while True:
            try:
                idprojeto = int(input("\nDigite o ID do projeto que será trabalhado: "))
                break  
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para o ID do projeto.")

        #Validação para carga horária
        while True:
            try:
                carga_horaria = int(input("\nDigite a carga horária (Hrs): "))
                break 
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a carga horária.")

        papel_funcionario = input("Digite a função do funcionário no projeto: ")

        alocacao = Alocacao(carga_horaria, papel_funcionario, idprojeto, idfuncionario)
        self.banco.cadastrar_alocacao(alocacao)


#FUNÇÕES DE CONSULTA

    def consultar_tipos(self):
        print("\nConsultando tipos...")
        time.sleep(1)
        self.banco.consultar_tipos()


    def consultar_funcionarios(self):
        print("\nConsultando funcionários...")
        time.sleep(1)
        self.banco.consultar_funcionarios()


    def consultar_projetos(self):
        print("\nConsultando projetos...")
        time.sleep(1)
        self.banco.consultar_projetos()


    def consultar_alocacoes(self):
        print("\nConsultando alocações...")
        time.sleep(1)
        self.banco.consultar_alocacoes()


#FUNÇOES ADICIONAIS

    def validar_idtipo(self): #Função responsável por validar o ID escolhido
        while True:
            try:
                print("\n==== Tipos de Funcionários ====")
                self.banco.consultar_tipos()
                print("Escolha um dos tipos acima:")
                idtipo = int(input("\nDigite o ID do tipo de funcionário: "))

                if not self.banco.consultar_tipo_id(idtipo):
                    print(f"Erro: Não existe um tipo com o ID {idtipo}. Tente novamente.")
                else:
                    return idtipo
            except ValueError:
                print("Por favor, insira um número válido para o ID.")


    def atualizar_salario(self): #Função de interface responsável por realizar a atualização do salário do usuario
        print("\n==== Atualizar Salário  ====")
        time.sleep(1)
        funcionarios = self.banco.consultar_funcionarios()
        
        while True:
            try:
                ids_funcionarios = [funcionario[0] for funcionario in funcionarios]

                idfuncionario = int(input("\nEscolha um Funcionario(ID): "))

                if idfuncionario <= 0:
                    print("Insira um ID maior do que 0.")
                    continue
                elif idfuncionario not in ids_funcionarios:
                    print("ID nao presente no banco de dados.")
                    continue
                break
            except ValueError:
                print("Por favor, insira um número válido para o ID do funcionário.")

        print("\n==== Funcionário Escolhido ====")
        self.banco.consultar_funcionario_id(idfuncionario)

        while True:
            try:
                novo_salario = float(input(f"\nNovo salário do funcionário (ID {idfuncionario}): "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número para o novo salário.")
        
        self.banco.atualizar_salario(novo_salario, idfuncionario)
