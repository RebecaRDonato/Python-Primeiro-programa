from pessoa import Pessoa

class Funcionario(Pessoa):
    #Método construtor (método inicializador __init__)
    def __init__(self, nome, data_nascimento, genero, cpf, email, matricula, salario, data_admissao, data_demissao, vendas_mensais = 0):
        
        #Atributos herdados
        super().__init__(nome, data_nascimento, genero, cpf, email)
        
        #Atributos adcionados
        self.__matricula = matricula
        self.__salario = salario
        self.__data_admissao = data_admissao
        self.__data_demissao = data_demissao
        self.__vendas_mensais = vendas_mensais

    #Polimorfismo com o atributo nome
    @property
    def nome(self):
        return super().nome

    #getter and setter for matricula
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, nova_matricula):
        self.__matricula = nova_matricula

    #getter and setter for salario
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario

    #getter and setter for data de admissão
    @property
    def dataAdmissao(self):
        return self.__data_admissao
    @dataAdmissao.setter
    def dataAdmissao(self, nova_data_admissao):
        self.__data_admissao = nova_data_admissao

    #getter and setter for data de demissão
    @property
    def dataDemissao(self):
        return self.__data_demissao
    @dataDemissao.setter
    def dataDemissao(self, nova_data_demissao):
        self.__data_demissao = nova_data_demissao

    #getter and setter for vendas mensais
    @property
    def vendasMensais(self):
        return self.__vendas_mensais
    @vendasMensais.setter
    def vendasMensais(self, novas_vendas):
        self.__vendas_mensais += novas_vendas