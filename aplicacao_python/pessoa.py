class Pessoa:
    #Metodo Construtor
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf #Encapsulamento

    #Get
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf

    #Set
    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf
