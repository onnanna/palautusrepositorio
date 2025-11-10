class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality, season):
        players = self.reader.get_players_by_season(season)
        filtered_players = [player for player in players if player.natinality == nationality]
        filtered_players.sort(key=lambda player: player.points(), reverse=True)
        return filtered_players

    def all_players(self):
        return self.reader.get_players()
