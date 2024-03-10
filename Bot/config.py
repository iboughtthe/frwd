from dotenv import load_dotenv
from os import environ, path

load_dotenv()

if path.exists("bot_config.py"):
    from bot_config import Config
else:
    class Config(object):
       APP_ID = "26075120"
        API_HASH = "1fda88a5d1de46058a4791c78bce198e"
        BOT_TOKEN = "6581740047:AAEfKQdnv4VzX3zzMLBtb1dEuJcHyvH6-aI"
        BOT_WORKERS = int(environ.get("BOT_WORKERS", 40))
        SUDO_USERS = "6519328993, 6551696176"
        DB_URI = "mongodb+srv://gaganthespy:gaganthespy@cluster0.feyeyvr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        SESSION_NAME = "BQGUFZYAQmbt7QFe2YIZoRuyZxmnypRHT3g3kkVwiQdeIehfCBgGJOkam9hirLq1VGwsL8o_FgQP8emcVwCVXLEw5SW6syG-vnfwYFPmusz7mo0dFrQecbPwQP8swld1w1eb0xbcUzdBMgjnWs5j_xhhW4KpHfKW682_L1UYMoaYy7OwScEbo2Dv5dx1cp5Q2aRy_U_9L8LUAjyOnh4ri8gZ8QvG0r4nfO57Modj803N8AnE-cXno0U18op1RKllxQm8nof6R4cMp_aDtWZbwD7OVB5nm9C0vlf4LV-dUPUS6sMp_Bi_wCn36cfdn3QZrzPGV6wJJRQvUKZBK37eGlrOqhmjLgAAAAGGgvMwAA"
        MULTI_USER_MODE = "6519328993, 6551696176"
