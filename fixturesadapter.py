# Imports
from fixturesscraper import FixturesScraper
from bs4 import BeautifulSoup
from fixturesrow import FixturesRow
from datetime import datetime
from datetime import date

class FixturesAdapter:

    def getFixturesData(self):
        fixturesScraper = FixturesScraper()
        rawData = fixturesScraper.getFixturesData()
        rawDataSoup = BeautifulSoup(rawData)
        fixturesData = []
        for tr in rawDataSoup.tbody.contents:
            if isinstance(tr, basestring):
                continue
            fixturesRow = FixturesRow()
            tdCounter = 0
            for td in tr.contents:
                if isinstance(td, basestring):
                    continue
                else:
                    tdCounter = tdCounter + 1
                    if tdCounter == 1:
                        fixturesRow.dateTimeOfMatch = date_object = datetime.strptime(td.contents[0] + " " + str(self.getRelevantYear(td.contents[0])), '%d %b %H:%M %Y')
                    elif tdCounter == 2:
                        fixturesRow.homeTeam = td.contents[0]
                    elif tdCounter == 3:
                        continue
                    elif tdCounter == 4:
                        continue
                    elif tdCounter == 5:
                        continue
                    elif tdCounter == 6:
                        fixturesRow.awayTeam = td.contents[0]
                        tdCounter = 0
                        fixturesData.append(fixturesRow)
                        fixturesRow = FixturesRow()
        return fixturesData

    def getRelevantYear(self, fixtureDateTime):
        monthToday = date.today().month
        yearToday = date.today().year
        fixtureMonth = datetime.strptime(fixtureDateTime, '%d %b %H:%M').date().month
        if (fixtureMonth < monthToday):
            return yearToday + 1
        else:
            return yearToday

          
# Example call
# fixturesAdapter = FixturesAdapter()
# print fixturesAdapter.getFixturesData()[0]
