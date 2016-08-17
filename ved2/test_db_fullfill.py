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
import uuid


# Создание или открытие файла базы данных и создание схемы
filterwarnings('ignore', category = db.Warning)
db_name = 'ved3'

def db_insert(numrows):    # adds or replaces values into tables
  cur.execute("""
        create table if not exists Offshores_asset (
            id                  INTEGER PRIMARY KEY AUTO_INCREMENT,
            asset_name          VARCHAR(100),
            asset_link          VARCHAR(200),
            slug                VARCHAR(200)
    );
    """)
  cur.execute("""
        create table if not exists Offshores_offshore (
            id                  INTEGER PRIMARY KEY AUTO_INCREMENT,
            off_name            VARCHAR(50),
            off_jurisdiction    VARCHAR(50),
            file                VARCHAR(100),
            image               VARCHAR(100),
            off_parent          VARCHAR(50),
            off_link            VARCHAR(300),
            slug                VARCHAR(200),
            uuid                CHAR(36)
    );
    """)
  cur.execute("""
        create table if not exists Offshores_offshore (
            id                  INTEGER PRIMARY KEY AUTO_INCREMENT,
            ben_name            VARCHAR(50),
            ben_lastname        VARCHAR(100),
            ben_midname         VARCHAR(30),
            ben_holding         VARCHAR(70),
            ben_link            VARCHAR(300),
            slug                VARCHAR(200),
            uuid                CHAR(36)
    );
    """)
  print('tables created')
  
    for x in xrange(0,numrows):
      num = str(x)
      a_name = 'Asset' + num
      a_link = 'http://somelink/'+a_name
      a_slug = a_name + '-' + num
      o_name = 'Offshore' + num
      o_jur = 'Cyprus'
      o_file = '/media/offshores/favicon.xcf'
      o_image = '/media/offshores/favicon.png'
      o_prnt = 'parent' + num
      o_link = o_name + '-' + num
      o_uuid = str(uuid.uuid4())
      o_slug = o_name + str(o_uuid)

      try:
        cur.execute("""INSERT INTO Offshores_asset (asset_name, asset_link, slug) VALUES (%s,%s,%s)""",(a_name, a_link, a_slug))
        cur.execute("""INSERT INTO Offshores_offshore (off_name, off_jurisdiction, file, image, off_parent, off_link, slug, uuid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(o_name, o_jur, o_file, o_image, o_prnt, o_link, o_slug, o_uuid))
        conn.commit()
      except Exception as e:
        print ("Exception 1:", type(e), e)


try:
  conn = db.connect("localhost","root","0013Tau","ved3" )
  cur = conn.cursor()
  db_insert(20)

except Exception as e:
  print ("Exception 0:", type(e), e)

except: db.rollback() 


conn.commit()
conn.close()
print ('DB installation script finished')


# def main():
#   if len(sys.argv) != 2:
#     print('usage: python3 db_fullfill.py [numrows]')
#     sys.exit(1)

#   if len(sys.argv) == 2: 
#     numrows = sys.argv[1]

#   else:
#     numrows = 15
#   print (numrows)

#   return numrows
#   sys.exit(1)

# if __name__ == '__main__':
#     main()

