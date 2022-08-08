# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('5590655918:AAEwOj8MyVfudf6xxBNmgD9v9W1-oew2bmk')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Ассалому алейкум,  <b>{message.from_user.first_name}  {message.from_user.last_name}</b>\n'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Боздиди веб-сомона", url='https://nekruzsadriddinzoda.github.io/ziroat/'))
#     # markup.add(types.InlineKeyboardButton("Боздиди сомона", url='https://nekruzsadriddinzoda.github.io/ziroat/'))
#     bot.send_message(message.chat.id, "Веб-сомонаро боздид кунед", reply_markup=markup)
#
#
#
#
#
# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Салом алейкум":
#         bot.send_message(message.chat.id, "Воалейкум салом", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"ID - и Шумо: {message.from_user.id}", parse_mode='html')
#     elif message.text == "Салом":
#         bot.send_message(message.chat.id, "Ассалому алейкум", parse_mode='html')
#     elif message.text == "Ассалому алейкум":
#         bot.send_message(message.chat.id, "Воалейкум салом", parse_mode='html')
#     elif message.text == "Воалейкум салом":
#         bot.send_message(message.chat.id, "Ассалом", parse_mode='html')
#     elif message.text == "Ассалом":
#         bot.send_message(message.chat.id, "Воалейкум салом", parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, "Ман Шуморо намефахмам", parse_mode='html')
#
# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, "Бехтарин сурат")
#
# # @bot.message_handler(commands=['website'])
# # def website(message):
# #      markup = types.InlineKeyboardMarkup()
# #      markup.add(types.InlineKeyboardButton("Боздиди сомона", url='https://nekruzsadriddinzoda.github.io/ziroat/'))
# #      # markup.add(types.InlineKeyboardButton("Боздиди сомона", url='https://nekruzsadriddinzoda.github.io/ziroat/'))
# #      bot.send_message(message.chat.id, "Сомонаро боздид кунед", reply_markup=markup)
#
#
# bot.polling(none_stop=True)




import telebot
import wikipedia
import re
# Создаем экземпляр бота
bot = telebot.TeleBot('5590655918:AAEwOj8MyVfudf6xxBNmgD9v9W1-oew2bmk')
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:100000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'Энциклопедия дар ин бора маълумот надорад.'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):

    bot.send_message(m.chat.id,  f'Ассалому алейкум  {m.from_user.first_name}  {m.from_user.last_name}\nЯгон калимаро ба ман фиристед ва ман онро дар Википедиа ҷустуҷӯ мекунам')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0)

