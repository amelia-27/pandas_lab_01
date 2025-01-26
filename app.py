import pandas as pd

s = pd.Series([42, 21, 7, 3.5])
print(s)

df = pd.DataFrame({'age':18, 'name':['Alice', 'Carlos', 'Smithy'], 'cardio':[60, 70, 80]})
print(df)

print(df[df['cardio']>60])
#from last example

df.loc[1: 'age'] = 16
print(df)

df['friend'] = 'Donnie'
print(df)