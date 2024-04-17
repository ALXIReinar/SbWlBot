import telebot
from telebot import types
import webbrowser

TOKEN = 'WRITE YOUR TOKEN'
bot = telebot.TeleBot(TOKEN)

'''Команда "старт" '''
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Спорт")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Красота")
    btn3 = types.KeyboardButton("Витамины и добавки")
    btn4 = types.KeyboardButton("Парфюмерия")
    btn5 = types.KeyboardButton("Питание")
    btn6 = types.KeyboardButton("Новинки")
    btn7 = types.KeyboardButton("Акции")
    markup.add(btn2, btn3, btn4, btn5, btn6, btn7,)

    welcome = f"Привет, <b>{message.from_user.first_name}</b>\nЯ бот PERSON - консультанта компании COMPANY\nЗдесь Вы оперативно сможете выбрать желаемый товар по категории\nЕсли у Вас возникнут вопросы, пишите мне\nPERSON\nВыберите дейсвтие:"
    bot.send_message(message.chat.id, welcome, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, sport)


'''Команда "назад" '''
@bot.message_handler(commands=['back'])
def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Спорт")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Красота")
    btn3 = types.KeyboardButton("Витамины и добавки")
    btn4 = types.KeyboardButton("Парфюмерия")
    btn5 = types.KeyboardButton("Питание")
    btn6 = types.KeyboardButton("Новинки")
    btn7 = types.KeyboardButton("Акции")
    markup.add(btn2, btn3, btn4, btn5, btn6, btn7,)

    welcome = "Выберите действие:"
    bot.send_message(message.chat.id, welcome, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, sport)


'''Первая кнопка меню'''
def sport(message):
    bot_get_message = message.text.strip().lower()
    if bot_get_message == 'спорт':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Протеины")
        markup.row(btn1)
        btn2 = types.KeyboardButton("Аминокислоты")
        btn3 = types.KeyboardButton("Витамины и микроэлементы")
        btn4 = types.KeyboardButton("Продукты для суставов")
        btn5 = types.KeyboardButton("Бальзамы")
        btn6 = types.KeyboardButton("Стройная фигура")
        btn7 = types.KeyboardButton("Коллаген")
        markup.add(btn2, btn3, btn4, btn5, btn6, btn7)

        bot.send_message(message.chat.id, "Выберите подкатегорию:", reply_markup=markup)
        bot.register_next_step_handler(message, sport1)
    elif bot_get_message == 'красота':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Уход за лицом")
        markup.row(btn1)
        btn2 = types.KeyboardButton("Уход за волосами")
        btn3 = types.KeyboardButton("Уход за телом")
        btn4 = types.KeyboardButton("Уход за полостью рта")
        btn5 = types.KeyboardButton("Мужчинам")
        btn6 = types.KeyboardButton("Детская косметика")
        btn7 = types.KeyboardButton("Антивозрастной уход")
        markup.add(btn2, btn3, btn4, btn5, btn6, btn7, )

        bot.send_message(message.chat.id, "Выберите подкатегорию:", reply_markup=markup)
        bot.register_next_step_handler(message, beauty)
    elif bot_get_message == 'витамины и добавки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Мультивитамины")
        markup.row(btn1)
        btn2 = types.KeyboardButton("Минералы")
        btn3 = types.KeyboardButton("Омега 3,6,9")
        btn4 = types.KeyboardButton("Пробиотики и сорбенты")
        btn5 = types.KeyboardButton("Женщинам")
        btn6 = types.KeyboardButton("Мужчинам")
        btn7 = types.KeyboardButton("Детям")
        btn8 = types.KeyboardButton("Беременным и кормящим")
        btn9 = types.KeyboardButton("Вегетарианцам")
        btn10 = types.KeyboardButton("Иммунитет")
        btn11 = types.KeyboardButton("Суставы")
        btn12 = types.KeyboardButton("Детокс и очищение")
        btn13 = types.KeyboardButton("ANTI AGE")
        markup.add(btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12,  btn13)


        bot.send_message(message.chat.id,"Выберите подкатегорию:", reply_markup=markup)
        bot.register_next_step_handler(message, v_and_d)
    elif bot_get_message == 'парфюмерия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Для женщин")
        btn2 = types.KeyboardButton("Для мужчин")
        btn3 = types.KeyboardButton("Цветочные ароматы")
        btn4 = types.KeyboardButton("Цитрусовые ароматы")
        btn5 = types.KeyboardButton("Восточные ароматы")
        btn6 = types.KeyboardButton("Древесные ароматы")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        bot.send_message(message.chat.id, "Выберите подкатегорию:", reply_markup=markup)
        bot.register_next_step_handler(message, parfum)
    elif bot_get_message == 'питание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Функциональные напитки")
        btn2 = types.KeyboardButton("Батончики")
        btn3 = types.KeyboardButton("Заменители питания")
        btn4 = types.KeyboardButton("Вегетарианское питание")
        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id, "Выберите подкатегорию:", reply_markup=markup)
        bot.register_next_step_handler(message, food)
    elif bot_get_message == 'новинки':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_back = types.KeyboardButton("Назад")
        markup1.add(btn_back)
        bot.send_message(message.chat.id, "Ок", reply_markup=markup1)
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/new/?referral=2538460522")
        bot.register_next_step_handler(message, back)
    elif bot_get_message == 'акции':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_back = types.KeyboardButton("Назад")
        markup1.add(btn_back)
        bot.send_message(message.chat.id, "Ок", reply_markup=markup1)
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/actions/?referral=2538460522")
        bot.register_next_step_handler(message, back)
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Siberian Wellness", url="https://ru.siberianhealth.com/ru/?referral=2538460522"))
        bot.send_message(message.chat.id, "Официальный сайт:", reply_markup=markup)

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_back = types.KeyboardButton("Назад")
        markup1.add(btn_back)
        bot.send_message(message.chat.id, "Ок", reply_markup=markup1)

        bot.register_next_step_handler(message, back)


'''Вторая кнопка меню'''
def sport1(message):
    bot_get_message = message.text
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton("Назад")
    markup1.add(btn_back)
    bot.send_message(message.chat.id, "Ок", reply_markup=markup1)
    if bot_get_message == 'Протеины':
         webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/proteiny-226/?referral=2538460522")
    elif bot_get_message == 'Аминокислоты':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/aminokisloty-227/?referral=2538460522")
    elif bot_get_message == 'Витамины и микроэлементы':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-mikroelementy-228/?referral=2538460522")
    elif bot_get_message == 'Продукты для суставов':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/produkty-dlya-sustavov-229?referral=2538460522")
    elif bot_get_message == 'Бальзамы':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/balzamy-32/?referral=2538460522")
    elif bot_get_message == 'Стройная фигура':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/stroynaya-figura-210/?referral=2538460522")
    elif bot_get_message == 'Коллаген':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/kollagen-235/?referral=2538460522")
    bot.register_next_step_handler(message, back)


'''Третья кнопка меню'''
def beauty(message):
    bot_get_message = message.text
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton("Назад")
    markup1.add(btn_back)
    bot.send_message(message.chat.id, "Ок", reply_markup=markup1)
    if bot_get_message == 'Уход за лицом':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/uhod-za-litsom-33/?referral=2538460522")
    elif bot_get_message == 'Уход за волосами':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/ukhod-za-volosami-34/?referral=2538460522")
    elif bot_get_message == 'Уход за телом':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/ukhod-za-telom-35/?referral=2538460522")
    elif bot_get_message == 'Уход за полостью рта':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/ukhod-za-polostyu-rta-36/?referral=2538460522")
    elif bot_get_message == 'Мужчинам':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/muzhchinam-205/?referral=2538460522")
    elif bot_get_message == 'Детская косметика':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/detskaya-kosmetika-40/?referral=2538460522")
    elif bot_get_message == 'Антивозрастной уход':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/antivozrastnoy-uhod-43/?referral=2538460522")
    bot.register_next_step_handler(message, back)


'''Четвертая кнопка меню'''
def v_and_d(message):
    bot_get_message = message.text
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton("Назад")
    markup1.add(btn_back)
    bot.send_message(message.chat.id, "Ок", reply_markup=markup1)
    if bot_get_message == 'Мультивитамины':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vse-multivitaminy-11/?referral=2538460522")
    elif bot_get_message == 'Минералы':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vse-mineraly-12/?referral=2538460522")
    elif bot_get_message == 'Омега 3,6,9':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/omega-3-6-9-13/?referral=2538460522?referral=2538460522")
    elif bot_get_message == 'Пробиотики и сорбенты':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/probiotiki-i-sorbenty-125/?referral=2538460522")
    elif bot_get_message == 'Женщинам':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-dobavki-1/f/zhenshchinam-26/?referral=2538460522")
    elif bot_get_message == 'Мужчинам':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-dobavki-1/f/muzhchinam-3/?referral=2538460522")
    elif bot_get_message == 'Детям':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-dobavki-1/f/detyam-1/?referral=2538460522")
    elif bot_get_message == 'Беременным и кормящим':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-dobavki-1/f/beremennym-i-kormyaschim-2/?referral=2538460522")
    elif bot_get_message == 'Вегетарианцам':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-dobavki-1/f/vegetariantsam-5/?referral=2538460522")
    elif bot_get_message == 'Иммунитет':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-dobavki-1/f/silnyy-immunitet-15/?referral=2538460522")
    elif bot_get_message == 'Суставы':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-dobavki-1/f/sustavy-18/?referral=2538460522")
    elif bot_get_message == 'ANTI AGE':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-dobavki-1/f/anti-age-19/?referral=2538460522")
    elif bot_get_message == 'Детокс и очищение':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vitaminy-i-dobavki-1/f/detoks-i-ochishchenie-organizma-21/?referral=2538460522")
    bot.register_next_step_handler(message, back)


'''Пятая кнопка меню'''
def parfum(message):
    bot_get_message = message.text
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton("Назад")
    markup1.add(btn_back)
    bot.send_message(message.chat.id, "Ок", reply_markup=markup1)
    if bot_get_message == 'Для женщин':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/dlya-zhenshchin-213/?referral=2538460522")
    elif bot_get_message == 'Для мужчин':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/dlya-muzhchin-214/?referral=2538460522")
    elif bot_get_message == 'Цветочные ароматы':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/tsvetochnye-aromaty-220/?referral=2538460522")
    elif bot_get_message == 'Цитрусовые ароматы':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vostochnye-aromaty-223/?referral=2538460522")
    elif bot_get_message == 'Восточные ароматы':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vostochnye-aromaty-223/?referral=2538460522")
    elif bot_get_message == 'Древесные ароматы':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/tsvetochnye-aromaty-220/?referral=2538460522?referral=2538460522")
    bot.register_next_step_handler(message, back)


'''Шестая кнопка меню'''
def food(message):
    bot_get_message = message.text
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton("Назад")
    markup1.add(btn_back)
    bot.send_message(message.chat.id, "Ок", reply_markup=markup1)
    if bot_get_message == 'Функциональные напитки':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/funktsionalnye-napitki-18/?referral=2538460522")
    elif bot_get_message == 'Батончики':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/funktsionalnye-napitki-18/?referral=2538460522")
    elif bot_get_message == 'Заменители питания':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/zameniteli-pitaniya-17/?referral=2538460522")
    elif bot_get_message == 'Вегетарианское питание':
        webbrowser.open("https://ru.siberianhealth.com/ru/shop/catalog/vegetarianskoe-pitanie-128/?referral=2538460522")
    bot.register_next_step_handler(message, back)


bot.polling(none_stop=True)