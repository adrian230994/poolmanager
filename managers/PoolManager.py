class PoolManager:
    @staticmethod
    def add_player(pool, player):
        pool.players[player.name] = player

    @staticmethod
    def delete_player(player):
        if player is None:
            print("No existe el usuario")
        else:
            player.active = False
            print("Jugador %s eliminado con éxito" % player.name)

    @staticmethod
    def remove_ball(pool, points):
        if pool.number_balls > 0:
            pool.number_balls -= int(points)
        else:
            print("No hay más bolas")

    @staticmethod
    def finish_game(pool):
        pool.finish = True

    @staticmethod
    def print_summary(pool):
        print("FIN DEL JUEGO")
        for (name, player) in pool.players.items():
            print(player)
        print(pool)
        print("Quedan %s bolas sobre la mesa" % pool.number_balls)
