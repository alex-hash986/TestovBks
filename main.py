import time
from config import BOT_TOKEN, EXCEL_PATH, TELEGRAM_CHAT_ID
from notifier import get_notifications
import schedule
from telegram_sender import send_telegram_message


def job():
  print("\n[Планировщик] Запуск проверки базы...")
  notifications = get_notifications(EXCEL_PATH)
  print(f"Записей к отправке: {len(notifications)}")

  for item in notifications:
    print(f"Отправка для: {item['name']}...")
    send_telegram_message(
        bot_token=BOT_TOKEN, chat_id=TELEGRAM_CHAT_ID, text=item["text"]
    )
  print("[Планировщик] Проверка завершена.")


def run():
  # 1. Разовый запуск сразу при старте скрипта для проверки
  job()

  # 2. Настройка ежедневного расписания
  TARGET_TIME = "10:00"  # Можно изменить на нужное время (например, "09:00" или "18:00")
  schedule.every().day.at(TARGET_TIME).do(job)

  print(f"\nСкрипт запущен в режиме демона. Проверка настроена на {TARGET_TIME}.")
  print("Для остановки нажмите Ctrl+C.\n")

  # 3. Бесконечный цикл ожидания наступления времени
  while True:
    schedule.run_pending()
    time.sleep(30)  # Спим 30 секунд между проверками таймера


if __name__ == "__main__":
  try:
    run()
  except KeyboardInterrupt:
    print("\nРабота планировщика остановлена пользователем.")