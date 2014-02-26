#!/bin/usr/python
# Main GUI
from gi.repository import Gtk

class XKCDWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="**Xkcd Downloader**")

        self.box = Gtk.Box(spacing=2)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, False, True, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, False, True, 0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")

win = XKCDWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()