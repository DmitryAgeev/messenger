import requests

# response = requests.get('http://127.0.0.1:5000')
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)

name = input('Write nickname: ')

while True:
    text = input()
    response = requests.post('http://127.0.0.1:5000/send', json={'name': name, 'text': text})
