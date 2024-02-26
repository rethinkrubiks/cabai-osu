import discord
from ossapi import Ossapi
from osutil import response_osu

client_id = '30542'
client_secret = 'mhDf5MLsXMF67W3FZiBABqnt0DKWN8ZCRUtSTTTp'
api = Ossapi(client_id, client_secret)
    

def handle_response(message): 
    p_message = message.lower()

    if p_message == 'hello':
        return 'hi'
    
#    if p_message == 'reto_item': <---- scrap anjign jangan dimasukin
#        return 'item banget ngentot'
    
#    if p_message == 'genosida': <---- JANGAN COK
#        return 'GENOSIDA KULIT HITAM'
    
    else: return response_osu(p_message)
        

        
