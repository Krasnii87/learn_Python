# 2. Реализовать класс Road (дорога).

class Road:

    def __init__(self, length, width, weight, height):
        self.length = length
        self.width = width
        self.weight = weight
        self.height = height

    def asphalt_mass(self):
        asphalt_mass = self.length * self.width * self.weight * self.height / 1000
        print('Для покрытия всего дорожного полотна неободимо', round(asphalt_mass), 'тонны асфальта')

r = Road(int(input('Введите длину асфальта в метрах: ')), int(input('Введите ширину асфальта в метрах: ')),
         int(input('Введите массу асфальта в килограммах: ')), int(input('Введите толщину асфальта в сантиметрах: ')))
r.asphalt_mass()