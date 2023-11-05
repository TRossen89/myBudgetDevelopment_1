import mysql.connector


class DBConnection():

    @classmethod
    def connect_to_DB(cls):

        print("Connecting to database...")

        cls.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="/TRosseneri1899",
            database="mybudgetdev"
        )

        myCursor = cls.mydb.cursor()
        print("Connected!")

        return myCursor

    @classmethod
    def commit_and_close_DB(cls):

        cls.mydb.commit()
        cls.mydb.close()





"""
print("Inserting username and password into DB...")
sqlInsertCommand = "INSERT INTO user (username, password) VALUES (%s, %s)"

username = "tobias"
password = "123"

allValues = (username, password)
myCursor.execute(sqlInsertCommand, allValues)

mydb.commit()
#myCursor.execute("CREATE TABLE IF NOT EXISTS user (id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(60), password VARCHAR(60))")

print("Username and password inserted!")
mydb.close()
print("DB closed")

"""



