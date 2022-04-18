from asyncore import dispatcher
from email import message
from lib2to3.pgen2 import token
from statistics import mean
from turtle import up, update
import telegram
from telegram.ext import Upadter, MessageHandler, Filters
from telegram.ext import CommandHandler
from dictionary import get_info

telegram_bot_token = ""

updater = Upadter(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat_id
    context.bot.send_message(chat_id=chat_id, text="Hello there. Provide any English word and I will give you a bunch "
                                                   "of information about it.")
                                        
def get_word_info(update, context):
    word_info = get_info(update.message.text)
    if word_info.__class__ is str:
        upadeted_state = update.message.reply_text(word_info)
        return upadeted_state

    word = word_info['word']
    origin = word_info['origin']
    meanings = '\n'

    synonyms = ''
    definition = ''
    example = ''
    antonyms = ''

    meanings_counter = 1

    for word_meaning in word_info['meanings']:
        meanings += 'Meanings' + str(meanings_counter) + ':\n'

    for word_definition in word_meaning['definitions']:
        definition = word_definition['definition']

        if 'example' in word_definition:
            example = word_definition['example']

        for word_synonym in word_definition['synonyms']:
            synonyms += word_synonym + ', '

        for word_antonym in word_definition['antonyms']:
            antonyms += word_antonym

    meanings += 'Definition: ' + definition + '\n\n'
    meanings += 'Example: ' + example + '\n\n'
    meanings += 'Synonyms: ' + synonyms + '\n\n'
    meanings += 'Antonyms`: ' + antonyms + '\n\n'

    meanings_counter += 1

    message = f"Word: {word}\n\nOrigin: {origin}\n{meanings}"

    update.message.reply_text(message)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, get_word_info))
    updater.start_polling()