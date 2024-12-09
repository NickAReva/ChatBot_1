# bot.py

# import ChatBot
from chatterbot import ChatBot

# create a ChatBot instance
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# define exit conditions
exit_conditions = (":q", "quit", "exit")

# that’ll keep looping unless you enter one of the exit conditions defined in line 10
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        bot_input = bot.get_response(input())
        print(bot_input)