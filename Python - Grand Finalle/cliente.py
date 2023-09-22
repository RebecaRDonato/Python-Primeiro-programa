from pessoa import Pessoa

class Cliente(Pessoa):
    #Método construtor (método inicializador __init__)
    def __init__(self, nome, data_nascimento, genero, cpf, email, endereco, telefone, renda, total_compras):
        
        #Atributos herdados
        super().__init__(nome, data_nascimento, genero, cpf, email)

        #Atributos adcionados
        self.__endereco = endereco
        self.__telefone = telefone
        self.__renda = renda
        self.__total_compras = total_compras

    #Polimorfismo com o atributo nome
    @property
    def nome(self):
        return super().nome

    #getter and setter for endereço
    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    #getter and setter for telefone
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, novo_telelfone):
        self.__telefone = novo_telelfone

    #getter and setter for renda
    @property
    def renda(self):
        return self.__renda
    @renda.setter
    def renda(self, nova_renda):
        self.__renda = nova_renda
    
    #getter and setter for total de compras
    @property
    def totalCompras(self):
        return self.__total_compras
    @totalCompras.setter
    def totalCompras(self, novo_total):
        self.__total_compras += novo_total