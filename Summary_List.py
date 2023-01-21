import cohere
co = cohere.Client('{apiKey}')
response = co.generate(
  model='command-xlarge-nightly',
  prompt='Make a list that summarizes the main points of the Essay numerically. The points are concise. \n\nEssay = \"Before examining American Sniper, I will begin my argument by exploring the history of Muslim representation in Western films and prove that the use of this derogatory stereotype has been extremely repetitive. Surprisingly, the use of the vile Muslim stereotype had not began after the 9/11 attacks as I had first assumed, but many years ago dating back to as early as 1912. Reel Bad Arabs written by Jack Shaheen, who has watch over 900 Hollywood films analysing the way Arabs have been represented in the films, has concluded that “the vast majority of which portray Arabs by distorting at every turn what most Arab men, women, and children are really like” (Shaheen, 2003). One of the first elements of this stereotype is that all Muslims are Arabs, and all Arabs are Muslims, when Arabs only account for approximately 20% of the global population of 2 billion Muslims and the Islamic world is in fact very culturally and ethnically diverse, in addition there is a significant population of Christian Arabs in the Middle East. Another commonly shared aspect of the stereotype is that Muslims are violent by nature, religious extremists and are highly anti-Christian, anti-American/anti-West and in other words antidemocracy. Muslims or as Hollywood likes to put it “Arabs” when shown on screen are principally the villains of the story, this type of character can be seen in films such as Imar the Servitor (1914) to more recent films like The Mummy (2001) where the white English hero must save the damsel in distress from the filthy Arab man. There has also been a more comedic approach which mocks Muslims painting them as not only villains but “buffoons”.\"\n\nOutputList:\n',
  max_tokens=1000,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))