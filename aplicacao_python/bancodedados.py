import mysql.connector #Importação da biblioteca mysql.connector para poder conectar com o banco
#OBS: os dados para a entrada no banco são colocado no arquivo "main.py"
from tabulate import tabulate #Uso da biblioteca tabulate para consultar as informaçoes simulando uma tabela

class BancoDeDados:
    #Metodo Construtor tendo como atributo os componentes para conectar ao banco de dados
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    #Conexao com o banco
    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conexao.cursor()
            print("\nConexão com o banco de dados estabelecida com SUCESSO.\n")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar com o banco de dados: {e}")


    #Desconexao com o banco
    def desconectar(self):
        if self.conexao and self.cursor:
            self.cursor.close() #Encerramento do banco
            self.conexao.close()
            print("Conexão com o banco de dados encerrada com SUCESSO.\n")
        else:
            print("Nenhuma conexão ativa para desconectar.")


#CADASTRAR

    def cadastrar_funcionario(self, funcionario):  #Método para cadastrar funcionários (INSERT)
        try:
            #Verifica se o id do cargo é None, se for deixa como None para que o banco insira NULL
            idcargo = funcionario.get_idcargo() if funcionario.get_idcargo() is not None else None
            query = "INSERT INTO funcionario (nome, cpf, salario, cargo_idcargo) VALUES (%s, %s, %s, %s)"
            valores = (funcionario.get_nome(), funcionario.get_cpf(), funcionario.get_salario(), idcargo)
            self.cursor.execute(query, valores)
            self.conexao.commit()
            print(f"\nFuncionário(a) {funcionario.get_nome()} cadastrado com SUCESSO.\n")
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar funcionário: {e}")


    def cadastrar_cargo(self, cargo): #Metodo para cadastrar cargos (INSERT)
        try:
            query = "INSERT INTO cargo (descricao, informacao_adicional) VALUES (%s, %s)"
            valores = (cargo.get_descricao(), cargo.get_informacao_adicional())
            self.cursor.execute(query, valores)
            self.conexao.commit()
            print(f"\nCargo {cargo.get_descricao()} cadastrado com SUCESSO.\n")
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar cargo: {e}")


    def cadastrar_projeto(self, projeto): #Metodo para cadastrar projetos (INSERT)
        try:
            query = "INSERT INTO projetos (nome, descricao) VALUES (%s, %s)"
            valores = (projeto.get_nome(), projeto.get_descricao())
            self.cursor.execute(query, valores)
            self.conexao.commit()
            print(f"\nProjeto {projeto.get_nome()} cadastrado com SUCESSO.\n")
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar projeto: {e}")


    def cadastrar_alocacao(self, alocacao): #Metodo para cadastrar alocaçoes (INSERT)
        try:
            query = "INSERT INTO alocacoes (horas_trabalhadas, papel_funcionario, projetos_idprojetos, funcionario_idfuncionario) VALUES (%s, %s, %s, %s)"
            valores = (alocacao.get_horas_trabalhadas(), alocacao.get_papel_funcionario(), alocacao.get_idProjeto(), alocacao.get_idFuncionario())
            self.cursor.execute(query, valores)
            self.conexao.commit()
            print(f"\nAlocação registrada para o funcionário (ID {alocacao.get_idFuncionario()}) com SUCESSO.\n")
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar alocação: {e}")


#CONSULTAR

    def consultar_funcionarios(self): #Consulta de funcionarios (SELECT)
        try:
            query = """
            SELECT 
                f.idfuncionario,
                f.nome, 
                f.cpf, 
                f.salario, 
                COALESCE(c.descricao, 'Sem cargo')
            FROM 
                funcionario f
            LEFT JOIN
                cargo c ON f.cargo_idcargo = c.idcargo
            ORDER BY idfuncionario ASC
            """
            self.cursor.execute(query)
            funcionarios = self.cursor.fetchall()
            if funcionarios:
                print(tabulate(funcionarios, headers=["ID", "Nome", "CPF", "Salário", "Cargo"], tablefmt="fancy_grid"))
            else:
                print("Nenhum funcionário encontrado.")
        except mysql.connector.Error as e:
            print(f"Erro ao consultar funcionários: {e}")


    def consultar_funcionario_id(self, idfuncionario): #Consulta de somente um funcionario escolhido pelo ID (SELECT)
        try:
            query = """
            SELECT 
                f.idfuncionario,
                f.nome, 
                f.cpf, 
                f.salario, 
                COALESCE(c.descricao, 'Sem cargo')
            FROM 
                funcionario f
            LEFT JOIN
                cargo c ON f.cargo_idcargo = c.idcargo
            WHERE
                f.idfuncionario = %s
            """
            self.cursor.execute(query, (idfuncionario,))
            funcionario = self.cursor.fetchone()
            return funcionario
        except mysql.connector.Error as e:
            print(f"Erro ao consultar ID do funcionário: {e}")
            return None


    def consultar_funcionario_por_cpf(self, cpf): #Consulta de CPF no banco para analisar se há funcionários com o cpf a ser registrado
        try:
            query = "SELECT cpf FROM funcionario WHERE cpf = %s"
            self.cursor.execute(query, (cpf,))
            resultado = self.cursor.fetchone()
            return resultado is not None #Validação para indicar se o CPF esta no banco
        except mysql.connector.Error as erro:
            print(f"Erro ao consultar CPF no banco: {erro}")


    def consultar_projetos(self): #Consulta de projetos (SELECT)
        try:
            query = """
            SELECT 
                idprojetos,
                nome, 
                descricao 
            FROM 
                projetos
            ORDER BY idprojetos ASC
            """
            self.cursor.execute(query)
            projetos = self.cursor.fetchall()

            if projetos:
                print(tabulate(projetos, headers=["ID", "Nome", "Descrição"], tablefmt="fancy_grid"))
            else:
                print("Nenhum projeto encontrado.")
        except mysql.connector.Error as e:
            print(f"Erro ao consultar projetos: {e}")
    

    def consultar_projeto_id(self, idprojeto):  #Consulta das informaçoes de um projeto pelo ID
        try:
            query = """
            SELECT 
                idprojeto,
                nome, 
                descricao 
            FROM 
                projetos
            WHERE 
                idprojeto = %s
            """
            self.cursor.execute(query, (idprojeto,))
            projeto = self.cursor.fetchone()

            if projeto:
                print(tabulate([projeto], headers=["ID", "Nome", "Descrição"], tablefmt="fancy_grid"))
                return True
            else:
                print(f"Projeto com ID {idprojeto} não encontrado.")
                return None
        except mysql.connector.Error as e:
            print(f"Erro ao consultar o projeto pelo ID: {e}")
            return None


    def consultar_alocacoes(self): #Consulta de alocaçoes (Local onde os funcionarios estão trabalhando, especificando o projeto)
        try:
            query = """
            SELECT 
                a.idalocacoes,
                f.nome,
                p.nome,
                a.papel_funcionario, 
                a.horas_trabalhadas
            FROM 
                alocacoes a
            JOIN 
                funcionario f ON a.funcionario_idfuncionario = f.idfuncionario
            JOIN
                projetos p ON a.projetos_idprojetos = p.idprojetos
            ORDER BY a.idalocacoes ASC
            """
            self.cursor.execute(query)
            alocacoes = self.cursor.fetchall()
            if alocacoes:
                print(tabulate(alocacoes, headers=["ID", "Funcionario", "Projeto", "Função", "Carga Horária"], tablefmt="fancy_grid"))
            else:
                print("Nenhuma alocação encontrada.")
        except mysql.connector.Error as e:
            print(f"Erro ao consultar alocações: {e}")


    def consultar_alocacao_id(self, idalocacao):  # Consulta de alocação pelo ID
        try:
            query = """
            SELECT 
                a.idalocacoes,
                f.nome AS funcionario,
                p.nome AS projeto,
                a.papel_funcionario, 
                a.horas_trabalhadas
            FROM 
                alocacoes a
            JOIN 
                funcionario f ON a.funcionario_idfuncionario = f.idfuncionario
            JOIN
                projetos p ON a.projetos_idprojetos = p.idprojetos
            WHERE 
                a.idalocacoes = %s
            """
            self.cursor.execute(query, (idalocacao,))
            alocacao = self.cursor.fetchone()  # Retorna a primeira linha correspondente ao ID

            if alocacao:
                print(tabulate([alocacao], headers=["ID", "Funcionário", "Projeto", "Função", "Carga Horária"], tablefmt="fancy_grid"))
                return True
            else:
                print(f"Alocação com ID {idalocacao} não encontrada.")
                return None
        except mysql.connector.Error as e:
            print(f"Erro ao consultar a alocação pelo ID: {e}")
            return None


    def consultar_cargos(self):  # Consulta de cargos (descrição de cargos de funcionários)
        try:
            query = """
            SELECT 
                idcargo, 
                COALESCE(descricao, 'Sem cargo'), 
                informacao_adicional 
            FROM 
                cargo
            ORDER BY idcargo ASC
            """ 
            self.cursor.execute(query)
            cargos = self.cursor.fetchall()
            if cargos:
                print(tabulate(cargos, headers=["ID", "Cargo", "Informação Adicional"], tablefmt="fancy_grid"))
            else:
                print("Nenhum cargo encontrado.")
        except mysql.connector.Error as e:
            print(f"Erro ao consultar cargos: {e}")


    def consultar_cargo_id(self, idcargo):  # Consulta de somente um cargo escolhido pelo ID (SELECT)
        try:
            query = """
            SELECT 
                c.idcargo,
                COALESCE(c.descricao, 'Sem cargo'), 
                c.informacao_adicional
            FROM 
                cargo c
            WHERE
                c.idcargo = %s
            """
            self.cursor.execute(query, (idcargo,))
            cargo = self.cursor.fetchone()
            if cargo:
                print(tabulate([cargo], headers=["ID", "Cargo", "Informação Adicional"], tablefmt="fancy_grid"))
                return True
            else:
                print(f"ID {idcargo} não encontrado no banco de dados. Tente novamente.")
                return None
        except mysql.connector.Error as e:
            print(f"Erro ao consultar ID do cargo: {e}")
            return None


    def consulta_geral(self): #Realiza a consulta da VIEW criada no banco de dados onde é possivel visualizar de forma geral as informaçoes do banco.
        try:
            query = "SELECT * FROM vw_dados_completos ORDER BY idfuncionario ASC"
            self.cursor.execute(query)
            geral = self.cursor.fetchall()
            if geral:
                print(tabulate(geral, headers=["ID", "Nome", "CPF", "Salário", "Cargo", "Projeto", "CargaHoraria", "Função"], tablefmt="fancy_grid"))
            else:
                print("Nenhuma consulta geral encontrada.")
        except mysql.connector.Error as e:
            print(F"Erro ao realizar consulta geral: {e}")


#VERIFICAÇÕES / VALIDAÇÕES

    def verificar_cargo_associado(self, idcargo):
        try:
            query = "SELECT COUNT(*) FROM funcionario WHERE cargo_idcargo = %s"
            self.cursor.execute(query, (idcargo,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0  #Retorna True se houver funcionários associados ao cargo
        except mysql.connector.Error as e:
            print(f"Erro ao verificar cargo associado: {e}")


    def validar_cargo_id(self, idcargo): #Consulta realizada para validar se o ID escolhido existe, caso contrário o loop ira continuar até pedir um ID válido
        try:
            query = "SELECT COUNT(*) FROM cargo WHERE idcargo = %s"
            self.cursor.execute(query, (idcargo,))
            resultado = self.cursor.fetchone()
            if resultado[0] > 0: 
                return True
            else:
                return False
        except mysql.connector.Error as e:
            print(f"Erro ao validar o ID: {e}")
            return False

    
    def verificar_funcionario_associado(self, idfuncionario):
        try:
            query = "SELECT COUNT(*) FROM alocacoes WHERE funcionario_idfuncionario = %s"  
            self.cursor.execute(query, (idfuncionario,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0  #Retorna True se o funcionário estiver associado a alguma alocação
        except mysql.connector.Error as e:
            print(f"Erro ao verificar funcionário associado: {e}")
            return False


    def validar_funcionario_id(self, idfuncionario):
        try:
            query = "SELECT COUNT(*) FROM funcionario WHERE idfuncionario = %s"
            self.cursor.execute(query, (idfuncionario,))
            resultado = self.cursor.fetchone()
            if resultado[0] > 0: 
                return True
            else:
                return False
        except mysql.connector.Error as e:
            print(f"Erro ao validar o ID: {e}")
            return False
        

    def verificar_projeto_associado(self, idprojeto):
        try:
            query = "SELECT COUNT(*) FROM alocacoes WHERE projetos_idprojetos = %s"  
            self.cursor.execute(query, (idprojeto,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0  #Retorna True se o projeto estiver associado a alguma alocação
        except mysql.connector.Error as e:
            print(f"Erro ao verificar projeto associado: {e}")
            return False


    def validar_projeto_id(self, idprojeto):
        try:
            query = "SELECT COUNT(*) FROM projetos WHERE idprojetos = %s"
            self.cursor.execute(query, (idprojeto,))
            resultado = self.cursor.fetchone()
            if resultado[0] > 0:
                return True  #O ID do projeto existe
            else:
                return False  #O ID do projeto não existe
        except mysql.connector.Error as e:
            print(f"Erro ao validar o ID: {e}")
            return False

    
    def verificar_alocacao_associada(self, idalocacao):
        try:
            query = "SELECT COUNT(*) FROM alocacoes WHERE idalocacoes = %s AND projetos_idprojetos IS NOT NULL"
            self.cursor.execute(query, (idalocacao,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0  #Retorna True se a alocação estiver associada a um projeto
        except mysql.connector.Error as e:
            print(f"Erro ao verificar alocação associada a projeto: {e}")
            return False


    def validar_alocacao_id(self, idalocacao):
        try:
            query = "SELECT COUNT(*) FROM alocacoes WHERE idalocacoes = %s"
            self.cursor.execute(query, (idalocacao,))
            resultado = self.cursor.fetchone()
            if resultado[0] > 0:
                return True  #O ID da alocação existe
            else:
                return False  #O ID da alocação não existe
        except mysql.connector.Error as e:
            print(f"Erro ao validar o ID: {e}")
            return False


#REMOVER

    def remover_funcionario(self, idfuncionario): #Método para remover funcionarios
        try:
            query = "DELETE FROM funcionario WHERE idfuncionario = %s"
            self.cursor.execute(query, (idfuncionario,))
            self.conexao.commit()
            print(f"Funcionário (ID {idfuncionario}) removido com SUCESSO!\n")
        except mysql.connector.Error as e:
            print(f"Erro ao remover funcionário: {e}")


    def remover_cargo(self, idcargo): #Método para remover cargos
        try:
            query = "DELETE FROM cargo WHERE idcargo = %s"
            self.cursor.execute(query, (idcargo,))
            self.conexao.commit()
            print(f"Cargo ID {idcargo} removido com SUCESSO!\n")
        except mysql.connector.Error as e:
            print(f"Erro ao remover cargo: {e}")


    def remover_projeto(self, idprojeto): #Método para remover projetos
        try:
            query = "DELETE FROM projetos WHERE idprojetos = %s"
            self.cursor.execute(query, (idprojeto,))
            self.conexao.commit()
            print(f"Projeto ID {idprojeto} removido com SUCESSO\n!")
        except mysql.connector.Error as e:
            print(f"Erro ao remover projeto: {e}")


    def remover_alocacao(self, idalocacao): #Método para remover alocações
        try:
            query = "DELETE FROM alocacoes WHERE idalocacoes = %s"
            self.cursor.execute(query, (idalocacao,))
            self.conexao.commit()
            print(f"Alocação ID {idalocacao} removida com SUCESSO!\n")
        except mysql.connector as e:
            print(f"Erro ao remover alocacao: {e}")


#ATUALIZAR

    def atualizar_cargo(self, idcargo, idfuncionario):
        try:
            query = "UPDATE funcionario SET cargo_idcargo = %s WHERE idfuncionario = %s"
            valores = (idcargo, idfuncionario)
            self.cursor.execute(query, valores)
            self.conexao.commit()

            if self.cursor.rowcount > 0:
                print(f"Cargo do funcionário (ID {idfuncionario}) atualizado com SUCESSO!\n")
            else:
                print(f"\nNenhum funcionário encontrado com o ID fornecido.")
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar cargo: {e}")


    def atualizar_salario(self, novo_salario, idfuncionario): #Metodo responsável por atualizar o salário do funcionario escolhido (UPDATE)
        try:
            query = "UPDATE funcionario SET salario = %s WHERE idfuncionario = %s"
            valores = (novo_salario, idfuncionario)
            self.cursor.execute(query, valores)
            self.conexao.commit()

            if self.cursor.rowcount > 0:
                print(f"Salário do funcionário (ID {idfuncionario}) atualizado com SUCESSO!\n")
            else:
                print("\nNenhum funcionário encontrado com o ID escolhido.")
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar salário: {e}")
