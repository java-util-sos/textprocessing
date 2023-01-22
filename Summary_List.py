import cohere
from api_keys import cohere_key

def process_text(text):
  prompts = []
  text_lst = text.split('\n')
  print(text_lst)
  
  for txt in text_lst:
    prompts.append(txt.split('. ')[1])
    
  return prompts


def generate_summary(prompt):
  global cohere_key
  co = cohere.Client(f'{cohere_key}')
  response = co.generate(
    model='command-medium-nightly',
    prompt=f'Make a numerical list that summarizes the main points of the Essay as. Make sure the points are concise and short.\n\nEssay = {prompt}\'\'\'\n\'\'\'',
    max_tokens=1000,
    temperature=0.9,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
  summary = response.generations[0].text
    
  return summary

def generate_questions(prompt_lst):
  global cohere_key
  co = cohere.Client(f'{cohere_key}')
  prompts = ""
  for i, prt in enumerate(prompt_lst):
    prompts += f'{i}. {prt} \n'
  
  n = len(prompt_lst)
  
  response = co.generate(
    model='command-medium-nightly',
    prompt=f'Make a list of questions from the list, the list of questions should be in the same order as the list is being asked. There should be as many questions as in the list.\n\n\nX= \'\'\' {prompts}\" \'\'\'',
    max_tokens=500,
    temperature=1,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
  return response.generations[0].text

def generate_questions_new(prompt, n):
  global cohere_key
  co = cohere.Client(f'{cohere_key}')
  
  response = co.generate(
    model='command-medium-nightly',
    prompt=f'Make a list of questions from the list {n}, the list of questions should be in the same order as {n} is being asked.\n\n\nX= \'\'\' {prompt}\" \'\'\'',
    max_tokens=500,
    temperature=1,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
  return response.generations[0].text

def generate_questions_new_v2(prompt):
  global cohere_key
  co = cohere.Client(f'{cohere_key}')
  
  response = co.generate(
    model='command-medium-nightly',
    prompt=f'Make a list of questions from the list, the list of questions should be in the same order as the list is being asked. There should be as many questions as in the list.\n\n\nX= \'\'\' {prompt}\" \'\'\'',
    max_tokens=500,
    temperature=1,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
  return response.generations[0].text
