import pandas as pd

data = [
    [846, "Mason", 21, "Forward", "Real Madrid"],
    [749, "Riley", 30, "Winger", "Barcelona"],
    [155, "Bob", 28, "Striker", "Manchester United"],
    [583, "Isabella", 32, "Goalkeeper", "Liverpool"],
    [388, "Zachary", 24, "Midfielder", "Bayern Munich"],
    [883, "Ava", 23, "Defender", "Chelsea"],
    [355, "Violet", 18, "Striker", "Juventus"],
    [247, "Thomas", 27, "Striker", "Paris Saint-Germain"],
    [761, "Jack", 33, "Midfielder", "Machester City"],
    [642, "Charlie", 36, "Center-back", "Arsenal"]
]


def createDataFrame(data: list[list[int, object, int, object, object]]) -> pd.DataFrame:
    return pd.DataFrame(data, columns=["player_id", "name", "age", "position", "team"])


players = createDataFrame(data)
print(players)


def getDataFrameSize(players: pd.DataFrame) -> list[int]:
    return [players.shape[0], players.shape[1]]


result = getDataFrameSize(players)
print('\n', result)

# return [players.shape[0], players.shape[1]] - данная строка кода возвращает ответ в виде массива
# print('\n', result) - данная строка кода выводит массив с новой строки
