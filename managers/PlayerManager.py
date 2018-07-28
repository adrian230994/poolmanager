class PlayerManager:
    @staticmethod
    def add_points(player, points):
        if int(points) < 0:
            print("No")
        else:
            player.points += int(points)
