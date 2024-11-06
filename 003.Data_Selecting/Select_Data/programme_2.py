import pandas as pd

data = [
    [101, "Ulysses", 13],
    [53, "William", 10],
    [128, "Henry", 6],
    [3, "Henry", 11]
]


def CreateDataFrame(data: list[list[int, object, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["student_id", "name", "age"])


students = CreateDataFrame(data)


def SelectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101][['name', 'age']]


result = SelectData(students)
print(result)

# return students.loc[students["student_id"] == 101][['name', 'age']] - 2 способ вернуть строчку с заданным id
