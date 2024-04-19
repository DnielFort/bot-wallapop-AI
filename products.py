class Product:
    def __init__(self, link=None, titulo=None, precio=None, descripcion=None):
        self.link = link
        self.titulo = titulo
        self.precio = precio
        self.descripcion = descripcion
        self.location = None
    def set_link(self, link):
        self.link = link
    def get_link(self):
        return self.link
    def set_name(self, titulo):
        self.titulo = titulo
    def get_name(self):
        return self.titulo
    def set_price(self, precio):
        self.precio = precio
    def get_price(self):
        return self.precio
    def set_description(self, descripcion):
        self.descripcion = descripcion
    def get_description(self):
        return self.descripcion
    def set_location(self, location):
        self.location = location
    def get_location(self):
        return self.location
    
    