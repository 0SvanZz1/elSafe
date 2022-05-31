import sqlite3
import sys
from elsafe.enums import db, errors

def initConnection():
    """Creates a SQLite3 database
    
    Returns
    -------
    Connection, None
        SQLite database connection object
    Exception, None (default is None)
        Exception class
    """
    try:
        connection = sqlite3.connect('kdb.db')
    except Exception as e:
        return None, e
    return connection, None

def getConnection():
    """Gets the database connection
    
    If no database is found, a new database will be created.
    
    Returns
    -------
    Connection, None
        SQLite database connection object
    """
    connection, e = initConnection()

    if connection == None:
        print("{error_message}. Error Message: {exception_message}".format(
            error_message=errors.ErrorMessages.schemaCreationError.value,
            exception_message=e)
        )
        sys.exit(1)

    return connection

def createSchema():
    """Creates the database schema"""
    connection = getConnection()

    cursor = connection.cursor()

    cursor.execute(db.CreateStatements.CreateTableKeys.value)

def updateDatabase(args, multiData=None):
    """Updates table 'keys' from the database
    
    Parameters
    ----------
    args : tuple
        Values for db insertion
    multiData : bool, optional (default is None)
        Flag used to consider argument `args` as an array of tuples
    """
    connection = getConnection()

    cursor = connection.cursor()

    if multiData:
        cursor.executemany(db.InsertStatements.InsertTableKeys.value, args)
    else:
        cursor.execute(db.InsertStatements.InsertTableKeys.value, args)

    connection.commit()