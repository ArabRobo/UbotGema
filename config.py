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

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://doadmin:rVx3Pn21609u48he@private-db-mongodb-sgp1-32502-5c293f0e.mongo.ondigitalocean.com/admin?tls=true&authSource=admin")
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
SESSION1 = getenv("SESSION1", "BQAP-GEAFZ8bLZmMl8s0Xgb7MRSLBPciUix30pOqvBBOohS02iuQT5yoSG8-KT7j6mcW_EP3dhIxnv8nQAMb8iErx0AIwLGzIkdNHJPuik9GulkUPrUHn4Pjpg8N-hLezONaZ0veE9bLI8OKiqRM8KGiWkV9L0PORouuUf8ZNhfJBwg0RjxJlx69PIBwL9Q5fiZZkn7p2VMdXqdBHy31d7ynQRT8YfC5wJZY9ZRpTLPSqn4rZ1r_rkQD2zg6hBSAYJq8hW6aAO0GLMpLwE_Jw1uDdygCrQxwg8YbZrvPk_BF6XejH_fnqjKelyGoE0_kg18IhCSwGLgR_gJDMmc04_0k5V-JjgAAAABS0loBAA")
SESSION2 = getenv("SESSION2", "BQAP-GEAdXtqtZ4svvAGAlI3YatEv8_gUrXqkbKb5r2zcK_KAFs-EpEjNKcyDKV4bP-Lo6hihhF8F0J40r8zc_NYy4MW44kvHiNoO_OIUi7_ODsSe2pXNcOb8aHuimUdNH9oHj47v-AaD04FZHiVeiMlWtNm81l29Yd7SjIb6UaJFx91wK24EMtzt3pPjWW8BY5_1WmFNemhaxqUzxRfOD5-0ZZ37mUoQic5pQNPJkQMu0Wuy8Wxf1XVEqs4YX9EWo_hKy0R-HOcgp0IwxO0QwwdFqRE1fAF4DWwKLEbyOoFT4lYMh4IBbG59iK2iAFJ0mVGcaE3shB9recConsn-eGMjwaGtwAAAABX1hxpAA")
SESSION3 = getenv("SESSION3", "BQAP-GEAH3-DjboiEK6OGSKCSRx3Vh9AVHLZ6KanS5t9pG_uhnx_Ujy8gWH61K28uGEJ0-pojssf8LXVu1_ihrhRCWSR8hpxH_XEbD8AdysKrWt49gHQ7EnTZd_FVQX9XtNQRJY-b0saC9dku6XfvIRjEx_Dl0V3i4ZV7OGKJ5Bu7QSHoGRNJfEnpdwxj_wcrGiC_IiK_5-tR-jkYDG31PJRrooe-zjjvFEXZcWjpdxqFTYhY1PrWofDXWyvbetBlTcXgYmttwFY3XklW-RmUhhtVa0d2Xf9UedD_85KbACTZlPKoSnKRtNWkP0thgW2qSFjgHCd-ToPGtzMDKTzD2RVcOPAZwAAAABpDqruAA")
SESSION4 = getenv("SESSION4", "BQAP-GEAtXIG87zNd349zGqDaM1pn101vfMWB8MePh2VQfCZz9jwpa3vmrnqSSgzz-mt5Gvc5OH-brVx45PHF1EwLk2EpeAkmBM60GXnjnLueaS5mDZu2wgX4wAsVcBvcX-X-zM_fj3SFGJhdp4vUgHFechJRLiyYUCZYzsyvLNMkQfnhWaiHN3smJf4RREONbrTdFtQAundeWA9CjcOCzQJStwtYGgbny3Ev9TZ6ZV5cinGM86ecijhl5suIkgx1he1D6StvSqbHau3j0Y3RWfKoc9DbVOBE76LfXqa2qEkxfIfhRjjhrb4YgFRqb1mU87rmoRpyHPuEMlbyBTnmkJ7YT80cQAAAABbK4hiAA")
SESSION5 = getenv("SESSION5", "BQAP-GEAjW5IlBlluyEtrbb5Mu6mKXieiB-mUYd_Y2nLLOH1IZI2cZDzevjxMcN9ejyEhGPBEdK0nzczmDdcmvZ_0om31H9n1qYHPC1L7fgi-cn_kwyGsUORMPhukUtqAdjni1FsECjhu78SQkk2lWy6KjIrP37_m9xtjgnHPVcEpkbh7csTLCgLYnCqxmZfRDz8KpR4y0dVOIKDOV4QQdb5zRdtHqDrPjzUEGwgAWgZTZ8D980N86CD5k1Dx4-6jM8X3KxtAhY0nFudGumkX_T_PtaGVV709bJU7xZvltB5nVZFN2D2iyUSuXtQ3pcp0HHkyazX0FJFo-R8jXq6wTG2YTX2KQAAAABXl4KVAA")
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
