from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 8700952672  # my telegram ID
    OWNER_USERNAME = "NAKS4PANDIT"  # my telegram username
    API_KEY = "8010952431:AAFRiWPMgyCJ5yZjruC0ngwG0rgJewxW45c"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jFCobtpmTMJHmXRppoYYguguGghuitsM@postgres.railway.internal:5432/railway'  # sample db credentials
    MESSAGE_DUMP = '-1003894294224' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [6154383311, 5385377266]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
