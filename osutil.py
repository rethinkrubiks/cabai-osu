import discord
from ossapi import Ossapi, GameMode
from datetime import datetime as dt
import dotenv

client_id = '30542'
config = dotenv.dotenv_values('.env')
api = Ossapi(client_id, config['SECRET'], 'http://localhost:3900/')

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
        
        #no score
        if len(scores) == 0:
            embed.description = 'No recent play'
            return embed

        #Score / Replay
        recent = scores[0]
        score = recent.score
        formatted_score = '{:,}'.format(score)
        replay = api.download_score(GameMode('osu'), recent.id)

        #Map details
        beatmapid = recent.beatmap.id
        beatmapset = recent.beatmapset
        diff = recent.beatmap.version
        #beatmap_attributes = api.beatmap_attributes(beatmap_id={beatmapid}, mods=None, ruleset=None, ruleset_id=None)

        title = f'{beatmapset.artist} - {beatmapset.title} [{diff}]' #fix diff name
        
        embed.description = f'[{title}](https://osu.ppy.sh/b/{beatmapid})\n'
        embed.description += f'Score: {formatted_score}\n'

        #Rank emoji
        rank = str(recent.rank).split('.')[1]
        rank_emoji = get_rank_emoji(rank)
        
        #Beatmap image
        image = f'https://b.ppy.sh/thumb/{recent.beatmapset.id}.jpg'
        embed.set_thumbnail(url=image)

        #Combo
        combo = str(recent.max_combo)
        embed.description += f' Combo: ({combo}/{replay.max_combo}) \n'

        #Acc
        acc = recent.accuracy*100
        acc_rounded= round(acc,2)
        embed.description += f' Accuracy: {rank_emoji} {acc_rounded}% \n'

        #PP (harus submitted / overwritten & ranked)
        pp = recent.pp
        if pp is float:
            pp = round(pp,2)
        elif pp is None:
            pp = 'No pp'
        embed.description += f' PP: {pp}\n'

        #Mods
        mods = str(recent.mods)
        embed.description += f' Mods: {mods}\n'

        #Time
        time = recent.created_at
        if isinstance(time, str):
            time = dt.strptime(time, '%Y-%m-%d %H:%M:%S%z')
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
        
        embed.set_footer(text=f'Played at {formatted_time} UTC+0', icon_url=f'https://cdn.discordapp.com/attachments/1211770479828803665/1213033595237703730/Osu_Logo_2016.svg.png?ex=65f40092&is=65e18b92&hm=438f30196ac3633c44193d185da4d5eac7cf0eafd9ad0335193885a6823e6b51&')
        
        return embed
    
    if p_message[0] == 'p':

        #User ID / Name
        username = ''
        for i in range(1, len(p_message)):
            username += p_message[i] + ' '
        username = username.rstrip()
        user = api.user(username)
        id = api.user(username).id
        username = user.username

        embed = discord.Embed()
        embed.colour=discord.Colour.dark_teal()
        embed.title = f'osu! profile of {username}'

        #pfp
        image = f'https://a.ppy.sh/{id}'
        embed.set_thumbnail(url=image)

        #Rank
        globalrank = user.statistics.global_rank
        formatted_globalrank = '{:,}'.format(globalrank)

        countryrank = user.statistics.country_rank
        formatted_countryrank = '{:,}'.format(countryrank)
        embed.description = f'Global Rank: #{formatted_globalrank}\n Country Rank: #{formatted_countryrank}\n'

        #pp
        pp = user.statistics.pp
        pp_rounded = round(pp,2)
        embed.description += f'PP: {pp_rounded}\n'

        #playcount
        pc = user.statistics.play_count
        embed.description += f'Playcount: {pc}'

        #join date
        jd = user.join_date
        if isinstance(jd, str):
            jd = dt.strptime(jd, '%Y-%m-%d %H:%M:%S%z')
        formatted_jd = jd.strftime('%Y-%m-%d %H:%M:%S')
        embed.set_footer(text=f'Joined at {formatted_jd} UTC+0', icon_url=f'https://cdn.discordapp.com/attachments/1211770479828803665/1213033595237703730/Osu_Logo_2016.svg.png?ex=65f40092&is=65e18b92&hm=438f30196ac3633c44193d185da4d5eac7cf0eafd9ad0335193885a6823e6b51&')

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

 