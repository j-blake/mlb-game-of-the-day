from unittest import TestCase

from output import Console


class TestConsole(TestCase):
    out = None

    def setUp(self) -> None:
        self.out = Console()

    def test_format_ranked_games(self):
        self.assertEqual('No games today', self.out.format_ranked_games([]))
