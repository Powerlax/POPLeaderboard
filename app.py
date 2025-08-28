from flask import Flask, request, jsonify

from utils import LeaderBoard

leaderboard = LeaderBoard()

app = Flask(__name__)

@app.route('/createUser', methods=['POST'])
def createUser():
    try:
        leaderboard.addNewUser(request.get_json()['username'])
        return "success", 200
    except Exception as e:
        return "failed", 400

@app.route('/updateScore', methods=['POST'])
def updateScore():
    try:
        thing = request.get_json()
        leaderboard.updateScore(thing['username'], thing['reason'], thing['score'])
        return "success", 200
    except Exception as e:
        return "failed", 400

@app.route('/getLeaderboard', methods=['GET'])
def getLeaderboard():
    try:
        return jsonify(leaderboard.returnSortedLeaderboard()), 200
    except Exception as e:
        return "failed", 400

@app.route('/getUserList', methods=['GET'])
def getUserList():
    try:
        return jsonify(leaderboard.returnSortedLeaderboard()), 200
    except Exception as e:
        return "failed", 400

if __name__ == '__main__':
    app.run()



