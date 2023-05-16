import os

class Config:

    BOT_TOKEN = os.environ.get("6114988028:AAGZHGazdSwdZFhZZiQEHvJxNvPW4RjVQEk")
    
    SESSION_NAME = os.environ.get("rawalytuploadbot_bot")

    API_ID = "16494736"

    API_HASH = "2cb7fa5859e2de684e3e10d9c049621a"

    CLIENT_ID = os.environ.get("260176737372-iu17pd3mkkm4lejrlaatbr08kmo604ec.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = "656718180"
    
    AUTH_USERS_TEXT = os.environ.get("656718180", '')

    AUTH_USERS = [BOT_OWNER, ] + ([int(user.strip()) for user in AUTH_USERS_TEXT.split(",")] if AUTH_USERS_TEXT else [])
    
    VIDEO_DESCRIPTION = os.environ.get("VIDEO_DESCRIPTION", '').replace('<', '').replace('>', '')
    
    VIDEO_CATEGORY = os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    
    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", '')
    
    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", '')
    
    DEBUG = bool(os.environ.get("DEBUG"))
    
    UPLOAD_MODE = os.environ.get("private") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ['private', 'public', 'unlisted']:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"



