from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 14357885
    API_HASH = "099d3d7d9becd37011ffca3595df677a"
    # the name to display in your alive message
    ALIVE_NAME = "Mikey"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://kfiwdnnb:q0xMeaVQDdihRsw-abkt25KUN7I7O7te@tuffi.db.elephantsql.com/kfiwdnnb"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOMABu4nJOmFQtIDjX7EeAFD4dSvssAdNEG8lIxe9_6LvWf4nw9Rqc42aGaQzXyKk8RiN4udqhJwnUEAayeOJCdTOHM5dLTKkqL-XP69r1XAX44rgup2h51eW_EJ4yPTLrlhZm3dV3vlEz48EdyRA4L5ASr8VEmFElQQ0gdaJcNBg2vSZQ8WE1X4YdK8JI7NBSaBKWsdh4AokHMJmyUSxrNiT4JYR-CiZ83TyBv5wftijoLZtN3sfujLYomezKFFLms5uWcbQ6uLINHL6wdPyIgW4cn08viEFYxS1MflM3yn7nSWhXmAHMvSNWZgqo78UxhiCazOpicm3ViWPrvuGsXe4bu0="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6393455098:AAF1S_zcADaqv7wNF4BSTKkL-ALSHTvVJac"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001945008331
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
