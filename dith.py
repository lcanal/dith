from flask import Flask,url_for,render_template
from os import environ as env
import json
from stattleship_query import query_api

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

## Game 1 function
@app.route('/nbafinals-game1')
def nbafinalsGame1():
    apikey = env['STATTLESHIP_API_KEY']
    queried_data = query_api(token=apikey)
    parsed_json = json.loads(queried_data)

    # Start parsing json
    playerIndex = dict()
    gameIndex = dict()
    finalSet = dict()

    games = parsed_json["games"]
    players = parsed_json["players"]
    gamelogs = parsed_json["game_logs"]

    for player in players:
        playerIndex[player['id']] = player

    for game in games:
        gameIndex[game['id']] = game

    ## Print
    for gamelog in gamelogs:
        pid = gamelog['player_id']
        gid = gamelog['game_id']
        player = playerIndex[pid]
        game = gameIndex[gid]
        sid = game['timestamp']

        points = str(gamelog['points'])
        scoreline = game['scoreline']
        assists = str(gamelog['assists'])
        steals = str(gamelog['steals'])
        blocks = str(gamelog['blocks'])
        turnovers = str(gamelog['turnovers'])
        field_g_made = str(gamelog['field_goals_made'])
        free_t_made = str(gamelog['free_throws_made'])
        three_p_m = str(gamelog['three_pointers_made'])

        printString = ','.join([player['last_name'],field_g_made,free_t_made,three_p_m,assists,steals,blocks,turnovers])

        if sid in finalSet:
            finalSet[sid] += printString + '\n'
        else:
            finalSet[sid] = printString + '\n'

    finalString = "Player,FG,FT,3pts,Assists,Steals,Blocks,Turnovers\n"

    for printLine in finalSet.values():
            finalString += printLine

    finalString.rstrip()

    return finalString

if __name__ == "__main__":
    app.run()
