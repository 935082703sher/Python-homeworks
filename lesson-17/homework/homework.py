import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
df.rename(columns={'First Name':'first_name','Age':'age'},inplace=True)
a=df.head(3)
s=df['age'].mean()
print(df, s, a)
df[['first_name','City']]
import numpy as np
df['Salary']=np.random.rand(len(df))*100
df.describe()
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
sale={'Month':['jan','feb','mar','apr'],'Sales':[5000,6000,7500,8000],'Expenses':[3000,3500,4000,4500]}
rf=pd.DataFrame(sale)
rf.describe()
rf['Expenses'].mean()
rf['Expenses'].min()
rf['Expenses'].max()
rf['Sales'].mean()
rf['Sales'].min()
rf['Sales'].max()
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
bros={'Category':['Rent','utilities','groceries','entertainment'],'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]}
vf=pd.DataFrame(bros)
vf[['January'	,'February'	,'March',	'April']].max(axis=1) 
vf[['January'	,'February'	,'March',	'April']].mean(axis=1) 
vf[['January'	,'February'	,'March',	'April']].min(axis=1) 
vf.set_index('Category').mean(axis=1)
