import logging
import settings

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from handlers import (greet_user, const_planet, guess_number, send_dog_picture, 
                        user_coordinates, talk_to_me, check_user_photo)

logging.basicConfig(filename='bot.log', level=logging.INFO)

#PROXY = {'proxy_url': settings.PROXY_URL,'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.USER_PASSWORD}}



def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', const_planet))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('dog', send_dog_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Send me a dog)$'), send_dog_picture))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    

    logging.info('The bot has been initiated...')

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
