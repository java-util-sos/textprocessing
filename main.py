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
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

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
    print(data)
    long_form_text = data['text']
    request_type = data['type']
    
    prompt_lst = long_form_text.split('\n')
    
    if request_type not in REQUESTS:
        return jsonify({'text': 'Invalid request type'}).headers.add("Access-Control-Allow-Origin", "*")
    
    elif request_type == 'QUIZ':
        question_answer = []
        for prompt in prompt_lst:
            summary = Summary_List.generate_summary(prompt)
            questions = Summary_List.generate_questions_new_v2(summary)
            
            summary = summary.split('\n')
            summary = [x for x in summary if x]
            
            questions = questions.split('\n')
            questions = [x for x in questions if x]
            
            #print(summary)
            #print(questions)
            
            for i, s in enumerate(summary):
                summary[i] = s.split('. ')[1]
                
            for i, q in enumerate(questions):
                questions[i] = q.split('. ')[1]
            
            for s,q in zip(summary, questions):
                question = {'question': q, 'answer': s}
                question_answer.append(question)
                
        json = {'question_jsons': question_answer}
        
        return jsonify(json)

    elif request_type == 'MINDMAP':
        return jsonify({'text': resources.generate_mindmap(prompt_lst)}).headers.add("Access-Control-Allow-Origin", "*")
    else:
        return jsonify({'text': 'Unknown error'}).headers.add("Access-Control-Allow-Origin", "*")
    
@cross_origin()
@app.route('/summaryv2/', methods= ['POST'])
def request_summary_unordered():
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
            questions = Summary_List.generate_questions_new_v2(summary)
            
            summary = summary.split('\n')
            summary = [x for x in summary if x]
            
            questions = questions.split('\n')
            questions = [x for x in questions if x]
               
        json = {'questions': questions,
                'answers': summary}
        
        return jsonify(json)

    elif request_type == 'MINDMAP':
        return jsonify({'text': resources.generate_mindmap(prompt_lst)}).headers.add("Access-Control-Allow-Origin", "*")
    else:
        return jsonify({'text': 'Unknown error'}).headers.add("Access-Control-Allow-Origin", "*")

    
@app.route('/hello', methods = ['POST'])
def aws_test():
    return jsonify({'text': 'Hello World'})
    


if __name__ == "__main__":
    app.run(host=IPAddr, threaded=false, port=7777)