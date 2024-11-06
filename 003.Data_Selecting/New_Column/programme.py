import pandas as pd

data = [
    ["Piper", 4548],
    ["Grace", 28150],
    ["Gergia", 1103],
    ["Willow", 6593],
    ["Finn", 74576],
    ["Thomas", 24433]
]


def CreateDataFrame(data: list[list[object, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["name", "salary"])


employees = CreateDataFrame(data)


def CreateBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bonuses = employees["salary"] * 2
    employees.insert(2, "bonus", bonuses)
    return employees


result = CreateBonusColumn(employees)
print(result)

# bonuses = employees["salary"] * 2 - данная строка удваивает значения столбца salary и присваивает их новой переменной bonuses
# employees.insert(2, "bonus", bonuses) - данная команда создает новый столбец bonus со значениями bonuses и вставляет его справа, после столбца salary
