import sqlite3

createDb = sqlite3.connect('customer1.db')
queryCurs = createDb.cursor()

def createTable():
    queryCurs.execute('''CREATE TABLE customers1(id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT,state TEXT, balance REAL)''')

def addCust(name,street,city,state,balance):
    queryCurs.execute('''INSERT INTO customers1(name,street,city,state,balance) VALUES(?,?,?,?,?)''',(name,street,city,state,balance))
    
    
def main():
    createTable()
    addCust('rohit', 'neeladri', 'bangalore', 'katnataka', 2000)
    addCust('rakesh', 'madivala', 'bangalore', 'katnataka', 10000.80)
    addCust('raghu', 'gottigere', 'bangalore', 'katnataka', 345.67)
    addCust('santhosh', 'chikban', 'bangalore', 'katnataka', 346.77)
    
    createDb.commit()
    queryCurs.execute('SELECT * FROM customers')
    for i in queryCurs:
        print"\n"
        for j in i:
            print j 
            
if __name__=='__main__':main()

'''output:

Traceback (most recent call last):
  File "E:\python\demo2\prg5.py", line 28, in <module>
    if __name__=='__main__':main()
  File "E:\python\demo2\prg5.py", line 15, in main
    createTable()
  File "E:\python\demo2\prg5.py", line 8, in createTable
    queryCurs.execute('''CREATE TABLE customers1(id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT,state TEXT, balance REAL)''')
sqlite3.OperationalError: table customers1 already exists'''
