class ClubNameMatcher:

    def __init__(self):
        self.clubAliases = []
        # I expect to see at most 20 lines following this comment
        # 20 lines = 20 premier league clubs
        self.clubAliases.append(("Cardiff", "Cardiff City"))
        self.clubAliases.append(("Spurs", "Tottenham"))
        self.clubAliases.append(("Hull", "Hull City"))
        self.clubAliases.append(("Stoke", "Stoke City"))
        
    def isSameClub(self,name1, name2):
        for clubNames in self.clubAliases:
            if(name1 in clubNames and name2 in clubNames):
                return True
        return name1 == name2
