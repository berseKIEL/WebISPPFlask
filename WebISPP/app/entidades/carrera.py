from ..common.request import get_request_json

class Carrera():
    def __init__(self, CarreraID, CarreraNombre) -> None:
        self.CarreraID = CarreraID
        self.CarreraNombre = CarreraNombre
    
    @classmethod
    def buscarAPI(self):
        listacar= []
        listaCarreras = get_request_json("http://127.0.0.1:5000/api/v1.0/carreras/").json()
        for item in listaCarreras:
            listacar.append(list(item.values()))
        return listacar