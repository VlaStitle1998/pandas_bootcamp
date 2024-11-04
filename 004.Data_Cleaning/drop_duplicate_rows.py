import pandas as pd

data = [
    [1, "Ella", "emily@example.com"],
    [2, "David", "michael@example.com"],
    [3, "Zachary", "sarah@example.com"],
    [4, "Alice", "john@example.com"],
    [5, "Finn", "john@example.com"],
    [6, "Violet", "alice@example.com"]
]


def CreateDataFrame(data: list[list[int, object, object]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["customer_id", "name", "email"])


customers = CreateDataFrame(data)


def DropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers


result = DropDuplicateEmails(customers)
print(result)

# customers.drop_duplicates - данная строка код позволяет удалить строчки с совпадениями
# subset='email' - данная строка кода позволяет выставить фильтр по столбцу email
# keep='first' - данная строка кода позволяет удалить второе значение, а первое сохранить как уникальное
# inplace=True - данная строка кода позволяет изменять исходный DataFrame без создания нового
