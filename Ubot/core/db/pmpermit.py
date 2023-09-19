from . import pmdb


PMPERMIT_MESSAGE = ("""
𝙎𝙄𝘼𝙍𝘼𝘽-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🖍 
Sabar dulu ya nyet jangan ngespam ini pesan otomatis dari bot, sabar aja dulu sampe pesan lu di bales mek..

• ᴘᴇꜱᴀɴ ᴏᴛᴏᴍᴀᴛɪꜱ ʙʏ ᴀʀᴀʙ-🇺‌🇧‌🇴‌🇹‌ •
"""
)

BLOCKED = "**🇦‌🇳‌🇩‌🇦‌ 🇹‌🇪‌🇱‌🇦‌🇭‌ 🇲‌🇪‌🇱‌🇦‌🇰‌🇺‌🇰‌🇦‌🇳‌ 🇸‌🇵‌🇦‌🇲‌, 🇧‌🇱‌🇴‌🇨‌🇰‌🇪‌🇩‌!**"

LIMIT = 5


async def set_pm(user_id: int, value: bool):
    doc = {"user_id": user_id, "pmpermit": value}
    doc2 = {"user_id": "Approved", "users": []}
    r = await pmdb.find_one({"user_id": user_id})
    r2 = await pmdb.find_one({"user_id": "Approved"})
    if r:
        await pmdb.update_one({"user_id": user_id}, {"$set": {"pmpermit": value}})
    else:
        await pmdb.insert_one(doc)
    if not r2:
        await pmdb.insert_one(doc2)


async def set_permit_message(user_id: int, text):
    await pmdb.update_one({"user_id": user_id}, {"$set": {"pmpermit_message": text}}, upsert=True)



async def set_block_message(user_id: int, text):
    await pmdb.update_one({"user_id": user_id}, {"$set": {"block_message": text}}, upsert=True)


async def set_limit(user_id: int, limit):
    await pmdb.update_one({"user_id": user_id}, {"$set": {"limit": limit}}, upsert=True)


async def get_pm_settings(user_id: int):
    result = await pmdb.find_one({"user_id": user_id})
    if not result:
        return False
    pmpermit = result["pmpermit"]
    pm_message = result.get("pmpermit_message", PMPERMIT_MESSAGE)
    block_message = result.get("block_message", BLOCKED)
    limit = result.get("limit", LIMIT)
    return pmpermit, pm_message, limit, block_message


async def allow_user(chat):
    r = await pmdb.find_one({"user_id": "Approved"})
    if r:
        await pmdb.update_one({"user_id": "Approved"}, {"$addToSet": {"users": chat}})
    else:
        doc = {"user_id": "Approved", "users": [chat]}
        await pmdb.insert_one(doc)



async def get_approved_users(user_id: int):
    results = await pmdb.find_one({"user_id": "Approved"})
    if results:
        return results["users"]
    else:
        return []


async def deny_user(chat):
    await pmdb.update_one({"user_id": "Approved"}, {"$addToSet": {"users": chat}}, upsert=True)


async def pm_guard(user_id: int):
    result = await pmdb.find_one({"user_id": user_id})
    if not result:
        return False
    if not result.get("pmpermit", False):
        return False
    else:
        return True
