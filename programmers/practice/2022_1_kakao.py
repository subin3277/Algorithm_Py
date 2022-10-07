# x_auth_token: daeacb02445b638741bd6f6edc4c4ed8
# BASE URL: https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod

# response = requests.get(url).json()
# headers = {'Content-Type' : 'application/json'}
# response = requests.post(url, data=datas, headers = headers)
import json
import requests

x_auth_token = "daeacb02445b638741bd6f6edc4c4ed8"
BASE_URL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
auth_key = ""

def startapi():
    global auth_key
    url = BASE_URL + "/start"
    headers = {'X-Auth-Token': x_auth_token}
    datas = {"problem": 1}
    response = requests.post(url, data=datas, headers=headers)
    response = json.loads(response.text)
    auth_key = response['auth_key']
    problem = response['problem']
    time = response['time']
    return auth_key, problem, time

def waitinglineapi(auth_key):
    url = BASE_URL + "/waiting_line"
    headers = {'auth_key': auth_key}
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)
    #response = json.loads(requests.get(url, headers=headers).json())
    print(response)
    waiting_line = response['waiting_line']
    return waiting_line

def GameResultAPI():
    url = BASE_URL + "/game_result"
    headers = {'auth_key': auth_key}
    response = json.loads(requests.get(url, headers=headers).json())
    game_result = response['game_result']
    return game_result

def UserInfoAPI():
    url = BASE_URL + "/user_info"
    headers = {'auth_key': auth_key}
    response = json.loads(requests.get(url, headers=headers).json())
    user_info = response['user_info']
    return user_info

def MatchAPI():
    url = BASE_URL + "/match"
    headers = {'X-Auth-Token': x_auth_token}
    datas = {"pairs": [] }
    response = json.loads(requests.put(url, data=datas, headers=headers).json())
    status = response['status']
    time = response['time']
    return status, time

def ChangeGradeAPI():
    url = BASE_URL + "/change_grade"
    headers = {'X-Auth-Token': x_auth_token}
    datas = {"commands": []}
    response = json.loads(requests.put(url, data=datas, headers=headers).json())
    status = response['status']
    return status

def ScoreAPI():
    url = BASE_URL + "/score"
    headers = {'auth_key': auth_key}
    response = json.loads(requests.get(url, headers=headers).json())
    status = response['status']
    efficiency_score = response['efficiency_score']
    accuracy_score1 = response['accurancy_score1']
    accuracy_score2 = response['accurancy_score2']
    score = response['score']
    return status, efficiency_score, accuracy_score1, accuracy_score2, score

startapi()
print(waitinglineapi(auth_key))
