#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import MySQLdb as mdb

def connsql(command):
    dbsql = mdb.connect('localhost','datalogin','P@ssw0rd','Users')
    cursor = dbsql.cursor()
    cursor.execute(command)
    dbsql.commit()
    dbsql.close()
