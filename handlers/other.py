from aiogram import types
from create_bot import dp

# Хэндлер на команду /test1
@dp.message_handler(text=['Люблю','люблю','коть'])
async def cmd_test2(message: types.Message):
    await message.reply("И я тебя очень люблю, лапочка")