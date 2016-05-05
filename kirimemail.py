import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage

def kirim(toadr, mailsub, body):
	fromaddr = "rukocipa@gmail.com"
	fromname = "Rumah Cerdas Ruko Cipamokolan"
	
	msg = MIMEMultipart()
	msg['From'] = fromname
	msg['To'] = ", ".join(toadr)
	msg['Subject'] = mailsub

	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(fromaddr, "rumaht0k0cipam0k0lan")
	text = msg.as_string()
	server.sendmail(fromaddr, toadr, text)
	server.quit()
