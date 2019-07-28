import csv
import datetime
from unittest import TestCase
from index import Index


class TestIndex(TestCase):
    _mlb = None
    _data = []
    _games = []

    def setUp(self) -> None:
        self._mlb = Index('https://projects.fivethirtyeight.com/mlb-api/mlb_elo_latest.csv')
        today = datetime.date.today().isoformat()
        self._data = [
            {'date': today, 'team1': 'BOS', 'team2': 'NYY', 'rating1_pre': '1553.978383', 'rating2_pre': '1577.287098', 'score1': '', 'score2': ''},
            {'date': today, 'team1': 'SEA', 'team2': 'DET', 'rating1_pre': '1465.969521', 'rating2_pre': '1400.125175', 'score1': '', 'score2': ''},
            {'date': today, 'team1': 'SDP', 'team2': 'SFG', 'rating1_pre': '1478.476255', 'rating2_pre': '1483.525948', 'score1': '', 'score2': ''},
            {'date': today, 'team1': 'OAK', 'team2': 'TEX', 'rating1_pre': '1533.82836', 'rating2_pre': '1482.208556', 'score1': '', 'score2': ''},
            {'date': today, 'team1': 'ANA', 'team2': 'BAL', 'rating1_pre': '1508.112092', 'rating2_pre': '1416.839614', 'score1': '', 'score2': ''},
            {'date': today, 'team1': 'STL', 'team2': 'HOU', 'rating1_pre': '1525.354599', 'rating2_pre': '1576.318804', 'score1': '2', 'score2': '6'},
            {'date': today, 'team1': 'KCR', 'team2': 'CLE', 'rating1_pre': '1445.033261', 'rating2_pre': '1547.549023', 'score1': '9', 'score2': '6'},
            {'date': today, 'team1': 'MIL', 'team2': 'CHC', 'rating1_pre': '1517.557536', 'rating2_pre': '1531.10697', 'score1': '4', 'score2': '11'},
            {'date': today, 'team1': 'CHW', 'team2': 'MIN', 'rating1_pre': '1454.105141', 'rating2_pre': '1536.932884', 'score1': '1', 'score2': '11'},
            {'date': today, 'team1': 'WSN', 'team2': 'LAD', 'rating1_pre': '1533.715203', 'rating2_pre':  '1587.920402', 'score1': '11', 'score2': '4'},
            {'date': today, 'team1': 'NYM', 'team2': 'PIT', 'rating1_pre': '1509.833102', 'rating2_pre':  '1486.175166', 'score1': '8', 'score2': '7'},
            {'date': today, 'team1': 'FLA', 'team2': 'ARI', 'rating1_pre': '1442.316268', 'rating2_pre':  '1515.463816', 'score1': '5', 'score2': '1'},
            {'date': today, 'team1': 'CIN', 'team2': 'COL', 'rating1_pre': '1504.54197', 'rating2_pre':  '1500.873062', 'score1': '3', 'score2': '2'},
            {'date': today, 'team1': 'TOR', 'team2': 'TBD', 'rating1_pre': '1462.464636', 'rating2_pre':  '1532.676135', 'score1': '9', 'score2': '10'},
            {'date': today, 'team1': 'PHI', 'team2': 'ATL', 'rating1_pre': '1507.87584', 'rating2_pre':  '1531.83517', 'score1': '9', 'score2': '4'}
        ]

    def test_fetch_data(self):
        self.assertTrue(isinstance(self._mlb.fetch_data(), csv.DictReader))

    def test_prepare_data(self):
        data = self._mlb.prepare_data(self._data)
        self.assertTrue(data, list)

    def test_print_ranked_games(self):
        self.assertEqual('No games today', self._mlb.format_ranked_games([]))
