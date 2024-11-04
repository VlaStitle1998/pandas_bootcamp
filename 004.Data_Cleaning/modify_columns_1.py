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
    return employees.assign(salary=2 * employees['salary'])


result = ModifySalaryColumn(employees)
print(result)

# employees.assign(salary = 2 * employees['salary']) - данная строка кода позволяет удвоить все значения в столбце salary (1 способ)
