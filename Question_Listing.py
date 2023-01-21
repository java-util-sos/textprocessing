import cohere
co = cohere.Client('{apiKey}')
response = co.generate(
  model='command-xlarge-nightly',
  prompt='Make a list of questions from the list X, the list of questions should be in the same order as X is being asked.\n\n\nX= \'\'\'1. The media used battles and atrocities to their advantage in order to propagate anti-war sentiments.\n\n2. Vietnam was the first televised war, with blood, bodies, and bombs being broadcast directly into the living rooms of millions of Americans and billions around the world.\n\n3. The world watched as the United States dropped 643,000 tons of ordinance during Operation Rolling Thunder just as they saw pictures of Vietnamese children covered in napalm in the street (Napalm Girl).\n\n4. The media heavily utilized these images to propagate their disapproval of the war.\n5. However, there is historical debate over the objectivity of the media during the conflict. Mirror theory argues that reporters \"unconditionally followed the doctrine of objective journalism\".\n\n6. Dr. Daniel Hallin (Professor of Communication at the UC San Diego), argues that the media only took on a non-objective stance once the upper-class started voicing their discontent.\n\n7. Hallin further argues that this was the catalyst in propagating dissent among the public to transfer from \"the fringes of society into its main stream.\" \'\'\'',
  max_tokens=500,
  temperature=1,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))
