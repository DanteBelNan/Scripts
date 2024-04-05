class Materia:
    def __init__(self,name,id,req_reg,req_apr,anual,hs):
        self.name = name
        self.id = id
        self.req_reg = req_reg
        self.req_apr = req_apr
        self.anual = anual
        self.hs = hs

    def __str__(self):
            duracion = "anual" if self.anual else "cuatrimestral"
            return f"Materia: {self.name}, ID: {self.id}, Requerimientos de regularizar: {self.req_reg}, Requerimientos de aprobar: {self.req_apr}, Es {duracion} y tiene carga de {self.hs}hs semanales"