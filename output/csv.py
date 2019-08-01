import csv
import os

from output import Output


class Csv(Output):
    def get_games_output(self, games: list):
        sorted_games = sorted(games, key=lambda g: g['rating'], reverse=True)
        with open(os.path.join(os.path.expanduser('~'), 'Desktop', 'mlb-game-of-the-day.csv'), 'w', newline='') as file:
            writer = csv.DictWriter(file, sorted_games[0].keys())
            writer.writeheader()
            writer.writerows(sorted_games)
