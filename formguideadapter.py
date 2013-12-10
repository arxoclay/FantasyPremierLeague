# Imports
from formguidescraper import FormGuideScraper
from bs4 import BeautifulSoup
from formguiderow import FormGuideRow

class FormGuideAdapter:
    
    def getFormGuideData(self):
        formGuideScraper = FormGuideScraper()
        rawData = formGuideScraper.getFormGuideData()
        rawDataSoup = BeautifulSoup(rawData)
        formGuideData = []
        for tr in rawDataSoup.tbody.contents[:2]:
            if isinstance(tr, basestring):
                continue
            formGuideRow = FormGuideRow()
            tdCounter = 0
            for td in tr.contents:
                if isinstance(td, basestring):
                    continue
                else:
                    tdCounter = tdCounter + 1
                    if tdCounter == 1:
                        formGuideRow.currentPosition = int(td.contents[0])
                    elif tdCounter == 2:
                        continue
                    elif tdCounter == 3:
                        formGuideRow.lastPosition = int(td.contents[0][1:-1])
                    elif tdCounter == 4:
                        formGuideRow.club = str(td.contents[0].contents[0])
                    elif tdCounter == 5:
                        formGuideRow.tableRank = int(td.contents[0])
                    elif tdCounter == 6:
                        formGuideRow.homeForm = td.contents
                    elif tdCounter == 7:
                        formGuideRow.homePoints = int(td.contents[0])
                    elif tdCounter == 8:
                        formGuideRow.awayForm = td.contents
                    elif tdCounter == 9:
                        formGuideRow.awayPoints = int(td.contents[0])
                    elif tdCounter == 10:
                        formGuideRow.lastSixMatches = td.contents
                    elif tdCounter == 11:
                        formGuideRow.totalPoints = int(td.contents[0])
            formGuideData.append(formGuideRow)
        print formGuideData[0]

        
# Example call
formGuideAdapter = FormGuideAdapter()
formGuideAdapter.getFormGuideData()
