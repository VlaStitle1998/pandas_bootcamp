import pandas as pd

data = [
    [1, "Mason", "King", 6],
    [2, "Ava", "Wright", 7],
    [3, "Taylor", "Hall", 16],
    [4, "Georgia", "Thompson", 18],
    [5, "Thomas", "Moore", 10]
]


def CreateDataFrame(data: list[list[int, object, object, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["id", "first", "last", "age"])


students = CreateDataFrame(data)


def RenameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'})


result = RenameColumns(students)
print(result)

# students.rename(columns={'id':'student_id', 'first':'first_name', 'last':'last_name', 'age':'age_in_years'})
# Строка кода выше позволяет переименовать столбцы при помощи словаря(структура данных) (1 способ)
