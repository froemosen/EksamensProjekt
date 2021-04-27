import discord #pip install discord
from discord.ext import commands
import youtube_dl #pip install youtube_dl
import os
#pip install PyNaCl
#INSTALLÉR FRA NETTET, OG SMID DE TRE .EXE fra 'bin' I SAMME MAPPE SOM youtube_dl



class ChildBot():
    def __init__(self, token, name):
        botIntents = discord.Intents.default()
        botIntents.members = True
        self.name = name
        self.client = commands.Bot(command_prefix=(name), intents=botIntents)
        
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
        print("I Just Went Online")

        #SKAL BRUGES I MASTER BOT KODE!
        """
        @self.client.command(pass_context = True)
        async def join(ctx):
            if (ctx.author.voice):
                channel = ctx.message.author.voice.channel
                print(type(channel))
                await channel.connect()
            else:
                await ctx.send("You are not in a voice channel.")
        """
        

        @self.client.command(pass_context = True)
        async def leave(ctx):
            if (ctx.voice_client):
                await ctx.guild.voice_client.disconnect()
                await ctx.send("I left the voice channel")
            else:
                await ctx.send("I am not in a voice channel")

        @self.client.command(pass_context = True)
        async def play(ctx, channel, url):
            #Connecting to voice channel
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel) #Voice Channel to Object instead of channel name
            
            await voiceChannel.connect()

            #Playing a song
            await ctx.send("Downloading media")
            song_there = os.path.isfile(self.name+".mp3")
            try:
                if song_there:
                    os.remove(self.name+".mp3")
            except PermissionError: #Filen er åben - Musik spiller
                await ctx.send("Wait for current song to stop playing.")
            
            self.voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

            print(url)
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, self.name+".mp3")
            self.voice.play(discord.FFmpegPCMAudio(self.name+".mp3"))

        @self.client.command(pass_context = True)
        async def stop(ctx):
            try:
                self.voice.stop()
            except: 
                await ctx.send("Not Connected to Voice")

            
        """
        @self.client.event
        async def on_message(message):
            print(f"{message.author} said '{message.content}'")
            pass
        """
        
            


        """"
            TRASH THIS :((
                
            #print(f"{message.author} is in {message.author.voice}")

            self.voiceStatusRaw = str(message.author.voice)

            print("Raw String Status: "+self.voiceStatusRaw)

            self.voiceStatusList= self.voiceStatusRaw.split(" ")

            print("List String Status:", self.voiceStatusList)

            print("ID: ", self.voiceStatusList[7])

            self.voiceStatusList[7] = self.voiceStatusList[7].replace("id=","")

            print("ID: ", self.voiceStatusList[7])

            channelID = self.voiceStatusList[7]

            

            #voiceClient = discord.VoiceClient(self.client, channelID)

            #await voiceClient.connect(reconnect=False, timeout=1000)
            #await voiceClient.change_voice_state(channelID, self_mute=False, self_deaf=False)

            
            __________________LINE OF SEPERATION__________________
            
            
            Tried to join a channel, didnt work... (https://discordpy.readthedocs.io/en/latest/api.html#voiceclient)
            voice_client = await self.client.connect(reconnect=True)

            await voice_client.change_voice_state(channelID, self_mute=False, self_deaf=False)"""

    
            


if __name__ == '__main__':
    bot = ChildBot('ODMxMDY2MDQ1NTk0MDc1MTQ3.YHP0kQ.Q7BqwyIvUKGOj-7t2V4zzd2Fli0', "Node Child (00000) ")

    
  


