import pandas as pd
from datetime import datetime, timedelta

# Текущая дата для проверки совпадений
today = datetime.now().date()

data = [
    {
        "Имя": "Иван Иванов",
        "Номер телефона": "+79991112233",
        "Сумма": 15000,
        "Дата": today.strftime("%Y-%m-%d"),  # Оплата сегодня
    },
    {
        "Имя": "Петр Сидоров",
        "Номер телефона": "+79992223344",
        "Сумма": 8500,
        "Дата": (today + timedelta(days=1)).strftime("%Y-%m-%d"),  # Оплата завтра
    },
    {
        "Имя": "Анна Смирнова",
        "Номер телефона": "+79993334455",
        "Сумма": 12000,
        "Дата": (today - timedelta(days=2)).strftime("%Y-%m-%d"),  # Просрочено
    },
]

df = pd.DataFrame(data)
df.to_excel("clients.xlsx", index=False)
print("Файл clients.xlsx успешно создан!")