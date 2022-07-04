from asyncio.windows_events import NULL
from queue import Empty
from telegram import *
from telegram.ext import *
from requests import *
import open_wheater_api
import os

##las pongo aca porque lo tengo que enviar sino lo mejor seria ponerlo en la maquina local o variable de entorno
api_key = "4630bf4acbe9679c0a98217c6be2201e"
updater = Updater('5432032388:AAG0F-oPzHht8OhJmA3ZPCCF7a9uFN7L3Hs', use_context=True)
dispatcher = updater.dispatcher


def startCommand(update: Update, context: CallbackContext):
   file1 = open("Original.txt", "a")
   file1.write(update.message.text + "\n")
   file1.close
   buttons = [[KeyboardButton("/clima")], [KeyboardButton("/contador")]]
   context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot",
   reply_markup=ReplyKeyboardMarkup(buttons))

def ClimaHandler(update: Update, context: CallbackContext):
   file1 = open("Original.txt", "a")
   file1.write(update.message.text + "\n")
   file1.close
   result = open_wheater_api.get_weater(api_key, "montevideo")
   update.message.reply_text(result)




def CountHandler(update: Update, context: CallbackContext):
   file1 = open("Original.txt", "r+")
   file1.write(update.message.text + "\n")
   total_lines = len(file1.readlines())
   print(file1.closed)
   if update.message.text == "/contador":
      update.message.reply_text("sus mensajes hasta ahora son: " + total_lines)
      os.remove("Original.txt")

            




def help(update: Update, conntext: CallbackContext):
   file1 = open("Original.txt", "a")
   file1.write(update.message.text + "\n")
   file1.close
   update.message.reply_text("im not here for help you")


##ejecuta los handlers
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(CommandHandler("clima", ClimaHandler))
dispatcher.add_handler(CommandHandler("contador", CountHandler))
dispatcher.add_handler(CommandHandler("help", help))
updater.start_polling()
updater.idle()