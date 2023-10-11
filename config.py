import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "9873769")) #optional
API_HASH = getenv("API_HASH", "3816d0a91c7affbda8a93465cf841665") #optional
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
BOT_TOKEN = getenv("BOT_TOKEN", "6444863574:AAGPcq4_KeosabTH2eR8eo6svXfaypY5Zy8")
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "4"))
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
SESSION1 = getenv("SESSION1", "BQAP-GEAPCImLM8sDHEPTsI1SH9VuC3nokcKly_13rusISjiP_P_PCxm-u9-4A9ewSXQjRtW_at4tHA-d4r2u7688wLJhlneX8CLj1_1Yp17YaL270JeRz5tVPl_YQ4Lf0Ik5mGRf8qCvEFbPHR95jn84n_3b01uOaw_O4x0dggA-EWL-N8Gf_04PHSMjrnnANqqH87Y-PmVsMqMuix78ktK1IMuXhfzI0C8PwoIIx9XrrErZcjQpR4QdIpD6iauqtT2jNZaRO7wPtEfL6FLU3feluF1nxz0R4Wl28-8S8RDpOnFiagzA8Q-yVgxrfVRri82wqR9PqglbylTC1vizizkD-RiHAAAAABXCWEvAA")
SESSION2 = getenv("SESSION2", "BQAP-GEABxvHoy7GGnjFV5V4acnha2070nThNrKiDn3CkvtScs27rdYA2TWDsPxY6E5sHVqVvtaTLm2tAhlWu8Gi6pQNkRME9ZnqIDM6dH9TVPujLlVFsnE48EVG377XUTe_IpuLylLT22ZlapyBDK9QIlEYOsQKAwfVXUZ-OEm41wO0VVP5NRo7n2l7IzwQdi9-tmz1IEBZyNJSy6IcJF7MSNnbHwNlk5_3oRuYN80b9-FRlZEbZ2NHGSe0ai_15WFsly9zBGAXuodDSDjPR_9lQfA_Lpg62sxMAPp83lU9Ytw6sCyyKP1oolRG4cb_6f9Ch4axr1MfcvgiCvIrGV3Zw-RzhgAAAAByU4g-AA")
SESSION3 = getenv("SESSION3", "AQAP-GEAwY-hxzLZHDnEQP7yqrc2oOHVpIjlcJdEtIWnEHGwZjy55OPAbC-IAgt49u5Gd5Tr_SS1tf9IJ9bB2YXG7tr34FcPEovMmbZlTU-U9F5CO3Ks5N3qFTD_bmTLoZTURKeM9WbWMedc5uMye41WnoaCP28OJZJmnI1MGVgobhR5ZNrHB5ubkCGxESCpN0aEJ1w-OyeEale75NMoqOjZY5mqKo8BSE008NiiFZMG0n5umlho3KMZEDloKn9gbdtrBdc6KXl-MJEIK4zbE14WUupWiE7NDqubG6_b7Nn8PnSqCB2WT-d2JqJ0GvAYda8fdWfJu9zbHmNqSmF9xVv1V-haMAAAAABxHqS8AA")
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
