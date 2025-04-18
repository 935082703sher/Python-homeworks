import sqlite3
with sqlite3.connect('SherzodbekK.db') as connection:
    cursor =connection.cursor()
    query =' create table Roster( Name varchar(50), Species varchar(50), Age int )'
    query1 ="insert into Roster values ( 'Benjamin Sisko'	,'Human',	40 )"
    query2 ="insert into Roster values ( 'Jadzia Dax'	,'Trill',	300 )"
    query3 ="insert into Roster values ( 'Kira Nerys'	,Bajoran',	29 )"
    results =cursor.execute(query)
    r=cursor.execute(query1)
    r2=cursor.execute(query2)
    r3=cursor.execute(query3)
with sqlite3.connect('SherzodbekK.db') as connection:
    cursor =connection.cursor()
    query="UPDATE Roster SET Name= 'Ezri Dax' Where Age=300"
