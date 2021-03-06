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
        self.window.set_title(wigdet.get_text())
        self.label1.set_text(wigdet.get_text())

    def clear_text(self, wigdet):
        self.textbox.set_text("")

    def combo_text(self, widget):
        self.textbox.set_text(widget.get_active_text)

    def add_combo(self, widget):
        self.combo.append_text(self.textbox.get_text())

    def about_win(self, widget):
        about = gtk.AboutDialog()
        about.set_program_name("My First GTK Python")
        about.set_version("0.1")
        about.set_copyright("(c) Fenikspl")
        about.set_comments("This is my first GTK Program written in Python")
        about.set_website("http://www.fenikspl.eu")
        about.set_logo(gtk.gdk.pixbuf_new_from_file("pics/tux.png"))
        about.run()
        about.destroy()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(600, 600)
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

        self.button5 = gtk.Button("clear text")
        self.button5.connect("clicked", self.clear_text) 

        self.button6 = gtk.Button("Add to Combo")
        self.button6.connect("clicked", self.add_combo)

        self.about_button = gtk.Button("About")
        self.about_button.connect("clicked", self.about_win)

        self.label1 = gtk.Label("New Label")

        self.textbox = gtk.Entry()
        self.textbox.connect("changed", self.textchange)

        self.combo = gtk.combo_box_entry_new_text()
        self.combo.connect("changed", self.combo_text)
        self.combo.append_text("This is some text")
        self.combo.append_text("This is option nr2")

        dialog = gtk.FileChooserDialog("Choose an Image",
            None, gtk.FILE_CHOOSER_ACTION_OPEN,
            (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
            gtk.STOCK_OPEN, gtk.RESPONSE_OK))

        dialog.set_default_response(gtk.RESPONSE_OK)
        filter = gtk.FileFilter()
        filter.set_name("Images")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpg")
        filter.add_pattern("*.png")
        filter.add_pattern("*.jpg")
        filter.add_pattern("*.jpeg")
        dialog.add_filter(filter)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
             self.pix = gtk.gdk.pixbuf_new_from_file(dialog.get_filename())
             self.pix = self.pix.scale_simple(300, 300, gtk.gdk.INTERP_BILINEAR)

        elif response == gtk.RESPONSE_CANCEL:
             print "no file seleted"
             print "Exiting..."
             em = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, 
                  gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE,
                  "ERROR LOADING FILE\nNow Exiting!!!")
             em.run()
             em.destroy() 
             raise SystemExit
        dialog.destroy()

        self.image = gtk.image_new_from_pixbuf(self.pix)
       
#        self.image = gtk.Image()
#        self.image.set_from_pixbuf(self.pix)

        self.box1 = gtk.HBox()
        self.box1.pack_start(self.button1)
        self.box1.pack_start(self.button2)
        self.box1.pack_start(self.button3)
        self.box1.pack_start(self.button4)
        self.box1.pack_start(self.button5)
        self.box1.pack_start(self.about_button)

        self.box3 = gtk.HBox()
        self.box3.pack_start(self.textbox)
        self.box3.pack_start(self.button6)

        self.box2 = gtk.VBox()
        self.box2.pack_start(self.box1)
        self.box2.pack_start(self.label1)
        self.box2.pack_start(self.box3)
        self.box2.pack_start(self.combo)
        self.box2.pack_start(self.image)

        self.window.add(self.box2)
        self.window.show_all()
        self.window.connect("destroy", self.destroy)

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()

