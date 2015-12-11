#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import menu
import BD
from gi.repository import Gtk

class abonado:

    builder = Gtk.Builder()
    builder.add_from_file("anadir.glade")
    win = builder.get_object("window1")
    nombre = builder.get_object("entryName")
    apellido = builder.get_object("entryLast")
    dni = builder.get_object("entryDNI")

    def __init__(self, nom, ape, dni_):

        signals = { "onButtonBack" : self.onButtonBack,
                    "onButtonConfirm" : self.onButtonConfirm
                    }
        self.builder.connect_signals(signals)

        self.nombre.set_text(str(nom))
        self.apellido.set_text(str(ape))
        self.dni.set_text(str(dni_))

        self.win.show_all()

    def onButtonBack(self, *args):
        print ("Retroceder")
        self.win.hide()
        menu.principal()

    def onButtonConfirm(self, *args):
        print ("Confirmar")
        nom=self.nombre.get_text()
        ape=self.apellido.get_text()
        dni_=self.dni.get_text()
        print(nom,ape,dni_)
        BD.BD().insertar(nom,ape,dni_)