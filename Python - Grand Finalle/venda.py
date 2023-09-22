class Venda:
    #Método construtor (método inicializador __init__)
    def __init__(self, cod_transacao = 'Default', cod_funcionario = int, cod_produto = int, preco_produto = int, cod_cliente = 'Default', quant_vendida = int):
        self.__cod_transacao = cod_transacao
        self.__total = preco_produto*quant_vendida
        self.__cod_funcionario = cod_funcionario
        self.__cod_produto = cod_produto
        self.__cod_cliente = cod_cliente
    
    #getter and setter for código de transação
    @property
    def cod_transacao(self):
        return self.__cod_transacao
    @cod_transacao.setter
    def cod_transacao(self, novo_cod_transacao):
        self.__cod_transacao = novo_cod_transacao

    #getter and setter for total
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, novo_total):
        self.__total += novo_total
    
    #getter and setter for código do funcionário
    @property
    def cod_funcionario(self):
        return self.__cod_funcionario
    @cod_funcionario.setter
    def cod_funcionario (self, novo_cod_funcionario):
        self.__cod_funcionario = novo_cod_funcionario
    
    #getter and setter for código do produto
    @property
    def cod_produto(self):
        return self.__cod_produto
    @cod_produto.setter
    def cod_produto(self, novo_cod_produto):
        self.__cod_produto = novo_cod_produto
    
    #getter and setter for código do cliente
    @property
    def cod_cliente(self):
        return self.__cod_cliente
    @cod_cliente.setter
    def cod_cliente(self, novo_cod_cliente):
        self.__cod_cliente = novo_cod_cliente