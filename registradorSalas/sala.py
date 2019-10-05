class Sala(object):
   
    def __init__(self,num_sala, materia, professor, periodo):
        self.setNum_sala(num_sala)
        self.setMateria(materia)
        self.setProfessor(professor)
        self.setPeriodo(periodo)

    def setNum_sala(self, num_sala):
        self.num_sala = num_sala
    def setMateria(self ,materia):
        self.materia = materia
    def setProfessor(self, professor):
        self.professor = professor
    def setPeriodo(self, periodo):
        self.periodo = periodo


    def getNum_sala(self):
        return self.num_sala
    def getMateria(self):
        return self.materia 
    def getProfessor(self):
        return self.professor
    def getPeriodo(self):
        return self.periodo

  
  