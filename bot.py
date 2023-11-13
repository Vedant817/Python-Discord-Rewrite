import discord

def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"Welcome to the server {member.mention}")

@client.event
async def on_message(message):
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

client.run(token)