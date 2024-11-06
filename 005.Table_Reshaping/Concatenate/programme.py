import pandas as pd
from tabulate import tabulate

data_1 = [
    [1, "Mason", 8],
    [2, "Ava", 6],
    [3, "Taylor", 15],
    [4, "Georgia", 17]
]

data_2 = [
    [5, "Leo", 7],
    [6, "Alex", 7]
]


def CreateDataFrame(data: list[list[int, object, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["student_id", "name", "age"])


df1 = CreateDataFrame(data_1)
df2 = CreateDataFrame(data_2)


def ConcatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])


result = ConcatenateTables(df1, df2)
print(tabulate(result, headers='keys', tablefmt='grid',
      stralign='center', numalign='center', showindex=False))

# pd.concat([df1, df2]) - данная строка кода позволяет соединить две таблицы
# tabulate - библиотека, которая позволяет визуализировать красивую таблицу
# print(tabulate(result, headers='keys', tablefmt='grid', stralign='center', numalign='center', showindex=False))
# Строка кода, расположенная выше, позволяет нарисовать красивую таблицу с названиями и значениями по центру без отображения индексов
