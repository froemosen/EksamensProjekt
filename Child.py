import discord #pip install discord
import youtube_dl #pip install youtube_dl



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
            

            print(f"{message.author} is in {message.author.voice}")
            
            #FIND UD AF message.author.voice variabel definition.
            


if __name__ == '__main__':
    bot = ChildBot('ODMxMDY2MDQ1NTk0MDc1MTQ3.YHP0kQ.Q7BqwyIvUKGOj-7t2V4zzd2Fli0')

    
  


