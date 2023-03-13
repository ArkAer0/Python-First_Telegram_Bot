from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
#from create_bot import dp, bot
from KeyBoards import kb_client


# Хэндлер на команду /start
#@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await message.answer("Привет! Я мастер по маникюру! \nУзнать список доступных команд ты можешь написав /help "
                        "\nЕсли хочешь сказать мне про свою любовь напиши люблю или коть)", reply_markup=kb_client)

# Хендлер на команду /help
#@dp.message_handler(commands=['help'])
async def command_help(massage: types.Message):
    await massage.reply('Чем могу помочь?\n Напиши /photo что бы увидеть мои работы)')


#Регестрируем хендлеры
def handlers_clients(dp):
    dp.register_message_handler(command_start, Text(equals=['Начать']))
    dp.register_message_handler(command_help, commands=['help'])