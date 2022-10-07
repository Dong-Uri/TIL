import requests

BASE_URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
X_AUTH_TOKEN = '9befd74203c7f82c381394d3e03e9e08'

def start(scenario):
    headers = {
        'X-Auth-Token': X_AUTH_TOKEN,
    }

    json_data = {
        'problem': scenario,
    }

    response = requests.post(BASE_URL + '/start', headers=headers, json=json_data).json()

    return response

def waiting_line():
    headers = {
    'Authorization': AUTH_KEY,
    'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/waiting_line', headers=headers).json()
    
    return response['waiting_line']

def game_result():
    headers = {
    'Authorization': AUTH_KEY,
    'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/game_result', headers=headers).json()

    return response['game_result']

def user_info():
    headers = {
    'Authorization': AUTH_KEY,
    'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/user_info', headers=headers).json()

    return response['user_info']

def match(pairs):
    headers = {
    'Authorization': AUTH_KEY,
    }

    json_data = {
        'pairs': pairs,
    }

    response = requests.put(BASE_URL + '/match', headers=headers, json=json_data).json()

    return response

def change_grade(commands):
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }

    json_data = {
        'commands': commands,
    }

    response = requests.put(BASE_URL + '/change_grade', headers=headers, json=json_data).json()

    return response

def score():
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/score', headers=headers).json()
    
    return response

scenario = 2
starting = start(scenario)
AUTH_KEY = starting['auth_key']

grade = [5000] * 901
time = 0
cg = {'status': 'ready'}

while True:
    for result in game_result():
        if result['taken'] <= 10:
            continue
        rate = int(1.2 ** (40 - result['taken']))
        grade[result['win']] += rate
        grade[result['lose']] -= rate

    wait = sorted(waiting_line(), key= lambda x: x['from'])
    wait_num = len(wait)
    pairs = []
    if wait_num >= 2:
        waiting = [0] * wait_num
        for i in range(len(wait)-1):
            if waiting[i]:
                continue
            else:
                for j in range(i+1, len(wait)):
                    if abs(grade[i] - grade[j]) < 100:
                        pairs.append([wait[i]['id'], wait[j]['id']])
                        waiting[j] = 1
                        break
    mr = match(pairs)
    print(mr)
    if mr['time'] == 595:
        if scenario == 1:
            n = 30
        else:
            n = 900
        commands = []
        for i in range(1, n+1):
            if grade[i] < 0:
                commands.append({'id': i, 'grade': 0})
            elif grade[i] > 9999:
                commands.append({'id': i, 'grade': 9999})
            else:
                commands.append({'id': i, 'grade': grade[i]})
        cg = change_grade(commands)
    if mr['status'] != 'ready' or cg['status'] != 'ready':
        break

print(score())