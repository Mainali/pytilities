import sys
from subprocess import check_output
import mysql.connector

def hello() :
	usrname = raw_input('your name please')
	print('hello '+usrname)

def mysqlExport(db=None) :
	db = raw_input('enter database name: ')
	check_output('mysqldump -u root -proot '+db+' > '+db+'.sq',shell=True)
	print('--------------------done-----------------------')

def mysqlImport() :
	db = raw_input('enter database name: ')
	check_output('mysql -u root -proot',shell=True)
	check_output('CREATE DATABASE IF NOT EXISTS '+db+';use '+db+';SET autocommit=0 ; source sos_db.sql ; COMMIT ;exit',shell=True)
	print('--------------------Import successful-----------------------')
	
config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
    }

def mysqlImport2() :
	db = raw_input('enter database name: ')
	con = mysql.connector.connect(config)
	cur = con.cursor()
	cur.execute('CREATE DATABASE IF NOT EXISTS '+db+';use '+db+';SET autocommit=0 ; source sos_db.sql ; COMMIT')
	#cur.execute()
	cursor.close()		
	con.close()

mysqlImport2()
#print('man')
