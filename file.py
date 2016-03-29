#!/usr/bin/env python

import pygtk, gtk

if gtk.pygtk_version <= (2,3,90):
    print "Please upgade your pygtk"
    raise SystemExit

dialog = gtk.FileChooserDialog("Open...", None, 
    gtk.FILE_CHOOSER_ACTION_OPEN,
    (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
    gtk.STOCK_OPEN, gtk.RESPONSE_OK))

dialog.set_default_response(gtk.RESPONSE_OK)

filter = gtk.FileFilter()
filter.set_name("All files")
filter.add_pattern("*")
dialog.add_filter(filter)

response = dialog.run()
if response == gtk.RESPONSE_OK:
    print dialog.get_filename(), 'selected'
elif response == gtk.RESPONSE_CANCEL:
    print "Closed, you didn't choose any files"

dialog.destroy()
