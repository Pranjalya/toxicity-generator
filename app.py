import os
import random
import gdown

import torch
import fastai 
from fastai.basic_train import load_learner

from flask import Flask, request, jsonify
from flask_cors import CORS,cross_origin


#fastai.device = torch.device('cpu')

app = Flask(__name__)
CORS(app, support_credentials=True)

try:
    os.mkdir('model')
except:
    print("Can't do that")

# load the learner
url = 'https://drive.google.com/uc?id=13a-VopEnvc2YTji4SbmhqxFGkxnVjw3j'
output = 'model/export.pkl'

gdown.download(url, output, quiet=True)
learn = load_learner(path='./model', file='export.pkl')


def get_sentences():
    """
    Function to return new set of abuses.
    """
    shower_me = 20
    toxic_counter = 0
    all_toxics = []

    for i in range(30):
        sent = learn.predict("xxbos ", n_words=40, temperature=0.8)
        sents = sent.split("xxbos ")
        sents = sents[1:-1]

        for sent in sents:
            sent = sent.replace("xxbos","").strip()
            if(sent):
                all_toxics.append(sent)
                toxic_counter = toxic_counter+1

        if toxic_counter > shower_me:
            break
    
    toxics = random.sample(all_toxics, 10)

    return toxics


#default route
@app.route("/")
def default():
    return 'Please use right end point'

# route for prediction
@app.route('/gettoxic', methods=['POST'])
def predict():
    toxic_sentences = get_sentences()
    result_toxic_dict = result_dict = {'toxic_sentences': toxic_sentences}
    return jsonify(result_toxic_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0:6000')
