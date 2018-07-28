class Pool:
    finish = False
    players = {}

    def __init__(self):
        pass

    def __str__(self):
        return " - ".join(["%s (%s)" % (name, player.points) for (name, player) in self.players.items()])
        '''result = ""
        sep = " - "
        lista = []
        # return "jugadores %s" % self.players
        for (name, player) in self.players.items():
            result += player.name + player.points + sep

        return result[:-len(sep)]'''