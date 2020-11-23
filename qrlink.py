import qrcode
import socket
from config import get_config


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def get_qr_code(ip=get_ip(), port=get_config().PORT):
    qr = qrcode.QRCode()
    qr.add_data('http://%s:%s' % (ip, port))
    return qr.make_image()
