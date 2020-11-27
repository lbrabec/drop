#!/usr/bin/env python
import os
import threading
import tkinter
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk

from config import get_config
from server import run_server
from qrlink import get_qr_code, get_interfaces


class DropApp():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('400x600')
        self.root.title('Phone Drop')
        self.root.config(background='white')
        self.icon = tkinter.Image("photo", file=os.path.join(os.path.dirname(__file__),"static/icon.png"))
        self.root.tk.call('wm', 'iconphoto', self.root._w, self.icon)
        self.canvas = tkinter.Canvas(self.root,
                                     width=400,
                                     height=400,
                                     bg='white',
                                     bd=0,
                                     highlightthickness=0,
                                     relief='ridge')
        self.canvas.pack()
        self.image = ImageTk.PhotoImage(get_qr_code(ip=get_interfaces()[0][1]))
        self.imagesprite = self.canvas.create_image(200, 200, image=self.image)
        self.iflabel = ttk.Label(self.root,
                              text="Select network interface",
                              background='white',
                              padding=(0,0,0,10))
        self.ifvar = tkinter.StringVar()
        self.ifvar.set("%s: %s" % get_interfaces()[0])
        self.iflabel.pack()
        self.ifselect = tkinter.OptionMenu(self.root,
                                           self.ifvar,
                                           *["%s: %s" % i for i in get_interfaces()],
                                           command=self.handle_if_select)
        self.ifselect.pack()

        self.path = ttk.Label(self.root,
                              text="Dropping to %s" % get_config().UPLOAD_FOLDER,
                              background='white',
                              padding=(0,30,0,10))
        self.path.pack()
        self.B = tkinter.Button(self.root,
                                text="Select drop dir",
                                command=self.set_upload_dir,
                                highlightthickness=0)
        self.B.pack()

    def run(self):
        self.root.mainloop()

    def set_upload_dir(self):
        upload_dir = filedialog.askdirectory(initialdir=get_config().UPLOAD_FOLDER)
        if upload_dir:
            get_config().set_drop_dir(upload_dir)
        self.path.config(text="Dropping to %s" % get_config().UPLOAD_FOLDER)

    def handle_if_select(self, value):
        self.image = ImageTk.PhotoImage(get_qr_code(ip=value.split(": ")[1]))
        self.imagesprite = self.canvas.create_image(200, 200, image=self.image)


if __name__ == "__main__":
    if os.getenv('DEV') == 'true':
        run_server(debug=True)
    else:
        t = threading.Thread(target=run_server, daemon=True)
        t.start()
        dropapp = DropApp()
        dropapp.run()

    print("exiting...")


