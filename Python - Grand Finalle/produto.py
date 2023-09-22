class Produto:
    #Método construtor (método inicializador __init__)
    def __init__(self, nome = 'Default', codigo = 'Default', valor = int, quantidade = int):
        self.__nome = nome
        self.__codigo = codigo
        self.__valor = valor
        self.__quantidade = quantidade

    #getter and setter for nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    #getter and setter for codigo
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo
    
    #getter and setter for valor
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor
    
    #getter and setter for quantidade
    @property
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self.__quantidade -= nova_quantidade