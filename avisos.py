import requests
"""
COMENTADO HASTA QUE LOS COMANDOS DEL BOT ESTEN INCORPORADOS

#IMPORTS NECESARIOS PARA EL BOT DE TELEGRAM
from telegram import ReplyKeyboardRemove, Update, InlineKeyboardButton, InlineKeyboardMarkup 
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    CallbackContext,
    CallbackQueryHandler, 
    
)#pip install python-telegram-bot

#CONSTANTE PARA EL ESTADO DE LA CONVERSACION (en este caso para almacenar el nombre del producto)
NOMBRE_PRODUCTO = range(1)

#CANCELAR OPERACION
async def cancelar(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    cancelar = query.data
    if cancelar.lower() == "cancelar" or cancelar.lower() == "no":
        await query.message.delete() 
        await query.message.reply_text("Operación cancelada.")
        return ConversationHandler.END

async def añadir_producto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #verificar_registro = await encontrar_usuario(update, context)
    #if verificar_registro != None: esto es parte de una futura funcion para verificar si esta 
    #registrado o no el usuario en la BBDD
    Teclas = [
        [InlineKeyboardButton("Cancelar", callback_data="cancelar")]
    ]
    reply_markup = InlineKeyboardMarkup(Teclas)
    mensaje = "Introduce el nombre del producto que deseas añadir: "
    await update.message.reply_text(mensaje, reply_markup=reply_markup)
    
    return NOMBRE_PRODUCTO"""


def enviar_mensaje_telegram(token, chat_id, texto):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}"
    requests.get(url)

