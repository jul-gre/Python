class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_mass(self):
        self.mass1 = 25
        self.tolschina = 0.05
        asphalt_mass = self._length * self._width * self.mass1 * self.tolschina
        print(f'Для покрытия одного дорожного полотна необходимо {asphalt_mass} кг')

res = Road(20,5000)
res.asphalt_mass()
