import numpy as np
import cohere
from api_keys import cohere_key

import cohere
co = cohere.Client('{apiKey}')
response = co.embed(
  model='large',
  texts=["On January 31st, 1968, the Army of the Republic of Vietnam (ARVN) and the American Forces experienced the largest offensive in the sixteen years of the Vietnam War.", "The Tet truce was a ceasefire that was to take place during the Vietnamese harvest festival celebrating the arrival of spring.", "Firstly, the United States being unprepared for the Tet Offensive was a huge embarrassment to the government and its intelligence services.", "With this deterioration in public support, the administration had less leeway to enact new initiatives. LBJ assembled a Tet Task Force, headed by Secretary of Defense Clark Clifford, in order to prioritize and make strategic decisions.", "People did not feel safe in their own homes and felt their government could not protect them, leading to a sudden increase in anti-war sentiments."])
print('Embeddings: {}'.format(response.embeddings))

if __name__ == "__main__":
    print("Hello World!")
