import telebot

API_KEY = 'AQUÍ_VA_TU_API_KEY_DE_TELEGRAM'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'ayuda'])
def enviar_bienvenida(mensaje):
    bot.reply_to(mensaje, "Hola, soy Estefany González, tu asistente brutal. ¿En qué puedo ayudarte hoy?")

@bot.message_handler(func=lambda m: True)
def responder_mensajes(mensaje):
    respuesta = f"No entendí bien, pero estoy aprendiendo. Tú dijiste: '{mensaje.text}'"
    bot.reply_to(mensaje, respuesta)

print("Estefany está activa...")
bot.polling()
