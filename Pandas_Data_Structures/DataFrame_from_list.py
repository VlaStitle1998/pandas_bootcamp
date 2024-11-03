import pandas as pd

student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]


def createDataFrame(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])


df = createDataFrame(student_data)
print(df)


# Данная программа создает DataFrame из списка, содержащего списки с целыми числами, и выводит его на экран
# list[list[int]] - ожидается, что на вход придет список, содержащий списки с целыми числами
# -> pd.DataFrame - указывается, что функция должна возвращать объект DataFrame из библиотеки pandas
