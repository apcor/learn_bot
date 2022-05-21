import logging
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

#PROXY = {'proxy_url': settings.PROXY_URL,'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.USER_PASSWORD}}

def greet_user(update, context):
    print('You clicked on /start')
    update.message.reply_text('Hello, user!')
    #print(update)

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def const_planet(update, context):
    user_pl = update.message.text.split()[1].lower().capitalize()
    loc_date = datetime.date.today()
    if user_pl in planets:
        user_pl_eph = getattr(ephem, user_pl)
        user_pl_const = ephem.constellation(user_pl_eph(loc_date.strftime("%Y/%m/%d")))
        update.message.reply_text(f'Today is {loc_date.strftime("%A, %d of %B %Y")}. \n{user_pl} is in the constellation {user_pl_const[1]}.')
    else:
        update.message.reply_text('Please insert a valid name of a planet (other than Earth)')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', const_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    logging.info('The bot has been initiated...')

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()