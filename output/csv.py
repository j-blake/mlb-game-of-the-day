import csv
import os

from output import Output


class Csv(Output):
    def get_games_output(self, games: list):
        with open(os.path.expanduser('~/Desktop/mlb-game-of-the-day.csv'), 'w+')as file:
            writer = csv.DictWriter(file, games[0].keys())
            writer.writeheader()
            writer.writerows(games)
