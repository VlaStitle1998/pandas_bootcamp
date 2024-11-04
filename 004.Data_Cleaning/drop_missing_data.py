import pandas as pd

data = [
    [32, "Piper", 5],
    [217, None, 19],
    [779, "Georgia", 20],
    [849, "Willow", 4]
]


def CreateDataFrame(data: list[list[int, object, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["student_id", "name", "age"])


students = CreateDataFrame(data)


def DropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students_clean = students.dropna(subset=['name'])
    return students_clean


result = DropMissingData(students)
print(result)

# students.dropna(subset=['name']) - данная строка кода позволяет удалить строку с пустым значением None
