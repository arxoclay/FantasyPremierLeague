# Imports
from formguideadapter import FormGuideAdapter
from fixturesadapter import FixturesAdapter
from clubnamematcher import ClubNameMatcher

class FormHeuristics:

    hotnessWeights = (50, 30, 10, 5, 3, 2)
    resultWeights = (100, 60, 0) # W,D,L
    
    def __init__(self):
        self.fixturesAdapter = FixturesAdapter()
        self.formGuideAdapter = FormGuideAdapter()

        self.fixturesData = self.fixturesAdapter.getFixturesData()
        self.formGuideData = self.formGuideAdapter.getFormGuideData()
        
    # Returns a form discrepancy corresponding to each fixture row
    # -> List of (int, FixturesRow)
    # The form discrepancy is computed by returning the difference of form table rankings
    # The discrepancy will be positive if its in the home team's favor and vice versa
    def getFormTableDiscrepancy(self):
        formDiscrepancyData = []

        for fixture in self.fixturesData:
            formDiscrepancyData.append((self.getFormRanking(fixture.awayTeam) - self.getFormRanking(fixture.homeTeam), fixture))

        return formDiscrepancyData

    # Returns the hotness discrepancy corresponding to each fixture row
    # -> List of (int, FixturesRow)
    # The weighted form over the last 6 matches is treated as the hotness of a team
    # The discrepancy will be positive if its in the home team's favor and vice versa
    def getHotnessDiscrepancy(self):
        hotnessDiscrepancyData = []

        for fixture in self.fixturesData:
            hotnessDiscrepancyData.append((self.getHotness(fixture.homeTeam) - self.getHotness(fixture.awayTeam), fixture))

        return hotnessDiscrepancyData

    # Returns current position in the form guide data for team
    # -> int
    def getFormRanking(self, team):
        clubNameMatcher = ClubNameMatcher()
        for formGuideRow in self.formGuideData:
            if (clubNameMatcher.isSameClub(formGuideRow.club, team)):
                return formGuideRow.currentPosition
        raise NameError("No matching form information found for " + team)

    # Returns "hotness" in the form guide data for team
    # -> int
    def getHotness(self, team):
        clubNameMatcher = ClubNameMatcher()
        for formGuideRow in self.formGuideData:
            if (clubNameMatcher.isSameClub(formGuideRow.club, team)):
                hotness = 0
                for i in range(len(formGuideRow.lastSixMatches)):
                    matchResult = formGuideRow.lastSixMatches[i]
                    if matchResult == "W":
                        hotness = hotness + (FormHeuristics.resultWeights[0] * FormHeuristics.hotnessWeights[i])
                    elif matchResult == "D":
                        hotness = hotness + (FormHeuristics.resultWeights[1] * FormHeuristics.hotnessWeights[i])
                # print "Hotness of " + team + " is " + str( hotness/100)
                return hotness/100                      
        raise NameError("No matching form information found for " + team)

# Example call
formHeuristics = FormHeuristics()
formDiscrepancyData = formHeuristics.getFormTableDiscrepancy()
hotnessDiscrepancyData = formHeuristics.getHotnessDiscrepancy()
print "----Form Discrepancy----"
for formDiscrepancy in formDiscrepancyData:
    print str(formDiscrepancy[0])
    print str(formDiscrepancy[1])
print "----Hotness Discrepancy----"
for hotnessDiscrepancy in hotnessDiscrepancyData:
    print str(hotnessDiscrepancy[0])
    print str(hotnessDiscrepancy[1])
     
