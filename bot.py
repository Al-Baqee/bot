from pyrogram import Client, filters

# Bot Configuration
API_ID = 5112381637  # আপনার টেলিগ্রাম API_ID
API_HASH = "2003fb6ad71dceca0c827d28af18ca01"  # আপনার টেলিগ্রাম API_HASH
BOT_TOKEN = "7505817785:AAF-sfMEa4fsyII-ePYmUmV5AmZZ-xyzrHU"  # BotFather থেকে নেয়া BOT টোকেন

bot = Client("FLMovie_search_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Video Database (Just change names and file_ids)
video_db = {
    "Mohanagar (2021) Bangla S01": {"file_id": "AAMCBAADGQEAAl8VZ2_X97CjTlHe3uGYg1xwRsO1-AMAAuIYAAIq4IBT3R-BxVpc_moBAAdtAAM2BA
", "caption": "Mohanagar (2021) Bangla S01"},
    "batman": {"file_id": "file_id_2", "caption": "Batman Begins HD 2022"},
    "superman": {"file_id": "file_id_3", "caption": "Superman Returns 2021"}


























}


# Start Command Handler
@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply("👋 Hello, send me any part of the video name or caption. I will find it for you!")

# Video Search by Caption or Name
@bot.on_message(filters.text)
def search_video(client, message):
    query = message.text.lower()
    found = False
    for key, value in video_db.items():
        if query in key.lower() or query in value["caption"].lower():
            client.send_video(chat_id=message.chat.id, video=value["file_id"], caption=value["caption"])
            found = True
    if not found:
        message.reply("sorry, File no found requaest:@flstudio_fl")

# Get File ID from Channel
@bot.on_message(filters.command("getfile"))
def get_file_id(client, message):
    if message.reply_to_message and message.reply_to_message.video:
        file_id = message.reply_to_message.video.file_id
        message.reply(f"📂 এই ভিডিওর File ID:\n`{file_id}`")
    else:
        message.reply("⚠️ দয়া করে কোনো ভিডিওতে রিপ্লাই দিন।")

# Run the Bot
bot.run()
