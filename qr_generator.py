import qrcode
import os

url = "https://ejls220.github.io/frvmfi-campus-portal/map.html"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

if not os.path.exists("static"):
    os.makedirs("static")

img_path = os.path.join("static", "qrcode.png")
img = qr.make_image(fill="black", back_color="white")
img.save(img_path)

print(f"QR code generated at {img_path}")