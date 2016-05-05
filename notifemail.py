import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage

def email(text2):
	fromaddr = "bbic.indisbuilding@gmail.com"
	fromname = "Rumah Cerdas Aria Graha Regency"
	penerima = ['faicanhas@gmail.com']
	
	msg = MIMEMultipart()
	msg['From'] = fromname
	msg['To'] = ", ".join(penerima)
	msg['Subject'] = 'Pemberitahuan dari Rumah Cerdas Aria Graha Regency'

	text1 = "Perintah berhasil dieksekusi. \nStatus : \n"
	#text2  = "nyala"
	pesan = MIMEText(text1 + text2)
	msg.attach(pesan)

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(fromaddr, "bbic.building")
	server.sendmail(fromaddr, penerima, msg.as_string())
	server.quit()

#email("ayolah")
