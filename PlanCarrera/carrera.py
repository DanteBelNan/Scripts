from materia import Materia
import json

class Carrera:
    def __init__(self, name="Ingenieria en Sistemas"):
        self.name = name
        self.materias = []
        self._loadMaterias()

    def _addMateria(self, materia=[]):
        if(len(self.materias) > 0):
            for mat in self.materias:
                if mat.id == materia.id:
                    raise Exception(f"La materia {mat.name} ya esta cargada")
            for req_apr in materia.req_apr:
                exists = False
                for mat in self.materias:
                    if req_apr == mat.id:
                        exists = True
                if exists == False:
                    raise Exception(f"La correlativa para {materia.name}, {req_apr} no existe. carguela primero")
            for req_reg in materia.req_reg:
                exists = False
                for mat in self.materias:
                    if req_reg == mat.id:
                        exists = True
                if exists == False:
                    raise Exception(f"La correlativa para {materia.name}, {req_reg} no existe. carguela primero")
                
        self.materias.append(materia)


    def _loadMaterias(self):
        self.materias = []
        try:
            with open("PlanCarrera/materias.json", "r") as file:
                materias_json = json.load(file)

            for mat_json in materias_json:
                #Deberia de ver una forma de que esta carga sea mas dinamica, sin hardcodear los valores del json.
                materia = Materia(
                    mat_json["name"],
                    mat_json["id"],
                    mat_json["req_reg"],
                    mat_json["req_apr"],
                    mat_json["anual"],
                    mat_json["hs"]
                )
                #materia = Materia(mat_json)
                self._addMateria(materia)
            
        except Exception as error:
            print(f"Error: {error}")
    
    def showMaterias(self):
        for materia in self.materias:
            print(materia)

    def searchMateria(self,nombreMateria):
        for materia in self.materias:
            if materia.name == nombreMateria:
                idMateria = materia.id

        regs = self.getRegReg(idMateria)
        aprs = self.getRegApr(idMateria)


                    
    def getReqReg(self,idMateria):
        regs = []

        for materia in self.materias:
            if materia.id == idMateria:
                regs += materia.req_reg  
                pseudoregs = []
                for reg in regs:
                    pseudoregs += self.getReqReg(reg)
                
                regs += pseudoregs
        regs = list(set(regs)) # por algun tipo de razon magica, elimina los duplicados.
        return regs
    
    def getReqApr(self,idMateria):
        regs = []

        for materia in self.materias:
            if materia.id == idMateria:
                regs += materia.req_reg  
                pseudoregs = []
                for reg in regs:
                    pseudoregs += self.getReqApr(reg)
                
                regs += pseudoregs
        regs = list(set(regs)) # por algun tipo de razon magica, elimina los duplicados.
        return regs

                

    