from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20628833")
    API_HASH = environ.get("API_HASH", "63f1813aba275748d92ed3aebc7827bd")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7792197139:AAHKR7EyQYXecZU001-UOK6NxWXDF69nqFQ") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://mdemonpops123:8dNjNO1Pl52a4SC1@cluster0.99wiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7798801272').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
