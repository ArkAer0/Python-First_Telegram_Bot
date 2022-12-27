import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1
@dp.message_handler(commands=["test1"])
async def cmd_test1(message: types.Message):
    await message.reply("Солнышко")

# Хэндлер на команду /test2
@dp.message_handler(commands="test2")
async def cmd_test2(message: types.Message):
    await message.reply("Я тебя люблю")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)