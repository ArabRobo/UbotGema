
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
       f"""<b>👋🏻 ʜᴀʟᴏ ɴɢᴇ sᴀʜᴀʙᴀᴛ @ArabPremUbot .\n
💭 ꜱᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ ʙᴏᴛ ᴀʀᴀʙ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀʙᴏᴛ\n
👉🏻 ᴊɪᴋᴀ ɪɴɢɪɴ ᴍᴇᴍʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ . ᴋᴀᴍᴜ ʙɪꜱᴀ ʜᴜʙᴜɴɢɪɴ ᴀᴅᴍɪɴ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʙᴏᴛ.</b>""",
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="👮‍♂ ʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ", url=f"https://t.me/Dhilnihnge"),
                ],
	    ]
    ))

@app.on_callback_query(filters.regex("help_u"))
async def module_help(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="helper")
            await asyncio.gather(
                message.delete(),
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")
            ac = PrettyTable()
            ac.header = False
            ac.title = "Modules"
            ac.align = "l"
            for x in split_list(sorted(CMD_HELP.keys()), 2):
                ac.add_row([x[0], x[1] if len(x) >= 2 else None])
            xx = await client.send_message(
                message.chat.id,
                f"```{str(ac)}```",
                reply_to_message_id=ReplyCheck(message),
            )
            await xx.reply(
                f"**Usage:** `help broadcast` **To View Module Information**"
            )
            return

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"**Bantuan {str(help_arg).upper()}**\n\n"
            for x in commands:
                this_command += f"๏ **Keterangan:** `{str(commands[x])}`\n\n"
            this_command += "@Dhilnihnge | Arab-Uprem"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"`{help_arg}` **tidak ada dalam list modul.**",
            )


def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
