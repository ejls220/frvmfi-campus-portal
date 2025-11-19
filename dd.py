import qrcode

url = "https://example.com"

img = qrcode.make(url)
img.save("qrcode.png")
print("QR code saved as qrcode.png")
