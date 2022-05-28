import datetime
import logging
from glob import glob
from random import choice, randint

import ephem
from emoji import emojize
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

#PROXY = {'proxy_url': settings.PROXY_URL,'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.USER_PASSWORD}}

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']

def greet_user(update, context):
    print("/start has been called")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Hello user {context.user_data['emoji']}!")
    #print(update)

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}")

def send_dog_picture(update, context):
    dog_photos_list = glob('images/dog*.jp*g')
    dog_pic_filename = choice(dog_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(dog_pic_filename, 'rb'))


def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Your number {user_number}, my number {bot_number}. \nYou won!"
    elif user_number == bot_number:
        message = f"Your number {user_number}, my number is also {bot_number}.\nIt's a draw!"
    else:
        message = f"Your number {user_number}, my number {bot_number}.\nYou lost! :-("
    return message

def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Enter an integer please'
    else:
        message = "Introduce an integer"
    update.message.reply_text(message)

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
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('dog', send_dog_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    logging.info('The bot has been initiated...')

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
