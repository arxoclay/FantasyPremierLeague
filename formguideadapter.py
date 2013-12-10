# Imports
import formguidescraper

class FormGuideAdapter:
    
    def getFormGuideData(self):
        formGuideScraper = formguidescraper.FormGuideScraper()
        rawData = formGuideScraper.getFormGuideData()

# Example call
formGuideAdapter = FormGuideAdapter()
formGuideAdapter.getFormGuideData()
