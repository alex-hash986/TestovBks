import requests


def send_telegram_message(
    bot_token: str, chat_id: str | int, text: str
) -> bool:
  """Отправляет текстовое сообщение в Telegram через официальный Bot API."""
  url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
  payload = {"chat_id": chat_id, "text": text}

  try:
    response = requests.post(url, json=payload, timeout=10)
    data = response.json()

    if data.get("ok"):
      print(f"Сообщение успешно отправлено в чат {chat_id}")
      return True
    else:
      print(f"Ошибка от Telegram API: {data.get('description')}")
      return False

  except Exception as e:
    print(f"Сетевая ошибка при отправке: {e}")
    return False


if __name__ == "__main__":
  # Тестовый блок для изолированной проверки модуля
  from config import BOT_TOKEN, TELEGRAM_CHAT_ID

  print("Тестовая отправка сообщения...")
  send_telegram_message(
      bot_token=BOT_TOKEN,
      chat_id=TELEGRAM_CHAT_ID,
      text="Проверка связи из модуля telegram_sender!",
  )