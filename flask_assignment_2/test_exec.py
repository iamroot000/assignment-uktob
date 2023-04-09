import requests

#test 
def register(username, password):
    url = 'http://127.0.0.1:5000/register'
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return response.text

def login(username, password):
    url = 'http://127.0.0.1:5000/login'
    data = {
        'username': username,
        'password': password,
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

if __name__=="__main__":
    print(register('nikkorei', 'test123'))
    print(login('rei', 'test123'))
