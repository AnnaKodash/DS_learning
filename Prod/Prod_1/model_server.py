from flask import Flask,request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

with open('Prod/Prod_1/model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

@app.route('/predict', methods=['POST'])
def predict():
    features = request.json #get('features')
    #print(features)
     
    pred = model.predict(np.array(features).reshape(1, -1))
    return jsonify({'result':pred[0]})

if __name__ == '__main__':
    app.run('localhost', 5000)