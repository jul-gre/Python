class Stationery:
    title = None
    def draw(self):
        print("Запуск")

class Pen(Stationery):
    title = "ручка"
    def draw(self):
        print(f"{self.title} пишет")

class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        print(f"{self.title} чертит")

class Handle(Stationery):
    title = "маркер"

    def draw(self):
        print(f"{self.title} рисует")

stationery = Stationery()
stationery.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
