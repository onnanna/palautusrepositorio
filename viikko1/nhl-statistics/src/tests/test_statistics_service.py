import unittest

from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_existing_player(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_non_existing_player(self):
        player = self.stats.search("NonExistent")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        player_names = [player.name for player in edm_players]
        self.assertIn("Semenko", player_names)
        self.assertIn("Kurri", player_names)
        self.assertIn("Gretzky", player_names)

    def test_top_returns_requested_number(self):
        top_players = self.stats.top(3)
        # should return 3 players sorted by points descending
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # 124 points
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 points
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 points

    def test_top_by_assists(self):
        top_assists = self.stats.top(2, sort_by=SortBy.ASSISTS)
        self.assertEqual(len(top_assists), 2)
        self.assertEqual(top_assists[0].name, "Gretzky")
        self.assertEqual(top_assists[1].name, "Yzerman")

    def test_top_by_goals(self):
        top_goals = self.stats.top(2, sort_by=SortBy.GOALS)
        self.assertEqual(len(top_goals), 2)
        self.assertEqual(top_goals[0].name, "Lemieux")
        self.assertEqual(top_goals[1].name, "Yzerman")

    def test_top_how_many_zero_or_negative(self):
        self.assertEqual(self.stats.top(0), [])
        self.assertEqual(self.stats.top(-5), [])

    def test_top_more_than_available_returns_all(self):
        all_players = self.stats.top(10)
        self.assertEqual(len(all_players), 5)
        self.assertEqual(all_players[0].name, "Gretzky")


if __name__ == "__main__":
    unittest.main()
