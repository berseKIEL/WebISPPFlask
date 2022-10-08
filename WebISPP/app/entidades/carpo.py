class Carpo():
    def __init__(self, CarpoID, CarreraID, OrientacionID, PlanDeEstudioID,CarpoPrograma):
        self.CarpoID = CarpoID
        self.CarreraID = CarreraID
        self.OrientacionID = OrientacionID
        self.PlanDeEstudioID = PlanDeEstudioID
        self.CarpoPrograma = CarpoPrograma

    @classmethod
    def buscarAPI(self):
        listacarpos = []
        listaCARPOS = get_request_json(
            "http://127.0.0.1:5000/api/v1.0/carpos/").json()
        for item in listaCARPOS:
            listacarpos.append(list(item.values()))
        return listacarpos
    
    @classmethod
    def noOrientacion(self,carreraid):
        pass