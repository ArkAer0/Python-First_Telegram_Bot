from aiogram import types
from create_bot import dp, bot


# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.answer("Привет! Я мастер по маникюру! \nУзнать список доступных команд ты можешь написав /help "
                        "\nЕсли хочешь сказать мне про свою любовь напиши люблю или коть)")

# Хендлер на команду /help
@dp.message_handler(commands=['help'])
async def process_help_command(massage: types.Message):
    await massage.reply('Чем могу помочь?\n Напиши /photo что бы увидеть мои работы)')


@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):

    await bot.send_photo(message.from_user.id, open('KITTENS/2.jpg','rb'),
                         'Вот примеры моих работ!',
                         reply_to_message_id=message.message_id)
