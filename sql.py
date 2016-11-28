#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import MySQLdb as mdb

def connsql(command):
    try:
        dbsql = mdb.connect(host='localhost',user='datalogin',db='Users',
                            passwd='P@ssw0rd')
        cursor = dbsql.cursor()
        cursor.execute(command)
        dbsql.commit()
    except Exception as e:
        print("Error: %s" %e)
        dbsql.rollback()
    finally:
        cursor.close()
        dbsql.close()
