__author__ = 'aquinoacordero'

import sqlite3 as dbapi

class BD:
    bd=dbapi.connect("basedatos.dat")
    cursor = bd.cursor()

    def __init__(self):
        #self.cursor.execute('''create table abonados(id dni text primary key, nombre text, apellido text)''')
        self.bd.commit()

    def insertar(self,nom,ape,dni_):
        val=(nom,ape,dni_)
        print(val)
        self.cursor.execute("insert into abonados values(?,?,?)",val)
        self.bd.commit()

    def buscar(self,dni):
        id=dni
        print(id)
        #abonado=self.cursor.execute("select * from abonados where id =(?)",id)


    def borrar(self):
        print("borrando bd")