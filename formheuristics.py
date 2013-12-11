# Imports
from formguideadapter import FormGuideAdapter
from fixturesadapter import FixturesAdapter
from clubnamematcher import ClubNameMatcher

class FormHeuristics:

    def __init__(self):
        self.fixturesAdapter = FixturesAdapter()
        self.formGuideAdapter = FormGuideAdapter()

        self.fixturesData = self.fixturesAdapter.getFixturesData()
        self.formGuideData = self.formGuideAdapter.getFormGuideData()
        
    # Returns a form discrepancy corresponding to each fixture row
    # -> List of (int, FixturesRow)
    # The discrepancy will be positive if its in the home team's favor and vice versa
    def getFormDiscrepancy(self):
        formDiscrepancyData = []

        for fixture in self.fixturesData:
            formDiscrepancyData.append((self.getFormRanking(fixture.awayTeam) - self.getFormRanking(fixture.homeTeam), fixture))

        return formDiscrepancyData

    # Returns current position in the form guide data for team
    # -> int
    def getFormRanking(self, team):
        clubNameMatcher = ClubNameMatcher()
        for formGuideRow in self.formGuideData:
            if (clubNameMatcher.isSameClub(formGuideRow.club, team)):
                return formGuideRow.currentPosition
        raise NameError("No matching form information found for " + team)

# Example call
# formHeuristics = FormHeuristics()
# formDiscrepancyData = formHeuristics.getFormDiscrepancy()
# for formDiscrepancy in formDiscrepancyData:
#     print str(formDiscrepancy[0])
#     print str(formDiscrepancy[1])
