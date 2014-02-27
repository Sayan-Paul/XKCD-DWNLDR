#!/bin/usr/python
# Main GUI
from gi.repository import Gtk

import img_downloader
import archive_scraper

class XKCDWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="**Xkcd Downloader**")
        self.set_size_request(600, 600)
        self.set_border_width(10)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=2)
        self.add(self.vbox)

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
        self.entry2 = Gtk.Entry()

        self.label1 = Gtk.Label()
        self.label1.set_text("View Comics")
        self.label1.set_justify(Gtk.Justification.CENTER)

        self.label2 = Gtk.Label()
        self.label2.set_text("Download Comics")
        self.label2.set_justify(Gtk.Justification.CENTER)

        self.label3 = Gtk.Label()
        self.label3.set_text("Enter Number or Select :")
        self.label3.set_justify(Gtk.Justification.CENTER)

        self.label4 = Gtk.Label()
        self.label4.set_text("Enter Number or Select :")
        self.label4.set_justify(Gtk.Justification.CENTER)

        self.list1 = Gtk.ComboBoxText()
        self.list1.set_entry_text_column(0)
        self.list1.connect("changed", self.on_view_combo_changed)

        self.list2 = Gtk.ComboBoxText()
        self.list2.set_entry_text_column(0)
        self.list2.connect("changed", self.on_dwnld_combo_changed)

        for comic in archive_scraper.Comics:
            self.list1.append_text(str(comic)+" - "+archive_scraper.Comics[comic])
            self.list2.append_text(str(comic)+" - "+archive_scraper.Comics[comic])


        self.sup_me = Gtk.Button(label="Surprise Me")
        self.dwn_all = Gtk.Button(label="Download them all..")
        self.dwn = Gtk.Button(label="Download")  

        #packing first box
        self.vbox1.pack_start(self.label1, False, True, 0)
        self.vbox1.pack_start(self.vw_rndm, False, True, 0)
        self.vbox1.pack_start(self.label3, False, True, 0)
        self.vbox1.pack_start(self.entry1, False, True, 0)
        self.vbox1.pack_start(self.list1, False, True, 0)
        self.vbox1.pack_start(self.view, False, True, 0)

        #packing second box
        self.vbox2.pack_start(self.label2, False, True, 0)

        self.hbox2.pack_start(self.sup_me, True, True, 0)
        self.hbox2.pack_start(self.dwn_all, True, True, 0)
        
        self.vbox2.pack_start(self.hbox2, False, True, 0)
        self.vbox2.pack_start(self.label4, False, True, 0)
        self.vbox2.pack_start(self.entry2, False, True, 0)
        self.vbox2.pack_start(self.list2, False, True, 0)
        self.vbox2.pack_start(self.dwn, False, True, 0)


        # self.button1.connect("clicked", self.on_button1_clicked)

        image = Gtk.Image.new_from_file ("xkcd.png")
        self.vbox.pack_start(image, False, True, 0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_view_combo_changed(self, combo):
        text = combo.get_active_text()
        if text != None:
            print("Selected: %s" % text)

    def on_dwnld_combo_changed(self, combo):
        text = combo.get_active_text()
        if text != None:
            print("Selected: %s" % text)


archive_scraper.scrape()
win = XKCDWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()