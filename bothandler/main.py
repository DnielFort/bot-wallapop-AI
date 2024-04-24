import telebot
from dotenv import load_dotenv
import os
from auxiliares import *

# Obtiene ruta al directorio padre
parent_dir = os.path.dirname(os.getcwd())

# Construye la ruta al archivo .env
dotenv_path = os.path.join(parent_dir, 'bot-wallapop-AI-main 2', '.env')

print("\n",dotenv_path,"\n")
# Carga las variables de entorno del archivo .env en el entorno actual
load_dotenv()
# Ahora puedes acceder a las variables de entorno con os.getenv
TOKEN = os.getenv('TOKEN')
PASSWORD = "ronnie"
print("la contra es: ",PASSWORD)


authorized_users = obtener_nombres_carpetas_usuarios()
for autori in authorized_users:
    print(autori)

mensaje_principal = (
    "👋 Hola, soy un bot que te avisa de las nuevas ofertas rápidamente para que no se te escapen! 🚀\n"
    "Actualmente el bot se encuentra en fase de pruebas 🧪, si experimentas algún problema o quieres una nueva funcionalidad \n"
    "por favor, contacta conmigo con los datos que encontrarás en /help 📬\n"
    "Estos son los comandos que puedes usar: \n"
    "Utiliza el comando /menu para comenzar 📋\n"
    "Utiliza el comando /help para obtener ayuda 🆘\n"
)
mensaje_no_autorizado = "🚫 No tienes acceso. Por favor, ingresa la contraseña con /password tu_contraseña 🔑."
bot = telebot.TeleBot(TOKEN)

mensaje_ayuda = (
     "🆘 Ayuda:\n"
                          "Para buscar productos, utiliza el comando /nuevo_aviso (link a tu anuncio)\n"
                          "Para ver el menú, utiliza el comando /menu\n"
                          "Para obtener ayuda personalizada contacta con el desarrollador:\n"
                          "danifort1205@gmail.com\n")








@bot.message_handler(commands=['password'])
def handle_password(message):
    if message.text == f'/password {PASSWORD}':
        authorized_users.append(message.from_user.id)
        bot.reply_to(message, "✅ Contraseña correcta. ¡Bienvenido! 🎉")
        bot.reply_to(message, mensaje_principal)
    else:
        bot.reply_to(message, "❌ Contraseña incorrecta.")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id not in authorized_users:
        bot.reply_to(message, mensaje_no_autorizado)
        return
    bot.reply_to(message, mensaje_principal)

@bot.message_handler(commands=['menu'])
def send_menu(message):
    if message.from_user.id not in authorized_users:
        bot.reply_to(message, mensaje_no_autorizado)
        return
    bot.reply_to(message, "📋 Menú:\n"
                          "/nuevo_aviso (link a tu anuncio) - 🕵️‍♂️ Buscar productos\n"
                          "/help - 🆘 Obtener ayuda\n")

@bot.message_handler(commands=['help'])
def send_help(message):
    if message.from_user.id not in authorized_users:
        bot.reply_to(message, mensaje_no_autorizado)
        return
    bot.reply_to(message, mensaje_ayuda)

# cuando el usuario pone /id le envia su chat id
@bot.message_handler(commands=['id'])
def send_id(message):
    bot.reply_to(message, f"Tu ID es: {message.from_user.id}")


@bot.message_handler(commands=['nuevo_aviso'])
def handle_nuevo_aviso(message):
    if message.from_user.id not in authorized_users:
        bot.reply_to(message, mensaje_no_autorizado)
        return
    
    if link_valido(message.text):
        añadir_producto(message.from_user.id, message.text)
        bot.reply_to(message, "✅ Link registrado con éxito, ¡te avisaremos de los nuevos anuncios! 📢")

    else:
        bot.reply_to(message, "❌ El link no es válido. Por favor, introduce un link de Wallapop válido.")
        return


if __name__ == '__main__':
    bot.polling(non_stop=True)