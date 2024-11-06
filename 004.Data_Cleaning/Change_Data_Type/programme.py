import pandas as pd

data = [
    [1, "Ava", 6, 73.0],
    [2, "KAte", 15, 87.0]
]


def CreateDataFrame(data: list[list[int, object, int, float]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["student_id", "name", "age", "grade"])


students = CreateDataFrame(data)


def ChangeDataType(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade': int})


result = ChangeDataType(students)
print(result)

# students.astype({'grade':int}) - данная строка кода позволяет изменить тип данных с float на int
