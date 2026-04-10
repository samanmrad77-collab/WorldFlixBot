
import os
import subprocess
from pyrogram import Client, filters

# فەرمان بۆ دابەزاندنی FFmpeg لەسەر سێرڤەری میواندار
os.system("apt-get update && apt-get install -y ffmpeg")

# زانیارییەکانی بۆتەکە
BOT_TOKEN = "8616718569:AAHTt00XciUVfRkm64VGGq9VB0F8nL7whq4"
API_ID = "22557342"
API_HASH = "8ba120015f694e5e41416e788e2c8449"

app = Client("worldflix_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.text & filters.private)
async def compress_video(client, message):
    url = message.text
    if not url.startswith("http"):
        await message.reply("تکایە لینکێکی ڕاستەوخۆ بنێرە.")
        return

    status = await message.reply("خەریکی ئامادەکردنی ڤیدیۆکەم بۆ WORLD FLIX...")
    
    input_f = "video.mp4"
    output_f = "WORLD_FLIX_Video.mp4"

    try:
        # داگرتنی ڤیدیۆ
        subprocess.run(["wget", "-O", input_f, url])
        
        # کەمکردنەوەی قەبارە
        subprocess.run([
            "ffmpeg", "-i", input_f, 
            "-vcodec", "libx264", "-crf", "28", 
            "-preset", "ultrafast", "-acodec", "aac", output_f
        ])
        
        # ناردنەوەی ڤیدیۆکە
        await message.reply_video(video=output_f, caption="فەرموو ڤیدیۆکەت بە قەبارەی کەم ئامادەیە.\nبەرهەمی WORLD FLIX")
    
    except Exception as e:
        await message.reply(f"هەڵەیەک ڕوویدا: {e}")
    
    finally:
        if os.path.exists(input_f): os.remove(input_f)
        if os.path.exists(output_f): os.remove(output_f)

app.run()
