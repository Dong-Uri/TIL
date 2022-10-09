import requests

x_auth_token = '0108f5a5e35f0574c810e4e37aa32fca'
BASE_URL = 'https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api'

def start(scenario):

    headers = {
        'X-Auth-Token': x_auth_token,
        'Content-Type': 'application/json',
    }

    json = {'problem': scenario}

    response = requests.post(BASE_URL + '/start', headers=headers, json=json).json()

    return response # auth_key, problem, day

def new_requests():

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/new_requests', headers=headers).json()

    return response['reservations_info'] # {id, amount, check_in_date, check_out_date}

def reply(replies): # {id, reply} accepted refused

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json',
    }
    
    json = {'replies': replies}

    response = requests.put(BASE_URL + '/reply', headers=headers, json=json).json()

    return response # day

def simulate(room_assign): # {id, room_number}

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json',
    }

    json = {'room_assign': room_assign}

    response = requests.put(BASE_URL + '/simulate', headers=headers, json=json).json()

    return response # day, fail_count

def score():

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json',
    }

    response = requests.get(BASE_URL + '/score', headers=headers).json()

    return response # accuracy_score, efficiency_score, penalty_score, score

def find_room(day, amount):
    available = set()
    for i in range(H):
        cnt = 0
        for j in range(W):
            if empty_room[day][i][j]:
                cnt = 0
            else:
                cnt += 1
            if cnt >= amount:
                room_num = (i + 1) * 1000 + (j - amount + 2)
                available.add(room_num)
    return available


scenario = 2
auth_key = start(scenario)['auth_key']

if scenario == 1:
    H = 3
    W = 20
    D = 200

    empty_room = [[[0] * W for _ in range(H)] for _ in range(D+1)]
    go_room = [[] for _ in range(D+1)]
    reply_date = [[] for _ in range(D+1)]
    day = 1
    refuse_cnt = 0
    refuse_room = 0

    while day < D:
        replies = []
        reservations = []
        for reservation in new_requests():
            available = find_room(reservation['check_in_date'], reservation['amount'])
            for day in range(reservation['check_in_date'] + 1, reservation['check_out_date']):
                available = available & find_room(day, reservation['amount'])
            available = list(available)

            if not available:
                replies.append({'id': reservation['id'], 'reply': 'refused'})
                refuse_cnt += 1
                refuse_room += reservation['amount']
                print('refuse: ', refuse_cnt, refuse_room, refuse_room/refuse_cnt)
                continue

            available.sort(key = lambda x: (x % 1000, x // 1000))
            room_number = available[0]
            replies.append({'id': reservation['id'], 'reply': 'accepted'})
            go_room[reservation['check_in_date']].append({'id': reservation['id'], 'room_number': room_number})
            for day in range(reservation['check_in_date'], reservation['check_out_date']):
                for i in range(reservation['amount']):
                    empty_room[day][room_number // 1000 - 1][room_number % 1000 - 1 + i] = 1
        
        day = reply(replies)['day']
        print(simulate(go_room[day]))

    print(refuse_cnt, refuse_room, refuse_room/refuse_cnt)
    print(score())

else:
    H = 10
    W = 200
    D = 1000

    empty_room = [[[0] * W for _ in range(H)] for _ in range(D+1)]
    go_room = [[] for _ in range(D+1)]
    reply_date = [[] for _ in range(D+1)]
    sungsu_cnt = [0] * (D+1)
    max_sungsu_cnt = 0
    day = sungsu_day = 1
    refuse_cnt = 0
    refuse_room = 0

    while day < D:
        replies = []
        reservations = []
        for reservation in new_requests():
            if reservation['amount'] >= 13 and 7 <= reservation['check_out_date'] - reservation['check_in_date'] <= 30:
                sungsu_cnt[day] += 1
            reply_date[day].append(reservation)

        reply_date[day].sort(key=lambda x: x['amount'], reverse=True)
        for reservation in reply_date[day]:
            available = find_room(reservation['check_in_date'], reservation['amount'])
            for day in range(reservation['check_in_date'] + 1, reservation['check_out_date']):
                available = available & find_room(day, reservation['amount'])
            available = list(available)

            if not available:
                replies.append({'id': reservation['id'], 'reply': 'refused'})
                refuse_cnt += 1
                refuse_room += reservation['amount']
                print('refuse: ', refuse_cnt, refuse_room, refuse_room/refuse_cnt)
                continue

            room_number = min(available)
            if not sungsu_day + 305 < day <= sungsu_day + 365:
                if reservation['amount'] < 30 and room_number > 9000:
                    replies.append({'id': reservation['id'], 'reply': 'refused'})
                    refuse_cnt += 1
                    refuse_room += reservation['amount']
                    print('refuse: ', refuse_cnt, refuse_room, refuse_room/refuse_cnt)
                    continue
                if reservation['amount'] < 40 and room_number > 10000:
                    replies.append({'id': reservation['id'], 'reply': 'refused'})
                    refuse_cnt += 1
                    refuse_room += reservation['amount']
                    print('refuse: ', refuse_cnt, refuse_room, refuse_room/refuse_cnt)
                    continue

            replies.append({'id': reservation['id'], 'reply': 'accepted'})
            go_room[reservation['check_in_date']].append({'id': reservation['id'], 'room_number': room_number})
            for day in range(reservation['check_in_date'], reservation['check_out_date']):
                for i in range(reservation['amount']):
                    empty_room[day][room_number // 1000 - 1][room_number % 1000 - 1 + i] = 1
        
        day = reply(replies)['day']
        
        if max_sungsu_cnt < sum(sungsu_cnt[max(0, day-60):day]):
            max_sungsu_cnt = sum(sungsu_cnt[max(0, day-60):day])
            sungsu_day = day
        print(simulate(go_room[day]), sungsu_day, sum(sungsu_cnt[max(0, day-60):day]))

    print(refuse_cnt, refuse_room, refuse_room/refuse_cnt)
    print(score())