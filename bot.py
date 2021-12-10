from sqlite3.dbapi2 import connect
import telebot
import config
import sqlite3


from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])


def welcome(message):
    #sti = open('static/welcome.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti)

    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        balance REAL,
        chat INTEGER,
        referrals INTEGER);
        """)

    conn.commit()

    people_id = message.chat.id 
    cur.execute(f"""SELECT id FROM users WHERE id = {people_id}""")
    data = cur.fetchone()
    if data is None:

        user_id = [message.chat.id, 0, 0, 0]
        cur.execute("INSERT INTO users VALUES(?,?,?,?);", user_id)

        conn.commit()
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Русский")
    item2 = types.KeyboardButton("English")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Select language / Выберите язык".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Русский' :

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Я уже с вами")
            
            markup.add(item1)

            bot.send_message(message.chat.id, "Добро пожаловать в бота play-to-earn игры Earn to Corn🌽\nhttps://earntocorn.com\nХочешь начать зарабатывать криптовалюту еще до старта игры?\n 👌Добавляйся в официальный канал игры ".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)
            
            markup = types.InlineKeyboardMarkup(row_width=1)
            reg_button1 = types.InlineKeyboardButton('Перейти в чат', url = "https://t.me/earntocorn")
            
            markup.add(reg_button1)

            bot.send_message(message.chat.id, "Присоедиться к чату".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)
            
        elif message.text == 'Я уже с вами' :
                
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item4 = types.KeyboardButton("Узнать больше")
            item5 = types.KeyboardButton("Получить реф.ссылку")

            markup.add(item4, item5)

            bot.send_message(message.chat.id, "За что я получу токены игры?\n✅ Приглашение нового члена комьюнити по реферальной ссылке = 1 TCORN\n✅ 10 ТОП лидеров по количеству приглашений = 5 TCORN ежедневно.\n✅ Еженедельный розыгрыш 1000 TCORN 🎁 среди участников\n⚡После старты игры токены tcorn будут конвертированы в токены CORN 1 к 1 ⚡ ".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)

        elif message.text == 'Получить реф.ссылку':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            mainkbr = types.KeyboardButton('Мой аккаунт')
            mainkbr1 = types.KeyboardButton('Реферальная ссылка')
            mainkbr2 = types.KeyboardButton('Токен CORN')
            mainkbr3 = types.KeyboardButton('Мои рефералы')
            mainkbr4 = types.KeyboardButton('Мои промокоды')
            mainkbr5 = types.KeyboardButton('Вопросы и ответы')
            mainkbr6 = types.KeyboardButton('Официальные ресурсы')
            mainkbr7 = types.KeyboardButton('Техподдержка')

            markup.add(mainkbr, mainkbr1, mainkbr2, mainkbr3, mainkbr4, mainkbr5, mainkbr6, mainkbr7)

            bot.send_message(message.chat.id, "Забери свою персональную реферальную ссылку!\nt.me/earntocorn_bot\nВсе, что тебе нужно – это приглашать друзей в игру 🌽".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup )

        elif message.text == 'Узнать больше' :

            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            mainkbr = types.KeyboardButton('Мой аккаунт')
            mainkbr1 = types.KeyboardButton('Реферальная ссылка')
            mainkbr2 = types.KeyboardButton('Токен CORN')
            mainkbr3 = types.KeyboardButton('Мои рефералы')
            mainkbr4 = types.KeyboardButton('Мои промокоды')
            mainkbr5 = types.KeyboardButton('Вопросы и ответы')
            mainkbr6 = types.KeyboardButton('Официальные ресурсы')
            mainkbr7 = types.KeyboardButton('Техподдержка')

            markup.add(mainkbr, mainkbr1, mainkbr2, mainkbr3, mainkbr4, mainkbr5, mainkbr6, mainkbr7)

            bot.send_message(message.chat.id, "👇 Панель управления ботом 👇".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup )

        elif message.text == 'English':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  
            reg_button = types.KeyboardButton("I'm already with you")

            markup.add(reg_button,)

            bot.send_message(message.chat.id, "Welcome to the bot play-to-earn games Earn to Corn🌽\nhttps://earntocorn.com\n Do you want to start earning cryptocurrency even before the start of the game? 👌Add to the official channel of the game".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup )
            
            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton(text = 'Join the channel', url = "t.me/earntocorn")

            markup.add(item3)

            bot.send_message(message.chat.id, "Join the comunity".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup )
        elif message.text == "I'm already with you" :
                
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item4 = types.KeyboardButton("Lern more")
            item5 = types.KeyboardButton("Get the referral link")

            markup.add(item4, item5)

            bot.send_message(message.chat.id, "What will I get game tokens for?\nInvitation of a new community member by referral link = 1 TCORN\n✅ TOP 10 leaders in the number of invitations = 5 TCORN daily.\n✅ Weekly drawing of 1000 TCORN 🎁 among the participants\ntcAfter the game starts, TCORN tokens will be converted to CORN tokens 1 to 1 ⚡".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)

        elif message.text == 'Get the referral link':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            mainkbr = types.KeyboardButton('My account')
            mainkbr1 = types.KeyboardButton('Referral link')
            mainkbr2 = types.KeyboardButton('CORN token')
            mainkbr3 = types.KeyboardButton('My referrals')
            mainkbr4 = types.KeyboardButton('My promo codes')
            mainkbr5 = types.KeyboardButton('Questions and answers')
            mainkbr6 = types.KeyboardButton('Official resources')
            mainkbr7 = types.KeyboardButton('Support')

            markup.add(mainkbr, mainkbr1, mainkbr2, mainkbr3, mainkbr4, mainkbr5, mainkbr6, mainkbr7)

            bot.send_message(message.chat.id, "Here is your personal referral link\nt.me/earntocorn_bot\nAll youneed to invite your friends to the game 🌽".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup )

        elif message.text == 'Lern more' :

            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            mainkbr = types.KeyboardButton('My account')
            mainkbr1 = types.KeyboardButton('Referral link')
            mainkbr2 = types.KeyboardButton('CORN token')
            mainkbr3 = types.KeyboardButton('My referrals')
            mainkbr4 = types.KeyboardButton('My promo codes')
            mainkbr5 = types.KeyboardButton('Questions and answers')
            mainkbr6 = types.KeyboardButton('Official resources')
            mainkbr7 = types.KeyboardButton('Support')

            markup.add(mainkbr, mainkbr1, mainkbr2, mainkbr3, mainkbr4, mainkbr5, mainkbr6, mainkbr7)

            bot.send_message(message.chat.id, "👇 Bot control panel 👇".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup )



# RUN
bot.polling(none_stop=True)