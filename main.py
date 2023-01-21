import numpy as np
import cohere
import cosine_distance
import Summary_List
import matplotlib.pyplot as plt
import json
import requests as rq

from api_keys import cohere_key

if __name__ == "__main__":
    prompt = "In plant biology, plants are, for the most part, photosynthetic eukaryotes that make up the kingdom Plantae. In their respective environments/habitats, plants use water, light energy, and carbon dioxide (these being inorganic substances) to synthesize sugar/nutrients that serve as food for various animals. In addition to synthesizing their own food, plants in different environments (aquatic, terrestrial etc) play an important role in the production of oxygen making them essential to all life on earth. Although plant biology enables photosynthesis (a unifying characteristic), different types of plants have various physical and genetic characteristics."
    text = Summary_List.generate_summary(prompt)
    print(text)
    
    text  = Summary_List.process_text(text)
    questions = Summary_List.generate_questions(text)
    print("[][][][][][][][][][][][][][][][][][]")
    print(questions)
    print("[][][][][][][][][][][][][][][][][][]")
    print(text)
    print("======================================")
    result = cosine_distance.process_text(text)
    
    print(result)
    print('\n')
    print(result[0][:5])
    
    for i in range(1,len(result)):
        print(cosine_distance.get_angle(result[0], result[i]))
    #graph the resulting points
    
    print("Hello World!")
