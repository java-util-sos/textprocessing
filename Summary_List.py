import cohere
co = cohere.Client('{apiKey}')
response = co.generate(
  model='command-xlarge-nightly',
  prompt='Make a numerical list that summarizes the main points of the Essay as. Make sure the points are concise and short.\n\nEssay = \'\'\'The Muslim stereotype is not only seen in war or action films but in children’s movies and cartoons which can be very damaging to young children, making them narrow-minded at an early age. Lastly, one of the most popular false stereotypes is that all Muslim women are oppressed, and need help being liberated by the West; but when looking at the religious book of Islam, the Holy Quran, women are given the right to: pursue an education, vote, inherit land and wealth from their parents and even get a divorce if they want to. The use of these stereotypes only increased as the years went on especially after the 9/11 attacks in New York. The sheer number of times these offensive stereotypes have been used, for well over a century now, attest to the fact that most Western filmmakers have followed a particular narrative when representing Muslims in their work.\n\'\'\'',
  max_tokens=1000,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))
