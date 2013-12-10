class FormGuideRow:
    def __init__(self):
        currentPosition = 0
        lastPosition = 0
        # Note that we are going to use the club name displayed
        # on the form table for now
        club = ""
        tableRank = 0
        homeForm = []
        homePoints = 0
        awayForm = []
        awayPoints = 0
        lastSixMatches = []
        totalPoints = 0

    def __str__(self):
        s = "Current Position: " + str(self.currentPosition) + "\n"
        s = s + "Last Position: " + str(self.lastPosition) + "\n"
        s = s + "Club: " + self.club + "\n"
        s = s + "Table Rank: " + str(self.tableRank) + "\n"
        s = s + "Home Form: " + str(self.homeForm) + "\n"
        s = s + "Home Points: " + str(self.homePoints) + "\n"
        s = s + "Away Form: " + str(self.awayForm) + "\n"
        s = s + "Away Points: " + str(self.awayPoints) + "\n"
        s = s + "Last Six Matches: " + str(self.lastSixMatches) + "\n"
        s = s + "Total Points: " + str(self.totalPoints) + "\n"
        return s
    
