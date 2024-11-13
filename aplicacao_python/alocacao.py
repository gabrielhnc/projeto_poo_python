class Alocacao:
    #Método Construtor
    def __init__(self, horas_trabalhadas, papel_funcionario, idProjeto, idFuncionario):
        self.__horas_trabalhadas = horas_trabalhadas
        self.__papel_funcionario = papel_funcionario 
        self.__idProjeto = idProjeto
        self.__idFuncionario = idFuncionario #Encapsulamento
        
    #Get
    def get_horas_trabalhadas(self):
        return self.__horas_trabalhadas

    def get_papel_funcionario(self):
        return self.__papel_funcionario
    
    def get_idProjeto(self):
        return self.__idProjeto

    def get_idFuncionario(self):
        return self.__idFuncionario

    #Set
    def set_horas_trabalhadas(self, horas_trabalhadas):
        self.__horas_trabalhadas = horas_trabalhadas

    def set_papel_funcionario(self, papel_funcionario):
        self.__papel_funcionario = papel_funcionario

    def set_idProjeto(self, idProjeto):
        self.__idProjeto = idProjeto

    def set_idFuncionario(self, idFuncionario):
        self.__idFuncionario = idFuncionario
