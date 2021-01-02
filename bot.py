# This example show how to use inline keyboards and process button presses
import telebot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import os, sys
from PIL import Image, ImageDraw, ImageFont
import random

TELEGRAM_TOKEN = '1344114096:AAHHt1B0-LtNJpmP5YaeP4bSNuUvSIQqE4c'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

channelId = -1001390673326
channelId1 = -1001462619192
user_dict = {}

markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = KeyboardButton("🧕 Xijobli 🌙")
btn2 = KeyboardButton("❤️ Chiroyli 🎀")
btn3 = KeyboardButton("🌸 Judayam Chiroyli 🌊")
btn4 = KeyboardButton("💞 Dugonalarga 🧸🧸")
markup.add(btn1, btn2, btn3, btn4)


def TextToImgx(ext):
    IMAGES = [
        'g006.jpg',
        'g011.jpg',
        'g014.jpg',
        'g021.jpg',
        'g031.jpg',
        'g034.jpg',
        'g035.jpg',
        'g036.jpg',
        'g045.jpg',
        'g048.jpg',
        'g049.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    try:
        fnt = ImageFont.truetype("New Year.ttf", 100)
    except:
        fnt = ImageFont.truetype("OpenSans-BoldItalic.ttf", 80)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/2,(1300)/2), text, font=fnt, fill=(255,0,0,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,35)
    g = out.save(f'{filename}.png')
    return filename

def TextToImgch(ext):
    IMAGES = [
        'g001.jpg',
        'g007.jpg',
        'g004.jpg',
        'g012.jpg',
        'g024.jpg',
        'g025.jpg',
        'g028.jpg',
        'g038.jpg',
        'g041.jpg',
        'g042.jpg',
        'g043.jpg',
        'g044.jpg',
        'g047.jpg',
        'g052.jpg',
        'g055.jpg',
        'g056.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    try:
        fnt = ImageFont.truetype("Pacifico.ttf", 80)
    except:
        fnt = ImageFont.truetype("OpenSans-BoldItalic.ttf", 80)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/2,(1300)/2), text, font=fnt, fill=(255,0,0,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,35)
    g = out.save(f'{filename}.png')
    return filename

def TextToImgjch(ext):
    IMAGES = [
        'g002.jpg',
        'g003.jpg',
        'g008.jpg',
        'g009.jpg',
        'g010.jpg',
        'g013.jpg',
        'g015.jpg',
        'g016.jpg',
        'g017.jpg',
        'g018.jpg',
        'g019.jpg',
        'g020.jpg',
        'g022.jpg',
        'g023.jpg',
        'g026.jpg',
        'g027.jpg',
        'g029.jpg',
        'g030.jpg',
        'g032.jpg',
        'g033.jpg',
        'g037.jpg',
        'g039.jpg',
        'g040.jpg',
        'g046.jpg',
        'g050.jpg',
        'g051.jpg',
        'g053.jpg',
        'g054.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    fnt = ImageFont.truetype("The Tide.ttf", 70)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/2,(1320)/2), text, font=fnt, fill=(255,0,0,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,35)
    g = out.save(f'{filename}.png')
    return filename

def TextToImgd(ext):
    IMAGES = [
        'f1.jpg',
        'f2.jpg',
        'f3.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    try:
        fnt = ImageFont.truetype("WinterYesterday.ttf", 50)
    except:
        fnt = ImageFont.truetype("OpenSans-BoldItalic.ttf", 50)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/2,(1320)/2), text, font=fnt, fill=(255,0,0,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,35)
    g = out.save(f'{filename}.png')
    return filename


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Azo bo'ling", url='t.me/onideal'), InlineKeyboardButton("Azo bo'ling", url='t.me/quyichirchiq_bozori'),
                               InlineKeyboardButton("Tasdiqlash", callback_data="yes"))
    return markup

def getUserFromChannel(userId):
    u = bot.get_chat_member(channelId, userId)
    u1 = bot.get_chat_member(channelId1, userId)
    a = 'left'
    if u.status == 'member':
        if u1.status == 'member':
            a = 'member'
        else:
            a = 'left'
    return a


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "yes":
        u = getUserFromChannel(call.from_user.id)
        if u == 'member':
            bot.send_message(call.from_user.id, "Juda soz!!!, Tugmalardan birini bosing", reply_markup=markup)
        else:
            bot.send_message(call.from_user.id, f"Salom {call.from_user.first_name}, kanallarga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tanlang", reply_markup=gen_markup())


def process_name_step_x(message):
    try:
        name = message.text
        myfile = TextToImgx(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f'{name} : 🕋🕌 \n@ismborbot'
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_name_step_ch(message):
    try:
        name = message.text
        myfile = TextToImgch(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f'{name} : 🌊🏹 \n@ismborbot'
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_name_step_jch(message):
    try:
        name = message.text
        myfile = TextToImgjch(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f'{name} : 🌞🌝 \n@ismborbot'
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_name_step_d(message):
    try:
        name = message.text
        myfile = TextToImgd(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f'{name} : 🌱🌛 \n@ismborbot'
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')



@bot.message_handler(commands=['start','help'])
def start(message):
    us = getUserFromChannel(message.chat.id)
    if us == 'member':
        bot.send_message(message.chat.id, "Assalomu Aleykum Shirin Qiz", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}, Kanalimizga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tasdiqlang", reply_markup=gen_markup())


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    us = getUserFromChannel(message.chat.id)
    msg = bot.send_message(message.chat.id, """\
                Juda soz!!!, Ismingizni yozing
                """)
    if us == 'member':
        if message.text == "🧕 Xijobli 🌙":
            bot.register_next_step_handler(msg, process_name_step_x)
        elif message.text == "❤️ Chiroyli 🎀":
            bot.register_next_step_handler(msg, process_name_step_ch)
        elif message.text == "🌸 Judayam Chiroyli 🌊":
            bot.register_next_step_handler(msg, process_name_step_jch)
        elif message.text == "💞 Dugonalarga 🧸🧸":
            bot.register_next_step_handler(msg, process_name_step_d)
    else:
        bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}, kanallarga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tanlang", reply_markup=gen_markup())


bot.polling(none_stop=True)
