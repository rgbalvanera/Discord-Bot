import discord 
import os 
def handle_user_messages(msg) ->str:
    message = msg.lower() #Converts all inputs to lower case
    if(message == 'hi'):
        return 'Hi there'
    if(message =="hello"):
        return "Hello user. Welcome"

async def processMessage(message, user_message):
    try:
        botfeedback = handle_user_messages(user_message)
        await message.channel.send(botfeedback)
    except Exception as error:
        print(error)

def runBot():
    discord_token = 'MTE0MjAyNTYyNDkzMjg0MzU5MA.GAvF0I.ZRAgSRHz6YlEaIek2y5dyvybJJTc7Jhr10hI2E'
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print({client.user}, 'is live')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        await processMessage(message, 'hi')

    client.run(os.getenv('TOKEN'))