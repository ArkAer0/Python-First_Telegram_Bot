from aiogram import types, Dispatcher
from create_bot import dp, bot


# Хэндлер на команду /start
#@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await message.answer("Привет! Я мастер по маникюру! \nУзнать список доступных команд ты можешь написав /help "
                        "\nЕсли хочешь сказать мне про свою любовь напиши люблю или коть)")

# Хендлер на команду /help
#@dp.message_handler(commands=['help'])
async def command_help(massage: types.Message):
    await massage.reply('Чем могу помочь?\n Напиши /photo что бы увидеть мои работы)')


#@dp.message_handler(commands=['photo'])
async def command_photo(message: types.Message):

    await bot.send_photo(message.from_user.id, open('KITTENS/2.jpg','rb'),
                         'Вот примеры моих работ!',
                         reply_to_message_id=message.message_id)

def handlers_clients(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_photo, commands='photo')