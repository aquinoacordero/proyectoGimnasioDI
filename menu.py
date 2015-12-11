#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import add
import borrar
import buscar

from gi.repository import Gtk

class principal:

    builder = Gtk.Builder()
    builder.add_from_file("menu.glade")
    win = builder.get_object("window1")
    nombre = builder.get_object("entryName")
    apellido = builder.get_object("entryLast")
    dni = builder.get_object("entryDNI")

    def __init__(self):

        signals = { "onButtonPressedAdd" : self.onButtonPressedAdd,
                    "onButtonPressedSearch" : self.onButtonPressedSearch,
                    "onButtonPressedDelete" : self.onButtonPressedDelete
                    }

        self.builder.connect_signals(signals)

        self.win.show_all()

    def onButtonPressedAdd(self, *args):
        print ("Añadiendo")
        print(self.nombre.get_text(),self.apellido.get_text(),self.dni.get_text())
        nom = self.nombre.get_text()
        ape = self.apellido.get_text()
        dni_ = self.dni.get_text()
        self.win.hide()
        add.abonado(nom,ape,dni_)

    def onButtonPressedSearch(self, *args):
        print ("Buscando")
        dni_ = self.dni.get_text()
        self.win.hide()
        buscar.busqueda(dni_)

    def onButtonPressedDelete(self, *args):
        print ("Borrando")
        nom = self.nombre.get_text()
        ape = self.apellido.get_text()
        if(nom=="" and ape==""):
            print("DATOS NECESARIOS")
        else:
             borrar.eliminar(nom,ape)

if __name__== "__main__":
    principal()
    Gtk.main()

