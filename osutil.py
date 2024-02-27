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
        embed.title = f'Recent osu! play for {p_message[1]}'
        
        #User ID / Name
        id = api.user(p_message[1]).id
        scores = api.user_scores(id, "recent", include_fails=True, mode=None, limit=1)
        recent = scores[0]

        #Acc
        acc = recent.accuracy*100
        acc_rounded= round(acc,2)

        #PP (masih ga bisa)
        pp = recent.pp
        if pp is float:
            pp = round(pp,2)
        elif pp is None:
            pp = 'No pp'

        #Score
        score = recent.score

        #Map details
        title = recent.beatmapset.title
        beatmapid = recent.beatmap.id

        #Rank emoji gaje
        rank = str(recent.rank).split('.')[1]
        rank_emoji = get_rank_emoji(rank)
        
        #Beatmap image
        image = f'https://b.ppy.sh/thumb/{recent.beatmapset.id}.jpg'
        embed.set_thumbnail(url=image)

        embed.description = f'[{title}](https://osu.ppy.sh/b/{beatmapid}) \n Score: {score} \n Accuracy: {rank_emoji}{acc_rounded}% \n PP: {pp}\n'

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

 