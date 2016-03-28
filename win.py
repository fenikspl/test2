#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Base:
    def destroy(self, widget, data=None):
        print "You clicked the close button"
        gtk.main_quit()

    def myhide(self, widget):
        self.button1.hide()

    def myshow(self, widget):
        self.button1.show()

    def relabel(self, widget):
        self.label1.set_text("New text")

    def textchange(self, wigdet):
        self.window.set_title(self.textbox.get_text())

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(600, 100)
        self.window.set_title("This is my cool GTK window")
        self.window.set_tooltip_text("This is my GUI\nBy Fenikspl")

        self.button1 = gtk.Button("EXIT")
        self.button1.connect("clicked", self.destroy)
        self.button1.set_tooltip_text("This button will close this window")

        self.button2 = gtk.Button("hide")
        self.button2.connect("clicked", self.myhide)

        self.button3 = gtk.Button("show")
        self.button3.connect("clicked", self.myshow)

        self.button4 = gtk.Button("relabel label")
        self.button4.connect("clicked", self.relabel) 

        self.label1 = gtk.Label("New Label")

        self.textbox = gtk.Entry()
        self.textbox.connect("changed", self.textchange)


        self.box1 = gtk.HBox()
        self.box1.pack_start(self.button1)
        self.box1.pack_start(self.button2)
        self.box1.pack_start(self.button3)
        self.box1.pack_start(self.button4)
        self.box1.pack_start(self.label1)
        self.box1.pack_start(self.textbox)

        self.window.add(self.box1)
        self.window.show_all()
        self.window.connect("destroy", self.destroy)

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()

