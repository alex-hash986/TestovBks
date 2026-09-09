import pandas as pd


def load_clients_data(filepath: str = "clients.xlsx") -> list[dict]:
    # Читаем Excel, гарантируя строковый тип для телефонов и дат
    df = pd.read_excel(filepath, dtype={"Номер телефона": str, "Дата": str})
    return df.to_dict(orient="records")


if __name__ == "__main__":
    clients = load_clients_data()
    for client in clients:
        print(client)