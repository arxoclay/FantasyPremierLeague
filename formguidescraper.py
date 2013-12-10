# Imports
import mechanize
import re

class FormGuideScraper:
    # Constants/Magic values
    PAGE = "http://www.premierleague.com/content/premierleague/en-gb/matchday/form-guide.html"
    RELEVANT_TABLE_REGEX = "<table class=\"leagueTable home_vs_away_and_total\">.*</table>"

    # The actual action
    def getFormGuideData(self):
        br = mechanize.Browser()
        br.open(FormGuideScraper.PAGE)
        allContent = br.response().read()

        # Capture and return the raw table data
        match = re.search(FormGuideScraper.RELEVANT_TABLE_REGEX, allContent, re.DOTALL)
        return match.group(0)

# Example call
# formGuideScraper = FormGuideScraper()
# print formGuideScraper.getFormGuideData()
