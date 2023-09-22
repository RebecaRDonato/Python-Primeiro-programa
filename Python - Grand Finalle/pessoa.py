class Pessoa():
    #Método construtor (método inicializador __init__)
    def __init__(self, nome, data_nascimento, genero, cpf, email):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__genero = genero
        self.__cpf = cpf
        self.__email = email


    #getter and setter method for nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        print('Nome atualizado com sucesso')

    #getter and setter method for data de nascimento
    @property
    def dataNascimento(self):
        return self.__data_nascimento
    @dataNascimento.setter
    def dataNascimento(self, nova_data_nascimento):
        self.__data_nascimento = nova_data_nascimento

    #getter and setter for genero
    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def genero(self, novo_genero):
        self.__genero = novo_genero

    #getter ans setter for cpf
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    #getter ans setter for email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, novo_email):
        self.__email = novo_email