#!/usr/bin/env python

import gtk

class Base:
    def __init__(self):
        win = gtk.Window()
        win.connect("destroy", lambda w: gtk.main_quit())

        box = gtk.VBox()
        entry = gtk.Entry()
        entry2 = gtk.Entry()

        win.add(box)
        box.pack_start(entry)
        box.pack_start(entry2)

        win.show_all()
        entry.connect("activate", self.entry_go) 
        entry2.connect("activate", self.entry_go) 

    def entry_go(self, widget):
        print "You entered this: ", widget.get_text()

    def main(self):
        gtk.main() 

if __name__ == "__main__":
    base = Base()
    base.main()
