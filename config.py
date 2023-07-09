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
    STRING_SESSION = "1BVtsOGYBu7L-TWqfQsy_7ZKDgWu1ngF0EsOJY2G37hqlF62OEo_W3ixBl0JRv1OEmuXHrIp8JZYnbc_vtupI-igO5meTlztT9MD32DPwYQxHmeCOzDRpV2wR9RSuLF8LP2dieqpXvFDKDlHgufTDCfzOrZ85XZ2tvvhGCT4EWLkpdUae3Akfz5snN7hyMiaOKq3CgEWHRl2PQ4lse9r42EkCJ44tldjKtHM6JCA-C4V2EXTwFxVc9pSuo_UgAwDxjkRbVSD7OLhYh1MmKgHhJAvtZ9FBsed0H5ZzOr-W3kj1pQLF0BqT8IUNifCI20BSVCEk9fOPVe-x6AzIwsr0Ds68q_Upbjc="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6393455098:AAF1S_zcADaqv7wNF4BSTKkL-ALSHTvVJac"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001901315096
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
