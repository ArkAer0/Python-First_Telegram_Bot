from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Начать')
b2 = KeyboardButton('/Help')

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1).add(b2)