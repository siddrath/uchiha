import discord
from discord.ext import commands
import random
class BAfun():

    def __init__(ctx, bot):
        ctx.bot = bot
        ctx.toggle = False
        ctx.nsword = ctx.nlove = ctx.nsquat = ctx.npizza = ctx.nbribe = ctx.ndad = ctx.ncalc \
            = ctx.nbutt = ctx.ncom = ctx.nflirt = ctx.nup = 0
        
@commands.command(name="8ball")
async def _ball(self, ctx, *, question):
        ': Ask me a question'
        question = question
        answers = random.randint(1, 20)

        if question == "":
            return

        elif answers == 1:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}``` It is certain```""")

        elif answers == 2:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  It is decidedly so```""")

        elif answers == 3:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Without a doubt```""")

        elif answers == 4:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}``` Yes definitely```""")

        elif answers == 5:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  You may rely on it```""")

        elif answers == 6:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  As i see it, yes```""")

        elif answers == 7:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Most likely```""")

        elif answers == 8:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Outlook good```""")

        elif answers == 9:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Yes```""")

        elif answers == 10:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Signs point to yes```""")

        elif answers == 11:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Reply hazy try again```""")

        elif answers == 12:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Ask again later```""")

        elif answers == 13:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Better not to tell you now```""")

        elif answers == 14:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}``` Cannot predict now```""")

        elif answers == 15:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Concentrate and ask again```""")

        elif answers == 16:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Don't count on it```""")

        elif answers == 17:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  My reply is no```""")

        elif answers == 18:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  My sources say no```""")

        elif answers == 19:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Outlook not so good```""")

        elif answers == 20:
            await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Very doubtful```""")
     
@commands.command()
async def sword(ctx,  *, user: discord.Member):
    """Sword Duel!"""
    author = ctx.message.author
    if user.id == ctx.bot.user.id:
        await ctx.send("I'm not the fighting kind")
    else:
        await ctx.send(author.mention + " and " + user.mention + " dueled for " + str(randint(2, 120)) +
                            " gruesome hours! It was a long, heated battle, but " +
                            choice([author.mention, user.mention]) + " came out victorious!")
    ctx.counter(n)

@commands.command()
async def love(ctx, user: discord.Member):
    """Found your one true love?"""
    author = ctx.message.author
    if user.id == ctx.bot.user.id:
        await ctx.send("I am not capable of loving like you can. I'm sorry." )
    else:
        await ctx.send(author.mention + " is capable of loving " + user.mention + " a whopping " +
                            str(randint(0, 100)) + "%!")
    ctx.counter(n)

@commands.command()
async def squat(ctx):
    """How is your workout going?"""
    author = ctx.message.author
    await ctx.send(author.mention + " puts on their game face and does " + str(randint(2, 1000)) +
                        " squats in " + str(randint(4, 90)) + " minutes. Wurk it!")
    ctx.counter(n)

@commands.command()
async def pizza(ctx):
    """How many slices of pizza have you eaten today?"""
    author = ctx.message.author
    await ctx.send(author.mention + " has eaten " + str(randint(2, 120)) + " slices of pizza today.")
    ctx.counter(n)

@commands.command()
async def bribe(ctx):
    """Find out who is paying under the table"""
    author = ctx.message.author
    await ctx.send(author.mention + " has bribed " + ctx.bot.user.mention + " with " +
                        str(randint(10, 10000)) + " dollars!")
    ctx.counter(n)

@commands.command()
async def daddy(ctx):
    """Pass the salt"""
    author = ctx.message.author
    await ctx.send("I'm kink shaming you, " + author.mention)
    ctx.counter(n)

@commands.command()
async def calculated(ctx):
    """That was 100% calculated!"""
    await ctx.send("That was " + str(randint(0, 100)) + "% calculated!")
    ctx.counter(n)

@commands.command()
async def butts(ctx):
    """butts"""
    await ctx.send("ლ(́◉◞౪◟◉‵ლ)")
    ctx.counter(n)

@commands.command()
async def _commands(ctx):
    """Command the bot"""
    await ctx.send("Don't tell me what to do.")
    ctx.counter(n)

@commands.command()
async def flirt(ctx):
    """Slide into DMs"""
    await ctx.send(" ;)) ))) hey b a b e ; ; ;))) ) ;)")
    ctx.counter(n)

@commands.command()
async def updog(ctx):
    """This is updog"""
    await ctx.send("What's updog?")
    ctx.counter(n)
@commands.command(pass_context=True)
async def poke(ctx, member: discord.Member):
    """poke someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    poke = "**{0} poked {1}!**"

    choices = ['https://pa1.narvii.com/6021/b50b8078fa1d8e8f6d2ebfb085f106c642141723_hq.gif',
               'https://media1.tenor.com/images/8fe23ec8e2c5e44964e5c11983ff6f41/tenor.gif',
               'https://media.giphy.com/media/WvVzZ9mCyMjsc/giphy.gif',
               'https://media.giphy.com/media/pWd3gD577gOqs/giphy.gif',
               'http://gifimage.net/wp-content/uploads/2017/09/anime-poke-gif-12.gif', 'https://i.gifer.com/S00v.gif',
               'https://i.imgur.com/1NMqz0i.gif']

    image = random.choice(choices)

    embed = discord.Embed(description=poke.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)

@commands.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    """hug someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    hug = "**{0}Aww, I see you are lonely, take a hug <3{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/447337220895145998/466226631778893824/hug-rk_6GyncG.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466227315110576129/hug-ry6o__7D-.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466227511165190175/hug-Bk5haAocG.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466228974326906891/hug-BkBs2uk_b.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466229286966394881/hug-HkfgF_QvW.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466230001872666635/hug-BkZngAYtb.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466230123209687040/hug-Bk5T2_1Ob.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466230234795212802/hug-Hy4hxRKtW.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=hug.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)

@commands.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    """Slap someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    slap = "**{0}Hmm, why do you want this?Slaps.{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/447337220895145998/466229677300908042/slap-rJYqQyKv-.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466229535059345408/slap-r1PXzRYtZ.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466229453236731904/slap-SkSCyl5yz.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466231429337055242/slap-B1-nQyFDb.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466231614352130048/slap-HkskD56OG.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466231875120267284/slap-By2iXyFw-.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466232154112917504/slap-SkKn-xc1f.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466232493889290241/slap-rJrnXJYPb.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=slap.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)


@commands.command()
async def dog(ctx):
    ''''sends cute dog pics'''
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    embed=discord.Embed()
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed)



@commands.command(pass_context=True, no_pm=True)
async def insult(ctx, user : discord.Member=None):
    """Insult the user"""

    msg =" How original. No one else had thought of trying to get the bot to insult itself. I applaud your creativity. Yawn. Perhaps this is why you don't have friends. You don't add anything new to any conversation. You are more of a bot than me, predictable answers, and absolutely dull to have an actual conversation with."
    if user != None:
        if user.id == ctx.bot.user.id:
            user = ctx.message.author
            await ctx.send(user.mention + msg)
        else:
            await ctx.send(user.mention + msg + random.choice(msg))
    else:
        await ctx.send(ctx.message.author.mention + msg + random.choice(msg))

@commands.command(pass_context=True)
async def bite(ctx, member: discord.Member):
    """bites  someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    bite = "**{0}bites you.{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/456701536912015361/466571069973856256/bite-HkutgeXob.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466571762339938304/bite-ry00lxmob.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466572007258193920/bite-H1_Jbemjb.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466572188372434964/bite-H1hige7sZ.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466572377233293322/bite-Hk1sxlQjZ.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466572552739880961/bite-rkakblmiZ.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466572804385669120/bite-BJXRmfr6-.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466573024078987284/bite-ry3pQGraW.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=bite.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)

@commands.command(pass_context=True)
async def cuddle(ctx, member: discord.Member):
    """cuddle  someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    cuddle = "**cuddles you.{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/456701536912015361/466573538841591809/cuddle-SJn18IXP-.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466573996201082900/cuddle-r1s9RqB7G.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466574139805794306/cuddle-SJceIU7wZ.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466574279127859200/cuddle-r1XEOymib.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466574467070427156/cuddle-S1T91Att-.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466574644577697792/cuddle-BkZCSI7Pb.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466574850375548939/cuddle-Byd1IUmP-.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466575399862665216/cuddle-BkN0rIQDZ.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=cuddle.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)


@commands.command(pass_context=True)
async def pat(ctx, member: discord.Member):
    """pat someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    pat = "**you have been patted .{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/456701536912015361/466577618771378176/pat-rktsca40-.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466577986209185812/pat-rkZbJAYKW.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466578464619626496/pat-SJva1kFv-.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466578677090484224/pat-BkJBQlckz.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466578825468182538/pat-H1s5hx0Bf.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466579159435706380/pat-rJMskkFvb.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466579338490544128/pat-rkBZkRttW.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466579500117917727/pat-Sk2FyQHpZ.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=pat.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)

@commands.command(pass_context=True)
async def kiss(ctx, member: discord.Member):
    """kiss someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    kiss = "**  kissed you.{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/456701536912015361/466579840070582284/kiss-B1MJ2aODb.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466580423116324874/kiss-Hkt-nTOwW.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466581686591946763/kiss-r1VWnTuPW.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466582897755947017/kiss-BkUJNec1M.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466583102047780914/kiss-Sk1k3TdPW.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466583257341755392/kiss-BJv0o6uDZ.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466583404222087168/kiss-S1PCJWASf.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466583780736499712/kiss-SJ3dXCKtW.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=kiss.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)
@commands.command(pass_context=True)
async def pepe(ctx, user: discord.Member = None):
    """kiss someone!"""
    user = user or ctx.message.author

    pepe = "**  kissed you.{1}!**"

    choices = ["http://i.imgur.com/vpIyEue.png",
               "http://i.imgur.com/0koMC0v.jpg",
               "http://i.imgur.com/9Q6KMZa.png",
               "http://i.imgur.com/54xy6jr.png",
               "http://i.imgur.com/QvCngiJ.jpg",
               "http://i.imgur.com/ftWgrOE.jpg",
               "http://i.imgur.com/rhDSqRv.jpg",
               "http://i.imgur.com/89NZ3zM.jpg",
               "http://i.imgur.com/I4cIH5b.png",
               "http://i.imgur.com/GIFc4uX.png",
               "http://i.imgur.com/bgShJpZ.png",
               "http://i.imgur.com/jpfPLyn.png",
               "http://i.imgur.com/pZeYoej.png",
               "http://i.imgur.com/M8V9WKB.jpg",
               "http://i.imgur.com/ZBzHxNk.jpg",
               "http://i.imgur.com/xTyJ6xa.png",
               "http://i.imgur.com/TOozxRQ.png",
               "http://i.imgur.com/Eli5HdZ.png",
               "http://i.imgur.com/pkikqcA.jpg",
               "http://i.imgur.com/gMF8eo5.png",
               "http://i.imgur.com/HYh8BUm.jpg",
               "http://i.imgur.com/ZGVrRye.jpg",
               "http://i.imgur.com/Au4F1px.jpg",
               "http://i.imgur.com/gh36k9y.jpg",
               "http://i.imgur.com/MHDoRuN.png",
               "http://i.imgur.com/V3MJfyK.png",
               "http://i.imgur.com/QGGTipc.jpg",
               "http://i.imgur.com/PRFrTgz.png",
               "http://i.imgur.com/9UBJrwM.jpg",
               "http://i.imgur.com/WQY9Vhb.jpg",
               "http://i.imgur.com/sIbQdou.jpg",
               "http://i.imgur.com/LlUMg00.jpg",
               "http://i.imgur.com/MmijlWa.png",
               "http://i.imgur.com/i0CrtrX.png",
               "http://i.imgur.com/Dfpudwp.jpg",
               "http://i.imgur.com/hhg0wVF.gif",
               "http://i.imgur.com/7VDiIHN.jpg",
               "http://i.imgur.com/nxvXpNV.jpg",
               "http://i.imgur.com/DZYEjrW.gif",
               "http://i.imgur.com/mnyQ0Rh.jpg",
               "http://i.imgur.com/aHawbbs.jpg",
               "http://i.imgur.com/g8cCHV7.jpg",
               "http://i.imgur.com/E2cMU7Y.jpg",
               "http://i.imgur.com/PkmcgGF.jpg",
               "http://i.imgur.com/7qLQ1xl.jpg",
               "http://i.imgur.com/7qLQ1xl.jpg",
               "http://i.imgur.com/arSsPwf.png",
               "http://i.imgur.com/xcYh4iC.png",
               "http://i.imgur.com/9692WND.jpg",
               "http://i.imgur.com/diAK5Nu.jpg",
               "http://i.imgur.com/zDs0tRW.jpg",
               "http://i.imgur.com/PEM87nV.jpg",
               "http://i.imgur.com/zlCzlND.jpg",
               "http://i.imgur.com/n0OHxDl.jpg",
               "http://i.imgur.com/TQRf1WH.png",
               "http://i.imgur.com/zi9ad15.jpg",
               "http://i.imgur.com/b8A6Qke.jpg",
               "http://i.imgur.com/YuLapEu.png",
               "http://i.imgur.com/fWFXkY1.jpg",
               "http://i.imgur.com/i5vNvWU.png",
               "http://i.imgur.com/oXwUwtJ.jpg",
               "http://i.imgur.com/hadm4jV.jpg",
               "http://i.imgur.com/gbCvkqo.png",
               "http://i.imgur.com/wDiiWBG.jpg",
               "http://i.imgur.com/Mvghx4V.jpg",
               "http://i.imgur.com/SnTAjiJ.jpg",
               "http://i.imgur.com/QvMYBnu.png",
               "http://i.imgur.com/WkzPvfB.jpg",
               "http://i.imgur.com/PfAm4ot.png",
               "http://i.imgur.com/SIk4a45.png",
               "http://i.imgur.com/aISFmQq.jpg",
               "http://i.imgur.com/sMQkToE.png",
               "http://i.imgur.com/7i3cBrP.png",
               "http://i.imgur.com/1oMSz6e.png",
               "http://i.imgur.com/nVCRnRv.png",
               "http://i.imgur.com/FzWmxmi.jpg",
               "http://i.imgur.com/rpUI20F.jpg",
               "http://i.imgur.com/FDmnFDZ.jpg",
               "http://i.imgur.com/40Z1Yyg.jpg",
               "http://i.imgur.com/osy5Nu4.png",
               "http://i.imgur.com/4w81MSS.jpg",
               "http://i.imgur.com/qRXQFYa.png",
               "http://i.imgur.com/A1af62j.jpg",
               "http://i.imgur.com/wOc6fUe.jpg",
               "http://i.imgur.com/Z6ILiJ4.jpg",
               "http://i.imgur.com/537UpEJ.jpg",
               "http://i.imgur.com/HDc6kko.png",
               "http://i.imgur.com/oyLpuXq.jpg",
               "http://i.imgur.com/iCmGtJS.jpg",
               "http://i.imgur.com/MjpnlQm.png",
               "http://i.imgur.com/c6MWRQ9.jpg"]


    image = random.choice(choices)

    embed = discord.Embed(description=f"""{user.name}""", colour=discord.Colour(0xba4b5b))
    embed.add_field(name=' Random', value=f''' ~~pepe~~''', inline=False)
    embed.set_image(url=image)


    await ctx.send(embed=embed)



@commands.cooldown(1,120 , commands.BucketType.user)
@commands.command(aliases= ["s"])
async def spawn(ctx, user: discord.Member = None): 
    user = user or ctx.message.author
     


    spawn = "**  A wild .{1}!**"

    
    choices = ["http://www.pokestadium.com/sprites/xy/shiny/xerneas.gif",
                 "http://www.pokestadium.com/sprites/xy/xerneas-active.gif",
                 "http://www.pokestadium.com/sprites/xy/zekrom.gif",
                 "http://www.pokestadium.com/sprites/xy/charizard.gif",
                 "http://www.pokestadium.com/sprites/xy/shiny/charizard.gif",
                 "http://www.pokestadium.com/sprites/xy/yveltal.gif",
                 "http://www.pokestadium.com/sprites/xy/shiny/yveltal.gif",
                 "http://www.pokestadium.com/sprites/xy/raikou.gif",
                 "http://www.pokestadium.com/sprites/xy/shiny/raikou.gif",
                 "https://cdn.discordapp.com/attachments/386324037552308224/503050326627319809/PokecordSpawn.jpg",
                 "https://cdn.discordapp.com/attachments/386324037552308224/503050526603214848/PokecordSpawn.jpg",
                 "https://cdn.discordapp.com/attachments/386324037552308224/503050157286227968/PokecordSpawn.jpg",
                 "https://cdn.discordapp.com/attachments/482056981931098112/502861665180581908/PokecordSpawn.jpg",
                 "https://img.nijimen.net/uploads/topic/wide_image/18879/78ea52a0-5e3c-48ee-bbe4-8ff6fe38764b.jpg"
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRE1NX0EsJ0SUcP1LEdglNTN12UIatAoXfA1rxuz1fkL8Q8vWL9zQ",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOENKjnLEl2H8OdMbOaVqJT0QWr0toBNsWfKa3wQWh_mj827UsLg",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo8_G9cOLmqWNGNFh1BxSx_bkpNOxIW7sv2bqlClQgI_u9TiVx"]
      
    image = random.choice(choices)

    embed = discord.Embed(description=f"""{user.name}""", colour=discord.Colour(0xba4b5b))
    embed.add_field(name=' A wild pokémon has appeared!', value=f''' ~~Guess the pokemon~~''', inline=False)
    embed.set_image(url=image)



    await ctx.send(embed=embed)


@commands.command()
async def cat(ctx):
        """Get a random cat image!

        **Usage:** `g_dog`

        **Permission:** User"""
        isVideo = True
        while isVideo:
            r = requests.get('https://random.dog/woof.json')
            js = r.json()
            if js['url'].endswith('.mp4'):
                pass
            else:
                isVideo = False
        colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = int(random.random() * len(colours))
        content = [":dog: Don't be sad! This doggy wants to play with you!", "You seem lonely, {0.mention}. Here, have a dog. They're not as nice as cats, but enjoy!".format(ctx.message.author), "Weuf, woof, woooooooooof. Woof you.", "Pupper!", "Meow... wait wrong animal."]
        con = int(random.random() * len(content))
        em = discord.Embed(color=colours[col])
        em.set_image(url=js['url'])
        await ctx.send(content=content[con], embed=em)

@commands.command()
async def neko(ctx):
    ''''sends cute dog pics'''
    r = requests.get("https://nekos.life/api/neko").json()

    colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
    col = int(random.random() * len(colours))
    content = [":neko: Don't be sad! This neko wants to play with you!", "You seem lonely, {0.mention}. Here, have a neko. They're not as nice , but enjoy!".format(ctx.message.author), "Weuf, woof, woooooooooof. Woof you.", "Pupper!", "Meow... wait its neko."]
    con = int(random.random() * len(content))
    embed=discord.Embed()
    embed.set_image(url=r["neko"])
    await ctx.send(content=content[con],embed=embed)


@commands.command(pass_context=True)
async def rps(ctx, choice):
    """"""
    choices = ["rock", "paper", "scissors"]
    await ctx.send("You chose {} | CPU chose {}".format(choice, random.choice(choices)))

def setup(bot):
    bot.add_cog(BAfun(bot))
