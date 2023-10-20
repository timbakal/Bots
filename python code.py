import pandas as pd
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import csv

bot = Bot(token="1297943688:AAFG-TOiMmZRr6z2qZLNckx5peyDNu-iRsI")
dp = Dispatcher(bot)

button_hi = KeyboardButton('Привет! 👋')
button_help = KeyboardButton('/help 👩🏻‍🔧')
button_ph = KeyboardButton('/brushesphotoshop 🎨')
button_pr = KeyboardButton('/brushesprocreate 🖌')
button_top5 = KeyboardButton('/top5 🇮🇱🇷🇺🇵🇱')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_help).add(button_pr).add(
    button_ph).add(button_top5)


@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Hi,I will help you to find a cool colour combination!\nFor instructions write /help',
                           reply_markup=greet_kb)


@dp.message_handler(commands=['help'])
async def process_help(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Enter a color, so I can choose\ncolors for you, that match your color')
    await bot.send_message(message.from_user.id,
                           'Enter /brushesprocreate to get a link to download brushes kit for Procreate')
    await bot.send_message(message.from_user.id,
                           'Enter /brushesphotoshop to get a link to download brushes kit for Photoshop')
    await bot.send_message(message.from_user.id,
                           'Enter /top5 to get 5 most important colours for designers')


@dp.message_handler(commands=['brushesprocreate'])
async def process_brushes(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'https://procreate.brushes.work/ru/большой-набор-кистей-для-procreate-волосы-гла/')


@dp.message_handler(commands=['brushesphotoshop'])
async def process_brushes(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'https://creativo.one/adds/brushes/')


@dp.message_handler(commands=['top5'])
async def process_top5(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text='Red, blue, green, orange, purple')
    data = pd.read_csv('puk.csv', delimiter=';')
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Red']
    text = text['Match']
    text = text.values
    text = 'Red matched with ' + str(text[0])
    await bot.send_message(chat_id=chat_id, text=text)
    chat_id = message.chat.id
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Red']
    photo = text['Link']
    photo = photo.values
    photo = str(photo[0])
    await bot.send_photo(chat_id=chat_id, photo=photo)

    data = pd.read_csv('puk.csv', delimiter=';')
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Blue']
    text = text['Match']
    text = text.values
    text = 'Blue matched with ' + str(text[0])
    await bot.send_message(chat_id=chat_id, text=text)
    chat_id = message.chat.id
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Blue']
    photo = text['Link']
    photo = photo.values
    photo = str(photo[0])
    await bot.send_photo(chat_id=chat_id, photo=photo)

    data = pd.read_csv('puk.csv', delimiter=';')
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Green']
    text = text['Match']
    text = text.values
    text = 'Green matched with ' + str(text[0])
    await bot.send_message(chat_id=chat_id, text=text)
    chat_id = message.chat.id
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Green']
    photo = text['Link']
    photo = photo.values
    photo = str(photo[0])
    await bot.send_photo(chat_id=chat_id, photo=photo)

    data = pd.read_csv('puk.csv', delimiter=';')
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Orange']
    text = text['Match']
    text = text.values
    text = 'Orange matched with ' + str(text[0])
    await bot.send_message(chat_id=chat_id, text=text)
    chat_id = message.chat.id
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Orange']
    photo = text['Link']
    photo = photo.values
    photo = str(photo[0])
    await bot.send_photo(chat_id=chat_id, photo=photo)

    data = pd.read_csv('puk.csv', delimiter=';')
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Purple']
    text = text['Match']
    text = text.values
    text = 'Purple matched with ' + str(text[0])
    await bot.send_message(chat_id=chat_id, text=text)
    chat_id = message.chat.id
    text = message.text
    text = text.capitalize()
    text = data.loc[data['Colour'] == 'Purple']
    photo = text['Link']
    photo = photo.values
    photo = str(photo[0])
    await bot.send_photo(chat_id=chat_id, photo=photo)


@dp.message_handler()
async def get_message(message: types.Message):
    global chat_id
    try:

        chat_id = message.chat.id
        data = pd.read_csv('puk.csv', delimiter=';')
        text = message.text
        text = text.capitalize()
        text = data.loc[data['Colour'] == text]
        text = text['Match']
        text = text.values
        text = str(text[0])
        await bot.send_message(chat_id=chat_id, text=text)
        chat_id = message.chat.id
        text = message.text
        text = text.capitalize()
        text = data.loc[data['Colour'] == text]
        photo = text['Link']
        photo = photo.values
        photo = str(photo[0])
        await bot.send_photo(chat_id=chat_id, photo=photo)
    except IndexError:
        await bot.send_message(chat_id=chat_id, text='You need to enter color')


executor.start_polling(dp)
