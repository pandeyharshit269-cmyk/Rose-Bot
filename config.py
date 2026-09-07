from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 8700952672  # my telegram ID
    OWNER_USERNAME = "NAKS4PANDIT"  # my telegram username
    API_KEY = "8010952431:AAFRiWPMgyCJ5yZjruC0ngwG0rgJewxW45c"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'mongodb+srv://devilharshit02:devilharshit02@cluster0.9efk59a.mongodb.net/?appName=Cluster0'  # sample db credentials
    MESSAGE_DUMP = '-1003894294224' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [6154383311, 5385377266]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
