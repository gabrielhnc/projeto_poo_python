class Projeto:
    #Método Construtor
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao #Encapsulamento

    #Get
    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao

    #Set
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao
