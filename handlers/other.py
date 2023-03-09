from aiogram import types, Dispatcher
from create_bot import dp

# Хэндлер на команду /test1
#@dp.message_handler(text=['Люблю','люблю','коть'])
async def cmd_test2(message: types.Message):
    await message.reply("И я тебя очень люблю, лапочка")

def handlers_other(dp: Dispatcher):
    dp.register_message_handler(cmd_test2, text=['Люблю','люблю','коть'])
