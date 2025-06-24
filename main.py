
import logging
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = "YOUR_BOT_TOKEN"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Bu Iymon365 botidir.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
