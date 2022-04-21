

import telebot

from aut_token import  token
import random



def telegram_bot(token):

    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет 🙋🏼Я бот "Смайлик 😀".'
                                          ' Я был создан как учебный проект🤓 для'
                                          ' презентации в университете🧑🏼‍🎓.'
                                          ' Главная моя функция  — заменять все знаки пунктуации на смайлики 😐.'
                                          ' Поэтому просто напиши мне любой текст и заменю'
                                          ' все знаки препинания на разные веселые смайлики 😁'
                         )

    @bot.message_handler(content_types=["text"])


    bot.polling()



if __name__=='__main__':
    telegram_bot(token)
=======
import random


def replacing_symbols(some_text):

    emoji_list = ['😀', '😃', '😄', '😁',
                  '👹','☠️','🤖','👨‍💻',
                  '🤵','👓','👌🏻','🇺🇦',
                  '🖥','🛠','⚙️','💵',
                  '🩸','💿','💈','🪦',]

    marks = '''!()-[]{};?@#$%:'"\,./^&;*_'''

    for i in some_text:
        if i in marks:
             some_text = some_text.replace(i,random.choice(emoji_list))
    return some_text


if __name__ == '__main__':

  print(  replacing_symbols('Приве! Я, Антон.'))






