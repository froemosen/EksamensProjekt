import discord #pip install discord
from discord.ext import commands
import youtube_dl #pip install youtube_dl
import os
from asyncio import sleep
#pip install PyNaCl
#INSTALLÉR FRA NETTET, OG SMID DE TRE .EXE fra 'bin' I SAMME MAPPE SOM youtube_dl
import sys



class ChildBot():
    def __init__(self, token, name):
        botIntents = discord.Intents.all()
        botIntents.members = True
        self.client = commands.Bot(command_prefix=commands.when_mentioned, intents=botIntents)
        self.queue = []
        self.name = name
        
        self.ydl_opts = {
                "format" : "bestaudio/best",
                "postprocessors" : [{
                    "key" : "FFmpegExtractAudio",
                    "preferredcodec" : "mp3",
                    "preferredquality" : "192",
                }],
            }
        
        #while True:
        self.decodeMsg()
        self.client.run(token)

    def decodeMsg(self):
        print(f"{self.name}- Just Went Online")

            
        @self.client.command(pass_context = True)
        async def play(ctx, channelName, url):

            print(ctx.guild.voice_channels)

            #self.client.event KAN BRUGES VED AT KIGGE PÅ INDHOLDET I BESKEDEN I STEDET FOR COMMANDS HVIS BOT SKAL LÆSES
            try:
                #Connecting to voice channel
                voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channelName) #Voice Channel to Object instead of channel name
                print(voiceChannel)
                await voiceChannel.connect()
            except: pass

            #Downloading a song
            await ctx.send("Downloading media...") #Confirmation that download is happening.

            self.voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([url])
                
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    try:
                        self.queue.append(file)
                        os.rename(file, "songs/"+file)
                        print(self.queue)

                    except:
                        print("Song already exists")

            await ctx.send("Download Complete:100:") #Confirmation that download is complete.

            while len(self.queue) > 0:
                await sleep(4)

                """
                if len(voiceChannel.members) <= 1:
                    await pause(ctx)
                    await leave(ctx) 
                """

                if self.voice.is_playing() == False:
                    #Playing new song
                    self.voice.play(discord.FFmpegPCMAudio("songs/"+self.queue[0]))
                    await ctx.send(f"Queue is now:\n {self.queue}")
                    await ctx.send(f"Now Playing: '{self.queue[0]}'")

                    #Deleting old files
                    try: 
                        if not self.oldSong in self.queue: os.remove("songs/"+self.oldSong) #Delete file, if not still in queue
                    except: pass
                    self.oldSong = self.queue[0]
                    del(self.queue[0])

                    
                
        @self.client.command(pass_context = True)
        async def pause(ctx):
            try:
                self.voice.pause()
                print("pause command complete")
            except: 
                await ctx.send("I'm not playin' anythin', why u trippin'?")

        @self.client.command(pass_context = True)
        async def resume(ctx):
            try:
                self.voice.resume()
                print("resume command complete")
            except:
                if ctx.voice_client:
                    await ctx.send("I'm already playin', chill.")
                else: 
                    await ctx.send("´Not connected to voice. Use !play to make me join your channel :)")

        @self.client.command(pass_context = True)
        async def leave(ctx):
            if (ctx.voice_client):
                try: os.remove("songs/"+self.oldSong)
                except: pass
                for song in self.queue:
                    os.remove("songs/"+song)
                self.queue = []
                await ctx.guild.voice_client.disconnect()
                await ctx.send("I left the voice channel")
            else:
                await ctx.send("I am not in a voice channel")

           

    
if __name__ == '__main__':
    ChildBot(sys.argv[1], (sys.argv[2]))

