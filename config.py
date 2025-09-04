import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "22161204")
    API_HASH = environ.get("API_HASH", "fdffc74281153b3338e4474f5640095e")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8142366006:AAG7z04jesKbvXNCQYNkYv4ItQ4wEIN_vTI") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://restricted-saving-bot:dBvbge6fJCENXFCC@restricted-saving.nxv9tr4.mongodb.net/?retryWrites=true&w=majority&appName=restricted-saving")
    DATABASE_NAME = environ.get("DATABASE_NAME", "restricted-saving-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002644127305'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
