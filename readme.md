# Arsen's Telegram bot

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

- ### Random emoji assigned to each user

Passing a `/start` or sending a message to the bot (see _**ECHO**_ feature above) triggers the bot's response accompanied by a randomly-chosen emoji from a pre-defined list in `settings.py`. Python [`emoji` library](https://pypi.org/project/emoji/) was used, along with `random`.
