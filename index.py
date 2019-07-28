import csv
import urllib.error
import requests
import datetime
from string import Template


class Index:
    _url = ''

    def __init__(self, url):
        self._url = url

    def run(self):
        resource = self.fetch_data()
        data = self.prepare_data(resource)
        print(self.format_ranked_games(data))

    def fetch_data(self):
        try:
            response = requests.get(self._url)
            if response.status_code != 200:
                err = Template('Got an error trying to request $url')
                raise urllib.error.URLError(err.substitute(url=self._url))
            data = response.content.decode('utf-8').splitlines()
            return csv.DictReader(data)
        except urllib.error.URLError as err:
            print('Something went wrong!\n', str(err))
            return None

    @staticmethod
    def prepare_data(iterable):
        games = []
        try:
            for row in iterable:
                if row['date'] != datetime.date.today().isoformat():
                    continue
                game = {
                    'home': row['team1'],
                    'away': row['team2'],
                    'rating': int(float(row['rating1_pre']) + float(row['rating2_pre'])),
                    'home_score': row['score1'],
                    'away_score': row['score2'],
                    'home_prob': int(float(row['elo_prob1']) * 100),
                    'away_prob': int(float(row['elo_prob2']) * 100)
                }
                games.append(game)
        except TypeError as err:
            print('Something went wrong!\n', str(err))
        return games

    @staticmethod
    def format_ranked_games(games):
        if len(games) == 0:
            return 'No games today'
        out = ''
        sorted_games = sorted(games, key=lambda g: g['rating'], reverse=True)
        for idx, game in enumerate(sorted_games):
            template = Template('$rank\t$away_team$away_prob @ $home_team$home_prob'
                                '\t$rating\t$away_score-$home_score\n')
            out += (template.substitute(
                rank='{0:02d}'.format(idx + 1),
                away_team=game['away'],
                home_team=game['home'],
                rating=str(game['rating']),
                away_score=game['away_score'],
                home_score=game['home_score'],
                home_prob=('(' + str(game['home_prob']) + '%)' if game['home_prob'] > game['away_prob'] else ''),
                away_prob=('(' + str(game['away_prob']) + '%)' if game['away_prob'] > game['home_prob'] else '')
            ))
        return out


if __name__ == "__main__":
    Index('https://projects.fivethirtyeight.com/mlb-api/mlb_elo_latest.csv').run()
