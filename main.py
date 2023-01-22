import numpy as np
import cohere
import cosine_distance
import Summary_List
import resources
import matplotlib.pyplot as plt
import json
from flask import *
from flask_cors import CORS, cross_origin
import os

import json, time

try:
    from api_keys import cohere_key, estuary_key
except:
    cohere_key = os.getenv(cohere_key)
    estuary_key = os.getenv(estuary_key)
    

REQUESTS = [
    'QUIZ',
    'MINDMAP',
]
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = '*'

@app.route('/', methods= ['GET'])
def home():
    data_set = {'Page':'Home',
                'Message':'Success',
                'Timestamp': time.time()}
    
    return json.dumps(data_set)

@cross_origin()
@app.route('/summary/', methods= ['POST'])
def request_summary():
    data = request.get_json()
    long_form_text = data['text']
    request_type = data['type']
    
    prompt_lst = long_form_text.split('\n')
    
    if request_type not in REQUESTS:
        return jsonify({'text': 'Invalid request type'}).headers.add("Access-Control-Allow-Origin", "*")
    
    elif request_type == 'QUIZ':
        question_answer = []
        for prompt in prompt_lst:
            summary = Summary_List.generate_summary(prompt)
            questions = Summary_List.generate_questions_new(summary, 5)
            summary = summary.split('\n')
            questions = questions.split('\n')
            summary = [x for x in summary if x]
            questions = [x for x in questions if x]
            questions =questions[1:]
            
            
            for i, s in enumerate(summary):
                summary[i] = s.split('. ')[1]
                
            for i, q in enumerate(questions):
                questions[i] = q.split('. ')[1]
            
            for s,q in zip(summary, questions):
                question = {'question': q, 'answer': s}
                question_answer.append(question)
                
        json = {'question_jsons': question_answer}
        
        return jsonify(json).headers.add("Access-Control-Allow-Origin", "*")

    elif request_type == 'MINDMAP':
        return jsonify({'text': resources.generate_mindmap(prompt_lst)}).headers.add("Access-Control-Allow-Origin", "*")
    else:
        return jsonify({'text': 'Unknown error'}).headers.add("Access-Control-Allow-Origin", "*")
    

if __name__ == "__main__":
    app.run(port=7777)