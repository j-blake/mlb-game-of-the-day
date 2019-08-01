import csv
import importlib
import urllib.error
import requests
import datetime
from string import Template
import sys

import output


class Index:
    _url = 'https://projects.fivethirtyeight.com/mlb-api/mlb_elo_latest.csv'
    _date = None
    _output = None

    def __init__(
            self,
            output_generator,
            date=datetime.date.today().isoformat()
    ):
        self._date = date
        self._output = output_generator

    def run(self):
        resource = self.fetch_data()
        data = self.prepare_data(resource, self._date)
        return self._output.get_games_output(data)

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
    def prepare_data(iterable, date):
        games = []
        try:
            for row in iterable:
                if row['date'] != date:
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


if __name__ == "__main__":
    module_name = sys.argv[1]
    try:
        module = importlib.import_module('output.' + str(module_name).lower())
        module_name = str(module_name).capitalize()
        output_class = getattr(module, module_name)
        instance = output_class()
    except ModuleNotFoundError as err:
        print('Something went wrong!\n---' + str(err) + '---\n\n')
        instance = output.Console()
    Index(instance).run()
