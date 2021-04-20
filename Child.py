import discord #pip install discord
import youtube_dl #pip install youtube_dl
#pip install PyNaCl



class ChildBot():
    def __init__(self, token):
        self.client = discord.Client()
        self.decodeMsg()
        self.client.run(token)



    def decodeMsg(self):
        print("I Just Went Online")
        @self.client.event
        async def on_message(message):
            print(f"{message.author} said '{message.content}'")
            


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
    bot = ChildBot('ODMxMDY2MDQ1NTk0MDc1MTQ3.YHP0kQ.Q7BqwyIvUKGOj-7t2V4zzd2Fli0')

    
  


