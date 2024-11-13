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
            print("\nConexão com o banco de dados estabelecida com SUCESSO.")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar com o banco de dados: {e}")


    #Desconexao com o banco
    def desconectar(self):
        if self.conexao and self.cursor:
            self.cursor.close() #Encerramento do banco
            self.conexao.close()
            print("Conexão com o banco de dados encerrada.")
        else:
            print("Nenhuma conexão ativa para desconectar.")


#CADASTRAR
    def cadastrar_funcionario(self, funcionario): #Método para cadastrar funcionarios (INSERT)
        try:
            query = "INSERT INTO funcionario (nome, cpf, salario, tipo_idtipo) VALUES (%s, %s, %s, %s)"
            valores = (funcionario.get_nome(), funcionario.get_cpf(), funcionario.get_salario(), funcionario.get_idtipo())
            self.cursor.execute(query, valores)
            self.conexao.commit()
            print(f"\nFuncionário {funcionario.get_nome()} cadastrado com SUCESSO.")
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar funcionário: {e}")


    def cadastrar_tipo(self, tipo): #Metodo para cadastrar tipos (INSERT)
        try:
            query = "INSERT INTO tipo (descricao, informacao_adicional) VALUES (%s, %s)"
            valores = (tipo.get_descricao(), tipo.get_informacao_adicional())
            self.cursor.execute(query, valores)
            self.conexao.commit()
            print(f"\nTipo {tipo.get_descricao()} cadastrado com SUCESSO.")
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar tipo: {e}")


    def cadastrar_projeto(self, projeto): #Metodo para cadastrar projetos (INSERT)
        try:
            query = "INSERT INTO projetos (nome, descricao) VALUES (%s, %s)"
            valores = (projeto.get_nome(), projeto.get_descricao())
            self.cursor.execute(query, valores)
            self.conexao.commit()
            print(f"\nProjeto {projeto.get_nome()} cadastrado com SUCESSO.")
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar projeto: {e}")


    def cadastrar_alocacao(self, alocacao): #Metodo para cadastrar alocaçoes (INSERT)
        try:
            query = "INSERT INTO alocacoes (horas_trabalhadas, papel_funcionario, projetos_idprojetos, funcionario_idfuncionario) VALUES (%s, %s, %s, %s)"
            valores = (alocacao.get_horas_trabalhadas(), alocacao.get_papel_funcionario(), alocacao.get_idProjeto(), alocacao.get_idFuncionario())
            self.cursor.execute(query, valores)
            self.conexao.commit()
            print(f"\nAlocação registrada para o funcionário (ID {alocacao.get_idFuncionario()}) com SUCESSO.")
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
                t.descricao
            FROM 
                funcionario f
            JOIN 
                tipo t ON f.tipo_idtipo = t.idtipo
            ORDER BY idfuncionario ASC
            """
            self.cursor.execute(query)
            funcionarios = self.cursor.fetchall()
            if funcionarios:
                print(tabulate(funcionarios, headers=["ID", "Nome", "CPF", "Salário", "Tipo"], tablefmt="fancy_grid"))
                return funcionarios
            else:
                print("Nenhum funcionário encontrado.")
                return []
        except mysql.connector.Error as e:
            print(f"Erro ao consultar funcionários: {e}")
            return []


    def consultar_funcionario_id(self, idfuncionario): #Consulta de somente um funcionario escolhido pelo ID (SELECT)
        try:
            query = """
            SELECT 
                f.nome, 
                f.cpf, 
                f.salario, 
                t.descricao
            FROM 
                funcionario f
            JOIN 
                tipo t ON f.tipo_idtipo = t.idtipo
            WHERE
                f.idfuncionario = %s
            """
            self.cursor.execute(query, (idfuncionario,))
            funcionario = self.cursor.fetchone()
            if funcionario:
                print(tabulate([funcionario], headers=["Nome", "CPF", "Salário", "Cargo"], tablefmt="fancy_grid"))
            else:
                print(f"ID {idfuncionario} não está no banco de dados. Tente novamente")
        except mysql.connector.Error as e:
            print(f"Erro ao consultar ID do funcionário: {e}")
            return False


    def consultar_funcionario_por_cpf(self, cpf): #Consulta de CPF no banco para analisar se há funcionários com o cpf a ser registrado
        try:
            query = "SELECT cpf FROM funcionario WHERE cpf = %s"
            self.cursor.execute(query, (cpf,))
            resultado = self.cursor.fetchone()
            return resultado is not None #Validação para indicar se o CPF esta no banco
        except mysql.connector.Error as erro:
            print(f"Erro ao consultar CPF no banco: {erro}")
            return False


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


    def consultar_tipos(self): #Consulta de tipos (descrição nesse caso é o equivalente aos tipos de funcionarios)
        try:
            query = """
            SELECT 
                idtipo, 
                descricao, 
                informacao_adicional 
            FROM 
                tipo
            ORDER BY idtipo ASC
            """ 
            self.cursor.execute(query)
            tipos = self.cursor.fetchall()
            if tipos:
                print(tabulate(tipos, headers=["ID", "Tipo Funcionario", "Informação Adicional"], tablefmt="fancy_grid"))
            else:
                print("Nenhum tipo encontrado.")
        except mysql.connector.Error as e:
            print(f"Erro ao consultar tipos: {e}")


    def consultar_tipo_id(self, idtipo): #Consulta realizada para validar se o ID escolhido existe, caso contrário o loop ira continuar até pedir um ID válido
        try:
            query = """
            SELECT COUNT(*) FROM tipo WHERE idtipo = %s
            """
            self.cursor.execute(query, (idtipo,))
            resultado = self.cursor.fetchone()
            if resultado[0] > 0: 
                return True
            else:
                return False
        except mysql.connector.Error as e:
            print(f"Erro ao consultar o tipo: {e}")
            return False


#ATUALIZAR
    def atualizar_salario(self, novo_salario, idfuncionario): #Metodo responsável por atualizar o salário do funcionario escolhido (UPDATE)
        try:
            query = "UPDATE funcionario SET salario = %s WHERE idfuncionario = %s"
            valores = (novo_salario, idfuncionario)
            self.cursor.execute(query, valores)
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"Salário do funcionário (ID {idfuncionario}) atualizado com SUCESSO.")
            else:
                print("\nNenhum funcionário encontrado com o ID escolhido.")
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar salário: {e}")
