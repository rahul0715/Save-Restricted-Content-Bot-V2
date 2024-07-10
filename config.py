# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27862677"))
API_HASH = getenv("API_HASH", "e343ce2c81b2b6c2c0d6bee58284e3bd")
BOT_TOKEN = getenv("BOT_TOKEN", "7132722759:AAEEQyIy9cuqPSG9vs1vU4O-LNLZU4xm83w")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5881684718").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn")
LOG_GROUP = getenv("LOG_GROUP", "-1002111115192")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002111115192"))
