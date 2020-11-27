import qrcode
import socket
import json
import subprocess
from config import get_config


def get_interfaces():
    out = []
    ifs = json.loads(subprocess.check_output(["ip", "-4", "-j", "addr", "show"]))
    for i in ifs:
        if i['ifname'] == 'lo':
            continue
        out.append((i['ifname'], i['addr_info'][0]['local']))
    return out


def get_qr_code(ip, port=get_config().PORT):
    qr = qrcode.QRCode()
    qr.add_data('http://%s:%s' % (ip, port))
    return qr.make_image()
