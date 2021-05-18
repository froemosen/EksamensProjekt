import discord #pip install discord
from discord.ext import commands
import youtube_dl #pip install youtube_dl
import os
import time
from asyncio import sleep
#pip install PyNaCl
#INSTALLÉR FRA NETTET, OG SMID DE TRE .EXE fra 'bin' I SAMME MAPPE SOM youtube_dl
import subprocess, sys
from tokens import * #imports tokens for child bots.


class MasterBot():
    def __init__(self, token):
        botIntents = discord.Intents.default()
        botIntents.members = True
        self.client = commands.Bot(command_prefix="!", intents=botIntents)
        self.queue = []
        
        #while True:
        self.client.remove_command('help')
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
                await ctx.send("No bot was found in your channel.")
                    
            


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
                await ctx.send("No bot was found in your channel.")

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
                await ctx.send("No bot was found in your channel.")

        @self.client.command(pass_context = True)
        async def prefix(ctx):
            pass


        @self.client.command(pass_context = True)
        async def help(ctx):
            await ctx.send(f"The following commands can be used: :nerd:\n\n'!play **url**'  -  Guides you how to play a song of your choice\n'!pause'  -  Guides you how to pause the song\n'!resume'  -  Guides you how to resume the paused song\n'!leave'  -  Guides you how to make the Child Bot leave")

if __name__ == '__main__':
    for name in tokens:
        print(f"{name}is starting up")

        #os.system(f"python Child.py {tokens[name]} {name}")
        subprocess.Popen(["python", "Child.py"]+[str(tokens[name]), str(name)])
    
    MasterBot('ODMxMDYzNzY5NzY4OTE5MDkx.YHPycw.hdRrNgb17V_1wHl05pN0XYBhTAM')

    
