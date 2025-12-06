from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self):
        self.matcher = All()

    def plays_in(self, team):
        self.matcher = And(self.matcher, PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self.matcher = And(self.matcher, HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self.matcher = And(self.matcher, HasFewerThan(value, attr))
        return self
    
    def one_of(self, *matchers):
        self.matcher = Or(*matchers)
        return self

    def build(self):
        return self.matcher

