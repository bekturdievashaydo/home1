
import logging
from aiogram import executor,types,Bot,Dispatcher
API_TOKEN = '7267676343:AAGwir48-wKPEl9pplBCvSMzvU3hLlVyk6E'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
@dp.message_handler(commands=["yordam"])
async def send_welcome(msg:types.Message):
    await msg.answer('bu bot haqida @shayd0 dan \nmalumot oplishingiz mumkin')

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)