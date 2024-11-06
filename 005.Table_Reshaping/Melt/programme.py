import pandas as pd
from tabulate import tabulate

data = [
    ["Umbrella", 417, 224, 379, 611],
    ["Sleeping Bag", 800, 936, 93, 875]
]


def CreateDataFrame(data: list[list[object, int, int, int, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["product", "quarter_1", "quarter_2", "quarter_3", "quarter_4"])


report = CreateDataFrame(data)


def MeltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name='quarter', value_name='sales')


result = MeltTable(report)
print(tabulate(result, headers='keys', tablefmt='grid',
      stralign='center', numalign='center', showindex=False))

# pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name=['quarter'], value_name=['sales'])
# Строка кода, расположенная выше, позволяет скомпоновать все значения quarters в один столбец quarter
# Иными словами, данное действие напоминает транспонирование матрицы
