from datetime import datetime
import pandas as pd


def get_notifications(filepath: str = 'clients.xlsx') -> list[dict]:
  # Читаем телефон как строку, чтобы не терять плюс или ведущие нули
  df = pd.read_excel(filepath, dtype={'Номер телефона': str})

  # Приводим колонку с датами к типу datetime.date для точного сравнения
  df['Дата_dt'] = pd.to_datetime(df['Дата']).dt.date
  today = datetime.now().date()

  # Отбираем тех, у кого срок сегодня (можно расширить: <= today, если нужны и должники)
  urgent_clients = df[df['Дата_dt'] == today]

  notifications = []
  for _, row in urgent_clients.iterrows():
    # Шаг 3: формируем текст сообщения
    text = (
        f'Здравствуйте, {row["Имя"]}!\n'
        f'Напоминаем о необходимости внести оплату за обучение '
        f'в размере {row["Сумма"]} руб. Срок оплаты: {row["Дата"]}.'
    )
    notifications.append({
        'name': row['Имя'],
        'phone': str(row['Номер телефона']),
        'text': text,
    })

  return notifications


if __name__ == '__main__':
  ready_to_send = get_notifications()
  print(f'Найдено записей для отправки: {len(ready_to_send)}')
  for item in ready_to_send:
    print('---')
    print(f'Получатель: {item["name"]} ({item["phone"]})')
    print(f'Текст:\n{item["text"]}')