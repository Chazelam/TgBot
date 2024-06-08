import asyncio
from keys import api_id, api_hash
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pornhub_api import PornhubApi
from functions import download_yt, download_video_PH, makeThumbnail

bot = Client("Testy", api_id, api_hash)

def sendRawUpdate(bot, message):
    message.reply('```' + str(message) + '```')

async def isYouTube(self, bot, update):
    return "youtu" in update.text
isYouTube_filter = filters.create(isYouTube)

async def isPornHub(self, bot, update):
    return "pornhub.com" in update.text
isPornHub_filter = filters.create(isPornHub)

def youtube(bot, message):
    message.reply("Youtube")
    path, res = download_yt(message.web_page.url)
    match res:
        case "1080p":
            message.reply("download in 1080p")
            bot.send_video(message.chat.id, path) # reply_to_message_id=photo.id
        case "Already download":
            message.reply("sds")
            bot.send_video(message.chat.id, path) # reply_to_message_id=photo.id
        case "less1080p":
            message.reply("download in less 1080p")
            bot.send_video(message.chat.id, path)

def pornHub(bot, message):
    chat_id = message.chat.id
    Video_URLs = message.text.replace("\n", " ").split(" ")
    print(Video_URLs)
    for Video_URL in Video_URLs:
        if "pornhub.com" in Video_URL:
            print(Video_URL)

            PH = PornhubApi()
            video = PH.video.get_by_id(Video_URL.split("=")[1])
            Video_name = video.video.title + '.mp4'
            bot.send_message(chat_id, text = f"Start downloading [{Video_name}]({Video_URL})")

            tags = video.video.categories + video.video.tags + video.video.pornstars
            tags = ''.join([f" #{str(tag).split("'")[1].replace(" ", "_").replace("-", "_")}\n" for tag in tags])

            path = download_video_PH(Video_URL, Video_name)
            if path == -1:
                bot.send_message(chat_id , text="Проблема прии скачивании")
            else:
                bot.send_message(chat_id , text="Video downloaded")

                bot.send_message(chat_id , text="Making Thumbnail ...", disable_notification=True)
                thumbnail_path = makeThumbnail(path)
                photo = bot.send_photo(chat_id, thumbnail_path, caption=f"{Video_name[:-4]}\n\n{tags}", disable_notification=True)
                bot.send_video(chat_id, path, reply_to_message_id=photo.id)



bot.add_handler(MessageHandler(sendRawUpdate)) # Debugging
bot.add_handler(MessageHandler(youtube, isYouTube_filter))
bot.add_handler(MessageHandler(pornHub, isPornHub_filter))
if __name__ == "__main__":
    bot.run()
