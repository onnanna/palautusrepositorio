class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.natinality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']
        self.games = player_dict['games']

    def points(self):
        return self.assists + self.goals

    def __str__(self):
        return f"{self.name:20} {self.team:15}  {self.goals} + {self.assists} = {self.points()}"
