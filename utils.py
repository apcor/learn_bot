import settings
from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from random import choice, randint


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']

def main_keyboard():
    return ReplyKeyboardMarkup([['Send me a dog', KeyboardButton('See my location', request_location=True)]])

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Your number {user_number}, my number {bot_number}. \nYou won!"
    elif user_number == bot_number:
        message = f"Your number {user_number}, my number is also {bot_number}.\nIt's a draw!"
    else:
        message = f"Your number {user_number}, my number {bot_number}.\nYou lost! :-("
    return message