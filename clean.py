import pandas as pd 
df = pd.read_csv('pbp_reg_2018.csv')

for col in df:
    df[col] = df[col].fillna(0)
    # print( len(df[col].unique()) )

df.to_csv('pbp_reg_2018.csv', sep=',', encoding='utf-8')