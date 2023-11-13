import discord
import time
import asyncio

def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined} \n")
            messages = 0
            joined = 0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)



@client.event
async def on_member_join(member):
    global joined
    joined+=1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"Welcome to the server {member.mention}")

@client.event
async def on_message(message):
    global messages
    messages+=1
    id = client.get_guild(1124087027487490168)
    valid_users = ['.vedantmahajan']
    channels = ["commands"]
    #! For checking the valid user add the condition of str(message.author) in valid_users
    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == '!users':
            await message.channel.send(f"# of Members {id.member_count}")
    else:
        print(f"User: {message.author} tried to Command {message.content} in channel {message.channel}")

client.loop.create_task(update_stats()) #? This is added to apply any background task in the channel.
client.run(token)