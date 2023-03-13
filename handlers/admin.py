from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher.filters import Text

class FSM_admin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#Хендлер для начала диалога загрузки новой работы
#@dp.message_handler(commands = 'Загрузить', state = None)
async def cm_start(message: types.Message):
    await FSM_admin.photo.set()
    await message.reply('Загрузить фото')

#Ловим первый ответ от пользователя и пишем в словарь
#@dp.message_handler(content_types=['photo'], state=FSM_admin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSM_admin.next()
    await message.answer('Теперь введите название')

#Ловим второй ответ
#@dp.message_handler(state=FSM_admin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSM_admin.next()
    await message.answer('Теперь введите описание')

#Ловим третий ответ
#@dp.message_handler(state=FSM_admin.name)
async def load_discription(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['discription'] = message.text
    await FSM_admin.next()
    await message.answer('Теперь введите цену')

#Ловим четвертый ответ
#@dp.message_handler(state=FSM_admin.name)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))

    await state.finish()

#@dp.message_handler(state="*", commands='отмена')
#@dp.message_handler(Text(equals = 'отмена', ignore_case = True), state="*")
async def cancel_load(message: types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state == None:
        return
    await state.finish()
    await message.reply('Ok')

#Регестрируем хендлеры
def handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands='Загрузить', state=None)
    dp.register_message_handler(load_photo,content_types=['photo'], state=FSM_admin.photo)
    dp.register_message_handler(load_name, state=FSM_admin.name)
    dp.register_message_handler(load_discription, state=FSM_admin.description)
    dp.register_message_handler(load_price, state=FSM_admin.price)
    dp.register_message_handler(cancel_load, state="*", commands='отмена')
    dp.register_message_handler(cancel_load, Text(equals='отмена', ignore_case=True), state="*")