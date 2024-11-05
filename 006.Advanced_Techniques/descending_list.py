import pandas as pd
from tabulate import tabulate

data = [
    ["Tatiana", "Snake", 98, 464],
    ["Khaled", "Giraffe", 50, 41],
    ["Alex", "Leopard", 6, 328],
    ["Jonathan", "Monkey", 45, 463],
    ["Stefan", "Bear", 100, 50],
    ["Tommy", "Panda", 26, 349]
]


def CreateDataFrame(data: list[list[object, object, int, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["name", "species", "age", "weight"])


animals = CreateDataFrame(data)


def FindHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals.weight > 100].sort_values('weight', ascending=False)[['name']]


result = FindHeavyAnimals(animals)
print(tabulate(result, headers='keys', tablefmt='grid',
      stralign='center', numalign='center', showindex=False))

# animals[animals.weight > 100].sort_values('weight', ascending=False)[['name']]
# Строка кода, расположенная выше, позволяет вывести список животных, вес которых превышает 100 кг, и расположить их имена по убыванию веса
