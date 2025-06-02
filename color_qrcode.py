import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://github.com/Arpithajain26/portfoliowebsite")
qr.make(fit=True)
img = qr.make_image(fill_color="yellow", back_color="black")
img.save("my_qr.png")
