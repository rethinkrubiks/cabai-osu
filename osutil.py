import discord
from ossapi import Ossapi

client_id = '30542'
client_secret = 'mhDf5MLsXMF67W3FZiBABqnt0DKWN8ZCRUtSTTTp'
api = Ossapi(client_id, client_secret)

def response_osu(message):
    p_message = message.lower()

    p_message=p_message.split()

    if p_message[0] == 'r':

        embed = discord.Embed()
        embed.title = "Recent Play"
        
        
        id = api.user(p_message[1]).id
        scores = api.user_scores(id, "recent", include_fails=True, mode=None, limit=1)
        
        recent = scores[0]
        acc = recent.accuracy*100
        acc_rounded= round(acc,2)
        embed.description = "Accuracy: " + str(acc_rounded) + '%'

        return embed