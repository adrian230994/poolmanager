class PlayerManager:
    @staticmethod
    def add_points(player, points):
        if int(points) < 0 or int(points) > 7:
            print("Error al introducir puntuación")
        else:
            player.points += int(points)

    @staticmethod
    def add_type_ball(player, type_ball):
        player.type_ball = type_ball