import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection("localhost", "root", "password", "CreditCards")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occured")


create_table = """
CREATE TABLE IF NOT EXISTS cards (
    CUST_ID  VARCHAR(10) NOT NULL,
    BALANCE  FLOAT(16,6) NULL,
    BALANCE_FREQUENCY FLOAT(10,6) NULL ,
    PURCHASES FLOAT(10,2) NULL ,
    ONEOFF_PURCHASES FLOAT(10,2) NULL ,
    INSTALLMENTS_PURCHASES FLOAT(10,2) NULL ,
    CASH_ADVANCE FLOAT(16,6) NULL ,
    PURCHASES_FREQUENCY FLOAT(16,6) NULL ,
    ONEOFF_PURCHASES_FREQUENCY FLOAT(16,6) NULL ,
    PURCHASES_INSTALLMENTS_FREQUENCY FLOAT(16,6) NULL ,
    CASH_ADVANCE_FREQUENCY FLOAT(10,6) NULL ,
    CASH_ADVANCE_TRX INT NULL ,
    PURCHASES_TRX INT NULL ,
    CREDIT_LIMIT FLOAT(16,6) NULL  ,
    PAYMENTS FLOAT(16,6) NULL  ,
    MINIMUM_PAYMENTS FLOAT(16,6) NULL  ,
    PRC_FULL_PAYMENT FLOAT(16,6) NULL  ,
    TENURE INT NULL
) ENGINE = InnoDB
"""


execute_query(connection, create_table)