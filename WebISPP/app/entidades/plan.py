class PlandeEstudio():
    def __init__(self, PlanID, PlanNombre) -> None:
        self.PlanID = PlanID
        self.PlanNombre = PlanNombre
    
    @classmethod
    def buscarAPI(self):
        listaPlan= []
        listaPlanes = get_request_json("http://127.0.0.1:5000/api/v1.0/planes/").json()
        for item in listaPlanes:
            listaPlan.append(list(item.values()))
        return listaPlan