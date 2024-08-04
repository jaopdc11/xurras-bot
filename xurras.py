import discord
from discord.ext import commands
import datetime as dt
import requests as r
import os
import random
import re
import asyncio
from custom_commands import bot
import threading
import aiohttp
from googlesearch import search
import locale
import colorama
from colorama import Fore, Style
import youtube_dl


colorama.init()

os.system('cls')

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intents)

@client.event
async def on_ready():
    channel1 = client.get_channel(932333634596274191)
    channel2 = client.get_channel(1097322973930729572)
    os.system('cls')
    print(Fore.YELLOW + '-------------------' + Style.RESET_ALL)
    print(Fore.BLUE + 'BOT ON!!' + Style.RESET_ALL)
    print(Fore.GREEN + f'{client.user.name}' + Style.RESET_ALL)
    print(Fore.GREEN + f'{client.user.id}' + Style.RESET_ALL)
    print(Fore.YELLOW + '-------------------' + Style.RESET_ALL)
    #await channel1.send(f'to on rapazeada!!')
    await channel2.send(f'to livre, manda bala!')

@client.command(name='oi')
async def ola(context):
    await context.message.channel.send('koe pae, suave?')
    
@client.command(name='data')
async def data(context):
    d = dt.datetime.now()
    await context.message.channel.send(d)
    
@client.command(name='dol')
async def dol(context):
    req = r.get ('https://economia.awesomeapi.com.br/last/USD-BRL')
    req_dic = req.json()
    cot_dol = req_dic ['USDBRL']["bid"]
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    cot_dol_float = float(cot_dol)
    cot_dol_str = f"R${cot_dol_float:,.2f}".replace(",", ".")
    await context.message.channel.send('a cotação do dólar no momento é de: {}'.format(cot_dol_str))
    
@client.command(name='eur')
async def eur(context):    
    req = r.get ('https://economia.awesomeapi.com.br/last/EUR-BRL/')
    req_dic = req.json()
    cot_eur = req_dic ['EURBRL']["bid"]
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    cot_eur_float = float(cot_eur)
    cot_eur_str = f"R${cot_eur_float:,.2f}".replace(",", ".")
    await context.message.channel.send('a cotação do euro no momento é de: {}'.format(cot_eur_str))
    
@client.command(name='btc')
async def btc(context):
    req = r.get ('https://economia.awesomeapi.com.br/last/BTC-BRL/')
    req_dic = req.json()
    cot_btc = req_dic ['BTCBRL']["bid"]
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    cot_btc_float = float(cot_btc)
    cot_btc_str = f"R${cot_btc_float:,.2f}".replace(",", ".")
    await context.message.channel.send('a cotação do bitcoin no momento é de: {}'.format(cot_btc_str))

@client.command(name='id')
async def id(ctx, member: discord.Member):    
    userid = member.id
    await ctx.send(f"o id do(a) {member.name} é {userid}.")
    
@client.command(name='of')
async def id(ctx, member: discord.Member):
    with open ('of.txt', 'r') as of:
        of_list = of.readlines()
        of_ch = random.choice(of_list)
    
    await ctx.send(f"{of_ch} {member.mention}")

@client.command(name='rnum')
async def rnum(ctx):

    msg = ctx.message.content

    numeros = re.findall(r'\d+', msg)

    a = int(numeros[0])
    b = int(numeros[1])

    resultado = random.randint(a, b)

    await ctx.send(f'o número sorteado entre {a} e {b} é: {resultado}')

@client.command(name='soma')
async def soma(ctx):
    
    msg = ctx.message.content

    numeros = re.findall(r'\d+', msg)

    a = float(numeros[0])
    b = float(numeros[1])
    
    c = (a + b)
    
    await ctx.send(f'a soma de {a} + {b} é: {c}')
    
@client.command(name='sub')
async def sub(ctx):
    
    msg = ctx.message.content

    numeros = re.findall(r'\d+', msg)

    a = float(numeros[0])
    b = float(numeros[1])
    
    c = (a - b)
    
    await ctx.send(f'a diferença entre {a} e {b} é: {c}')
    
@client.command(name='multi')
async def sub(ctx):
    
    msg = ctx.message.content

    numeros = re.findall(r'\d+', msg)

    a = float(numeros[0])
    b = float(numeros[1])
    
    c = (a * b)
    
    await ctx.send(f'o produto de {a} e {b} é: {c}')

@client.command(name='div')
async def div(ctx):
    
    msg = ctx.message.content

    numeros = re.findall(r'\d+', msg)

    a = float(numeros[0])
    b = float(numeros[1])
    
    c = (a / b)
    
    await ctx.send(f'o resultado da divisão de {a} e {b} é: {c}')

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}'
API_KEY = 'f27ea92e69fe798fbc8604e05f42490d'

async def get_weather(city, state):
    async with aiohttp.ClientSession() as session:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},BR&units=metric&lang=pt_br&appid={API_KEY}'
        async with session.get(url) as resp:
            response = await resp.json()
            weather = response['weather'][0]['description']
            temperature = response['main']['temp']
            feels_like = response['main']['feels_like']
            return f"Em {city}/{state} está {weather} com temperatura de {temperature:.1f}°C e sensação térmica de {feels_like:.1f}°C."

@client.command(name='clima')
async def clima(ctx, city, state):
    weather = await get_weather(city, state)
    await ctx.send(weather)

@client.command(name='sabedoria')
async def sabedoria(context):
    resp_list = ['sim', 'não', 'talvez']
    resp_c = random.choice(resp_list)
    await context.message.channel.send('{}'.format(resp_c))

@client.command(name='ck')
@commands.has_role(932421124216746074)
async def ck(ctx, member: discord.Member, voice_channel: discord.VoiceChannel):
    voice_state = member.mention

    if voice_state:
        await member.move_to(None)
        await ctx.send(f'{member.mention} foi kickado da call!')
    else:
        await ctx.send(f'{member.mention} precisa estar em uma call para ser kickado!')    

@client.command(name='cm')
@commands.has_role(932421124216746074)
async def cm(ctx, member: discord.Member, channel: discord.VoiceChannel):
    if member.voice is None:
        await ctx.send(f"{member.name} não está em um canal de voz.")
    else:
        await member.move_to(channel)
        await ctx.send(f"{member.name} foi movido para #{channel.name}.")
        
@client.command(name='yt')
async def yt(ctx, *args):
    query = ' '.join(args)
    await ctx.send(f'Pesquisando por {query} no YouTube...')
    search_results = search(query, num_results=5)
    urls = []
    for result in search_results:
        if 'youtube.com' in result:
            urls.append(result)
    if not urls:
        await ctx.send('Nenhum resultado encontrado')
        return
    url = urls[0]
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': 'audio.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    vc = await ctx.author.voice.channel.connect()
    vc.play(discord.FFmpegPCMAudio('audio.mp3'))
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()
    os.remove('audio.mp3')

@client.command(name='sair')
async def sair(ctx):
    await ctx.voice_client.disconnect()

@client.command(name='pausa')
async def pausa(ctx):
    await ctx.voice_client.pause()

@client.command(name='continua')
async def continua(ctx):
    await ctx.voice_client.resume()

@client.command(name='p')
async def p(ctx):
    if not ctx.voice_client.is_playing():
        await ctx.send('Não há música tocando no momento.')
    return
    await ctx.voice_client.stop()
 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        title = info['title']
        url = info['url']

    vc.play(discord.FFmpegPCMAudio(url))
    await ctx.send(f'Tocando agora: {title}')

@client.command(name='h')
async def help(ctx):
    embed = discord.Embed(
        title = 'Comandos disponíveis:',
        description = 'Aqui está a lista de comandos que eu posso executar:',
        color = discord.Color.blue()
    )

    embed.add_field(
        
        name = '?oi',
        value = 'Dá um oi para você!',
        inline = False
        
    )

    embed.add_field(
        
        name = '?data',
        value = 'Mostra a data e a hora atual.',
        inline = False
        
    )

    embed.add_field(
        
        name = '?dol',
        value = 'Mostra a cotação atual do dólar em relação ao real.',
        inline = False
        
    )

    embed.add_field(
        
        name = '?eur',
        value = 'Mostra a cotação atual do euro em relação ao real.',
        inline = False
        
    )

    embed.add_field(
        
        name = '?btc',
        value = 'Mostra a cotação atual do bitcoin em relação ao real.',
        inline = False
        
    )

    embed.add_field(
        
        name = '?id',
        value = 'Mostra o ID de um usuário mencionado.',
        inline = False
        
    )

    embed.add_field(
        
        name = '?of <@user>',
        value = 'Sorteia uma mensagem de ofensa e menciona um usuário.',
        inline = False
        
    )

    embed.add_field(
        
        name = '?rnum <a> <b>',
        value = 'Sorteia um número inteiro aleatório entre os números a e b.',
        inline = False
        
    )

    embed.add_field(
        name = '?soma <a> <b>',
        value = 'Soma os valores a e b. Exemplo: ?soma 2 3',
        inline = False
    )

    embed.add_field(
        name = '?sub <a> <b>',
        value = 'Subtrai os valores b de a. Exemplo: ?sub 5 2',
        inline = False
    )

    embed.add_field(
        name = '?multi <a> <b>',
        value = 'Multiplica os valores a e b. Exemplo: ?multi 4 5',
        inline = False
    )

    embed.add_field(
        name = '?div <a> <b>',
        value = 'Divide o valor a pelo valor b. Exemplo: ?div 10 2',
        inline = False
    )

    embed.add_field(
        name = '?clima <cidade sem acento> <código do estado>',
        value = 'Mostra o clima, a temperatura e a sensação térmica de uma cidade brasileira.',
        inline = 'False'
    )
    
    embed.add_field(
        name = '?sabedoria <pergunta>',
        value = 'Responda uma pergunta com "sim", "não" ou "talvez".',
        inline = 'False'
    )

    embed.add_field(
        name = '?ck <@fulano>  <nome_de_um_canal_de_voz>',
        value = 'Kicka alguém de uma chamada de voz. Por enquanto, somente meu programador pode usar esse comando.',
        inline = 'False'
    )

    embed.add_field(
        name = '?cm <@fulano>  <nome_de_um_canal_de_voz',
        value = 'Move alguém da chamada de voz atual para uma específica. POr enquanto, somente meu programador pode usar esse comando.',
        inline = 'False'
    )

    embed.add_field(
        
        name = '?h',
        value = 'Mostra essa lista. Pensando bem, talvez eu não precisasse te avisar.',
        inline = False
        
    )

    await ctx.send(embed=embed)

client.run(bot token)
