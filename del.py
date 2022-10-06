import requests

BASE_URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
X_AUTH_TOKEN = 'd5ca5af014252dad190007f4eccf88e1'

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

starting = start(1)
AUTH_KEY = starting['auth_key']
time = starting['time']
while time < 595:
    users = user_info()

    commands = []
    for result in game_result():
        for user in users:
            if user['id'] == result['win']:
                commands.append({'id': user['id'], 'grade': user['grade'] + 50 - result['taken']})
            elif user['id'] == result['lose']:
                commands.append({'id': user['id'], 'grade': user['grade'] - 50 + result['taken']})
    change_grade(commands)           

    wait = sorted(waiting_line(), key= lambda x: x['from'])
    wait_num = len(wait)
    pairs = []
    if wait_num >= 2:
        waiting = [0] * wait_num
        for i in range(len(wait)-1):
            if waiting[i]:
                continue
            for user in users:
                if user['id'] == wait[i]['id']:
                    grade_a = user['grade']
                    break
            for j in range(i+1, len(wait)):
                for user in users:
                    if user['id'] == wait[j]['id']:
                        grade_b = user['grade']
                        break
                if abs(grade_a - grade_b) < 30:
                    pairs.append([wait[i]['id'], wait[j]['id']])
                    waiting[j] = 1
    time = match(pairs)['time']
    print(time)

print(AUTH_KEY)
print(score())