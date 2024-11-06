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
    students.columns = ['student_id',
                        'first_name', 'last_name', 'age_in_years']
    return students


result = RenameColumns(students)
print(result)

# student.columns=['student_id', 'first_name', 'last_name', 'age_in_years']
# Строка кода выше позволяет переименовать столбцы (2 способ)
