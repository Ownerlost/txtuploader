import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    me2 = (await bot.get_me()).mention
    editable = await m.reply_text(
       f"""𝐇𝐞𝐲 {m.from_user.mention}🍷,

𝐈 𝐀𝐦 {me2},
𝐅𝐨𝐫 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤𝐬 𝐅𝐫𝐨𝐦 𝐘𝐨𝐮𝐫 **.𝐓𝐗𝐓** 𝐅𝐢𝐥𝐞.
𝐀𝐧𝐝 𝐓𝐡𝐞𝐧 𝐔𝐩𝐥𝐨𝐚𝐝 𝐓𝐡𝐚𝐭 𝐅𝐢𝐥𝐞 𝐎𝐦 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐒𝐨 𝐁𝐚𝐬𝐢𝐜𝐚𝐥𝐥𝐲 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞 𝐅𝐢𝐫𝐬𝐭 𝐒𝐞𝐧𝐝 𝐌𝐞 ⟰ /madno 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐀𝐧𝐝 𝐓𝐡𝐞𝐧 𝐅𝐨𝐥𝐥𝐨𝐰 𝐅𝐞𝐰 𝐒𝐭𝐞𝐩𝐬..
𝐍𝐎 𝐀𝐍𝐘 𝐄𝐑𝐑𝐎𝐑.

𝐌𝐚𝐝𝐞 𝐁𝐲  : [𝙎𝙢𝙚𝙭𝙮 ᥫ᭡](channel name) !""", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✜ 𝐉𝐨𝐢𝐧 𝐔𝐩𝐃𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜" ,url=f"https://t.me/SmexyStore") ],
                    [
                    InlineKeyboardButton("✜◆ 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 ◆✜" ,url="https://t.me/SmexyOP") ],
                    [
                    InlineKeyboardButton("🦋 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🦋" ,url="https://www.youtube.com/@Vire_1_") ]                               
            ]))



@bot.on_message(filters.command(["Stop"]))
async def restart_handler(_, m):
    await m.reply_text("**💕𝑺𝒕𝒐𝒑𝒑𝒆𝒅 𝑩𝒂𝒃𝒆💕**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["madno"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('**𝐇𝐞𝐲 [Զเधे Զเधे](http://t.me/SmexyOP) 𝙃𝙚𝙧𝙚🍷 \n\n 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐀 𝐓𝐱𝐭 𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝 𝐇𝐞𝐫𝐞 ⏍**')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐢𝐥𝐞 𝐢𝐧𝐩𝐮𝐭.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**𝐓𝐨𝐭𝐚𝐥 𝐋𝐢𝐧𝐤 𝐅𝐨𝐮𝐧𝐝 𝐀𝐫𝐞 🔗🔗** **{len(links)}**\n\n**𝐒𝐞𝐧𝐝 𝐅𝐫𝐨𝐦 𝐖𝐡𝐞𝐫𝐞 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐈𝐧𝐢𝐭𝐚𝐥 𝐢𝐬** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**𝐄𝐧𝐭𝐞𝐫 𝐄𝐞𝐬𝐨𝐥𝐮𝐭𝐢𝐨𝐧 📸\n\nℚᴜᴀʟɪᴛʏ तो बताओ 𝕃ɪᴋᴇ 𝟷𝟺𝟺ᴘ, 𝟸𝟺𝟶ᴘ, 𝟹𝟼𝟶ᴘ, 𝟺𝟾𝟶ᴘ, 𝟽𝟸𝟶ᴘ, 𝟷𝟶𝟾𝟶ᴘ\nPlease Choose Quality**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("✏️ Now Enter A Caption to add caption on your uploaded file Otherwise send**   **`Զเधे Զเधे ᥫ᭡`**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'SmexyOP':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("🌄 Now send the Thumb url\nEg » **`https://graph.org/file/c9669066860d912fd5035.jpg`** \n\n Or if don't want thumbnail send = **`no`**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**𝐕𝐢𝐝_𝐢𝐝🎬➤ {str(count).zfill(3)}. {𝗻𝗮𝗺𝗲𝟭}{res}{MR}.mkv\n𝐁𝐚𝐭𝐜𝐡 ➤ {raw_text0} \n\n 🌟𝔻ᴏᴡɴʟᴏᴀᴅ 𝔹ʏ ✨ [Զเधे Զเधे 🦚 ᥫ᭡](http://t.me/SmexyOP)\n**'
                cc1 = f'**𝐩𝐝𝐟_𝐢𝐝📁➤ {str(count).zfill(3)}. {𝗻𝗮𝗺𝗲𝟭}{MR}.pdf \n𝐁𝐚𝐭𝐜𝐡 ➤ {raw_text0} \n\n 🌟𝔻ᴏᴡɴʟᴏᴀᴅ 𝔹ʏ ✨ —»»  [Զเधे Զเधे 🦚 ᥫ᭡](http://t.me/SmexyOP)\n**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**❊⟱𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »**\n\n**📝 𝐍𝐚𝐦𝐞 »** `{name}\n⌨ 𝐐𝐮𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n**🔗 𝐔𝐑𝐋 »** `{url}`\n\n𝐌𝐚𝐝𝐞 𝐁𝐲  : [Զเधे Զเधे 🦚 ᥫ᭡](http://t.me/SmexyOP)\n"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**Sb Nikal Diya Babe💕**")


bot.run()
