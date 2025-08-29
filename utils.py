import json
import boto3

class LeaderBoard:
    def __init__(self):
        self.leaderboard = json.load(open('leaderboard.json'))
        self.ledger = json.load(open('ledger.json'))
        self.s3 = boto3.boto3.client("s3", region_name="us-east-2")
        self.BUCKET_NAME = "pop-leaderboard-backup"

    def addNewUser(self, name):
        self.leaderboard[name] = 0
        self.ledger[name] = []
        self.s3.put_object(Bucket=self.BUCKET_NAME, Key="leaderboard.json", Body=json.dumps(self.leaderboard))
        self.s3.put_object(Bucket=self.BUCKET_NAME, Key="ledger.json", Body=json.dumps(self.ledger))
        with open("leaderboard.json", "w") as f:
            json.dump(self.leaderboard, f, indent=4)
        with open("ledger.json", "w") as f:
            json.dump(self.ledger, f, indent=4)

    def getUsers(self):
        return list(self.leaderboard.keys())

    def returnSortedLeaderboard(self):
        sorted_by_values = dict(sorted(self.leaderboard.items(), key=lambda item: item[1], reverse=True))
        return sorted_by_values

    def updateScore(self, name, reason, scoreMod):
        self.leaderboard[name] = self.leaderboard[name] + scoreMod
        self.ledger[name].append([reason, scoreMod])
        self.s3.put_object(Bucket=self.BUCKET_NAME, Key="leaderboard.json", Body=json.dumps(self.leaderboard))
        self.s3.put_object(Bucket=self.BUCKET_NAME, Key="ledger.json", Body=json.dumps(self.ledger))
        with open("leaderboard.json", "w") as f:
            json.dump(self.leaderboard, f, indent=4)
        with open("ledger.json", "w") as f:
            json.dump(self.ledger, f, indent=4)

        

