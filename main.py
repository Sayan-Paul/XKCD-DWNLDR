#!/bin/usr/python
# Main GUI
from gi.repository import Gtk

import img_downloader
import archive_scraper

class View_Image(Gtk.Dialog):

    def __init__(self, parent,title,image):
        Gtk.Dialog.__init__(self, title, parent, 0,(Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(500, 500)

        image = Gtk.Image.new_from_file (image)

        box = self.get_content_area()
        box.add(image)
        self.show_all()

class XKCDWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title=" * * Xkcd Downloader * * ")
        self.set_size_request(600, 660)
        self.set_border_width(10)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=2)
        self.add(self.vbox)


        self.label_t = Gtk.Label()
        self.label_t.set_text("- * - XKCD Comics - * -")
        self.label_t.set_justify(Gtk.Justification.CENTER)
        self.vbox.pack_start(self.label_t, False, True, 0)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        self.vbox.pack_start(self.hbox, False, True, 0)

        self.vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)
        self.vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)
        
        self.hbox.pack_start(self.vbox1, True, True, 0)
        self.hbox.pack_start(self.vbox2, True, True, 0)

        self.hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=2)
        
        self.vw_rndm = Gtk.Button(label="Random Comic")
        self.view = Gtk.Button(label="View")

        self.entry1 = Gtk.Entry()
        self.entry1.set_placeholder_text ("Enter valid Comic Number")
        self.entry2 = Gtk.Entry()
        self.entry2.set_placeholder_text ("Enter valid Comic Number")

        self.label1 = Gtk.Label()
        self.label1.set_text("View Comics")
        self.label1.set_justify(Gtk.Justification.CENTER)

        self.label2 = Gtk.Label()
        self.label2.set_text("Download Comics")
        self.label2.set_justify(Gtk.Justification.CENTER)

        self.label3 = Gtk.Label()
        self.label3.set_text("Enter Number to Select :")
        self.label3.set_justify(Gtk.Justification.CENTER)

        self.label4 = Gtk.Label()
        self.label4.set_text("Enter Number to Select :")
        self.label4.set_justify(Gtk.Justification.CENTER)

        self.scrolledwindow1 = Gtk.ScrolledWindow()
        self.scrolledwindow1.set_hexpand(True)
        self.scrolledwindow1.set_vexpand(True)
        self.textview1 = Gtk.TextView()
        self.textbuffer1 = self.textview1.get_buffer()
        self.textbuffer1.set_text("\n".join([str(x)+" - "+archive_scraper.Comics[x] for x in archive_scraper.Comics]))
        self.textview1.set_editable(False)
        self.scrolledwindow1.add(self.textview1)

        self.scrolledwindow2 = Gtk.ScrolledWindow()
        self.scrolledwindow2.set_hexpand(True)
        self.scrolledwindow2.set_vexpand(True)
        self.textview2 = Gtk.TextView()
        self.textbuffer2 = self.textview2.get_buffer()
        self.textbuffer2.set_text("\n".join([str(x)+" - "+archive_scraper.Comics[x] for x in archive_scraper.Comics]))
        self.textview2.set_editable(False)
        self.scrolledwindow2.add(self.textview2)


        self.sup_me = Gtk.Button(label="Surprise Me")
        self.dwn_all = Gtk.Button(label="Download them all..")
        self.dwn = Gtk.Button(label="Download")  

        #packing first box
        self.vbox1.pack_start(self.label1, False, True, 0)
        self.vbox1.pack_start(self.vw_rndm, False, True, 0)
        self.vbox1.pack_start(self.label3, False, True, 0)
        self.vbox1.pack_start(self.entry1, False, True, 0)
        self.vbox1.pack_start(self.scrolledwindow1, False, True, 0)
        self.vbox1.pack_start(self.view, False, True, 0)

        #packing second box
        self.vbox2.pack_start(self.label2, False, True, 0)

        self.hbox2.pack_start(self.sup_me, True, True, 0)
        self.hbox2.pack_start(self.dwn_all, True, True, 0)
        
        self.vbox2.pack_start(self.hbox2, False, True, 0)
        self.vbox2.pack_start(self.label4, False, True, 0)
        self.vbox2.pack_start(self.entry2, False, True, 0)
        self.vbox2.pack_start(self.scrolledwindow2, False, True, 0)
        self.vbox2.pack_start(self.dwn, False, True, 0)

        self.view.connect("clicked", self.on_view_clicked)

        self.image = Gtk.Image.new_from_file ("xkcd.png")
        self.vbox.pack_start(self.image, False, True, 0)

    def on_view_clicked(self, widget):
        vw_im=View_Image(self,"title","xkcd.png")
        vw_im.run()
        vw_im.destroy()


archive_scraper.scrape()
win = XKCDWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()