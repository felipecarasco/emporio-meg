import os
import platform
import getpass

from pymongo import MongoClient


class EmporioMeg(object):
    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://app_emporio:HuzjidytC5t1CvMe@clustercarasco-tekdv.mongodb.net/EmporioMeg?retryWrites=true&w=majority")

    def run(self):
        self.exibir_menu_inicial()
        opcao_selecionada = self.selecionar_opcao()

        while opcao_selecionada != 0:
            self.limpar_tela()

            if opcao_selecionada == 1:               
                print("#### LOGIN ####\n")       
                login = input("USUÁRIO: ")
                senha = getpass.getpass("SENHA: ")

                self.limpar_tela()
                print('###############################')
                print('      SISTEMA EMPÓRIO MEG      ')
                print('###############################\n')

                print('1 - ADMINISTRADOR')
                print('2 - SEGURANÇA')
                print('3 - ESTOQUE')
                print('4 - CAIXA')
                print('5 - FINANCEIRO')
                print('0 - VOLTAR') 

                opcao_selecionada = self.selecionar_opcao()

                while opcao_selecionada != 0:
                    self.limpar_tela()

                    if opcao_selecionada == 1: 
                        print("#### ADMINISTRADOR ####\n")                        
                    elif opcao_selecionada == 2: 
                        print("#### SEGURANÇA ####\n")
                        print('1 - CADASTRAR USUÁRIO')
                        print('2 - BUSCAR USUÁRIO')
                        print('3 - LISTAR USUÁRIOS')
                        print('0 - VOLTAR')                         
                    elif opcao_selecionada == 3: 
                        print("#### ESTOQUE ####\n")
                        print('1 - CADASTRAR PRODUTO')
                        print('2 - BUSCAR PRODUTO')
                        print('3 - EXIBIR ESTOQUE')
                        print('0 - VOLTAR')                         
                    elif opcao_selecionada == 4: 
                        print("#### CAIXA ####\n")
                        print('1 - ABRIR CAIXA')
                        print('2 - REGISTRAR COMPRA')
                        print('3 - FECHAR CAIXA')
                        print('0 - VOLTAR')                         
                    elif opcao_selecionada == 5: 
                        print("#### FINANCEIRO ####\n")
                        print('1 - RELATÓRIO DIÁRIO')
                        print('2 - RELATÓRIO MENSAL')
                        print('0 - VOLTAR')                         
                    else:                
                        print("OPÇÃO INDISPONÍVEL.")                
                        
                    input("\nPRESSIONE ENTER PARA CONTINUAR...")
                    self.limpar_tela()
                    print('###############################')
                    print('      SISTEMA EMPÓRIO MEG      ')
                    print('###############################\n')

                    print('1 - ADMINISTRADOR')
                    print('2 - SEGURANÇA')
                    print('3 - ESTOQUE')
                    print('4 - CAIXA')
                    print('5 - FINANCEIRO') 
                    print('0 - VOLTAR')       
                    opcao_selecionada = self.selecionar_opcao()

                

                '''
                banco = self.cliente["EmporioMeg"]
                usuario = banco["Usuario"]

                a = usuario.find_one({"usuario": login})
                if senha==a["senha"]:
                    print("LOGIN REALIZADO COM SUCESSO")
                else:
                    print("USUÁRIO OU SENHA INVÁLIDO")
                '''

            elif opcao_selecionada == 2:                
                print("#### AJUDA ####\n")
                print("VERSÃO: 1.0.0")
                print("CRIADO POR: FELIPE CARASCO")
                input("\nPRESSIONE ENTER PARA CONTINUAR...")

            else:                
                print("OPÇÃO INDISPONÍVEL.")  
                input("\nPRESSIONE ENTER PARA CONTINUAR...")              
                
            
            self.limpar_tela()
            self.exibir_menu_inicial()            
            opcao_selecionada = self.selecionar_opcao()
        else:
            self.limpar_tela()
            print("SAINDO...")

    def exibir_titulo_sistema(self):
        print('###############################')
        print('          EMPÓRIO MEG          ')
        print('###############################\n')

    def exibir_menu_inicial(self):
        self.exibir_titulo_sistema()
        print('1 - LOGIN')
        print('2 - AJUDA')
        print('0 - SAIR')  

    def limpar_tela(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def selecionar_opcao(self):        
        opcao = int(input("\nSELECIONE UMA OPÇÃO: "))
        return opcao

       

    