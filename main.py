
import telebot

from aut_token import  token
import random



def telegram_bot(token):

    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message (message):

        bot.send_message(message.chat.id, 'test')



    bot.polling()



if __name__=='__main__':
    telegram_bot(token)
