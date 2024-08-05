class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, enginePower):
        self.owner = owner
        self.__model = model

        self.__color = color
        self.__enginePower = int(enginePower)

    def getModel(self):
        return '{:<25}{:<10}'.format('Модель: ', self.__model)

    def getHorsepower(self):
        return '{:<25}{:<10}'.format('Мощность двигателя: ', self.__enginePower)

    def getColor(self):
        return '{:<25}{:<10}'.format('Цвет: ', self.__color)

    def printInfo(self):
        print(self.getModel())
        print(self.getHorsepower())
        print(self.getColor())
        print('{:<25}{:<10}'.format('Владелец:', self.owner))

    def setColor(self, newColor):
        if newColor.lower() in self.__COLOR_VARIANTS:
            self.__color = newColor
        else:
            print(f'Нельзя сменить цвет на {newColor}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.printInfo()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.setColor('Pink')
    vehicle1.setColor('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.printInfo()

    a = 10
