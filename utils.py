import json

class LeaderBoard:
    def __init__(self):
        self.leaderboard = json.load(open('leaderboard.json'))
        self.ledger = json.load(open('ledger.json'))

    def addNewUser(self, name):
        self.leaderboard[name] = 0
        self.ledger[name] = []

    def getUsers(self):
        return list(self.leaderboard.keys())

    def returnSortedLeaderboard(self):
        sorted_by_values = dict(sorted(self.leaderboard.items(), key=lambda item: item[1], reverse=True))
        return sorted_by_values

    def updateScore(self, name, reason, scoreMod):
        self.leaderboard[name] = self.leaderboard[name] + scoreMod
        self.ledger[name].append([reason, scoreMod])
