import pyodbc


class Connector:
    def __init__(self, database_url):
        # def __init__(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=EPBYMINL005C\SQLEXPRESS;'
                              'Database=TRN;'
                              'Trusted_Connection=yes;')
        self.cursor = conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
