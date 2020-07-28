import sqlite3 as sql

database = sql.connect("record.db")

database.execute("""CREATE TABLE transactions (date ntext, time NTEXT, name NTEXT, reason VARCHAR(10), amount INT)""" )

database.commit()