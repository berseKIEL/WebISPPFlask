
class Orientacion():
    def __init__(self, OrientacionID, OrientacionNombre) -> None:
        self.OrientacionID = OrientacionID
        self.OrientacionNombre = OrientacionNombre
    
    @classmethod
    def buscarAPI(self):
        listaOri= []
        listaOrientaciones = get_request_json("http://127.0.0.1:5000/api/v1.0/orientaciones/").json()
        for item in listaOrientacion:
            listaOri.append(list(item.values()))
        return listaOri
