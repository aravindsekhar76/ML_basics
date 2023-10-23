# main.py

from RPS_game import play, player, quincy, random_player, reflect, cycle, mr_defensive

# Test your player against different bots
play(player, quincy, 1000, verbose=True)
play(player, random_player, 1000, verbose=True)
play(player, reflect, 1000, verbose=True)
play(player, cycle, 1000, verbose=True)
play(player, mr_defensive, 1000, verbose=True)
