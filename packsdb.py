#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# #
import os.path
import uuid
from datetime import datetime
import json
from os import path
from sys  import getsizeof
import re


def create(name):
    return PacksDB(name)
class PacksDB(object):

    def __init__ (self):
        self.name =  ''
        self.db  = ''
        self.table = ''
        self.immutable = 'on'
        self.colId=''

    def create(self,name=''):
        if name!='' :
                if path.exists(path.join(name+".db")):
                #open and read database
                    openedDatabase = open(name+".db", "r")
                    self.name  = name+".db"
                    self.db =   openedDatabase.read()
                    return self
                else:
                    data  =  {
                        'name':os.path.basename(name+".db"),
                        'tables':{},
                        'data':{}
                    }
                    newDb = open(name+".db","x")
                    with open(name+".db", 'w') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        self.name   =  name
                        self.db =  name +".db"
                        return self
        else:
            raise Exception ("You need to specify the database name")
    def addKey(self,table):
        if self.db != '':
                info = json.loads(table)
                with open(str(self.name)) as f:
                    database  =  json.load(f)
                    if type(info).__name__ == 'dict' and 'name' in info  and 'cols' in info and info['cols'] != '':
                        for t in database:
                            if 'name' in t['tables']:
                                print("Table " + info['name'] +" already exist")
                            else:
                                self.colId = str(uuid.uuid4().hex)
                                table_cols = {}
                                table_cols[self.colId] = {}
                                table_cols[self.colId]['_id'] = ""
                                for col in info['cols']:
                                    table_cols[self.colId][col] = ""
                                table_cols[self.colId]["create_at"] = ""
                                table_cols[self.colId]["updated_at"] = ""
                                t['tables'][info['name']] =  table_cols
                                t['data'][info['name']] = {}
                                # print(self.db)
                                # newDb = open(self.db, "r")
                                with open(self.name, 'w', encoding='utf-8') as f:

                                    # f.write(json.dumps([database]).encode())
                                    json.dump([database], f, ensure_ascii=False, indent=4)
                                    # self.db =
                                    return True
                    else:
                        # raise Exception ("Invalid query")
                        print("Invalid query")
        else:
            raise Exception ("You need to select a database")

    def get(self,element=''):

        with open(self.name, "r") as db:
            data = json.load(db)
               #check if element is a key
            if element in data['tables']:
                return json.dumps(data['tables'][element])
            else:
                print ("Key doesn't exist")
    def selectKey(self,tableName):
        if  self.db != '':
            with open(str(self.name)) as f:
                database  =  json.load(f)
                for t in database:
                   for table in t:
                    if str(tableName) in table['tables']:
                        print(tableName)
                    # return self
                    # else:
                    #     print ("Invalid key selection")
    def addValue(self,data=''):
        if self.db  !='':
            with open(self.name,"r") as db:
                database =  json.load(db)
                data = json.loads(data)
                if self.table  != '':
                        for key in data:
                            mq = 0
                            for db_value in database['tables'][self.table]:
                                if db_value == key:
                                    mq = 1
                            if mq == 0:
                                print("column or key doesn't not exist ")
                        if len(data) == int(len(database['tables'][self.table]))-3:
                            newData = {}
                            newData['_id'] =  uuid.uuid4().hex
                            for key,value in data.items():
                                newData[key] =  value
                                # print(data.values())
                                newData['created_at'] =  datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
                                newData['updated_at'] = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
                                database['tables'][self.table]  =  newData
                                with open(self.name, 'ab+', encoding='utf-8') as f:
                                    f.seek(0,2)
                                    json.dump(database, f, ensure_ascii=False, indent=4)
                                    self.db =  f
                            return True
                                # else:
                                #     print ("All column or key must not be null")
                else:
                    print ("kindly set a table")

        else:
            print ("Kindly select a database")

    def getAll(self):
        if self.table != '' and self.db != '' and self.name != '':
            selected_table = self.selectKey(self.table)
            with open(self.name, "r") as tables:
                db_tables =  json.load(tables)
                return dict(db_tables['tables'][self.table])
        else:
            print ("No match key or db found")
    def byKey(self,name):
        if self.table != '' and self.db != '' and self.name != '':
            selected_table = self.selectKey(self.table)
            with open(self.name, "r") as tables:
                db_tables =  json.load(tables)
                return db_tables['tables'][self.table][name]
        else:
            print ("No match key or db found")
    def update(self,objs):
       if type(objs).__name__ == 'dict':
           with open(self.name, "r") as tables:
                db_tables =  json.load(tables)
                for key,value in objs.items():
                    db_tables['tables'][self.table][key] = value
                    with open(self.name, 'w', encoding='utf-8') as f:
                        json.dump(db_tables, f, ensure_ascii=False, indent=4)
                        self.db =  f
                else:
                    print("key or value not found ")
        # else:
        #     print("passed argument must be a dictionary")
    def remove(self,key=''):
        with open(self.name, 'r') as data_file:
            data = json.load(data_file)
        # if data['tables'] is type()
            if len(data['tables']) >=2:
                for element in list(data['tables']):
                    if key in element:
                        data['tables'].pop(key)
                        with open(self.name, 'w') as data_file:
                            data = json.dump(data, data_file)
                    else:
                        print ("Key: " +key+"doesn't exist")
            else:
                if key in element:
                        data['tables'].pop(key)
                        with open(self.name, 'w') as data_file:
                            data = json.dump(data, data_file)
                else:
                    print ("Key: " +key+"  doesn't exist")
    def query(self,qrys):
        # if type(qrys).__name__ == 'dict':
           with open(self.name, "r") as tables:
                db_tables =  json.load(tables)
                for key,value in qrys.items():
                   print(key)
