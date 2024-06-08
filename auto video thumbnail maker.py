import asyncio
import os
from keys import api_id, api_hash
from pyrogram import Client, filters
from pyrogram.types import Message, Video
from pyrogram.handlers import MessageHandler
from typing import AsyncGenerator
from functions import makeThumbnail


tags = "#actress\n\n#Pussy\n#Anal\n#noPenetration\n#Group\n#Pov\n#Short\n#Bewitchingly"
def reversse_message_history(messages: AsyncGenerator):
    reverse = [message for message in messages]
    return reverse[::-1]

def clone_content(donor_channel_id: int, target_channel_id: int):
    bot = Client("Testy2", api_id, api_hash)
    bot.start()

    messages = bot.get_chat_history(chat_id=donor_channel_id)
    reverssed_messages = reversse_message_history(messages)
    i = -1
    for message in reverssed_messages:
        i += 1
        print(f"{i}/{len(reverssed_messages)}")
        if str(message.media) == "MessageMediaType.VIDEO": # or "MessageMediaType.ANIMATION"
            if message.video.duration < 300:
                # print("vidio too short")
                continue
            video_id = message.video.file_id
            name = message.video.file_name
            file_name = f"{message.video.file_unique_id}.mp4"
            video_path = download_video_TG(bot, video_id, file_name)
            if video_path:
                thumbnail_path = makeThumbnail(video_path)
                caption = f"{name}\n{tags}"
                thumbnail = bot.send_photo(target_channel_id, thumbnail_path, caption)
            bot.send_video(target_channel_id, video_id, reply_to_message_id=thumbnail.id)
            # message.copy(chat_id = target_channel_id)
            message.delete()
    else:
        print("finish")


def download_video_TG(client: Client, video_id, name):
    os.chdir("d:/Doccuments/VSCode/VideoDownloadBot/")
    if os.path.isfile("./Download/" + name):
        return f"Download/{name}"
    
    if client.download_media(video_id, file_name = f"Download/{name}"):
        return f"Download/{name}"
    else: 
        return 0


if __name__ == "__main__":
    donor_channel_id =  -1002157572270
    target_channel_id = -1002203495352
    clone_content(donor_channel_id, target_channel_id)