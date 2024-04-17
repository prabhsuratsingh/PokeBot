import discord
import os
from dotenv import load_dotenv

from pokemon import *

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):

        msg = message.content
        # print(msg)
        # poke_name = msg.split('$')
        # print(poke_name)

        if message.author == self.user:
            return
        
        if message.content.startswith('$'):
            
            pokemon_name = msg.split('$')
            if is_valid_pokemon(pokemon_name[1]):
                await message.channel.send(get_sprite(pokemon_name[1    ]))
                await message.channel.send(f'{pokemon_name[1]} says hii!!!!')
            else:
                await message.channel.send('enter valid pokemon name!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents = intents)
client.run(os.environ['DISCORD_TOKEN'])
