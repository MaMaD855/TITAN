import os
import discord
import asyncio
import time
#import requests as rq
from discord.ext import commands
from discord.ext import tasks


class CONFING:
    TOKEN = 'Nzc0OTgyNjg1MjUyMTI0NzAy.X6fs3g.ltWFA84Dk4-RpjV4Q-qrKOGFttg'
    PREFIX = '^'

client = commands.Bot(command_prefix=CONFING.PREFIX)
client.remove_command('help')




## Events
@client.event
async def on_ready():
    print('Bot Is Ready!')
    client.my_current_task = live_status.start()



## Live Status
@tasks.loop()
async def live_status(seconds=75):
    Dis = client.get_guild(827883415654105119) #Int

    activity = discord.Activity(type=discord.ActivityType.watching, name=f'👥 {Dis.member_count}')
    await client.change_presence(activity=activity)
    await asyncio.sleep(15)

    activity = discord.Activity(type=discord.ActivityType.watching, name=f'MaMaD#9869')
    await client.change_presence(activity=activity)
    await asyncio.sleep(15)





@client.command(aliases=['avatar','profile','pro'])
async def profile_fard_ro_neshoo_mide(ctx):
    mention = ctx.author.mention
    
    avatar = ctx.author.avatar_url
    
    await ctx.send(mention +'avatar shoma '                                                            +str(avatar))



@client.command()
async def avbot(ctx):
    my_embed = discord.Embed(
        title="avatar bot",
        colour=0x000000
    )
    my_embed.set_footer(text='💖MaMaD#1912')
    my_embed.set_image(url='https://cdn.discordapp.com/attachments/788059961908658246/788310482875449364/1608018229337.png')
    await ctx.send(embed=my_embed)



@client.command()
async def password(ctx, *, values):
    values = values.split()

    password = values[0]
    name = values[1]

    await ctx.send('password : '+password+'\n'+
    'name : '+name)




@client.command()
@commands.has_permissions(administrator=True)
async def setstatus(ctx, status_type):
    if(status_type == 'idl'):
        #idle mishe
        await ctx.send('jojo status be ~~idle~~ taqir kard')
        await client.change_presence(status=discord.Status.idle)
    if(status_type == 'dnd'):
        #dnd mishe 
        await ctx.send('jojo status be ~~dnd~~ taqir kard')
        await client.change_presence(status=discord.Status.dnd)
    if(status_type == 'online'):
        #online mishe
        await ctx.send('jojo status be ~~online~~ taqir kard')
        await client.change_presence(status=discord.Status.online)
    else:
        #unknoe command
        await ctx.send('setstatus na moshakhas')




@client.command()
@commands.has_permissions(administrator=True)
async def setactivity(ctx, activity_type, *,activity_text):
    
    if(activity_type == 'playing'):
        await client.change_presence(activity=discord.Game(name=activity_text))
        await ctx.send('activity avaz shod jojo.')

    elif(activity_type == 'streaming'):
        await client.change_presence(activity=discord.Streaming(name=activity_text, url='https://www.twitch.tv/twitch'))
        await ctx.send('activity avaz shod jojo.')

    elif(activity_type == 'watching'):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching ,name=activity_text ))
        await ctx.send('activity avaz shod jojo.')

    elif(activity_type == 'listening'):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening ,name=activity_text ))
        await ctx.send('activity avaz shod jojo.')

    else:
        #unknoe command
        await ctx.send('Activity na moshakhas')

#-----------------------------------------------------------------------------------         



@client.command()
async def dv(ctx):
    my_embed = discord.Embed(
        title="MaMaD",
        colour=0x00CECE
    )
    my_embed.set_footer(text='💖MaMaD#1912')
    await ctx.send(embed=my_embed)


@client.command()
async def discordlink(ctx):
    my_embed = discord.Embed(
        title="📌link discord hatman ozv beshin",
        description="https://discord.gg/Qxvc57r5",
        colour=0x00CECE
    )
    my_embed.set_footer(text='nitro mide jojo ha')
    #my_embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/783319387134230558/7e9f018457d36e21a3c3d48488d316e9.png?size=1024')
    await ctx.send('~~@here~~',embed=my_embed)




@client.command()
async def help(ctx):
    colors = [0x00FF00, 0xFF0000, 0x0000FF, 0x00CECE, 0x000000]
    #titles = ["💦", '😎', '🎮', '💧', '💖', '🎁', '👳‍♂️', '📌', '🎃', '🌈']
    my_embed = discord.Embed(
        title="Relux Plugins Commands",
        description="#",
        colour=random.choice(colors)
    )
    my_embed.set_footer(text='MaMaD#1912')
    my_embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/783319387134230558/7e9f018457d36e21a3c3d48488d316e9.png?size=1024')
    await ctx.send(embed=my_embed)



@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, count='10'):
    count = int(count)
    await ctx.channel.purge(limit=count+1)
    await ctx.send(">>> "+str(count)+' Message pak shod. ')




## DiscordID Lookup
@client.command(aliases=['discord', 'did', 'whois'])
@commands.has_permissions(administrator=True) 
async def discord_identifier(ctx, disid: int=None):
    
    if not disid:
        await ctx.send('<@{}>, Please Specify A DiscordID!'.format(ctx.message.author.id))
        return
    try:
        obj = await client.fetch_user(disid)
        if not obj:
            await ctx.send('User `{}` Not Found!'.format(disid))
        else:
            dembed = discord.Embed(title='DiscrdID Identifier Query Successful!', descrption='API Returted Values :', color=discord.Color.dark_gold())
            dembed.add_field(name='Discord Username :', value=obj)
            dembed.add_field(name='DiscordID :', value=obj.id)
            dembed.set_image(url=obj.avatar_url)
            await ctx.send(embed=dembed)
    except Exception as err:
        print(err)









## Say Commands
@client.command(pass_content=True, aliases=['s'])
@commands.has_permissions(administrator=True) 
async def warn(ctx, *, text):
    
    try:
        await ctx.message.delete()
        timenow = time.strftime("%H:%M")
        embed=discord.Embed(description=" ", color=0xfff705)
        embed.set_author(name="NEW WARN !!", icon_url="https://cdn.discordapp.com/attachments/874612856082038784/874657883470561350/attention-png-5a3a5331f0bb88.7633395615137718259861.jpg")
        embed.add_field(name="reason:", value=text, inline=False)
        embed.set_footer(text=f"warn by : {ctx.message.author} | MaMaD | {timenow}")
        await ctx.send(embed=embed)
    except Exception as err:
        print(err)


## hasy
@client.command(pass_context=True, aliases=['hs'])
@commands.has_permissions(administrator=True) 
async def hasy(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)



client.run(CONFING.TOKEN) 