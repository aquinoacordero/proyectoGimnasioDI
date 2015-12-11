#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import menu
from gi.repository import Gtk

class eliminar:

    builder = Gtk.Builder()
    builder.add_from_file("eliminar.glade")
    win = builder.get_object("window1")
    nombre = builder.get_object("labelName")
    apellido = builder.get_object("labelLast")

    def __init__(self,nom,ape):

        signals = { "onButtonPressedDeleteSi" : self.onButtonPressedDeleteSi,
                    "onButtonPressedDeleteNo" : self.onButtonPressedDeleteNo
                    }
        self.builder.connect_signals(signals)

        self.nombre.set_text(str(nom))
        self.apellido.set_text(str(ape))

        self.win.show_all()

    def onButtonPressedDeleteSi(self, *args):
        print ("Borrado")
        self.win.hide()
        menu.principal()

    def onButtonPressedDeleteNo(self, *args):
        print ("Saliendo")
        self.win.hide()
        menu.principal()

