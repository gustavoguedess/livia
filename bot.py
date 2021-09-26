#%%
# bot.py
import os

import discord
from dotenv import load_dotenv
import random 
import openai
import json

load_dotenv()

CONTINUOUS_LEARNING = False

openai.api_key = os.getenv('OPENAI_API_KEY')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

def open_base(arquivo):
    with open(arquivo, 'r') as f:
        base = f.read()
    return json.loads(base) 
client = discord.Client()
training = open_base('conversation.json')
training

#%%

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            #await guild.get_channel(878706873858142240).send('AAHAAAM CROQUE!')
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Olá {member.name}, bem vindo ao servidor mais badalado da CEU! Eu sou a assistente virtual Livia e eu vou responder qualquer dúvida que você tenha!'
    )

@client.event
async def on_message(message):
    if not CONTINUOUS_LEARNING:
        training = open_base('conversation.json')

    if message.author == client.user:
        return
    mensagem = message.content.lower()
    first_name = message.author.name
    training['prompt']+=first_name+':'+mensagem+'\n'
    if not 'livia' in message.content.lower() and not 'lívia' in message.content.lower() and random.random()<0.95:
        return


    training['prompt']+='Livia:'
    response = openai.Completion.create(**training)

    if 'choices' not in response or not response['choices']:
        return

    print(response['choices'])
    response = random.choice(response['choices'])['text']

    with open('responses.txt', 'a') as f:
        f.write(str(training)+'\n')
    
    training['prompt']+=response+'\n'
    await message.channel.send(response)


client.run(TOKEN)

#%%
#'''
training['prompt']+='Gustavo Guedes'+':'+'Oi Livia'+'\n'

training['prompt']+='Livia:'    

response = openai.Completion.create(**training)
training['prompt'].replace('Livia:','')

if 'choices' not in response or not response['choices']:
    print('sem respostas')

print(response['choices'])
response = random.choice(response['choices'])['text']
#'''

'''
for guild in client.guilds:
    print(guild)
    for channel in guild.channels:
        print(channel)
'''