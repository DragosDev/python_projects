import qrcode

# Your Data
firstname = "name \n"
secondname = "name \n"
date_of_birth= "dob \n"
website_url = "url \n"
phone = "phone \n"
email = "email \n"

#Declaring varialble qr and parameters for the generated QR code
#Parameters fro the QR Code
#version - the size of the qr code 
#box_size - the size of each box in pixels
#border - the thickness of the border around the qr code

qr = qrcode.QRCode(
        version=1,
        box_size=20,
        border=3)
qr.add_data(firstname)
qr.add_data(secondname)
qr.add_data(date_of_birth)
qr.add_data(website_url)
qr.add_data(phone)
qr.add_data(email)


qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('generated_code.png')