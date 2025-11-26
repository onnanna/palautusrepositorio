class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.equal_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.win_or_advantage()
        return self.normal_score()

    def equal_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        return "Deuce"

    def win_or_advantage(self):
        minus_result = self.m_score1 - self.m_score2

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        return "Win for player2"

    def normal_score(self):
        score = ""

        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score += "-"
                temp_score = self.m_score2
            score += self.get_score_name(temp_score)
        return score

    def get_score_name(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
        return ""
