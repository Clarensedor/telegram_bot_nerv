from telegram import *
from telegram.ext import *
import open_wheater_api

##las pongo aca porque lo tengo que enviar sino lo mejor seria ponerlo en la maquina local o variable de entorno
api_key = "4630bf4acbe9679c0a98217c6be2201e"
updater = Updater('5432032388:AAG0F-oPzHht8OhJmA3ZPCCF7a9uFN7L3Hs', use_context=True)
dp = updater.dispatcher

def start(update, context):
  update.message.reply_text(main_menu_message(),
  reply_markup=main_menu_keyboard())


def help(update: Update,conntext: CallbackContext):
      update.message.reply_text("im not here for help you")

def main_menu_message():
  return 'Choose the option in main menu:'

def main_menu(bot, update):
  bot.callback_query.message.edit_text(main_menu_message(),
                          reply_markup=main_menu_keyboard())

def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Menu 1', callback_data='{"accion":"clima"}')],
              [InlineKeyboardButton('Menu 2', callback_data='{"accion":"count"}')]]
  return InlineKeyboardMarkup(keyboard)

def m1Calback(update, context):
      if(context.bot.message.handler(content_types=['text'])):
         context.bot.send_message(update.effective_chat.id, text=f"bien me escribiste")
         open_wheater_api.get_weater(api_key, update.message.text)


def m2Calback(update, context):
      context.bot.send_message(update.effective_chat.id, text=f"ingrese la ciudad")
      if(context.message.handler(content_types=['text'])):
         open_wheater_api.get_weater(api_key, 'montevideo')



##ejecuta los handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(m1Calback, pattern=".*clima.*"))
updater.dispatcher.add_handler(CallbackQueryHandler(m2Calback, pattern=".*count.*"))
##updater.dispatcher.add_handler(MessageHandler('messages',messages))
updater.start_polling()