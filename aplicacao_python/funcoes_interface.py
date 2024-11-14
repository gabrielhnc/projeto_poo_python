import time
from tabulate import tabulate
from alocacao import Alocacao
from funcionario import Funcionario
from projeto import Projeto
from cargo import Cargo

class Funcoes:
    def __init__(self, banco):
        self.banco = banco


#FUNÇÕES DE CADASTRO

    def cadastrar_cargo(self):
        while True:
            descricao = input("\nDigite o cargo [0 para cancelar]: ").strip()
            if descricao == '0':
                print("Cadastro cancelado.")
                return
            elif not descricao:
                print("Erro: A descrição do cargo não pode estar vazia. Tente novamente.")
                continue
            
            informacao_adicional = input(f"Informaçoes adicionais do cargo '{descricao}' [0 para cancelar]: ").strip()
            if informacao_adicional == '0':
                print("Cadastro cancelado.")
                return
            elif not informacao_adicional:
                print("Erro: As informações adicionais não podem estar vazias. Tente novamente.")
                continue
            
            cargo = Cargo(descricao, informacao_adicional)
            self.banco.cadastrar_cargo(cargo)
            break


    def cadastrar_funcionario(self):
        while True:
            nome = input("\nDigite o nome do funcionário [0 para cancelar]: ").strip()

            if nome == '0':
                print("Cadastro cancelado.")
                return
            elif not nome:
                print("Erro: O nome do funcionário não pode estar vazio. Tente novamente.")
                continue

            #Validação para o CPF
            while True:
                cpf = input("Digite o CPF (11 números) do funcionário [0 para cancelar]: ").strip()

                if cpf == '0':
                    print("Cadastro cancelado.")
                    return
                elif not (cpf.isdigit() and len(cpf) == 11):
                    print("Erro: Tente novamente com 11 números.")
                elif self.banco.consultar_funcionario_por_cpf(cpf):
                    print("Erro: CPF já cadastrado no sistema. Tente outro CPF.")
                else:
                    break

            #Validação para o salário
            while True:
                try:
                    salario = float(input("Digite o salário do funcionário [0 para cancelar]: ").strip())

                    if salario == '0':
                        print("Cadastro cancelado.")
                        return
                    elif salario < 0:
                        print("Erro: Salário deve ser maior que 0.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para o salário.")

            idcargo = self.validacao_idcargo()
            funcionario = Funcionario(nome, cpf, salario, idcargo)
            self.banco.cadastrar_funcionario(funcionario)
            break


    def cadastrar_projeto(self):
        while True:
            nome_projeto = input("\nDigite o nome do projeto [0 para cancelar]: ").strip()

            if nome_projeto == '0':
                print("Cadastro cancelado.")
                return
            elif not nome_projeto:
                print("Erro: O nome do projeto não pode estar vazio. Tente novamente.")
                continue

            descricao = input("Digite a descrição do projeto [0 para cancelar]: ").strip()

            if descricao == '0':
                print("Cadastro cancelado.")
                return
            elif not descricao:
                print("Erro: A descrição do projeto não pode estar vazia. Tente novamente.")
                continue

            projeto = Projeto(nome_projeto, descricao)
            self.banco.cadastrar_projeto(projeto)
            break


    def cadastrar_alocacao(self):
        print("\n=== Funcionários ===")
        print("\nConsultando Funcionários...")
        time.sleep(1)
        self.banco.consultar_funcionarios()
        
        #Validação para o ID do funcionário
        while True:
            try:
                idfuncionario = int(input("\nDigite o ID do funcionário a ser alocado [0 para cancelar]: "))
                if idfuncionario == 0:
                    print("Cadastro cancelado.")
                    return
                elif idfuncionario < 0:
                    print("Erro: Insira um ID maior do que 0.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para o ID do funcionário.")

        print("\n=== Projetos ===")
        print("\nConsultando projetos...")
        time.sleep(1)
        self.banco.consultar_projetos()
        
        #Validação para o ID do projeto
        while True:
            try:
                idprojeto = int(input("\nDigite o ID do projeto que será trabalhado [0 para cancelar]: "))

                if idprojeto == 0:
                    print("Cadastro cancelado.")
                    return
                elif idprojeto < 0:
                    print("Erro: Insira um ID maior do que 0.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para o ID do projeto.")

        #Validação para carga horária
        while True:
            try:
                carga_horaria = int(input("Digite a carga horária (Hrs) [0 para cancelar]: "))

                if carga_horaria == 0:
                    print("Cadastro cancelado.")
                    return
                elif carga_horaria < 0:
                    print("Erro: Carga horária deve ser maior do que 0.")
                    continue
                break 
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a carga horária.")

        papel_funcionario = input("Digite a função do funcionário no projeto: ")
        if not papel_funcionario:
            print("Erro: O papel do funcionário no projeto não pode estar vazio.")
            return
        
        alocacao = Alocacao(carga_horaria, papel_funcionario, idprojeto, idfuncionario)
        self.banco.cadastrar_alocacao(alocacao)


#FUNÇÕES DE CONSULTA

    def consultar_cargos(self):
        print("\nConsultando cargos...")
        time.sleep(1)
        self.banco.consultar_cargos()


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


    def consulta_geral(self):
        print("\nRealizando consulta geral...")
        time.sleep(1)
        self.banco.consulta_geral()


#FUNÇÕES DE REMOÇÃO

    def remover_funcionario(self):
        print("\n==== Remover Funcionário ====")
        print("\nConsultando funcionarios...")
        time.sleep(1)
        self.banco.consultar_funcionarios() #Exibe todos os funcionários presentes no banco

        while True:
            try:
                idfuncionario = int(input("\nDigite o ID do funcionário para ser removido [0 para cancelar]: "))

                if idfuncionario == 0:
                    print("Remoção de funcionário cancelada.")
                    return
                if idfuncionario < 0:
                    print("Erro: ID deve ser maior que 0.")
                    continue

                validarId = self.banco.validar_funcionario_id(idfuncionario)
                if validarId:
                    #Verifica se o cargo está associado a algum funcionário
                    funcionario_associado = self.banco.verificar_funcionario_associado(idfuncionario)
                    if funcionario_associado:
                        print(f"Não é possível remover o funcionário ID {idfuncionario}, pois ele está associado a outros registros.")
                        return  #Cancela a remoção

                    funcionario = self.banco.consultar_funcionario_id(idfuncionario)
                    if funcionario:
                        print("\n==== Funcionário Escolhido ====")
                        print(tabulate([funcionario], headers=["ID", "Nome", "CPF", "Salário", "Cargo"], tablefmt="fancy_grid"))
                    confirmacao = input("Confirme a remoção [S/N]: ").lower()

                    if confirmacao == 's':
                        print("Realizando remoção...")
                        time.sleep(1)
                        self.banco.remover_funcionario(idfuncionario)  #Chama o método para remover o funcionário
                        break
                    else:
                        print("Remoção cancelada.")
                        return
                else:
                    print(f"Funcionario com ID {idfuncionario} não encontrado no banco de dados.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o ID.")


    def remover_cargo(self):
        print("\n==== Remover Cargo ====")
        print("\nConsultando tipos de cargos...")
        time.sleep(1)
        self.banco.consultar_cargos()  #Exibe todos os cargos disponíveis

        while True:
            try:
                idcargo = int(input("\nDigite o ID do cargo para ser removido [0 para cancelar]: "))
                
                if idcargo == 0:
                    print("Remoção de cargo cancelada.")
                    return
                if idcargo < 0:
                    print("Erro: ID deve ser maior que 0.")
                    continue  #Volta para o início do loop
                
                validarId = self.banco.validar_cargo_id(idcargo)
                if validarId:
                    #Verifica se o cargo está associado a algum funcionário
                    cargo_associado = self.banco.consulta_verificar_cargo_associado(idcargo)
                    if cargo_associado:
                        print(f"Não é possível remover o cargo ID {idcargo}, pois ele está associado a outros registros.")
                        return  #Cancela a remoção

                    print("\n==== Cargo Escolhido ====")
                    self.banco.consultar_cargo_id(idcargo)  #Exibe os detalhes do cargo
                    confirmacao = input("Confirme a remoção [S/N]: ").lower()

                    if confirmacao == 's':
                        print("Realizando remoção...")
                        time.sleep(1)
                        self.banco.remover_cargo(idcargo)  #Chama o método para remover o cargo
                    else:
                        print("Remoção cancelada.")
                        return
                else:
                    print(f"Cargo com ID {idcargo} não encontrado no banco de dados.")

            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o ID.")


    def remover_projeto(self):
        print("\n==== Remover Projeto ====")
        print("\nConsultando projetos...")
        time.sleep(1)
        self.banco.consultar_projetos()  #Exibe todos os projetos presentes no banco

        while True:
            try:
                idprojeto = int(input("\nDigite o ID do projeto para ser removido [0 para cancelar]: "))

                if idprojeto == 0:
                    print("Remoção de projeto cancelada.")
                    return
                if idprojeto < 0:
                    print("Erro: ID deve ser maior que 0.")
                    continue

                validarId = self.banco.validar_projeto_id(idprojeto)
                if validarId:
                    # Verifica se o projeto está associado a alguma alocação
                    projeto_associado = self.banco.verificar_projeto_associado(idprojeto)
                    if projeto_associado:
                        print(f"Não é possível remover o projeto ID {idprojeto}, pois ele está associado a outros registros.")
                        return  # Cancela a remoção

                    print("\n==== Projeto Escolhido ====")
                    self.banco.consultar_projeto_id(idprojeto)  # Exibe os detalhes do projeto
                    confirmacao = input("Confirme a remoção [S/N]: ").lower()

                    if confirmacao == 's':
                        print("Realizando remoção...")
                        time.sleep(1)
                        self.banco.remover_projeto(idprojeto)  # Chama o método para remover o projeto
                    else:
                        print("Remoção cancelada.")
                        return
                else:
                    print(f"Projeto com ID {idprojeto} não encontrado no banco de dados.")

            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o ID.")

      
    def remover_alocacao(self):
        print("\n==== Remover Alocação ====")
        print("\nConsultando alocações...")
        time.sleep(1)
        self.banco.consultar_alocacoes()  # Exibe todas as alocações presentes no banco

        while True:
            try:
                idalocacao = int(input("\nDigite o ID da alocação para ser removida [0 para cancelar]: "))

                if idalocacao == 0:
                    print("Remoção de alocação cancelada.")
                    return
                if idalocacao < 0:
                    print("Erro: ID deve ser maior que 0.")
                    continue

                validarId = self.banco.validar_alocacao_id(idalocacao)
                if validarId:
                    #Verifica se a alocação está associada a algum projeto ou funcionário
                    alocacao_associada = self.banco.verificar_alocacao_associada(idalocacao)
                    if alocacao_associada:
                        print(f"Não é possível remover a alocação ID {idalocacao}, pois ela está associada a outros registros.")
                        return  #Cancela a remoção

                    print("\n==== Alocação Escolhida ====")
                    self.banco.consultar_alocacao_id(idalocacao)  #Exibe os detalhes da alocação
                    confirmacao = input("Confirme a remoção [S/N]: ").lower()

                    if confirmacao == 's':
                        print("Realizando remoção...")
                        time.sleep(1)
                        self.banco.remover_alocacao(idalocacao)  #Chama o método para remover a alocação
                    else:
                        print("Remoção cancelada.")
                        return
                else:
                    print(f"Alocação com ID {idalocacao} não encontrada no banco de dados.")

            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o ID.")


#FUNÇÕES ADICIONAIS

    def validacao_idcargo(self): #Função responsável por validar o ID escolhido
        print("\n==== Cargos Disponiveis ====")
        print("\nConsultando cargos...")
        time.sleep(1)
        cargos = self.banco.consultar_cargos()
        if cargos:
            print("Escolha um dos cargos de funcionário acima:")
        else:
            None
        
        while True:
            try:
                idcargo = input("\nDigite o ID do cargo desejado [0 para cancelar / N para não atribuir tipo ao funcionario]: ").lower()

                if idcargo == 'n':
                    print("Funcionário cadastrado sem cargo com SUCESSO!")
                    return None
                elif idcargo == '0':
                    print("Operação cancelada.")
                    return None
                elif idcargo < '0':
                    print("Erro: ID deve ser maior do que 0.")
                    continue
                elif not self.banco.validar_cargo_id(int(idcargo)):
                    print(f"Erro: Não existe um cargo com o ID {idcargo}. Tente novamente.")
                    continue
                else:
                    return int(idcargo)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o ID.")


    def atualizar_salario(self): #Função de interface responsável por realizar a atualização do salário do funcionário
        print("\n==== Atualizar Salário  ====")
        print("\nConsultando Funcionários...")
        time.sleep(1)
        self.banco.consultar_funcionarios()
        
        while True:
            try:
                idfuncionario = int(input("\nEscolha um Funcionario(ID) [0 para cancelar]: "))

                if idfuncionario == 0:
                    print("Atualização cancelada.")
                    return
                elif idfuncionario < 0:
                    print("Erro: Insira um ID maior do que 0.")
                    continue
                elif not idfuncionario:
                    print("Erro: O ID do funcionário não pode estar vazio.")
                    continue
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o ID do funcionário.")

        funcionario = self.banco.consultar_funcionario_id(idfuncionario)
        if funcionario:
            print("\n==== Funcionário Escolhido ====")
            print(tabulate([funcionario], headers=["ID", "Nome", "CPF", "Salário", "Cargo"], tablefmt="fancy_grid"))
        
        while True:
            try:
                novo_salario = float(input(f"\nNovo salário do funcionário (ID {idfuncionario}) [0 para cancelar]: "))

                if novo_salario == 0:
                    print(f"Atualização cancelada.")
                    return
                elif not novo_salario:
                    print("Erro: O novo salário do funcionário não pode estar vazio.")
                    continue
                elif novo_salario < 0:
                    print("Erro: Insira um salário maior do que 0.")
                    continue
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número para o novo salário.")
        
        #Atualizando o salário do funcionário
        self.banco.atualizar_salario(novo_salario, idfuncionario)


    def atualizar_cargo(self): #Função de interface responsável por realizar a atualização do cargo do funcionário escolhido
        print("\n==== Atualizar Cargo ====")
        print("\nConsultando Funcionários...")
        time.sleep(1)
        self.banco.consultar_funcionarios()
        
        while True:
            try:
                idfuncionario = int(input("\nEscolha um Funcionário (ID) para atualizar o cargo [0 para cancelar]: "))

                if idfuncionario == 0:
                    print("Atualização de cargo cancelada.")
                    return
                elif idfuncionario < 0:
                    print("Erro: Insira um ID maior que 0")
                else:
                    funcionario = self.banco.consultar_funcionario_id(idfuncionario)
                    if funcionario:
                        print("\n==== Funcionário Escolhido para Atualização ====")
                        print(tabulate([funcionario], headers=["ID", "Nome", "CPF", "Salário", "Cargo"], tablefmt="fancy_grid"))
                        break
                    else:
                        print("Funcionário nao encontrado. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o ID do funcionário.")

        #Validação e seleção do novo cargo de cargo
        idcargo = self.validacao_idcargo()

        #Atualizando o cargo do funcionário
        if idcargo is not None:
            self.banco.atualizar_cargo(idcargo, idfuncionario)
