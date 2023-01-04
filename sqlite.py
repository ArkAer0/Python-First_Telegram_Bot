#Импорт модуля для работ с БД
import sqlite3 as sq

#Создание ассинхронной фукнции отвечающая за запуск моей БД
async def db_start():
    global db, cur
#db это экземпляр базы данных ( как бы модель нашей базы данных)
    db = sq.connect('new.db') #Если нет будет создаваться, если есть будет подключаться
#Курсор необходим что бы выполнять какие либо операции с нашей БД
    cur = db.cursor()

#Создаем в нашей БД таблицы

    cur.execute('CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo TEXT, age TEXT, description TEXT)') #Создаем таблицу если не существует, иначе создавать не нужно, а если не
# существет то мы создаем таблицу с именем профиль

#Далее для того что бы опперация была завершена нам необходимо закомиттить
    db.commit()


#Функция отвечающая за создание профиля пользователя
#Будет сробатывать при команде старт
async def creat_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key = user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?,?,?,?)",(user_id, '','',''))
        db.commit()

async def edit_profile(user_id):
    async with proxy() as data:
        cur.execute("UPDATE profile WHERE user_id == '{}' SET photo = '{}', age = '{}', description = '{}'".format(
            user_id, data['photo'], data['age'],data['description']))
        db.commit()