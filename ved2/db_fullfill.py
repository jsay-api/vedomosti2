#coding: utf-8
#/usr/bin/python
__author__='julia sayapina'

from warnings import filterwarnings
import MySQLdb as db
import os
import shutil
import os
import sys 
from subprocess import Popen, PIPE, STDOUT


# Создание или открытие файла базы данных и создание схемы
filterwarnings('ignore', category = db.Warning)
db_name = 'ved3'
try:
  conn = db.connect("localhost","root","0013Tau","ved3" )
  # with db.connection(host="localhost",
  #               user="root",
  #               passwd="0013Tau",
  #               db="ved2") as conn:
  cur = conn.cursor()
  # creating db dump 
  # cur.execute("""
  #             mysqldump -u root -p 0013Tau ved2 | gzip > `date +/Users/devs/jsay_git/vedomosti2/dumps.sql.%Y%m%d.%H%M%S.gz;` 
  #         """)
  Popen('mysqldump -h localhost -P 3306 -uroot -p0013Tau ved3 | gzip > `date +/Users/devs/jsay_git/vedomosti2/dumps/%Y%m%d.%H%M%S.dumps.sql.gz;` | mysql -h localhost -P 3306 -u root -p 0013Tau ved2', shell=True)
  # dropping db
  cur.execute('DROP DATABASE IF EXISTS ' + db_name + ';')
  # Creating new database
  cur.execute('CREATE DATABASE IF NOT EXISTS ' + db_name + ' CHARACTER SET utf8 COLLATE utf8_general_ci;')
  conn.commit()


except Exception as e:
  print ("Exception 0:", type(e), e)


conn.commit()
conn.close()
print ('DB installation script finished')


# def main():
#     if len(sys.argv) != 3:
#         print('usage: python3 db_fullfill.py [--fullfill] [numrows]')
#         sys.exit(1)

#     option = sys.argv[1]
#     if len(sys.argv) == 3: 
#       numrows = sys.argv[2]
#     else:
#       numrows = 15
#     print (numrows)

#     return numrows
#     sys.exit(1)

# if __name__ == '__main__':
#     main()

