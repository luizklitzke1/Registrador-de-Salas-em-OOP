import registradorSalas.gerenciador as ger
import registradorSalas.interface as inter

class Interface(object):
    def menu(self):
        print("       [Lista de Funções]")
        print("     +-----------------------------+")
        print("     | 1 - Registrar Sala          |")
        print("     | 2 - Editar Sala             |")
        print("     | 3 - Remover Sala            |")
        print("     | 4 - Procurar Sala           |")
        print("     | 5 - Mostrar as Salas        |")
        print("     | 6 - Parar a execução        |")
        print("     +-----------------------------+")
        
    def registro_geral(self):
        interface = inter.Interface()
        gerenciador = ger.Gerenciador()
        print("\n +-------------------------------------[REGISTRO DE SALAS]-------------------------------------+ \n")
        interface.menu()
        operacao = 0
        while operacao != 6:
            operacao = (input("\n [O que deseja realizar?]  (Digite 0 para rever as opções)              "))
            print(" \n")
            if operacao == "0":
                interface.menu()    
            elif operacao == "1":
                num_sala = input("Qual o número do sala? (Ex: D04, C12)    ")
                materia = input("Qual a matéria na sala? ")
                professor = input("Qual será o professor? ")
                periodo = input("Qual o periodo? ")
                result = gerenciador.registrar_sala(num_sala, materia, professor, periodo)
                if result == 1:
                    print ("ERRO: Valore(s) inválidos!")
                elif result == 2:
                    print("Sala: ", num_sala, " registrada!" )
                elif result == 3:
                    print("ERRO: Sala: ", num_sala, " já existe!" )


            elif operacao == "2":
                num_sala = input("Qual sala você deseja mudar? ")
                oq_mudar = input("O que você deseja mudar?  (materia, professor ou periodo)  ")
                valor_novo = input("Qual você quer que seja o valor novo? ")
                if (gerenciador.editar_sala(num_sala, oq_mudar, valor_novo)) == True:
                    print("A sala ", num_sala, " foi editada com sucesso!")
                else:
                    print("ERRO: A sala ", num_sala, " não foi encontrada ou valor informado é inválido!")   

            elif operacao == "3": 
                num_sala = input("Qual sala você deseja remover? ")
                if (input("Deseja realmente apagar a sala: ?   1- Sim   2 - Não ")) == "2":
                    print("Processo cancelado.")
                else:
                    if(gerenciador.remover_sala(num_sala) == True):
                        print("A sala ", num_sala, " foi removida!")
                    else:
                        print("ERRO: A sala ", num_sala, " não foi encontrada!")  

            elif operacao == "4":
                num_sala = input("Qual sala você deseja procurar? ")
                if (gerenciador.procurar_sala(num_sala) == False):
                    print ("Sala ", num_sala, " não foi encontrada!")   
                else:    
                    achados = gerenciador.procurar_sala(num_sala)
                    print("\n+--------------------------------------------")
                    print("| Sala: ", achados.getNum_sala(), " Matéria: ", achados.getMateria())
                    print("| Professor: ", achados.getProfessor(), " Periodo: ", achados.getPeriodo())

            elif operacao == "5":
                gerenciador.mostrar_salas()
            else:
                print("Execução Finalizada!")
                break    

