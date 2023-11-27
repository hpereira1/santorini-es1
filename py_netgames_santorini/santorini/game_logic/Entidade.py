class Entidade:
    def __init__(self):
        self._coordenada_xyz = list 
        self._id = 0

    def set_coordenada_xyz(self, coordenada_xyz):
        self._coordenada_xyz = coordenada_xyz

    def get_coordenada_xyz(self):
        return self._coordenada_xyz

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id
