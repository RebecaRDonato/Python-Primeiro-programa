#Importando Pessoa
from pessoa import Pessoa
'''
    Atributos de pessoa:
    >> nome
    >> data_nascimento
    >> genero
    >> cpf
    >> email
'''

#Importando Funcionario
from funcionario import Funcionario
'''
    Atributos de pessoa:
    >> nome
    >> data_nascimento
    >> genero
    >> cpf
    >> email
    >> matricula
    >> salario
    >> data_admissao
    >> data_demissao
    >> vendas_mensal
'''

#Importando Cliente
from cliente import Cliente
'''
    Atributos de pessoa:
    >> nome
    >> data_nascimento
    >> genero
    >> cpf
    >> email
    >> endereco
    >> telefone
    >> renda
    >> total_compras
'''

#Importando Produto
from produto import Produto
'''
    Atributos de produto:
    >> Nome
    >> Código
    >> Valor
    >> Quantidade
'''

#Importando Vendas
from venda import Venda
'''
    Atributos de venda
    >> Código da transação
    >> Total (preço do produto * quantidade da venda)
    >> Código do funcionáro (será a matrícula)
    >> Código do produto (será o próprio código)
    >> Código do cliente (será o cpf)
'''


#Banco de funcionários
funcionario_teste = Funcionario('Nome', 'Data de nascimento', 'Gênero', 'CPF', 'E-mail', 'Matrícula', 'Salário', 'Data de admissão', 'data de demissão', 'Vendas mensais')
funcionario_1 = Funcionario('Adriana', '21/08/1997', 'Feminino', '123.456.789.10', 'adriana@gmail.com', '001', '1.500,50', '25/07/2023', None, 20158)
funcionario_2 = Funcionario('Kevin', '04/12/2022', 'Masculino', '963.852.741.01', 'kevin@gmail.com', '002', '1.500,50', '22/06/2023', None, 15564)

#Banco de clientes
cliente_teste = Cliente('Nome', 'Data de nascimento', 'Gênero', 'CPF', 'E-mail', 'Endereço', 'Telefone', 'Renda', 'Total de compras')
cliente_1 = Cliente('Keury', '03/11/2005', 'Feminino', '150.583.209-04', 'keury@gmail.com', 'Jatobá, n° 525, Rua Sucupira', '(93) 9 9138-0258', 350, 0)
cliente_2 = Cliente('Jhonatan', '22/11/1993', 'Masculino', '147.258.369-01', 'jhonatan@gmail.com', 'São Paulo, Pinheiros, n° 23, Apt. 45', '(93) 9 9188-5656', 30.000, 0)

#Banco de produtos
produto_teste = Produto('Nome', 'Código', 'Valor', 'Quantidade')
produto_1 = Produto('Loção Dory Smith', '07', 50, 20)

#Banco de vendas
#venda_teste = Venda('Código da transação', 'Código do funcionário', 'Código do produto', 'Preço do produto', 'Código do cliente', 'Quantidade vendida')

'''--->> SISTEMA <<---'''

#Funcionalidades
''' Lista de funcionários e clientes '''
lista_funcionarios = [funcionario_1, funcionario_2]
lista_clientes = [cliente_1, cliente_2]
lista_vendas = []
lista_produtos = [produto_1]

''' Cadastro de clientes '''
def CadastrarCliente():
    print('\nPara cadastrar um novo cliente, insira os dados abaixo:')
    nome = input('>> Nome: ')
    data_nascimento = input('>> Data de nascimento: ')
    genero = input('>> Gênero: ')
    cpf = input('>> CPF: ')
    email = input('>> E-mail: ')
    endereco = input('>> Endereço: ')
    telefone = input('>> Telefone: ')
    renda = input('>> Renda: ')
    total_compras = input('>> Total de compras: ')

    cliente = Cliente(nome, data_nascimento, genero, cpf, email, endereco, telefone, renda, total_compras)

    lista_clientes.append(cliente)

''' Cadastro de funcionários '''
def CadastrarFuncionario():
    print('\nPara cadastrar um novo Funcionario, insira os dados abaixo:')
    nome = input('>> Nome: ')
    data_nascimento = input('>> Data de nascimento: ')
    genero = input('>> Gênero: ')
    cpf = input('>> CPF: ')
    email = input('>> E-mail: ')
    matricula = input('>> Matrícula: ')
    salario = input('>> Salário: ')
    data_admissao = input('>> Data de admissão: ')

    funcionario = Cliente(nome, data_nascimento, genero, cpf, email, matricula, salario, data_admissao)

    lista_funcionarios.append(funcionario)

#Interface inicial
iniciar_finalizar = True

while iniciar_finalizar == True:
    if iniciar_finalizar == 1:
        menu = input('\n|    sysElegancy - Sua boutique digital  |\n\nBem-vindo à sysElegancy. O que você deseja fazer hoje?\n\n°~°~°| CADASTRO |°~°~°\n|1| Cadastrar novo cliente\n|2| Cadastrar novo funcionário\n\n°~°~°| CONSULTA DE CLIENTES |°~°~°\n|3| Consultar Clientes\n|4| Consultar dados de Cliente\n\n°~°~°| CONSULTA DE FUNCIONÁRIO |°~°~°\n|5| Consultar Funcionários\n|6| Consultar dados de Funcionário\n\n°~°~°| EDITAR |°~°~°\n|7| Editar Cliente\n|8| Editar funcionário\n\n°~°~°| EXCLUIR |°~°~°\n|9| Excluir cliente\n|10| Excluir funcionário\n\n°~°~°| VENDAS |°~°~°\n|11| Lista de produtos\n|12| Realizar nova venda\n\n°~°~°| OUTROS |°~°~°\n|0| SAIR\n\n>> ')

        if menu == '1':
            #Cadastro de Clientes
            CadastrarCliente()
            print('Cliente cadastrado com sucessso!\n')

        elif menu == '2':
            #Cadastro de funcionários
            CadastrarFuncionario()
            print('Funcionário cadastrado com sucessso!\n')

        elif menu == '3':
            #Mostra os clientes cadastrados
            print('\nEstes são os clientes encontrados:')
            index = 0

            for x in lista_clientes:
                print(f'-->> ({index}) {x.nome}')
                index = index+1
        
        elif menu == '4':
            #Mostra os dados do cliente pela busca por nome
            busca = input('Quem você deseja buscar?: ')
            encontrado = 0

            for x in lista_clientes:
                if busca == x.nome:
                    print('Cliente encontrado!')
                    print(f'\n--> Data de nascimento: {x.dataNascimento}\n--> Gênero: {x.genero}\n--> CPF: {x.cpf}\n--> E-mail: {x.email}\n--> Endereço: {x.endereco}\n--> Telefone: {x.telefone}\n--> Renda: {x.renda}\n--> Total de compras: {x.totalCompras}')
                    encontrado = 1
                    break
                
                elif encontrado == 0:
                    print('Cliente não encontrado!')

        elif menu == '5':
            #Mostra os funcionários cadastrados
            print('\nEstes são os funcionários encontrados:')
            index = 0

            for y in lista_funcionarios:
                print(f'-->> ({index}) {y.nome}')
                index = index+1
        
        elif menu == '6':
            #Mostra os dados do funcionário pela busca por nome
            busca = input('Quem você deseja buscar?: ')
            encontrado = 0
        
            for x in lista_funcionarios:
                if busca == x.nome:
                    print('Funcionário encontrado!')
                    print(f'\n--> Data de nascimento: {x.dataNascimento}\n--> Gênero: {x.genero}\n--> CPF: {x.cpf}\n--> E-mail: {x.email}\n--> Matrícula: {x.matricula}\n--> Salário: {x.salario}\n--> Data de admissão: {x.dataAdmissao}\n--> Data de demissão: {x.dataDemissao}\n--> Vendas mensais: {x.vendasMensais}')
                    encontrado = 1
                    break
                
                elif encontrado == 0:
                    print('Funcionário não encontrado!')

        elif menu == '7':
            #Edita os dados de um cliente no sistema
            editar = input('Quem você deseja editar? ')
            busca = 0

            for x in lista_clientes:
                if editar == x.nome:
                    print('Cliente encontrado! Quais dados deseja editar?')
                    
                    escolha = input(f'\n|1| Nome\n|2| Data de nascimento\n|3| Gênero\n|4| CPF\n|5| E-mail\n|6| Endereço\n|7| Telefone\n|8| Renda\n|9| Total de compras\n\n>> ')

                    if escolha == '1':
                        novoNome = input('Novo nome: ')
                        x.nome = novoNome

                    elif escolha == '2':
                        novaDataNascimento = input('Nova data de nascimento: ')
                        x.dataNascimento = novaDataNascimento

                    elif escolha == '3':
                        novoGenero = input('Novo gênero: ')
                        x.genero = novoGenero
                    
                    elif escolha == '4':
                        novoCpf = input('Novo CPF: ')
                        x.cpf - novoCpf
                    
                    elif escolha == '5':
                        novoEmail = input('Novo e-mail: ')
                        x.email = novoEmail
                    
                    elif escolha == '6':
                        novoEndereco = input('Novo endereço: ')
                        x.endereco = novoEndereco
                    
                    elif escolha == '7':
                        novoTelefone = input('Novo telefone: ')
                        x.telefone = novoTelefone
                    
                    elif escolha == '8':
                        novaRenda = input('Nova renda: ')
                        x.renda = novaRenda
                    
                    elif escolha == '9':
                        novoTotal = input('Novo total de compras: ')
                        x.totalCompras = novoTotal
                    
                    else:
                        print('\nOpção inválida!\n')

                else:
                    print('Não encontrado!')
        
        elif menu == '8':
            #Edita os dados de um funcionário no sistema
            editar = input('Quem você deseja editar? ')
            busca = 0

            for x in lista_funcionarios:
                if editar == x.nome:
                    print('Funcionário encontrado! Quais dados deseja editar?')
                    
                    escolha = input(f'\n|1| Nome\n|2| Data de nascimento\n|3| Gênero\n|4| CPF\n|5| E-mail\n|6| Matrícula\n|7| Salário\n|8| Data de admissão\n|9| Data de demissão\n|10| Vendas mensais\n\n>> ')

                    if escolha == '1':
                        novoNome = input('Novo nome: ')
                        x.nome = novoNome

                    elif escolha == '2':
                        novaDataNascimento = input('Nova data de nascimento: ')
                        x.dataNascimento = novaDataNascimento

                    elif escolha == '3':
                        novoGenero = input('Novo gênero: ')
                        x.genero = novoGenero
                    
                    elif escolha == '4':
                        novoCpf = input('Novo CPF: ')
                        x.cpf - novoCpf
                    
                    elif escolha == '5':
                        novoEmail = input('Novo e-mail: ')
                        x.email = novoEmail
                    
                    elif escolha == '6':
                        novaMatricula = input('Nova matrícula: ')
                        x.matricula = novaMatricula
                    
                    elif escolha == '7':
                        novoSalario = input('Novo salário: ')
                        x.salario = novoSalario
                    
                    elif escolha == '8':
                        novaDataAdmissao = input('Nova data de admissão: ')
                        x.dataAdmissao = novaDataAdmissao
                    
                    elif escolha == '9':
                        novaDataDemissao = input('Nova data de demissão: ')
                        x.dataDemissao = novaDataDemissao
                    
                    elif escolha == '10':
                        novaVendaMensal = input('Novo total de vendas mensais: ')
                        x.vendasMensais = novaVendaMensal
                    
                    else:
                        print('\nOpção inválida!\n')

                else:
                    print('Não encontrado!')

        elif menu == '9':
            #Excluir cliente
            excluir = int(input('Digite o código do cliente que você deseja excluir: '))

            del(lista_clientes[excluir])
            
            print('Cliente removido com sucesso!')

        elif menu == '10':
            #Excluir funcionário
            excluir = int(input('Digite o código do funcionário que você deseja excluir: '))

            del(lista_funcionarios[excluir])

            print('Funcionário removido com sucesso!')
        
        elif menu == '11':
            #Lista de produtos
            print('\nEstes são os produtos disponíveis:')
            index = 0

            for y in lista_produtos:
                print(f'-->> ({index}) {y.nome}')
                index = index+1
        
        elif menu == '12':
            #Cadastrar nova venda
            cod_cliente = int(input('Insira o código do cliente: '))
            cod_funcionario = int(input('Insira o código do funcionário: '))
            cod_produto = int(input('Insira o código do produto: '))
            quant_vendida = int(input('Quantidade vendida: '))

            #variável que armazena a venda realizada
            venda = Venda('1', cod_funcionario, cod_produto, lista_produtos[cod_produto].valor, cod_cliente, quant_vendida)
            
            #Soma a nova venda nas vendas mensais do funcionário
            lista_funcionarios[cod_funcionario].vendasMensais = venda.total 

            #Soma a nova venda nas compras realizadas pelo cliente
            lista_clientes[cod_cliente].totalCompras = venda.total 

            #Subtrai a quantidade de produtos vendidos da quantidade que tem no estoque
            lista_produtos[cod_produto].quantidade =  quant_vendida

            print(f'\n~°~VENDA REALIZADA COM SUCESSO!~°~\n\nProduto:  {lista_produtos[cod_produto].nome}\nValor do produto: {lista_produtos[cod_produto].valor}\nQuantidade adiquirida: {quant_vendida}\nCliente: {lista_clientes[cod_cliente].nome}\nFuncionário responsável: {lista_funcionarios[cod_funcionario].nome}\n\n| INFORMAÇÕES ADICIONAIS |\nVendas mensais atualizadas: {lista_funcionarios[cod_funcionario].vendasMensais}\nTotal de compras atualizada: {lista_clientes[cod_cliente].totalCompras}\nQuantidade do produto no estoque: {lista_produtos[cod_produto].quantidade}\n')

        elif menu == '0':
            #Sistema finalizando
            print('\nObrigada por utilizar sysElegancy, até a próxima...\n')
            run = False
            break
            
        else:
            #Opção inválida
            print('\nOpção inválida, insira um dos números indicados.\n')