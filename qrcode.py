import pyqrcode
url = pyqrcode.create("https://github.com/DarikaSan", error='H')
print(url.png("C:\\Users\Marvin\PycharmProjects\qr_gen_read\qr_png\qrcode.png", module_color=(0, 0, 0, 255), background=(0, 255, 80, 255), scale=5))
