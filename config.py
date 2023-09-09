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

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ubot:6s5HmY4I31p8l9P2@private-db-mongodb-sgp1-31724-8e3eb49d.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-sgp1-31724")
BOT_TOKEN = getenv("BOT_TOKEN", "6622316489:AAFu3gq8rm1ZZzvPxzg8jsHcosXs9vQ9UAg")
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
REPO_URL = getenv("REPO_URL", "https://github.com/fadhilabdat04/TesdoangPr")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001803314750"))
CHANNEL = int(getenv("CHANNEL", "-1001681544718"))
SESSION1 = getenv("SESSION1", "BQERFPAAAX7v4v06p3fM30y56EKUGc9PS2nWvzwvpClSBezVS3rmGQVg0OxkOGkwO6jvAkOvDBt_cKJMW3DfFPS8O2_OApRCIihAfuPGWPxl4NZQD9a7eQKTQphjjcQo5XqqyHX-LhOs0WLHQRSPgR8ie5I8cqZiE8D3pus0Uhpie-wKk9ycp_OUGq6ItBqVa40Ju1Wum-FZ4fC0TZ6TndBlXSO6rgenc8hwpd3F8HnDjoiCHNxYRjzkKZAePLZIA0iOzc7HNjxl191QgINSzSjfNi0H84hHSlXBw5JGDxPzFcHp1rVdzQ03ewQ2cW0urL9mXSrP5PqfCLyHZ-wL00nrhexioAAAAABNnEf1AA")
SESSION2 = getenv("SESSION2", "BQAP-GEAZsHINwatkRZCFZ_J7MnMPELypLclOQ-XKz7TcijdC3_qFkFUsOsXs2vp45ptdluBXCFGHCdaoPNMgnPuaSLfDSozVihA65I-wO16bU4Fq2jc_Vk0AfA79BYAtc8XkmEB-RblrI4NAhjUVg5CLjHYdv71GQgxDufHutgvSX3sz3ZhNjLHKp7dpWeWYSNX1ABeO6CnLn3kg78GC8ftjeG3Eh8kMolhYgvgw9bN36oJsRAA0NAIc52oOqJpao_MTPBNl1WuLA37XCVhKl6XxX2A8x4F6VhEiPfvgdFM-iqmHh5Q4jIXMi3348UFiDxL6JoyWjGL6-pFg74isYnMf_h_owAAAAE43rOdAA")
SESSION3 = getenv("SESSION3", "BQAP-GEAH3-DjboiEK6OGSKCSRx3Vh9AVHLZ6KanS5t9pG_uhnx_Ujy8gWH61K28uGEJ0-pojssf8LXVu1_ihrhRCWSR8hpxH_XEbD8AdysKrWt49gHQ7EnTZd_FVQX9XtNQRJY-b0saC9dku6XfvIRjEx_Dl0V3i4ZV7OGKJ5Bu7QSHoGRNJfEnpdwxj_wcrGiC_IiK_5-tR-jkYDG31PJRrooe-zjjvFEXZcWjpdxqFTYhY1PrWofDXWyvbetBlTcXgYmttwFY3XklW-RmUhhtVa0d2Xf9UedD_85KbACTZlPKoSnKRtNWkP0thgW2qSFjgHCd-ToPGtzMDKTzD2RVcOPAZwAAAABpDqruAA")
SESSION4 = getenv("SESSION4", "BQFSFokAPXnpuV9hO5EmpgXhHzAU107hnwpeHPmcPZ_ZmrIrlbKF9-foZZzgIzlIw9XiJs_eI29W45pnTP-50x_Cu8HUr9-VmKsfY-qBE62_ydp0x8sG6UcauxG0Ya45gMyUJ5RRZSDoECjzmE0zJ90JdBSOIv9Yfcc-66TYruJAYOKak7GtVRIshVVuzqdireSJeLTg6imxRTXzvQ-hEoMiZGD7glCJm7vUEcoAB1ZuKrGU8HLCR-H8J08ueHGWKDak-KbKHFHRu1Xc2YJefBW2uCDfW0ljfbhVlXrtxkheot8RzNHT5vtkq_Pvsz_nCRLedCMao-jDfLS86x5A8Tez2zCz0gAAAAA22NgcAA")
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
