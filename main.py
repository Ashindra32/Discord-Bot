import json
import pandas as pd
import pickle
import random

model_data = {}

with open('model.pkl','rb') as f:
    model_data = pickle.loads(f.read())

rdf = pd.read_csv('response.csv')

def predict_tag(txt='Hello world', vectorizer=None,
                model=None,binarizer=None,*args,**kwargs):
    input_vector = vectorizer.transform([txt])
    result = model.predict(input_vector)
    output_tag = binarizer.inverse_transform(result)
    return output_tag[0]

def get_bot_reply(predicted_tag):
    resultdf = rdf[rdf['tag']==predicted_tag] 
    responses = resultdf.response.tolist()

    return random.choice(responses) if isinstance(responses,list) and len(responses) > 1 else responses[0]

def predict(query):
    if query:
        tag = predict_tag(query, **model_data)
        if tag:
            print(tag)
            response = get_bot_reply(tag)
        else:
            response = 'sorry, i am still learning. Call us to get more info'
    else:
        response = 'please ask me a question'
    # return json.dumps({'botreply':response, 'query' : query})
    return response

