import re
from pythonFiles.a_persistence.db_connection import DBConnection
from pythonFiles.b_functions.d_current_user import *

class UserMapper:


    @classmethod
    def login_request(cls, username, password):

        try:
            myCursor = DBConnection.connect_to_DB()

        except:
            return "connection_failed"

        else:

            ################################################################################################################
            # !!! FOLLOWING COMMAND IS NOT PROTECTED from SQL INJECTION:

            # sql_SELECT_Command = f"SELECT username, password FROM user
            #                       WHERE username = '{username}' AND password = '{password}'"

            # myCursor.execute(sql_SELECT_Command)
            ################################################################################################################

            try:
                sql_SELECT_Command = "SELECT id, username, password FROM mybudget_user WHERE username = %s AND password = %s"
                allValues = (username, password)
                myCursor.execute(sql_SELECT_Command, allValues)
                print("Sql command executed")
                list_with_tuple_with_userdata = myCursor.fetchall()

                print("Data fetched (see data below): ")
                print(list_with_tuple_with_userdata)

                if len(list_with_tuple_with_userdata) == 0:
                    return "credentials_failed"
                else:

                    tuple_with_user_data = list_with_tuple_with_userdata[0]

                    list_with_user_data = []

                    for ui in tuple_with_user_data:
                        list_with_user_data.append(ui)


                    set_current_user(list_with_user_data)


            except Exception:
                return "select_command_failed"

            finally:
                print("Committing to and closing DB")
                DBConnection.commit_and_close_DB()
                print("DB is closed")


        return "succes"

    pass



    @classmethod
    def create_user(cls, username, password):

        try:
            myCursor = DBConnection.connect_to_DB()

        except:
            return "connection_failed"

        else:
            try:
                sql_INSERT_Command = "INSERT INTO mybudget_user (username, password) VALUES (%s, %s)"
                allValues = (username, password)
                myCursor.execute(sql_INSERT_Command, allValues)

            except Exception as ex:
                error_message = str(ex)

                if re.search("^1062..23000.:.Duplicate.entry", error_message):
                    return "username_exists"
                else:
                    return "insert_command_failed"

            finally:
                DBConnection.commit_and_close_DB()
                print("DB is closed")

        return "succes"



    @classmethod
    def is_username_in_db(cls, username):

        try:
            myCursor = DBConnection.connect_to_DB()

            try:
                print("Select command:")
                sql_SELECT_Command = "SELECT username FROM mybudget_user WHERE username = %s"
                allValues = (username,)
                myCursor.execute(sql_SELECT_Command, allValues)
                print("Sql command executed")
                listWithUserdata = myCursor.fetchall()

                print("Data fetched (see data below): ")
                print(listWithUserdata)
                print(len(listWithUserdata))

                if len(listWithUserdata) == 0:
                    return "no_username"

            except Exception:
                return "no_username"

            finally:
                print("Committing to and closing DB")
                DBConnection.commit_and_close_DB()
                print("DB is closed")
        except:
            print("connection failed")
            return "connection_failed"


