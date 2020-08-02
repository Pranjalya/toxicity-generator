from flask import Flask, request, jsonify
import gdown
from fastai.basic_train import load_learner
from flask_cors import CORS,cross_origin
import random
import os

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


def get_sentences(request):
    """
    Function to return new set of abuses.
    """
    shower_me = 35
    toxic_counter = 0
    all_toxics = []

    for i in range(250):
        sent = learn.predict("xxbos ", n_words=50, temperature=0.8)
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

    return all_toxics


# route for prediction
@app.route('/gettoxic', methods=['POST'])
def predict():
    return jsonify(predict_single(request))

if __name__ == '__main__':
    app.run()