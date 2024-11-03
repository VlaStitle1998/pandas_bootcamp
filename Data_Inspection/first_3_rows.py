import pandas as pd

data = [
    [3, "Bob", "Operations", 48675],
    [90, "Alice", "Sales", 11096],
    [9, "Tatiana", "Engineering", 33805],
    [60, "Annabelle", "Information Technology", 37678],
    [49, "Jonathan", "Human Resources", 23793],
    [43, "Khaled", "Administration", 40454]
]


def CreateDataFrame(data: list[list[int, object, object, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["employee_id", "name", "department", "salary"])


def SelectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


employees = CreateDataFrame(data)
result = employees.head(3)
print(result)

# .head(3) - команда, которая выводит первые три строки DataFrame
