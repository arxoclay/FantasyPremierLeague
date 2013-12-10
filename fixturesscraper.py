# Imports
import mechanize
import re

class FixturesScraper:
    # Constants/Magic values
    PAGE = "http://fantasy.premierleague.com/fixtures/"
    RELEVANT_TABLE_REGEX = "<table id=\"ismFixtureTable\" class=\"ismFixtureTable\">.*</tbody></table>"

    # The actual action
    def getFixturesData(self):
        br = mechanize.Browser()
        br.open(FixturesScraper.PAGE)
        allContent = br.response().read()

        # Capture and return the raw table data
        match = re.search(FixturesScraper.RELEVANT_TABLE_REGEX, allContent, re.DOTALL)
        return match.group(0)

# Example call
# fixturesScraper = FixturesScraper()
# print fixturesScraper.getFixturesData()
