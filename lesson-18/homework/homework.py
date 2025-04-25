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

