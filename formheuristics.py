# Imports
from formguideadapter import FormGuideAdapter
from fixturesadapter import FixturesAdapter

class FormHeuristics:

    def __init__(self):
        self.fixturesAdapter = FixturesAdapter()
        self.formGuideAdapter = FormGuideAdapter()

        self.fixturesData = self.fixturesAdapter.getFixturesData()
        self.formGuideData = self.formGuideAdapter.getFormGuideData()
        
    # Returns a form discrepancy corresponding to each fixture row
    # -> List of (int, FixturesRow)
    def getFormDiscrepancy(self):
        formDiscrepancyData = []

        for fixture in self.fixturesData:
            formDiscrepancyData.append((self.getFormRanking(fixture.homeTeam) - self.getFormRanking(fixture.awayTeam), fixture))

        return formDiscrepancyData

    # Returns current position in the form guide data for team
    # -> int
    def getFormRanking(self, team):
        for formGuideRow in self.formGuideData:
            if formGuideRow.club == team:
                return formGuideRow.currentPosition
        print "Nothing found for " + team
        return 0

# Example call
formHeuristics = FormHeuristics()
formDiscrepancyData = formHeuristics.getFormDiscrepancy()
for formDiscrepancy in formDiscrepancyData:
    print str(formDiscrepancy[0]) + str(formDiscrepancy[1])
