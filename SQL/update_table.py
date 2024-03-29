import sqlite3
import sys
import pandas as pd

recip = pd.read_csv('ingredients.csv')
connection = sqlite3.connect("recipe.db")

curs = connection.cursor()
recip.to_sql('recip', connection, if_exists = 'append', index = False)


#sql_command = """ALTER TABlE ____ ADD COLUMN ____ TEXT;"""

#sql_command = """ALTER TABLE _____
#    rename column (old / current name) to (new name)"""

#EXECUTE
#curs.execute(sql_command)

connection.commit()


#connection.close()
#sql_command = """UPDATE _____(table name) set (column name) = (the specific name you'd like to change) where (Column 2 name) = (the specific one that matches with the name you'd like to change);"""
#curs.execute(sql_command)
#connection.commit()

#sql_command1 = """INSERT into Appliance VALUES ("Blender", "AP2");"""
#sql_command2 = """INSERT into Appliance VALUES ("Air Fryer", "AP3");"""
#sql_command3 = """INSERT into Appliance VALUES ("Microwave", "AP4");"""

#curs.execute(sql_command1)
#curs.execute(sql_command2)
#curs.execute(sql_command3)

connection.commit()

connection.close()

