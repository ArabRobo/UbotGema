
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
       f"""<b>👋🏻 ʜᴀʟᴏ {mention} .\n
💭 ꜱᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ ʙᴏᴛ ᴀʀᴀʙ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀʙᴏᴛ
👉🏻 ᴊɪᴋᴀ ɪɴɢɪɴ ᴍᴇᴍʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ . ᴋᴀᴍᴜ ʙɪꜱᴀ ʜᴜʙᴜɴɢɪɴ ᴀᴅᴍɪɴ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʙᴏᴛ.</b>""",
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="👮‍♂ ʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ", url=f"https://t.me/Dhilnihnge"),
                ],
	    ]
    ))
