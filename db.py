from pymysql import connect

def get_connection():
    connection = connect(
        host = "localhost",
        user = "root",
        password = "@9014855413",
        database = "smart_inventory_db"
    )
    return connection