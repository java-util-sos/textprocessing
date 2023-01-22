import numpy as np
import cohere
import cosine_distance
import Summary_List
import resources
import matplotlib.pyplot as plt
import json
from flask import *
import json, time

from api_keys import cohere_key

REQUESTS = [
    'QUIZ',
    'MINDMAP',
]
app = Flask(__name__)

@app.route('/', methods= ['GET'])
def home():
    data_set = {'Page':'Home',
                'Message':'Success',
                'Timestamp': time.time()}
    
    return json.dumps(data_set)

@app.route('/summary/', methods= ['POST'])
def request_summary():
    data = request.get_json()
    long_form_text = data['text']
    request_type = data['type']
    
    prompt_lst = long_form_text.split('\n')
    #return jsonify({'text': prompt_lst})
    
    if request_type not in REQUESTS:
        return jsonify({'text': 'Invalid request type'})
    
    elif request_type == 'QUIZ':
        question_answer = []
        for prompt in prompt_lst:
            summary = Summary_List.generate_summary(prompt)
            #return jsonify({'text': summary})
            questions = Summary_List.generate_questions_new(summary, 5)
            summary = summary.split('\n')
            questions = questions.split('\n')
            questions =questions[1:]
            
            
            #for i, s in enumerate(summary):
            #    summary[i] = s.split('. ')[1]
                
            #for i, q in enumerate(questions):
            #    questions[i] = q.split('. ')[1]
            
            for s,q in zip(summary, questions):
                question = {'question': q, 'answer': s}
                question_answer.append(question)
                
        json = {'question_jsons': question_answer}
        
        return jsonify(json)

    elif request_type == 'MINDMAP':
        return jsonify({'text': resources.generate_mindmap(prompt_lst)})
    else:
        return jsonify({'text': 'Unknown error'})
    

if __name__ == "__main__":
    app.run(debug=True, port=7777)
    #prompt = "In plant biology, plants are, for the most part, photosynthetic eukaryotes that make up the kingdom Plantae. In their respective environments/habitats, plants use water, light energy, and carbon dioxide (these being inorganic substances) to synthesize sugar/nutrients that serve as food for various animals. In addition to synthesizing their own food, plants in different environments (aquatic, terrestrial etc) play an important role in the production of oxygen making them essential to all life on earth. Although plant biology enables photosynthesis (a unifying characteristic), different types of plants have various physical and genetic characteristics."
    #text = Summary_List.generate_summary(prompt)
    #print(text)
    
    #text  = Summary_List.process_text(text)
    #questions = Summary_List.generate_questions(text)
    
    #print("[][][][][][][][][][][][][][][][][][]")
    #print(questions)
    #print("[][][][][][][][][][][][][][][][][][]")
    #print(text)
    #print("======================================")
    #result = cosine_distance.process_text(text)
    
    #print(result)
    #print('\n')
    #print(result[0][:5])
    
    #for i in range(1,len(result)):
    #    print(cosine_distance.get_angle(result[0], result[i]))
    
    #print("Hello World!")
