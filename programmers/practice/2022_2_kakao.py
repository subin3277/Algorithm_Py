import json
import requests

x_auth_token = "0477762637070e35ec097e8dbdf6a8f7"
BASE_URL = "https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api"
auth_key = "c34aaa93-be1c-483c-8382-117dff2559ac"

def startapi():
    global auth_key
    url = BASE_URL + "/start"
    headers = {'X-Auth-Token': x_auth_token}
    datas = {"problem": 1}
    response = requests.post(url, json=datas, headers=headers)
    response = json.loads(response.text)
    auth_key = response['auth_key']
    problem = response['problem']
    day = response['day']
    return auth_key, problem, day

def NewRequest(): # 현재 날짜에 들어온 예약 요청 정보
    url = BASE_URL + "/new_requests"
    headers = {'Authorization' : auth_key}
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)
    reservations_info = response['reservations_info']
    return reservations_info

def ReplyAPI(lst): # 승낙 or 거절 답변
    url = BASE_URL + "/reply"
    headers = {'Authorization' : auth_key}
    datas = {'replies' : lst } # reply = accepted or refused
    response = requests.put(url, json=datas, headers=headers )
    response = json.loads(response.text)
    day = response['day']
    return day

def SimulateAPI(lst):
    url = BASE_URL + "/simulate"
    headers = {'Authorization':auth_key}
    datas = {'room_assign' : lst}
    response = requests.put(url, json=datas, headers=headers)
    response = json.loads(response.text)
    day = response['day']
    fail_count = response['fail_count']
    return day, fail_count

def ScoreAPI():
    url = BASE_URL + "/score"
    headers = {'Authorization':auth_key}
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)
    accuacy_score = response['accuracy_score']
    efficiency_score = response['efficiency_score']
    penalty_score = response['penalty_score']
    score = response['score']
    return accuacy_score, efficiency_score, penalty_score, score

day = startapi()[2]
room = [[[0] * 20 for _ in range(3)] for _ in range(201)]
wait = []
check_in = [[] for _ in range(201)]
while day < 200:
    reservations_info = NewRequest()
    reply_list = []
    for i in reservations_info:
        wait.append(i)
    for i in range(len(wait)-1):
        for j in range(i+1,len(wait)):
            if wait[i]['amount'] < wait[j]['amount']:
                wait[i], wait[j] = wait[j], wait[i]
            elif wait[i]['amount'] == wait[j]['amount'] and wait[i]['check_out_date'] - wait[i]['check_in_date'] < wait[j]['check_out_date'] - wait[j]['check_in_date']:
                wait[i], wait[j] = wait[j], wait[i]

    state = True
    while state and wait:
        t = wait.pop(0)

        for x in range(len(room[0])):
            for y in range(len(room[0][0]) - t['amount']):
                if (not 0) in room[t['check_in_date']][x][y:y+t['amount']] :
                    break
                else:
                    for i in range(t['check_in_date'], t['check_out_date']):
                        if (not 0) in room[i][x][y:y+t['amount']]:
                            break
                    else:
                        reply_list.append({'id':t['id'], "reply":"accepted"})
                        check_in[t['check_in_date']].append([t, x*1000 + y])
                        state = False
                        break
            if not state:
                break
        else:
            reply_list.append({'id':t[id], 'reply':'refused'})

    ReplyAPI(reply_list)
    reply_list = []

    check = []
    for i in check_in[day]:
        check.append({'id' : i[0]['id'], 'room_number': i[1]})
    day = SimulateAPI(check)[0]

print(ScoreAPI())