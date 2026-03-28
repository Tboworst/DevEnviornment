def generate_postgres():
    return """  
    import psycopg2

  conn = psycopg2.connect(
      host="localhost",
      database="mydb",
      user="postgres",
      password="password"
  )

  cursor = conn.cursor()



"""
def generate_Sqlite():
    return """
  import sqlite3

  conn = sqlite3.connect("mydb.db")
  cursor = conn.cursor()



"""

