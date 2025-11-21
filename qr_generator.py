import qrcode
import os

# URL of your deployed Heroku map page
url = "https://frvmfi-campus-portal-85e78479c84b.herokuapp.com/map.html"  # <-- change to your actual Heroku URL

# Create QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

# Ensure 'static' folder exists
if not os.path.exists("static"):
    os.makedirs("static")

# Save QR code image in 'static' folder
img = qr.make_image(fill="black", back_color="white")
img_path = os.path.join("static", "qrcode.png")
img.save(img_path)

print(f"QR code generated at {img_path}")