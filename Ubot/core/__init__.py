from pyrogram import filters, Client

from .ai import *
from .data import *
from .func import *
from .inline import *
from .lgs import *
from .what import *
from .filter import *
from .constants import *

async def ajg(client):
    try:
        await client.join_chat("GroupSiArab")
        await client.join_chat("JasaSiArab")
        await client.join_chat("ArabCodee")
        await client.join_chat("lpm_bbg_ddk14")
        await client.join_chat("SXID_IN_GAME")
    except BaseException:
        pass
