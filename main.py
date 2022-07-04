from telegram import *
from telegram.ext import *
from requests import *
import open_wheater_api
import os
#la documentacion que use fue https://docs.python-telegram-bot.org/en/stable/index.html



##las pongo aca porque lo tengo que enviar sino lo mejor seria ponerlo en la maquina local o como variable de entorno
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

##no pude hacer que lo que devuelve el ususario ponerlo en la funcion que usa la api. le meti montevideo de una :p
def ClimaHandler(update: Update, context: CallbackContext):
   file1 = open("Original.txt", "a")
   file1.write(update.message.text + "\n")
   file1.close
   result = open_wheater_api.get_weater(api_key, "montevideo")
   update.message.reply_text(result)


##lo del contador lo hice con escribiendo en un texto, capaz lo podia hacer guardandolo en un json.
def CountHandler(update: Update, context: CallbackContext):
   file1 = open("Original.txt", "r+")
   file1.write(update.message.text + "\n")
   total_lines = len(file1.readlines())
   print(file1.closed)
   if update.message.text == "/contador":
      update.message.reply_text(total_lines)
      os.remove("Original.txt")
      file1 = open("Original.txt", "a")



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