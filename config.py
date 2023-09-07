import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "12857763")) #optional
API_HASH = getenv("API_HASH", "7b71e8bca0d5e1c6d8383ae818d9ec8d") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1948147616").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID", "1948147616") or 0)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "1948147616").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "0").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN2_ID", "0").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN2_ID", "0").split()))


ADMIN1_ID.append(1948147616)
ADMIN2_ID.append(0)
ADMIN3_ID.append(0)
ADMIN4_ID.append(0)

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://fadhil01:fadhil123@fadhil01.s6lkqsq.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5979250691:AAF3wQEP76-kD7JkN67qRWMw4WyMpqPlzzk")
BOT_WORKERS = int(getenv("BOT_WORKERS", "3"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "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")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN", "SHA256:azvkVegsZyKoLxKq30eyBdPZ1+iURKf/rurx70H/nZ4") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "arab") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/fadhilabdat04/ProjectArabUbot01")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001803314750"))
CHANNEL = int(getenv("CHANNEL", "-1001681544718"))
SESSION1 = getenv("SESSION1", "BQERFPAAEZIU2HVG10FLXTOUxHgxyxqbjBo7GXTJCwPLYYtB0tyG5V5_Z4GHCUi4zWMMypYJpBjZJ99UsnDD69m4xtYnMIhGMtcQkSl30hXgjVDlSr2NoABCuJicd6UnzmPJ2wgsJuVtTW_gU4AvvkLvs9tMvtd-JVadYn3NBS6XverM0TZHNXlp6flEfjJ5zyw13zXtA99N5ZCgkYtFlRfbqCizeIRmZQf7iafXWJz5HxIfE4-r8PbNtVQH1TFU060TLVkWvj24tsRQr7rpwfuEh7VQzI49F-b_DZPqWr6YaNFHPHaf1WqZN4iMwnaOJg9VM0zC16orXLXNOqdbn7vKLWhPugAAAAB_9mbRAA")
SESSION2 = getenv("SESSION2", "BQDQz2YAr8_ae1VDPvnmZrXAg-UAj9JDalo0jMkdzFhq_kdBMlDLc1R45mwPFtggsNmFdaJhVtOBCqyG5-EoKc5VWMKJuPN-K40sAC8nCjcZ6hi2UHWzRS2NanS0LROvE1Ii81VE8SXDsiJ5_XHQeJ5KFamr8yAOgptEUHKDZQ7FVEClg75bYbt7FWi2MfAo9UNwrKiGBWhGz0lho5NRvgcoLGETZ90ZMvHn0rX_NJHZo__muGmjxpdzh4rvGiBEwvLL2KR1ZIWRixnCRM4dDu2eLz1MItXi0hpcEFN6SplF2UaczXBdKANtzw3ad8_wdjsfHmgh8RHL53bc0NwuuexQYnL6uwAAAABiSIrgAA")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")
