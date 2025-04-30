import pandas as pd 
import sqlalchemy as sa
db_url = 'mssql+pyodbc://DESKTOP-1CVG1C6/master?driver=SQL+Server'
engine = sa.create_engine(db_url) #write to sql server
connection = engine.connect() #read from sql server
df = pd.read_sql(sa.text('select *,round(isnull((lag(CurrentQuota) over(order by (BusinessEntityID))),0),1) from lag'), con=connection)
vf = pd.read_sql(sa.text('select *from lag'),con=connection)
vf['CurrentQuota_lag']=vf['CurrentQuota'].shift(1)
vf['CurrentQuota_lag']=vf['CurrentQuota'].shift(-1)
bf=pd.read_sql(sa.text('SELECT EmpId,EmpName,BirthDate FROM EmpBirth where month(BirthDate)=5 and day(BirthDate) between 7 and 15'), con=connection)
bf
cf=pd.read_sql(sa.text('SELECT EmpId,EmpName,BirthDate FROM EmpBirth'), con=connection)
cf=cf[(cf['BirthDate'].dt.month==5) & ((cf['BirthDate'].dt.day>=7) & (cf['BirthDate'].dt.day<=15))]
cf
wf=pd.read_sql(sa.text("SELECT MName , AName , Roles FROM Movie where MName in(select MName from Movie where Roles = 'Actor' and (AName ='Amitabh' or AName = 'Vinod')group by MName having count(MName)>1)"), con=connection)
filtered = wf[(wf['Roles'] == 'Actor') & (wf['AName'].isin(['Amitabh', 'Vinod']))]
counts = filtered.groupby('MName')['AName'].nunique().reset_index()
movies_with_both = counts[counts['AName'] > 1]['MName']
result = wf[wf['MName'].isin(movies_with_both)]
print(result)
tf = pd.read_sql(sa.text('select *from PQ'),con=connection)
tf['Name'] = tf['Name'].astype(str)
tf['Typed'] = tf['Typed'].astype(str)
finalresult = tf.groupby('ID').agg({'Name': 'max', 'Typed':'max'})
finalresult
tuf = pd.read_sql(sa.text('select *from NthHighest'),con=connection)
yy=tuf['Salary'].max()
yy
tuf[tuf['Salary']<yy].max()
tif = pd.read_sql(sa.text('select *from list'),con=connection)
tif['osib']=tif['ID'].cumsum(axis=0)
tif
rty=pd.read_sql(sa.text('select *from TestMax'),con=connection)
rty.pivot_table(columns='Year1').max(axis=0)
top=pd.read_sql(sa.text('select * from [dbo].[EmpSalaryGreaterManager]'),con=connection)
import pandas as pd

# Sample data
data = {
    'EmpID': [1, 2, 3, 4, 5],
    'EmpName': ['Pawan', 'Dheeraj', 'Isha', 'Joteep', 'Suchita'],
    'EmpSalary': [80000, 70000, 100000, 90000, 110000],
    'MgrID': [4, 4, 4, None, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Merge employee DataFrame with itself to get manager info
df_merged = df.merge(
    df[['EmpID', 'EmpName', 'EmpSalary']], 
    left_on='MgrID', 
    right_on='EmpID', 
    how='left', 
    suffixes=('', '_Manager')
)

# Filter where employee salary > manager salary
result = df_merged[df_merged['EmpSalary'] > df_merged['EmpSalary_Manager']]

# Select and display relevant columns
final_result = result[['EmpID', 'EmpName', 'EmpSalary', 'MgrID', 'EmpName_Manager', 'EmpSalary_Manager']]
print(final_result)
import pandas as pd

# Department data
departments = pd.DataFrame({
    'DeptID': [1, 2, 3],
    'DeptName': ['Finance', 'IT', 'HR']
})

# Employees data
emps = pd.DataFrame({
    'EmpID': [101, 111, 102, 103, 104, 105, 106, 107, 108],
    'EmpName': ['Isha', 'Esha', 'Mayank', 'Ramesh', 'Avtaar', 
                'Gopal', 'Krishna', 'Suchita', 'Ranjan'],
    'DeptID': [1, 1, 1, 2, 2, 3, 3, 3, 3],
    'EmpSalary': [7000, 8970, 8900, 4000, 9000, 17000, 1000, 7000, 17900]
})

# Rank salaries within each department
emps['Rank'] = emps.groupby('DeptID')['EmpSalary'].rank(method='dense', ascending=False)

# Filter for second highest salary (rank 2)
second_highest = emps[emps['Rank'] == 2]

# Join with department names
result = second_highest.merge(departments, on='DeptID')

# Select and display relevant columns
final_result = result[['EmpID', 'EmpName', 'DeptID', 'DeptName', 'EmpSalary']]
print(final_result)
import pandas as pd
df = pd.read_csv('tackoverflow_qa.csv')
df.head()
#Find all questions that were created before 2014
df['creationdate']=pd.to_datetime(df['creationdate'])
df[df['creationdate'].dt.year<2014]
#Find all questions with a score more than 50
df[df['score']>50]
#Find all questions with a score between 50 and 100
df[(df['score']>50) & (df['score']<100)]
#Find all questions answered by Scott Boston
df[df['ans_name']=='Scott Boston'].index
#Find all questions answered by the following 5 users
df.iloc[5392:5397]
#Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
criteria2=df[(df['ans_name']=='unutbu')&(df['score']<5)]
criteria1
criteria1 = df[
    (df['creationdate'].dt.year == 2014) &
    (df['creationdate'].dt.month > 3) &
    (df['creationdate'].dt.month < 10) &
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5)
]
criteria1
#Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
df[((df['score']>5) & (df['score']<10))|(df['viewcount']>10000)]
# Find all questions that are not answered by Scott Boston
df[df['ans_name']!='Scott Boston']
#PassengerId: Id of every passenger.
#Survived: Indication whether passenger survived. 0 for yes and 1 for no.
#Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
#Name: Name of passenger.
#Sex: Gender of passenger.
#Age: Age of passenger in years.
#SibSp: Number of siblings or spouses aboard.
#Parch: Number of parents or children aboard.
#Ticket: Ticket number of passenger.
#Fare: Indicating the fare.
#Cabin: Cabin number of passenger.
#Embarked: Port of embarkation.
titanic_df = pd.read_csv('titanic (1).csv')
titanic_df.head()
#Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
titanic_df[(titanic_df['Sex']=='female')&(titanic_df['Pclass']==1)&(titanic_df['Age']>20)&(titanic_df['Age']<30)]
#Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
titanic_df[titanic_df['Fare']>100]
#Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
titanic_df[(titanic_df['Survived']==0)&(titanic_df['SibSp']==0)]
#Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
titanic_df[(titanic_df['Embarked']=='C')&(titanic_df['Fare']>50)]
#Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
titanic_df[(titanic_df['SibSp']>0)|(titanic_df['Parch']>0)]
#Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
titanic_df[(titanic_df['Age']==15)|(titanic_df['Survived']==1)]
#elect Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
import numpy as np
titanic_df['Cabin'].fillna(0,inplace=True)
titanic_df[(titanic_df['Fare']>200)&(titanic_df['Cabin']!=0)]
#Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
titanic_df[titanic_df['PassengerId']/2!=0]
#Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
titanic_df['Ticket'].unique()
unique_tickets_df = titanic_df[titanic_df['Ticket'].duplicated(keep=False)]
unique_tickets_df
br=titanic_df.groupby('Ticket').agg('count')
br[br['PassengerId']==1]
#Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
# Filter passengers with 'Miss' in name and Pclass == 1
miss_class1_df = titanic_df[
    titanic_df['Name'].str.contains('Miss', case=False) & 
    (titanic_df['Pclass'] == 1)
]
miss_class1_df


