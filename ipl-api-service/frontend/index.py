from flask import Flask, request, render_template
import requests

app = Flask(__name__)

all_teams = []

@app.route('/')
def index():
    response = requests.get("api/teams")
    if response.status_code == 200:
        teams = response.json()
        teams_l = teams['teams']
        all_teams = teams_l
        return render_template(teams=sorted(teams_l))
    else:
        return render_template("index.html",teams=["Teams Not found"])

@app.route('/teamVteam')
def TeamVteam():
    # get response
    response2 = requests.get("api/teamVteam?team1={}&team2={}".format(request.args['team1'], request.args['team2']))
    if response2.status_code == 200:
        data = response2.json()
        return render_template("index.html", teams=all_teams,result=data)
    else:
        return render_template("index.html", teams=all_teams,result={"message":"Uh oh! Couldn't get response"})


app.run(debug=True)