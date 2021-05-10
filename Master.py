import discord #pip install discord
from discord.ext import commands
import youtube_dl #pip install youtube_dl
import os
import time
from asyncio import sleep
#pip install PyNaCl
#INSTALLÉR FRA NETTET, OG SMID DE TRE .EXE fra 'bin' I SAMME MAPPE SOM youtube_dl



class MasterBot():
    def __init__(self, token):
        botIntents = discord.Intents.default()
        botIntents.members = True
        self.client = commands.Bot(command_prefix="!", intents=botIntents)
        self.queue = []
        
        #while True:
        self.decodeMsg()
        self.client.run(token)

    def decodeMsg(self):
        print("Master bot - Just Went Online")

        @self.client.command(pass_context = True)
        async def play(ctx, url):
            #Finding message author voice channel
            if (ctx.author.voice):
                channel = ctx.message.author.voice.channel
                print(channel)
                voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel) #Voice Channel to Object instead of channel name
            else:
                await ctx.send("You are not in a voice channel.")

            

            #Finding available bot
            members = ctx.guild.members
            for member in members:
                if member.bot and not member.voice and str(member).startswith("Node Child"):
                    print(member.name)
                    botName = member.id
                    print(botName)
                    
            await ctx.send(f"<@{botName}> play {channel} {url}")
          
                
        @self.client.command(pass_context = True)
        async def pause(ctx):
            try:
                self.voice.stop()
            except: 
                await ctx.send("I'm not playin' anythin', why u trippin'?")

        @self.client.command(pass_context = True)
        async def resume(ctx):
            try:
                self.voice.resume()
            except:
                await ctx.send("I'm already playin', chill.")

        @self.client.command(pass_context = True)
        async def leave(ctx):
            if (ctx.voice_client):
                await ctx.guild.voice_client.disconnect()
                await ctx.send("I left the voice channel")
            else:
                await ctx.send("I am not in a voice channel")

        @self.client.command(pass_context = True)
        async def prefix(ctx, ):
            pass



if __name__ == '__main__':
    MasterBot('ODMxMDYzNzY5NzY4OTE5MDkx.YHPycw.hdRrNgb17V_1wHl05pN0XYBhTAM')

    #START CHILD BOTS HERUNDER
    



    
  






