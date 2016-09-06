import time

class Combat():

    def showRound(player, enemy, enemy_hit):
        player_hpbar = player.hpBar()
        enemy_hpbar = enemy.hpBar()

        print("")
        print("{}  {} You:  Enemy:{}".format(player_hpbar,enemy_hpbar,enemy_hit))
        print("")

    def fight(player,enemy):
        while (player.alive == True) and (enemy.alive == True) and (player.flee == False):
            player.takeDamage(10)
            enemy.takeDamage(1)
            Combat.showRound(player,enemy,10)
            time.sleep(1)
        

