from pyrogram.types import InlineKeyboardButton, WebAppInfo
from Ubot import cmds
class Data:

    text_help_menu = (
        f"**Help Menu Arab-Ubot**\n**• Prefixes** : `. ! ?`"
    )
    reopen = [[InlineKeyboardButton("Open", callback_data="reopen")]]
