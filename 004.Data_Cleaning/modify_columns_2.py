import pandas as pd

data = [
    ["Jack", 19666],
    ["Piper", 74754],
    ["Mia", 62509],
    ["Ulysses", 54866]
]


def CreateDataFrame(data: list[list[object, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["name", "salary"])


employees = CreateDataFrame(data)


def ModifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.salary *= 2
    return employees


result = ModifySalaryColumn(employees)
print(result)

#  employees.salary *= 2 - данная строка кода позволяет удвоить все значения в столбце salary (2 способ)
