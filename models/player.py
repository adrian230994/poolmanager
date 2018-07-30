class Player:
    name = ""
    points = 0
    active = True
    type_ball = ""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "El jugador %s ha conseguido %s puntos con la bola %s y activo = %s" % (self.name, self.points, self.type_ball, self.active)