class FixturesRow:
    def __init__(self):
        self.dateTimeOfMatch = ""
        self.homeTeam = ""
        self.awayTeam = ""

    def __str__(self):
        s = "Date-Time of match: " + str(self.dateTimeOfMatch) + "\n"
        s = s + "Home Team: " + str(self.homeTeam) + "\n"
        s = s + "Away Team: " + str(self.awayTeam) + "\n"
        return s
