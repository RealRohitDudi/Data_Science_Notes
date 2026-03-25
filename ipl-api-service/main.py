from flask import Flask, request

import apis,jugaad

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World! check documentation page to see how to use our APIs."

@app.route("/teams")
def teams():
    return apis.get_teams()

@app.route("/teamVteam")
def teamVteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    return apis.get_matches(team1, team2)

@app.route("/team-record")
def teamRecord():
    team = request.args.get('team')
    return jugaad.teamAPI(team)

@app.route("/batting-record")
def battingRecord():
    batter = request.args.get('batter')
    return jugaad.batsmanAPI(batter)


@app.route("/bowling-record")
def bowlingRecord():
    bowler = request.args.get('bowler')
    return jugaad.ballerAPI(bowler)

app.run(debug=True)