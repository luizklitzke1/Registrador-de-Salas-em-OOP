import registradorSalas.sala as sl

class Gerenciador(object):

    def __init__(self):
        self.lista_salas = [ ]

    def registrar_sala(self, num_sala, materia, professor, periodo):
        exist = 0
        if num_sala == "" or materia == "" or professor == "" or  periodo == "":
            return 1 

        sala_temp = sl.Sala(num_sala, materia, professor, periodo)

        for sala in self.lista_salas:
            if sala.getNum_sala() == sala_temp.getNum_sala():
                exist = 1
        if exist != 1:        
            self.lista_salas.append(sala_temp)
            return 2
        else:
            return 3  

    def editar_sala(self, num_sala,oq_mudar,valor_novo):
        found = 0         
        for sala in self.lista_salas:
            if sala.getNum_sala() == num_sala:
                if oq_mudar == "num_sala":
                    return False
                if oq_mudar == "materia":
                    sala.setMateria(valor_novo) 
                if oq_mudar == "professor":
                    sala.setProfessor(valor_novo)   
                if oq_mudar == "periodo":
                    sala.setPeriodo(valor_novo)       
                found = 1
        if found == 1:  
            return True
        elif found == 0:
            return False

    def remover_sala(self, num_sala):
        found = 0
        for salax in self.lista_salas:
            if salax.getNum_sala() == num_sala:
                self.lista_salas.remove(salax)
                found = 1
        if found == 1:        
            return True
        else:
            return False

    def procurar_sala(self, num_sala):
        found = 0
        for sala in self.lista_salas:
            if sala.getNum_sala() == num_sala:
                found = 1
                return (sala)            
        return False 

    def mostrar_salas(self):
        if len(self.lista_salas) == 0:
            print("Ainda não foi registrada nenhuma sala!")
        else:    
            for sala in self.lista_salas:
                print("+-------------------------------------------")
                print("| Sala: ", sala.getNum_sala(), "Matéria: ", sala.getMateria())
                print("| Professor: ", sala.getProfessor(), "Periodo: ",sala.getPeriodo(), "\n")
                
                
        
