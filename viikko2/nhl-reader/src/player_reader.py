import requests

from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=5).json()
        players = [Player(player_data) for player_data in response]
        return players

    def get_players_by_season(self, season):
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        response = requests.get(url, timeout=5).json()
        players = [Player(player_data) for player_data in response]
        return players
