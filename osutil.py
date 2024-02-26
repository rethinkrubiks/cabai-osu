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

        title = recent.beatmapset.title

        rank = str(recent.rank).split('.')[1]
        rank_emoji = get_rank_emoji(rank)
        


        image = f'https://b.ppy.sh/thumb/{recent.beatmapset.id}.jpg'
        embed.set_thumbnail(url=image)

        embed.description = f'Played by {p_message[1]}, {title} \n Accuracy: {rank_emoji}{acc_rounded} %'

        return embed
    
def get_rank_emoji(rank: str) -> discord.Emoji:
    if rank == 'A':
        pass
    elif rank == 'B':
        pass
    elif rank == 'C':
        pass
    elif rank == 'D':
        pass
    elif rank == 'F':
        pass
    elif rank == 'S':
        pass
    elif rank == 'SH':
        pass