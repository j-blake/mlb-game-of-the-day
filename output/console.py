from string import Template


class Console:
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

    def get_games_output(self, games):
        return print(self.format_ranked_games(games))
