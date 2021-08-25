import pandas as pd
import random
from datetime import datetime


def create_sample_df(now: datetime)-> pd.DataFrame:

    FOODS = [
        {'name':'クリスマスケーキ', 'price':3000},
        {'name':'ブッシュドノエル', 'price':2000},
        {'name':'フライドチキン', 'price':1000},
        {'name':'ローストチキン', 'price':2000},
        {'name':'ローストビーフ', 'price':2000},
        {'name':'ピザ', 'price':1000},
        {'name':'ポットパイ', 'price':500},
        {'name':'寿司', 'price':5000},
        {'name':'オードブル', 'price':3000},
        {'name':'シャンパン', 'price':2000},
        {'name':'スパークリングワイン', 'price':2000},
        {'name':'シャンメリー', 'price':500},
    ]

    row_cnt = random.randint(5, 20)
    items = [random.choice(FOODS) for _ in range(row_cnt)]
    df = pd.DataFrame({
        'name':[d.get('name') for d in items],
        'price':[d.get('price') for d in items],
        'count':[random.randint(1, 5) for _ in range(row_cnt)],
        'put_datetime':[now.strftime('%Y-%m-%d %H:%M:%S') for _ in range(row_cnt)]
    })

    df = df[['name', "price", 'count', 'put_datetime']]
    print("sample dataframe created!")
    print(df)

    return df
