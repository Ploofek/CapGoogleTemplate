import os

def getSecrets():
    secrets = {
        'MONGO_HOST':'mongodb+srv://ssofiareyes:drowssap@cluster0.42vojfx.mongodb.net/?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'',
        'GOOGLE_CLIENT_ID': '',
        'GOOGLE_CLIENT_SECRET':'',
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration"
        }
    return secrets