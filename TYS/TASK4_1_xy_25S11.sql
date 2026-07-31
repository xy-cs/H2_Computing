#Task 4.1
import sqlite3

connection = sqlite3.connect("school.db")
connection.execute("DROP TABLE IF EXISTS People")
connection.execute("CREATE TABLE 'People' ("+
                   "'PersonID'	INTEGER PRIMARY KEY AUTOINCREMENT,"+
                   "'FullName'	TEXT NOT NULL,"+
                   "'DateOfBirth'	TEXT NOT NULL,"+
                   "'ScreenName'	TEXT NOT NULL,"+
                   "'IsAdult'	INTEGER NOT NULL)"
                   );
connection.close()