class Pool:
    finish = False
    players = {}
    number_balls = 15

    def __str__(self):
        return " - ".join(["%s (%s)" % (name, player.points) for (name, player) in self.players.items()])
