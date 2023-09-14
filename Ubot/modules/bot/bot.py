
import traceback
import re
from pyrogram import Client, filters
from pyrogram.errors import MessageDeleteForbidden
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Ubot import CMD_HELP, app
from Ubot.core import *
from Ubot import ids as users
from config import SUPPORT, CHANNEL


@Client.on_callback_query()
async def _callbacks(_, callback_query: CallbackQuery):
    query = callback_query.data.lower()
    bot_me = await app.get_me()
    if query == "helper":
        buttons = paginate_help(0, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            Data.text_help_menu,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query == "close":
        await app.edit_inline_text(callback_query.inline_message_id, "**ᴄʟᴏsᴇ**")
        return
    elif query == "close_help":
        if callback_query.from_user.id not in users:
           return
        await app.edit_inline_text(
            callback_query.inline_message_id,
            "**ᴄʟᴏsᴇ**",
            reply_markup=InlineKeyboardMarkup(Data.reopen),
        )
        return
    elif query == "closed":
        try:
            await callback_query.message.delete()
        except BaseException:
            pass
        try:
            await callback_query.message.reply_to_message.delete()
        except BaseException:
            pass
    elif query == "make_basic_button":
        try:
            bttn = paginate_help(0, CMD_HELP, "helpme")
            await app.edit_inline_text(
                callback_query.inline_message_id,
                Data.text_help_menu,
                reply_markup=InlineKeyboardMarkup(bttn),
            )
        except Exception as e:
            e = traceback.format_exc()
            print(e, "Callbacks")
            

@app.on_callback_query(filters.regex("cl_ad"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

@app.on_callback_query(filters.regex("ub_modul_(.*)"))
# @cb_wrapper
async def on_plug_in_cb(_, callback_query: CallbackQuery):
    modul_name = callback_query.matches[0].group(1)
    commands: dict = CMD_HELP[modul_name]
    this_command = f"**Bantuan Untuk {str(modul_name).upper()}**\n\n"
    for x in commands:
        this_command += f"• **Command:** `{str(x)}`\n• **Function:** `{str(commands[x])}`\n\n"
    this_command += "@Dhilnihnge | Arab-UbotPrem"
    bttn = [
        [InlineKeyboardButton(text="«ʙᴀᴄᴋ", callback_data="reopen")],
    ]
    reply_pop_up_alert = (
        this_command
        if this_command is not None
        else f"{modul_name} Belum ada penjelasannya ."
    )
    await app.edit_inline_text(
        callback_query.inline_message_id,
        reply_pop_up_alert,
        reply_markup=InlineKeyboardMarkup(bttn),
    )


@app.on_callback_query(filters.regex("reopen"))
# @cb_wrapper
async def reopen_in_cb(_, callback_query: CallbackQuery):
    buttons = paginate_help(0, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("helpme_prev\((.+?)\)"))
# @cb_wrapper
async def on_plug_prev_in_cb(_, callback_query: CallbackQuery):
    current_page_number = int(callback_query.matches[0].group(1))
    buttons = paginate_help(current_page_number - 1, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("helpme_next\((.+?)\)"))
# @cb_wrapper
async def on_plug_next_in_cb(_, callback_query: CallbackQuery):
    current_page_number = int(callback_query.matches[0].group(1))
    buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )

@app.on_callback_query(filters.regex("buat_ub"))
async def close(_, query: CallbackQuery):
    await query.message.reply_text(
       f"""<b>👋🏻 ʜᴀʟᴏ ɴɢᴇ sᴀʜᴀʙᴀᴛ @ArabStore_Robot .\n
💭 ꜱᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ ʙᴏᴛ ᴀʀᴀʙ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀʙᴏᴛ\n
👉🏻 ᴊɪᴋᴀ ɪɴɢɪɴ ᴍᴇᴍʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ . ᴋᴀᴍᴜ ʙɪꜱᴀ ʜᴜʙᴜɴɢɪɴ ᴀᴅᴍɪɴ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʙᴏᴛ.\n
ᴊɪᴋᴀ ᴀɴᴅᴀ ʟɪᴍɪᴛ ᴅᴀɴ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴɢʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ ᴀɴᴅᴀ ʙɪsᴀ ᴍᴇʟᴀʟᴜɪ ʙᴏᴛ ʟɪᴍɪᴛ ᴏʀᴅᴇʀ ᴀʀᴀʙ sᴛᴏʀᴇ</b>""",
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🧑🏻‍💻 ʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ", url=f"https://t.me/Dhilnihnge"),
                ],
	    ]
	    [
                [
                    InlineKeyboardButton(text="🤖 ʟɪᴍɪᴛ ʙᴏᴛ ᴏʀᴅᴇʀ", url=f"https://t.me/SiArabLimitBot"),
                ],
	    ]
    ))

@app.on_callback_query(filters.regex("store"))
async def close(_, query: CallbackQuery):
    await query.message.reply_text(
       f"""<b>👋🏻 ʜᴀʟᴏ ɴɢᴇ sᴀʜᴀʙᴀᴛ @ArabStore_Robot .\n
💭 ꜱᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ ʙᴏᴛ ᴀʀᴀʙ sᴛᴏʀᴇ ʙᴏᴛ\n
👉🏻 ᴊɪᴋᴀ ɪɴɢɪɴ ᴍᴇᴍʙᴜᴀᴛ ʙᴏᴛ ᴅɪ ᴀʀᴀʙ sᴛᴏʀᴇ. ᴋᴀᴍᴜ ʙɪꜱᴀ ʜᴜʙᴜɴɢɪɴ ᴀᴅᴍɪɴ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʙᴏᴛ.\n
ᴊɪᴋᴀ ᴀɴᴅᴀ ʟɪᴍɪᴛ ᴅᴀɴ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴɢʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ ᴀɴᴅᴀ ʙɪsᴀ ᴍᴇʟᴀʟᴜɪ ʙᴏᴛ ʟɪᴍɪᴛ ᴏʀᴅᴇʀ ᴀʀᴀʙ sᴛᴏʀᴇ</b>""",
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🧑🏻‍💻 ʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ", url=f"https://t.me/Dhilnihnge"),
                ],
	    ]
	    [
                [
                    InlineKeyboardButton(text="🤖 ʟɪᴍɪᴛ ʙᴏᴛ ᴏʀᴅᴇʀ", url=f"https://t.me/SiArabLimitBot"),
                ],
	    ]
    ))

@app.on_callback_query(filters.regex("listharga"))
async def close(_, query: CallbackQuery):
    await query.message.reply_text(
       f"""<b>👋🏻 ʜᴀʟᴏ ɴɢᴇ sᴀʜᴀʙᴀᴛ @ArabStore_Robot .\n
💭 ʟɪsᴛ ʜᴀʀɢᴀ ᴅᴇᴘʟᴏʏ ʙᴏᴛ ᴅɪ ᴀʀᴀʙ sᴛᴏʀᴇ\n
❏ ᴊᴀsᴀ ᴅᴇᴘʟᴏʏ ᴜsᴇʀʙᴏᴛ
├• Rᴘ. 25.000  [ VPS/1Bᴜʟᴀɴ { ᴘʀᴇᴍ } ]
├• Rᴘ. 20.000  [ VPS/1Bᴜʟᴀɴ { ʙɪᴀsᴀ } ]</b>
╰• sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ ᴛᴀɴᴘᴀ ʟᴏɢɪɴ ᴀᴋᴜɴ 
    
<b>❏ ᴊᴀsᴀ ᴅᴇᴘʟᴏʏ BOT ᴍᴜsɪᴋ
├ Rᴘ. 100.000 [ VPS/1ʙᴜʟᴀɴ ] 
├ ᴘʟᴜs ᴛᴀɢ ᴀʟʟ
├ ʀᴇϙ VPS 8/16 GB ɴᴀᴍʙᴀʜ ʜᴀʀɢᴀ</b> (ᴛᴀɴʏᴀ ᴀᴅᴍɪɴ)
╰•  sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ 

<b>❏ ᴊᴀsᴀ ᴅᴇᴘʟᴏʏ ʙᴏᴛ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ɢʀᴏᴜᴘ
├ Rᴘ. 40.000</b>
╰  sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ 

<b>❏  ᴊᴀsᴀ ᴅᴇᴘʟᴏʏ ʙᴏᴛ ғɪʟᴇ-sʜᴀʀɪɴɢ ғᴏʀᴄᴇ sᴜʙ / ᴀsᴜᴘᴀɴ CH
├ Rᴘ. 30.000 [ VPS/1ʙᴜʟᴀɴ ] 
├  ɴᴀᴍʙᴀʜ 1 ʙᴜᴛᴛᴏɴ +10ʀʙ
├  BISA REQ 1 - 6 FSUB
╰</b> sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ 

<b>❏ ᴊᴀsᴀ ᴅᴇᴘʟᴏʏ ʙᴏᴛ ᴍᴇɴғᴇs ғᴡʙ
├  Rᴘ. 130.000  [ VPS/1ʙᴜʟᴀɴ ]
├  ᴘᴇʀᴘᴀɴᴊᴀɴɢ sᴇᴛɪᴀᴘ ʙᴜʟᴀɴ 110K
├  sᴜᴘᴘᴏʀᴛ ᴀᴠᴀ ʙᴏʏ, ɢɪʀʟ, ᴛᴀʟᴇɴᴛ, sᴜɢᴅᴀᴅ, ɢғ/ʙғ ʀᴇɴᴛ, ᴍᴏᴀɴsʙᴏʏ, ᴍᴏᴀɴsɢɪʀʟ 
╰</b>  sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ 

<b>❏ ᴊᴀsᴀ ᴜᴘ ʟɪᴋᴇ, ʏᴛ ᴘʀᴇᴍ,  ɴᴏᴋᴏs ID 1/2/5, ɴᴏᴋᴏs WA ʟᴜᴀʀ/ɪɴᴅᴏ, ᴜᴘ ғᴏʟʟᴏᴡᴇʀs ᴅʟʟ
╰</b> ( ᴛᴀɴʏᴀᴋᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ sᴛᴏᴄᴋ ɴʏᴀ )

<b>❏ ᴄᴏɴᴛᴀᴄᴛ: @Dhilnihnge</b>""",
	reply_markup=InlineKeyboardMarkup(
@app.on_callback_query(filters.regex("help_u"))
# @cb_wrapper
async def commands_callbacc(_, cb: CallbackQuery):
    buttons = paginate_help(0, CMD_HELP, "helpme")
   
