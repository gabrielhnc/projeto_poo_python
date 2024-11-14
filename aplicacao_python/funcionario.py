from pessoa import Pessoa

#Classe herdada da classe Pessoa (Herança)
class Funcionario(Pessoa):
    #Metodo Construtor
    def __init__(self, nome, cpf, salario, idcargo = None, idfuncionario = None):
        super().__init__(nome, cpf)
        self.__salario = salario
        self.__idcargo = idcargo
        self.__idfuncionario = idfuncionario #(Encapsulamento)

    #Get
    def get_salario(self):
        return self.__salario

    def get_idcargo(self):
        return self.__idcargo
    
    def get_idfuncionario(self):
        return self.__idfuncionario

    #Set
    def set_idcargo(self, idcargo):
        self.__idcargo = idcargo

    def set_salario(self, salario):
        self.__salario = salario

    def set_idfuncionario(self, idfuncionario):
        self.__idfuncionario = idfuncionario

