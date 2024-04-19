import requests

def enviar_mensaje_telegram(token, chat_id, texto):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}"
    requests.get(url)

