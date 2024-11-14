class Cargo:
    #Método Construtor
    def __init__(self, descricao, informacao_adicional):
        self.__descricao = descricao
        self.__informacao_adicional = informacao_adicional #Encapsulamento

    #Get
    def get_descricao(self):
        return self.__descricao

    def get_informacao_adicional(self):
        return self.__informacao_adicional
    
    #Set
    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_informacao_adicional(self, informacao_adicional):
        self.__informacao_adicional = informacao_adicional
