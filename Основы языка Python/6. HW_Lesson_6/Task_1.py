# 1. Создать класс TrafficLight (светофор).

from time import *

class TrafficLight:
    color = ['Красный', 'Желтый', 'Зеленый']

    def run(self):
        i = 0
        while i != 3:
            print(TrafficLight.color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1

t = TrafficLight()
t.run()