import cohere
from api_keys import cohere_key as apiKey

co = cohere.Client('{apiKey}')

def generate_summary(prompt):
  response = co.generate(
    model='command-xlarge-nightly',
    prompt=f'Make a numerical list that summarizes the main points of the Essay as. Make sure the points are concise and short.\n\nEssay = {prompt}\'\'\'\n\'\'\'',
    max_tokens=1000,
    temperature=0.9,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
  return_likelihoods='NONE')
  
  return response.generations[0].text

def generate_questions(prompt):
  response = co.generate(
    model='command-xlarge-nightly',
    prompt=f'Make a list of questions from the list X, the list of questions should be in the same order as X is being asked.\n\n\nX= \'\'\' {prompt}\" \'\'\'',
    max_tokens=500,
    temperature=1,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
  return response.generations[0].text
