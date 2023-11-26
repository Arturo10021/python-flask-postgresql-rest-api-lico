class Bebida():
    def __init__(self, id=None, nombre=None, tipo_licor=None, precio=None, cantidad=None):
        self.id = id
        self.nombre = nombre
        self.tipo_licor = tipo_licor
        self.precio = precio
        self.cantidad = cantidad

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo_licor': self.tipo_licor,
            'precio': self.precio,
            'cantidad': self.cantidad
        }