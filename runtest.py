import models


pole = models.Pole(name='Pole one')
pole.create()
pole.view_pole()

ship = models.Ship(pole=pole, length=3, vector='down', point=('a', 3))
ship.show()
ship.place()
