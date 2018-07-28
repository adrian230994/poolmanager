from models.player import Player
from models.pool import Pool
from managers.PlayerManager import PlayerManager
from managers.PoolManager import PoolManager


pool = Pool()
yes = "s"

while yes == "s":
    name = input("Introduce el nombre")
    player = Player(name)
    PoolManager.add_player(pool, player)
    yes = input("Agregar otro usuario s/n")

while not pool.finish:
    for (name, player) in pool.players.items():
        if pool.finish:
            print("Fin del juego")
            break
        points = input("Puntos para %s" % player.name)
        PlayerManager.add_points(player, points)
        finish = input("Desea terminar? s/n")
        pool.finish = finish == "s"

for (name, player) in pool.players.items():
    print(player)

print(pool)
