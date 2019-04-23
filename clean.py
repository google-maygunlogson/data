import pandas as pd 
import numpy  as np
df = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2018.csv')

# df = df.fillna(0)
for col in df:
    df[col] =df[col].replace('nan',0)
    if np.issubdtype(df[col].dtype, np.number) :
        df[col] =df[col].replace('nan',0)
    else:
        df[col] =df[col].replace('nan','0')

df.to_csv('pbp.csv', sep=',', encoding='utf-8') 