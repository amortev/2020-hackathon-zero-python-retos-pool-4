import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    update.message.reply_text("Esto es mi primer bot para Hackthon Zero by Ana Morte")

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    update.message.reply_text("Esto es un mensaje de ayuda para los usuarios de este bot")

def mayus(update, context):
    update.message.reply_text(update.message.text.upper())
       

def alreves(update, context):
    """Repite el mensaje del usuario."""
    if(update.message.text.upper().find("MANZANAS VERDES") > 0):
        update.message.reply_text("Prefiero comer pizza")

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater( token="1191185053:AAFcJfXL88KvgZx1mMfLfx0sEtg1aj8YWyc", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("mayus", mayus))

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    dp.add_handler(MessageHandler(Filters.text, alreves))
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
