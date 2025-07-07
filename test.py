import pandas as pd

data = pd.read_csv('data/cc.csv')

for index, row in data.iloc[::-1].iterrows():
    print(f"x: {row['x']}, y: {row['y']}, level: {row['level']}")