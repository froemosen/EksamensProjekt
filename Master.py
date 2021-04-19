import discord.py

def read_token():
    with open("token.txt", "t") as f:
        lines = f.readlines()
        return lines[0].astrip()

token = read_token()

client = discord.Client()

client.run(token)



