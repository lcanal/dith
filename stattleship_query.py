import urllib.request

def query_api(token,sport='basketball',league='nba',ep='game_logs'):
    version = 1
     ### depends on page being requested
    stattleship_headers = {
        'Authorization': token,
        'Accept':'application/vnd.stattleship.com; version=%s' %version,
        'Content-Type':'application/json',
        'User-Agent':'Application Python',
     }
    url = 'https://www.stattleship.com/{}/{}/{}'.format(sport, league, ep)

    req = urllib.request.Request(url,headers=stattleship_headers)
    opener = urllib.request.build_opener()
    response = opener.open(req)
    #Return all of the data fetched as a string
    return response.read().decode('utf-8')
