from aiogram import Bot, Dispatcher
from config import TOKEN

# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)