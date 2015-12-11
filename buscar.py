#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import menu
import BD
from gi.repository import Gtk

class busqueda:

    builder = Gtk.Builder()
    builder.add_from_file("busqueda.glade")
    win = builder.get_object("window1")

    def __init__(self, dni_):

        signals = { "onButtonBack" : self.onButtonBack,
                    "onButtonExit" : self.onButtonExit
                    }
        self.builder.connect_signals(signals)

        self.win.show_all()

        print(dni_)
        BD.BD().buscar(dni_)

    def onButtonBack(self, *args):
        print ("Regresando")
        self.win.hide()
        menu.principal()

    def onButtonExit(self, *args):
        sys.exit(0)
