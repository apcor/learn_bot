from glob import glob
import os
from random import choice
from turtle import up
import ephem
import datetime
from utils import main_keyboard, get_smile, play_random_numbers, has_object_on_image


def greet_user(update, context):
    print("/start has been called")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Hello user {context.user_data['emoji']}!",
    reply_markup=main_keyboard())

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}", reply_markup=main_keyboard())

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
    update.message.reply_text(message, reply_markup=main_keyboard())

def check_user_photo(update, context):
    update.message.reply_text('Processing image...')
    os.makedirs('downloads', exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join('downloads', f'{update.message.photo[-1].file_id}.jpeg')
    photo_file.download(file_name)
    update.message.reply_text('Image saved successfully')
    if has_object_on_image(file_name, 'dog'):
        update.message.reply_text('A dog has been detected. Saving the image to my library...')
        new_file_name = os.path.join('images', f'dog_{photo_file.file_id}.jpeg')
        os.rename(file_name, new_file_name)
    else:
        os.remove(file_name)
        update.message.reply_text('Warning! No dog detected.')

def send_dog_picture(update, context):
    dog_photos_list = glob('images/dog*.jp*g')
    dog_pic_filename = choice(dog_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(dog_pic_filename, 'rb'), reply_markup=main_keyboard())

def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Your current coordinates are {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )

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