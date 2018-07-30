class Player:
    name = ""
    points = 0
    active = True

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "El jugador %s ha conseguido %s puntos y activo = %s" % (self.name, self.points, self.active)