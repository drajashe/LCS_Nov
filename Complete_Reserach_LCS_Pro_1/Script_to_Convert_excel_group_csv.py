import pandas as pd

df=pd.read_excel("data/excel.xlsx")
gk=df.groupby('Name')
print(gk.first())
