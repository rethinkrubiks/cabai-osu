import discord
from ossapi import Ossapi
from osutil import response_osu
import dotenv

client_id = '30542'
config = dotenv.dotenv_values('.env')
api = Ossapi(client_id, config['SECRET'])
    

def handle_response(message): 
    p_message = message.lower()

    if p_message == 'hello':
        return 'hi'
    
#    if p_message == 'reto_item': <---- scrap anjign jangan dimasukin
#        return 'item banget ngentot'
    
#    if p_message == 'genosida': <---- JANGAN COK
#        return 'GENOSIDA KULIT HITAM'
    
    if p_message == 'mewing':
        image = f'https://cdn.discordapp.com/attachments/1211770479828803665/1212438597152538624/retomewing.jpg?ex=65f1d66f&is=65df616f&hm=9e613a2f35ce191a94c2e4d4f164a53fa5de332cdc3b1f88a8604ecd3288850e&'
        return image
    
    else: return response_osu(p_message)
        

        
