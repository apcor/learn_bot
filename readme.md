# Arsen's Telegram bot

## Installation
1. Clone the repository:

`git clone https://github.com/apcor/learn_bot.git`

2. Create a virtual environment:
```
python3 -m venv env
source env/bin/activate
```

3. Install all required dependencies: 

`pip install -r requirements.txt`

4. Create a `settings.py` file.
5. Insert the following commands in `settings.py` :
```
API_KEY = 'API key received from @BotFather'
USER_EMOJI = [':grinning:', ':neckbeard:', ':zzz:', ':hurtrealbad:', ':pig:', ':dog2:']
```
6. Initiate the bot with the console command `python3 bot.py`

## General info

This bot was created by **Arsen Sogoyan** during the [Learn Python course](https://learn.python.ru/) (*14/05/2022 - 16/07/2022*).

The bot is accessible on Telegram via [link](https://t.me/LearnPythonArsensBot).

**Note:** currently the bot works _only_ when `bot.py` module is running on my local machine. 

## Features

- ### Echo
Passing a `/start` command to the bot initiates *echo* mode: every input by the user is replicated by the bot in its response.

- ### Planet constellation

Passing a `/planet` command followed by a name of a planet (other than Earth) prompts a reply with *today's date* and *constellation the planet is in*.

- ### Requirements.txt added

Now all the modules reuired by the bot to function are listed in the `requirements.txt` file. 

**Tip:** use `pip install -r requirements.txt` to install all the required dependencies in bulk.

- ### Random dog image served

Passing a `/dog` command to the bot returns a random dog photo from the folder `images/`. Python native [`glob`](https://docs.python.org/3/library/glob.html) and [`random`](https://docs.python.org/3/library/random.html) libraries are employed here.

- ### Dog recognition on a photo

Sending an image to the bot prompts checks via [Clarifai API](https://docs.clarifai.com/api-guide/api-overview/) whether there is a dog on the sent image (decision threshold is `0.90`). Verified dog images are saved to the folder that serves random dog images (_see previous item_)


- ### Random emoji assigned to each user

Passing a `/start` or sending a message to the bot (see _**ECHO**_ feature above) triggers the bot's response accompanied by a randomly-chosen emoji from a pre-defined list in `settings.py`. Python [`emoji` library](https://pypi.org/project/emoji/) was used, along with `random`.

- ### Keyboard and Location
Two keyword buttons are introduced in the chat interface:
    
1. #### Send me a dog

This button replaces the manual input of `/dog` to request a random dog image.

2. #### See my location

This button gets your current location and returns to the user their coordinates and a small map preview.

**Warning:** works seamlessly on mobile phones. 
