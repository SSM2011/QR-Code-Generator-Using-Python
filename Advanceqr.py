import qrcode

from PIL import Image

qr = qrcode.QRCode(version =1, error_correction=qrcode.constants.ERROR_CORRECT_H,   box_size =10, border = 4)

qr.add_data("https://www.youtube.com/results?search_query=code+with+harry")

qr.make(fit = True )
img = qr.make_image(fill_color= "aqua", back_color = "red")

img.save("Trevo_Gaming_Yt.png")