import pandas as pd
from tabulate import tabulate

data = [
    ["Jacksonville", "January", 13],
    ["Jacksonville", "February", 23],
    ["Jacksonville", "March", 38],
    ["Jacksonville", "April", 5],
    ["Jacksonville", "May", 34],
    ["El Paso", "January", 20],
    ["El Paso", "February", 6],
    ["El Paso", "March", 26],
    ["El Paso", "April", 2],
    ["El Paso", "May", 43]
]


def CreateDataFrame(data: list[list[object, object, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["city", "month", "temperature"])


weather = CreateDataFrame(data)


def PivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    month_order = ["January", "February", "March", "April", "May"]
    weather['month'] = pd.Categorical(
        weather['month'], categories=month_order, ordered=True)
    return weather.pivot(index='month', columns='city', values='temperature')


result = PivotTable(weather)
print(tabulate(result, headers='keys', tablefmt='grid',
      stralign='center', numalign='center'))

# weather.pivot(index='month', columns='city', values='temperature')
# Строка кода выше позволяет переделать таблицу таким образом, что в результате выводится сравнительная таблица температур по двум городам по месяцам

# month_order = ["January", "February", "March", "April", "May"]
# weather['month'] = pd.Categorical(
# weather['month'], categories=month_order, ordered=True)
# Строки кода, расположенные выше, позволяют отсортировать значения месяцев по порядку их следования
