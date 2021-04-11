# Name: Data base class contorler ( db )
# Main Job: This claass should be called whenever you want to read or write to the database
#
# Author: Ali Albahrani
# Craated Date: 30 March 2021
# Version: 1.0.0
# ClassID# 1000

# Class Usage
#   1. Call ConnectToDB function to establish the connection and save the return value of it.
#   2. Use the the return value, if not err, to send your sql either by calling SendSQL or InsertSQL funcions.
#   3. Cloase the connection if you are done using the CloseConnection function

# Database Paramters
#   Add the database paramters in the func_ConnectToDB funcion.

import mysql.connector as mysql
from austruckie.ErrorReporting import ausError as Err

# Those constent will be return by the function. You can use them to check the respond of the class's funcions
db_OK_RESPOND:str = "OK"
db_NO_DATA_RESPOND:str = "No Data"

# Establish Connection to the database
def func_ConnectToDB():
    # Return: the db connection that can be used to call the other class function OR ErrorReporting object on error
    # mysql://b89f7ac9ae97e7:12576c53@us-cdbr-east-03.cleardb.com/heroku_2c359834c332ed6?reconnect=true
    try:
        mydb = mysql.connect(
        host="us-cdbr-east-03.cleardb.com",
        user="b89f7ac9ae97e7",
        password="12576c53",
        database="heroku_2c359834c332ed6"
        )
        return mydb
    except:
        return Err(1001, "Database Conneciton", "Problem in the connection to database parameters, Please, make sure you supply the correct database parameters and the SQL server is running.")

# This function simply cut the connection to the database. please used it when you done.
def func_CloseConnection(connection):
    if (connection.is_connected()):
        connection.close()
    return True

# Main SQL request function that will return the result for your SQL statment
# NOTE: Use this function for all SQL except INSERT
def func_SendSQL(myDBin, SQLStatment:str, parameters={}, returnDate=True, returnColumns=False):

    #   -----------------------------------
    # parameters:
    #   myDBin: The return object from the 'ConnectToDB' funcion of this class. This object is must

    #   SQLStatmetn:str, a simple string that tell what is the SQL statment you want to send. The SQL statment must
    #       fallow this Templete "SELECT [whatever] FROM [Whaterver] WHERE [VAR] = %(varName)s AND ... "
    #       This format is to prevent SQL injection secrity issue

    #   parameters:dic, a dictionary array that will map the vars in SQLStatment paramters to thier value.
    #       E.g. SQLStatmetn = "SELECT * FROM `employee` WHERE `empName` like %(inEmpName)s"
    #       para = {"inEmpName": "Ali"}
    #       This is an OPTIONAL parameter

    #   returnData:bool, Is your SQL request will return any data? Normally this is use for the UDPATE sql
    #       True: [default] Yes, this request has some data the should be return
    #       False: No, This request has nothing to return, normaly for UPDATE sqls.
    #       This is an OPTIONAL parameter

    #   returnColumes: bool, Ask the function to return the names of column.
    #       NOTE: This will change the return type to Dic
    #       True: Yes return a dic that have the name of SQL column
    #       False: [default] No, just return an array (list) of data
    #   -----------------------------------
    # Returning:
    #   The return is a 2D  array of all the data found according to the sent SQL statement.
    #   The first index will indicate the Column and the second one will be the record number.
    #   NOTE: If returnColumns is set to TRUE, the return value will be dic, where the column number will be replaced
    #        but the feild name
    #   -----------------------------------

    try:
        # Create a cursor that point to the record aimed to by sql
        mycursor = myDBin.cursor()

        # Exucte the SQL
        mycursor.execute(SQLStatment, parameters)

        if (returnDate):
            # Funcion was asked to return some data
            if returnColumns:
                # Function was asked to return the columns names

                # Get the columns name from the return data
                columnsNames = mycursor.fetchone()
                # Check if we get any column names
                if columnsNames != None:
                    # connected the column names to the return data and return the result
                    row = dict(zip(mycursor.column_names, columnsNames))
                    return row
                else:
                    # No columns names was found, so there is not data to return
                    return db_NO_DATA_RESPOND

            # Return the resulted data
            return mycursor.fetchall()
        else:
            # The SQL statment should not return any data, so for UPDATE, we need to commit the changes
            myDBin.commit()
            return db_OK_RESPOND
    except (mysql.Error, mysql.Warning) as e:
        # Return the error we got
        err = Err(1002, "Database return an error", "The SQL statment submited is not in the correct format or have some error in it. Please check your SQL.")
        err.err_ExtraInfo = e
        return err

# Use this funcion for INSERT sqls only. This funcion can process a single INSERT statement
def func_InsertSQL(Conn, SQLStatment:str, parameters={}, returnID=True):
    #   -----------------------------------
    # Parameters:
    #   Conn: The db connection that can be obtain from SQLConne function of this class
    #   SQLStatment: Same as SQLStatment in the SendSql function of this class.
    #   parameters: Same as SQLStatment in the SendSql function of this class.
    #   returnID: Ask the funcion to return the ID (Primary Key) of the new inserted record
    #       TRUE: [default], Yes, the function should return inserted record ID
    #       FALSE: NO, no need to return that ID
    #   -----------------------------------
    # Return:
    #      Boolean value telling if the SQL run in the right way or not. In Case of the returnID was set to ture,
    #       return value will be str which is the value of the new inserted record in the database
    #   -----------------------------------

    try:
        mycursor = Conn.cursor()
        mycursor.execute(SQLStatment, parameters)
        Conn.commit()

        if returnID:
            lastEnteredID = mycursor.lastrowid
            return [db_OK_RESPOND, str(lastEnteredID)]
        return db_OK_RESPOND

    except (mysql.Error, mysql.Warning) as e:
        # Return the error we got
        err = Err(1002, "Database Insertion error", "The INSERT statment submited had been rejected by the database. Please check your insert statment.")
        err.err_ExtraInfo = e
        return err

    except:
        return Err(1111, "Database Unknown Error. We are sorry but unexpected error had happened. Please try again")

def func_connectionTest():
    cnn = func_ConnectToDB()
    if type(cnn) == Err:
        cnn.func_PrintError()
    else:
        print(cnn)

func_connectionTest()