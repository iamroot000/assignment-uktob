import requests

#test 
def sum(numbers):
    url = 'http://127.0.0.1:5000/sum'
    data = {'numbers': numbers}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return response.text

def concat(string1, string2, string3):
    url = 'http://127.0.0.1:5000/concat'
    data = {
        'string1': string1,
        'string2': string2,
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

if __name__=="__main__":
    print(sum([1, 2, 3, 4, 5]))
    print(concat('test', 'one', 'two'))