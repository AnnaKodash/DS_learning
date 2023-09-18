# Скрипт flask сервера для примеров из этого модуля

import pickle
from datetime import datetime

import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

with open('Prod/Prod_2/models/model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

@app.route('/')
def index():
    return 'Test message. The server is running'

# Пример из "5. Пишем сервер. Часть I" и "6. Пишем сервер. Часть II"
@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello, {name}', 200


# Задание 6.2
@app.route('/time')
def current_time():
    return f'CURRENT TIME: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}', 200


# Пример из "7. Пишем сервер. Часть III"
@app.route('/add', methods=['POST'])
def add_func():
    num = request.json.get('num')
    if num > 10:
        return 'too much', 400
    return jsonify({'result': num + 1})


# Задание 7.2
@app.route('/predict', methods=['POST'])
def predict():
    numbers = request.json  # .get('numbers')
    # print(numbers)
    result = model.predict(np.array(numbers).reshape(1, -1))
    return jsonify({'prediction': result[0]})


if __name__ == '__main__':
    app.run('localhost', 5000)
