import mysql.connector


class DatabaseOperations:

  def __init__(self):
    myconn = mysql.connector.connect(
      host="localhost",
      user="root",
      password="kanpur",
      # host="192.168.7.188",
      # user="devesh",
      # password="mishra@123",
      database="project",
      auth_plugin='mysql_native_password'
    )
    self.conn = myconn
    self.cursor = myconn.cursor()
  def getQuestionsFromDatabase(self, tableName):

    query="select * from " + tableName
    self.cursor.execute(query)
    myresult = self.cursor.fetchall()
    # for row in myresult:
    #   print(row)
    return myresult

  def closeConnetion(self):
    self.cursor.close()
    self.conn.close()


# databaseConnection = DatabaseOperations()
# dataAll = databaseConnection.getQuestionsFromDatabase("demo")
