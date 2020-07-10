from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.db')
table_names = engine.table_names()
#print(engine)
#print(table_names)
con = engine.connect()
result = con.execute('SELECT * from Album')
df = pd.DataFrame(result.fetchall())
df.columns = result.keys()
print(df.head())

