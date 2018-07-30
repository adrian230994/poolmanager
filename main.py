from models.player import Player
from models.pool import Pool
from managers.PlayerManager import PlayerManager
from managers.PoolManager import PoolManager


pool = Pool()
yes = "s"
delete = "n"

while yes == "s":
    name = input("Introduce el nombre")
    player = Player(name)
    PoolManager.add_player(pool, player)
    yes = input("Agregar otro usuario s/n")

if yes == "n":
    delete = input("Desea elminar algún jugador s/n")
    if delete != "n":
        name = input("Introduce el nombre")
        player = pool.players.get(name)
        PoolManager.delete_player(player)

while not pool.finish:
    for (name, player) in pool.players.items():
        if player.active:
            if pool.finish:
                print("Fin del juego")
                break
            points = input("Puntos para %s" % player.name)
            PlayerManager.add_points(player, points)
            PoolManager.remove_ball(pool, points)
            finish = input("Desea terminar? s/n")
            if finish == "s":
                PoolManager.finish_game(pool)

PoolManager.print_summary(pool)
