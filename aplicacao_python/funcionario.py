from pessoa import Pessoa

#Classe herdada da classe Pessoa (Herança)
class Funcionario(Pessoa):
    #Metodo Construtor
    def __init__(self, nome, cpf, salario, idtipo = None, idfuncionario = None):
        super().__init__(nome, cpf)
        self.__salario = salario
        self.__idtipo = idtipo
        self.__idfuncionario = idfuncionario #(Encapsulamento)

    #Get
    def get_salario(self):
        return self.__salario

    def get_idtipo(self):
        return self.__idtipo
    
    def get_idfuncionario(self):
        return self.__idfuncionario

    #Set
    def set_idtipo(self, idtipo):
        self.__idtipo = idtipo

    def set_salario(self, salario):
        self.__salario = salario

    def set_idfuncionario(self, idfuncionario):
        self.__idfuncionario = idfuncionario
