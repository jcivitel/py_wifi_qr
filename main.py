import sys

import qrcode

if __name__ == '__main__':
    SSID = sys.argv[1]
    Key = sys.argv[2]
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data(f"WIFI:S:{SSID};T:WPA;P:{Key};H:false;")
    img = qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")

