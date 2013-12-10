# Imports
import sys
import mechanize
import re

# Constants/Magic values
PAGE = "http://www.premierleague.com/content/premierleague/en-gb/matchday/form-guide.html"
RELEVANT_TABLE_REGEX = "<table class=\"leagueTable home_vs_away_and_total\">.*</table>"

# The actual action
def getFormGuideData():
    br = mechanize.Browser()
    br.open(PAGE)
    allContent = br.response().read()

    # Capture and return the raw table data
    match = re.search(RELEVANT_TABLE_REGEX, allContent, re.DOTALL)
    return match.group(0)

# Example call
# print getFormGuideData()
