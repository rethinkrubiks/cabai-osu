import discord
from ossapi import Ossapi

client_id = '30542'
client_secret = 'mhDf5MLsXMF67W3FZiBABqnt0DKWN8ZCRUtSTTTp'
api = Ossapi(client_id, client_secret)
    

def handle_response(message) -> str:
    p_message = message.lower()


    if p_message == 'hello':
        return 'hi'
    
    p_message=p_message.split()

    if p_message[0] == 'r':
        id = api.user(p_message[1]).id
        scores = api.user_scores(id, "recent", include_fails=True, mode=None, limit=1)
        
        recent = scores[0]
        return str(recent.accuracy) 
