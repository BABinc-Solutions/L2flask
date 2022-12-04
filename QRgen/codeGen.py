import qrcode


def gencode():
    fname = input("What do you want to name the file?")
    msg = input("What do you want the QR code to say?")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(msg)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(fname + ".png")
