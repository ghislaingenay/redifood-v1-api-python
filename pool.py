import sqlite3

class Pool:
  connection = None
  
  def __init__(self):
    pass
  
  def __str__(self) -> str:
    pass
  
  def connect(self):
    try:
      self.connection = sqlite3.connect('db.sqlite3')
    except sqlite3.Error as e:
      print(e)
    finally:
      print('Connection to database established')
    
  def query(self, sql: str):
    self.connect()
    with self.connection.cursor() as cursor:
      cursor.execute(sql)
      self.connection.commit()
      return cursor
