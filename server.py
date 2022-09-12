from datetime import datetime
from time import time

from flask import Flask, request, abort

app = Flask(__name__)
db = [
    {'name': 'Jack', 'text': 'Hello everyone, i`m Jack!', 'time': 0.1},
    {'name': 'Mary', 'text': 'Hello Jack, i`m Mary.', 'time': 0.2},
]


@app.route('/')
def hello():
    return "<b>Hello World!<b> <a href='/status'>Status</a>"


@app.route('/status')
def status():
    return {
        'status': True,
        'name': 'Messenger',
        'time1': datetime.now().strftime('%d %B %Y %H:%M:%S'),
        'num_of_messages': len(db),
        'num_of_users': len(set(mess['name'] for mess in db))
    }


@app.route('/send', methods=['POST'])
def send_message():
    data = request.json()
    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)

    # name = data.get('name')
    # text = data.get('text')
    name = data['name']
    text = data['text']

    if not isinstance(name, str) or len(name) == 0 or len(name) >= 64:
        return abort(400)

    if not isinstance(text, str) or len(text) == 0 or len(text) > 1000:
        return abort(400)

    message = {
        'name': name,
        'text': text,
        'time': time()
    }
    db.append(message)

    # if message == '/help':
    #     messages.append({
    #         'name': 'bot',
    #         'text': 'Я сам ничего не знаю',
    #         'time': time()
    #     })
    # TODO перенести бота на ресивер
    # TODO добавить авторизацию по паролям

    # return {'ok': True}
    return {}


@app.route('/messages')
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    response = []
    for message in db:
        if message['time'] > after:
            response.append(message)
    return {'messages': response[:50]}


app.run()
