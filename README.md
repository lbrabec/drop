## Drop

![Drop](./static/cz.lukasbrabec.Drop.svg)

Simple app for dropping files from phone to computer. Drop will show you a QR code which links to flask server that is running in the background. Just scan the code with your phone, open the web page and upload the files to your computer.


Fedora dependencies:
```
dnf install python3-tkinter python3-pillow-tk python3-flask python3-qrcode python3-notify2
```

Run
```
./drop.py
```

To run Drop from applications menu, install it:
```
./install.sh
```

