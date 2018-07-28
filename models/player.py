class Player:
    name = ""
    points = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "El jugador %s ha conseguido %s puntos" % (self.name, self.points)