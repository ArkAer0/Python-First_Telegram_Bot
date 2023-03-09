#Здесь происходит инициализация всего бота работает как точка входа
from aiogram import executor
from create_bot import dp

from handlers import clients, admin, other

clients.handlers_clients(dp)
other.handlers_other(dp)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)