import pandas as pd

df = pd.read_csv("cast.csv")
num_rows = len(df)
mid = int(num_rows / 2)
df1 = df[:mid]
df2 = df[mid:]
df1.to_csv("cast1.csv", index=False)
df2.to_csv("cast2.csv", index=False)

print(df1.head())
print(df2.head())