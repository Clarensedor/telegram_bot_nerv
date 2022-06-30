from telegram import *
from telegram.ext import *
from requests import *
import open_wheater_api

##las pongo aca porque lo tengo que enviar sino lo mejor seria ponerlo en la maquina local o variable de entorno
api_key = "4630bf4acbe9679c0a98217c6be2201e"
updater = Updater('5432032388:AAG0F-oPzHht8OhJmA3ZPCCF7a9uFN7L3Hs')
dispatcher = updater.dispatcher

climaText = "clima"
countText = "contador"

def startCommand(update: Update, context: CallbackContext):
   buttons = [[KeyboardButton(climaText)], [KeyboardButton(countText)]]

   context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot",
   reply_markup=ReplyKeyboardMarkup(buttons))





def messageHandler(update: Update, context: CallbackContext):
   count=0
   lista_mensajes = []
   if climaText in update.message.text:
      result = open_wheater_api.get_weater(api_key, 'montevideo')
      update.message.reply_text(result)
   if countText in update.message.text:
      i = 0
      lista_mensajes = []
      while update.message.text != "stop":
         if():
            print(dispatcher)
            i += 1
            lista_mensajes.append(update.message.text)
            print()

   if update.message.text == "stop":
      print(lista_mensajes)





def help(update: Update,conntext: CallbackContext):
      update.message.reply_text("im not here for help you")

##ejecuta los handlers
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()