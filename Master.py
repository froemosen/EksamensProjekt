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
            if ctx.author.voice:
                channel = ctx.message.author.voice.channel
                print(channel)
                voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel) #Voice Channel to Object instead of channel name
            else:
                await ctx.send("You are not in a voice channel.")

            #Searching for bot in author voice channel
            members = channel.members
            for member in members:
                if member.bot and str(member).startswith("Node Child"):
                    botName = member.id
                    await ctx.send(f"You get to keep your current bot! Type the following message in chat:\n\n<@{botName}> play {channel} {url}")
                    botFound = True
                    break
                else: botFound = False
                
            if not botFound:
                #Finding available bot (If no bot was already connected)
                members = ctx.guild.members
                for member in members:
                    if member.bot and not member.voice and str(member).startswith("Node Child"):
                        botName = member.id
                        await ctx.send(f"I found a bot for you! Type the following message in chat:\n\n<@{botName}> play {channel} {url}")
                        botFound = True
                        break
                    else: botFound = False

                if not botFound:
                    await ctx.send("No bot is available at the moment. :(")
                    
            
          
                
        @self.client.command(pass_context = True)
        async def pause(ctx):
            #Finding message author voice channel
            if ctx.author.voice:
                channel = ctx.message.author.voice.channel
                voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel) #Voice Channel to Object instead of channel name
            else:
                await ctx.send("You are not in a voice channel, so there's no bot to send a command.")
            
            #Searching for bot in author voice channel
            members = channel.members
            for member in members:
                if member.bot and str(member).startswith("Node Child"):
                    botName = member.id
                    await ctx.send(f"Type the following message in chat:\n\n<@{botName}> pause")
                    botFound = True
                    break
                else: botFound = False
                
            if not botFound:
                await ctx.send("No bot is available at the moment. :(")
                    
            


        @self.client.command(pass_context = True)
        async def resume(ctx):
            #Finding message author voice channel
            if ctx.author.voice:
                channel = ctx.message.author.voice.channel
                voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel) #Voice Channel to Object instead of channel name
            else:
                await ctx.send("You are not in a voice channel, so there's no bot to send a command.")
            
            #Searching for bot in author voice channel
            members = channel.members
            for member in members:
                if member.bot and str(member).startswith("Node Child"):
                    botName = member.id
                    await ctx.send(f"Type the following message in chat:\n\n<@{botName}> resume")
                    botFound = True
                    break
                else: botFound = False
                
            if not botFound:
                await ctx.send("No bot is available at the moment. :(")

        @self.client.command(pass_context = True)
        async def leave(ctx):
            #Finding message author voice channel
            if ctx.author.voice:
                channel = ctx.message.author.voice.channel
                voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel) #Voice Channel to Object instead of channel name
            else:
                await ctx.send("You are not in a voice channel, so there's no bot to send a command.")
            
            #Searching for bot in author voice channel
            members = channel.members
            for member in members:
                if member.bot and str(member).startswith("Node Child"):
                    botName = member.id
                    await ctx.send(f"Type the following message in chat:\n\n<@{botName}> leave")
                    botFound = True
                    break
                else: botFound = False
                
            if not botFound:
                await ctx.send("No bot is available at the moment. :(")

        @self.client.command(pass_context = True)
        async def prefix(ctx, ):
            pass


if __name__ == '__main__':
    MasterBot('ODMxMDYzNzY5NzY4OTE5MDkx.YHPycw.hdRrNgb17V_1wHl05pN0XYBhTAM')

    #START CHILD BOTS HERUNDER
    



    
  






