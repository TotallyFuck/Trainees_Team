import telebot
bot = telebot.TeleBot('7341855102:AAGp2g5F-xgb5B7JpNbgw2BKiynHPVzfu70')
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Удачи на Хакатоне!")

bot.polling(none_stop=True)
