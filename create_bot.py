from aiogram import Bot, Dispatcher
from config import TOKEN
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storege = MemoryStorage()

# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot, storage=storege)