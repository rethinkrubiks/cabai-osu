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
        embed.colour=discord.Colour.dark_teal()
        
        #User ID / Name / Scores
        username = ''
        for i in range(1, len(p_message)):
            username += p_message[i] + ' '
        username = username.rstrip()
        user = api.user(username)
        embed.title = f'Recent osu! play for {user.username}'
        scores = api.user_scores(user.id, "recent", include_fails=True, mode=None, limit=1)
        recent = scores[0]
        
        #no score
        if len(scores) == 0:
            embed.description = 'no recent play'
            return embed

        #Score
        score = recent.score

        #Map details
        title = recent.beatmapset.title
        beatmapid = recent.beatmap.id
        embed.description = f'[{title}](https://osu.ppy.sh/b/{beatmapid}) \n Score: {score}\n'

        #Rank emoji gaje
        rank = str(recent.rank).split('.')[1]
        rank_emoji = get_rank_emoji(rank)
        
        #Beatmap image
        image = f'https://b.ppy.sh/thumb/{recent.beatmapset.id}.jpg'
        embed.set_thumbnail(url=image)

        #Combo
        combo = str(recent.max_combo)
        maxcombo = str(recent.beatmap.max_combo)
        embed.description += f' Combo: ({combo}/{maxcombo}) \n'

        #Acc
        acc = recent.accuracy*100
        acc_rounded= round(acc,2)
        embed.description += f' Accuracy: {rank_emoji} {acc_rounded}% \n'

        #PP (masih ga bisa)
        pp = recent.pp
        if pp is float:
            pp = round(pp,2)
        elif pp is None:
            pp = 'No pp'
        embed.description += f' PP: {pp}\n'

        #Mods
        mods = str(recent.mods)
        embed.description += f' Mods: {mods}\n'
        
        return embed

    if p_message[0] == 'p':
        #User ID / Name
        user = api.user(p_message[1])
        id = api.user(p_message[1]).id

        embed = discord.Embed()
        embed.colour=discord.Colour.dark_teal()
        embed.title = f'osu! profile of {p_message[1]}'

        #pfp
        image = f'https://a.ppy.sh/{id}'
        embed.set_thumbnail(url=image)

        #Rank
        globalrank = user.statistics.global_rank
        countryrank = user.statistics.country_rank

        #pp
        pp = user.statistics.pp

        #playcount
        pc = user.statistics.play_count

        embed.description = f'Global Rank: #{globalrank}\n Country Rank: #{countryrank}\n PP: {pp}\n Playcount: {pc}'
        return embed
    

    
def get_rank_emoji(rank: str) -> discord.Emoji:
    if rank == 'A':
        return ":regional_indicator_a: "
    elif rank == 'B':
        return ":regional_indicator_b: "
    elif rank == 'C':
        return ":regional_indicator_c: "
    elif rank == 'D':
        return ":regional_indicator_d: "
    elif rank == 'F':
        return ":regional_indicator_f: "
    elif rank == 'S':
        return ":regional_indicator_s: "
    elif rank == 'SH':
        return ":regional_indicator_s: :regional_indicator_h: "

 