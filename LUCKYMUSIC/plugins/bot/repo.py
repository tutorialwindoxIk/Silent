import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from LUCKYMUSIC import app
from config import BOT_USERNAME, BANNED_USERS

LUCKY_VID = [
    "https://telegra.ph/file/9b7e1b820c72a14d90be7.mp4",
    "https://telegra.ph/file/a4d90b0cb759b67d68644.mp4",
    "https://telegra.ph/file/72f349b1386d6d9374a38.mp4",
    "https://telegra.ph/file/2b75449612172a96d4599.mp4",
    "https://telegra.ph/file/b3ac2d77205d5ded860de.mp4",
    "https://telegra.ph/file/58ae4ac86ef70dc8c8f6a.mp4",
    "https://telegra.ph/file/c6c1ac9aee4192a8a3747.mp4",
    "https://telegra.ph/file/55c840c8eba0555318f0d.mp4",
    "https://telegra.ph/file/e97715885d0a0cfbddaaa.mp4",
    "https://telegra.ph/file/943bb99829ec526c3f99a.mp4"
]

start_txt = """**
✪ ωεℓ¢σмє ƒσя jคяv¡ร яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo", prefixes=["/", "!",]) & ~BANNED_USERS)

  buttons = [
     
            [
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇs✪", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/JARVIS_V2"),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/JARVIS_X_SUPPORT"),
             ],
     
             [
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/CHATTING_2024"),          
             InlineKeyboardButton("︎ᴍᴜsɪᴄ", url=f"https://github.com/doraemon890/ANNIE-X-MUSIC"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_video(
          random.choice(LUCKY_VID),
        caption=start_txt,
        reply_markup=reply_markup
    )
