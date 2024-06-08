import asyncio
from keys import api_id, api_hash
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from typing import AsyncGenerator

async def reversse_message_history(messages: AsyncGenerator):
    reverse = [message async for message in messages]
    return reverse[::-1]

async def clone_content(donor_channel_id: int, target_channel_id: int):
    bot = Client("Testy2", api_id, api_hash)
    await bot.start()

    messages: AsyncGenerator[Message, None] = bot.get_chat_history(chat_id=donor_channel_id)

    reverssed_messages = await reversse_message_history(messages)

    for message in reverssed_messages:
        await message.copy(chat_id = target_channel_id)

if __name__ == "__main__":
    donor_channel_id = -1002185579056
    target_channel_id = -1002203495352
    asyncio.run(clone_content(donor_channel_id, target_channel_id))