import numpy as np
import cohere
import cosine_distance
import matplotlib.pyplot as plt
import json
import requests as rq

from api_keys import cohere_key

if __name__ == "__main__":
    text = [
        "How to win a hackathon.",
        "Why to win a hackathon."
        "How to win a competiton.",
        "Guide to winning a competition.",
        "Would You Like To Travel With Me ?",
        "He Denied Knowing Anything About Their Plans.",
        "Isn't Language Learning Fun ?",
        "Tom Got Angry At The Children.",
        "He Kindly Answered The Question.",
        "He Is At His Desk.",
        "To Drive A Car, You Need A License.",
        "There Is So Much To Understand.",
        "I Hope That, When I've Built Up My Savings, I'll Be Able To Travel To Mexico.",
        "No One Can Make You Feel Inferior Without Your Consent.",
        "I'm Coming Right Now.",
        "Jacob Stood On His Tiptoes.",
        "Oh, How I'd Love To Go!",
        "I'm Confident That I'll Win The Tennis Match.",
        "She Advised Him To See A Lawyer, So He Did.",
        "Nothing Beats A Complete Sentence.",
        "There Is Always A Next Time." 
    ]
    result = cosine_distance.process_text(text)
    
    print(result)
    print('\n')
    print(result[0][:5])
    
    for i in range(1,len(result)):
        print(cosine_distance.get_angle(result[0], result[i]))
    #graph the resulting points
    
    print("Hello World!")
