## Drop

![Drop](./static/cz.lukasbrabec.Drop.svg)

Simple app for dropping files from phone to computer, both devices have to be on the same network.
Drop runs flask server and generates QR code with server URL for easy scan on phone.


Install dependencies (Fedora):
```
dnf install python3-tkinter python3-pillow-tk python3-flask python3-qrcode python3-notify2
```

Run
```
./drop.py
```

Install to run from applications menu:
```
./install.sh
```

