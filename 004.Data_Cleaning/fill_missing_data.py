import pandas as pd

data = [
    ["Wristwatch", None, 135],
    ["Wireless Earbuds", None, 821],
    ["Golf Clubs", 779, 9319],
    ["Printer", 849, 3051]
]


def CreateDataFrame(data: list[list[object, int, int]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["name", "quantity", "price"])


products = CreateDataFrame(data)


def FillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0).astype(int)
    return products


result = FillMissingValues(products)
print(result)

# products["quantity"]=products["quantity"].fillna(0).astype(int) - данная строка кода позволяет заполнить отсутствующие значения нулями
