import qrcode

# Dados a serem codificados
github_url= 'https://github.com/sergioSinhoca'
linkedin_url = "https://www.linkedin.com/in/sergio-luiz-sinhoca/"

# Criando o QR code para o GitHub
qr_github = qrcode.QRCode(version=1, box_size=10, border=5)
qr_github.add_data(github_url)
qr_github.make(fit=True)

# Criando e salvando a imagem GitHub
img_github = qr_github.make_image(fill_color="black", back_color="white")
img_github.save("my_github_qr_code.png")




# Criando o QR code para o LinkedIn
qr_linkedin = qrcode.QRCode(version=1, box_size=10, border=5)
qr_linkedin.add_data(linkedin_url)
qr_linkedin.make(fit=True)

# Criando e salvando a imagem LinkedIn
img_linkedin = qr_linkedin.make_image(fill_color="black", back_color="white")
img_linkedin.save("my_linkedin_qr_code.png")


